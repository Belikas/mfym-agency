"""Dashboard de l'agence : serveur stdlib (127.0.0.1:8700). L'accès téléphone passe par `tailscale serve`.

Lecture seule : il lit memory/ et logs/runs.jsonl, n'écrit rien.
Self-check : python dashboard/server.py --selftest
"""
import json, os, re, struct, sys, time, zlib
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

HOST, PORT = "127.0.0.1", 8700
DASH = Path(__file__).resolve().parent
ROOT = DASH.parent
MEM = ROOT / "memory"
ACT = MEM / "activity.jsonl"
ACT_OLD = MEM / "activity.1.jsonl"   # nom donné par le hook à la rotation
RUNS = ROOT / "logs" / "runs.jsonl"
WORKING_S = 90          # dernier événement plus récent que ça = au travail
INFLIGHT_S = 900        # outil lancé (PreToolUse) sans retour : au travail jusqu'à 15 min
TERMINAL = {"Stop", "SessionEnd", "SubagentStop"}
STATIC = {"/": "index.html", "/index.html": "index.html", "/app.js": "app.js",
          "/style.css": "style.css", "/manifest.webmanifest": "manifest.webmanifest"}
TYPES = {".html": "text/html; charset=utf-8", ".js": "text/javascript; charset=utf-8",
         ".css": "text/css; charset=utf-8", ".webmanifest": "application/manifest+json"}


def parse_ts(s):
    try:
        d = datetime.fromisoformat(str(s).replace("Z", "+00:00"))
        return d.timestamp() if d.tzinfo else d.astimezone().timestamp()
    except ValueError:
        return None


def load_json(p):
    """(données, erreur) : un fichier absent donne (None, None), un JSON cassé (None, message)."""
    try:
        return json.loads(p.read_text(encoding="utf-8")), None
    except FileNotFoundError:
        return None, None
    except (ValueError, OSError) as e:
        return None, f"{p.name} illisible : {e}"


def tail_lines(paths, n, max_bytes=800_000):
    out = []
    for p in paths:
        try:
            with p.open("rb") as f:
                f.seek(0, 2)
                size = f.tell()
                f.seek(max(0, size - max_bytes))
                chunk = f.read()
        except OSError:
            continue
        lines = chunk.decode("utf-8", "replace").splitlines()
        if size > max_bytes:
            lines = lines[1:]   # première ligne coupée
        out += lines
    return out[-n:]


def read_jsonl(lines):
    rows = []
    for ln in lines:
        try:
            r = json.loads(ln)
            if isinstance(r, dict):
                rows.append(r)
        except ValueError:
            pass
    return rows


def live_status(last, now):
    if not last:
        return "idle"
    t = parse_ts(last.get("ts"))
    if t is None or last.get("event") in TERMINAL:
        return "idle"
    age = now - t
    limit = INFLIGHT_S if last.get("event") in ("PreToolUse", "SubagentStart") else WORKING_S
    return "working" if age < limit else "idle"


def activity_by_agent(events, now):
    by = {}
    for e in events:
        by.setdefault(str(e.get("agent") or "?"), []).append(e)
    out = {}
    for name, evs in by.items():
        last = evs[-1]
        # bulle : dernier événement porteur d'un outil (sinon le dernier tout court)
        cur = next((e for e in reversed(evs) if e.get("tool")), last)
        out[name] = {"status": live_status(last, now), "last_event": last.get("event"),
                     "last_active": last.get("ts"), "summary": cur.get("summary", ""),
                     "tool": cur.get("tool", ""), "recent": evs[-14:][::-1]}
    return out


def month_of(s):
    return str(s or "")[:7]


def journal_entries(text, n=5):
    secs, cur = [], None
    for line in text.splitlines():
        if line.startswith("## "):
            cur = {"title": line[3:].strip(), "body": []}
            secs.append(cur)
        elif cur is not None:
            cur["body"].append(line)
    for i, s in enumerate(secs):
        m = re.search(r"\d{4}-\d{2}-\d{2}", s["title"])
        s["_k"] = (m.group(0) if m else "", i)
        s["body"] = "\n".join(s["body"]).strip()
    secs.sort(key=lambda s: s["_k"], reverse=True)
    return [{"title": s["title"], "body": s["body"]} for s in secs[:n]]


def build_state():
    now = time.time()
    cur_month = datetime.now().strftime("%Y-%m")
    st = {"generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
          "server_now": now, "errors": {}, "mtimes": {}}

    def section(name, fn):
        try:
            st[name] = fn()
        except Exception as e:   # une section cassée ne casse pas les autres
            st[name] = None
            st["errors"][name] = str(e) if isinstance(e, ValueError) else f"{type(e).__name__}: {e}"

    def need(fname):
        data, err = load_json(MEM / fname)
        if err:
            raise ValueError(err)
        return data or {}

    for f in ["team.json", "pipeline.json", "tasks.json", "approvals.json", "revenue.json",
              "expenses.json", "activity.jsonl", "journal.md", "state.md"]:
        try:
            st["mtimes"][f] = (MEM / f).stat().st_mtime
        except OSError:
            st["mtimes"][f] = None
    try:
        st["mtimes"]["runs.jsonl"] = RUNS.stat().st_mtime
    except OSError:
        st["mtimes"]["runs.jsonl"] = None

    acts = activity_by_agent(read_jsonl(tail_lines([ACT_OLD, ACT], 2000)), now)

    def team():
        agents = need("team.json").get("agents") or []
        known = set()
        for a in agents:
            known.add(a.get("id"))
            a["live"] = acts.get(a.get("id")) or acts.get(a.get("name")) or None
        # renforts : agents vus dans l'activité mais absents de team.json, montrés seulement s'ils travaillent
        visitors = [{"id": k, "name": k, "live": v} for k, v in acts.items()
                    if k not in known and v["status"] == "working"]
        return {"agents": agents, "visitors": visitors}

    def revenue():
        rows = need("revenue.json").get("entries") or []
        mrows = [r for r in rows if month_of(r.get("date")) == cur_month]
        return {"month_net": round(sum(float(r.get("net_eur") or 0) for r in mrows), 2),
                "total_net": round(sum(float(r.get("net_eur") or 0) for r in rows), 2),
                "target": 1000, "entries": mrows[-10:], "count": len(rows)}

    def expenses():
        d = need("expenses.json")
        rows = d.get("entries") or []
        mrows = [r for r in rows if month_of(r.get("date")) == cur_month
                 or (r.get("recurring") and month_of(r.get("date")) < cur_month)]
        return {"month": round(sum(float(r.get("amount_eur") or 0) for r in mrows), 2),
                "budget": d.get("budget_monthly_eur", 60), "entries": mrows}

    def experiments():
        out = []
        for p in sorted((MEM / "experiments").glob("*.json")):
            data, err = load_json(p)
            out.append(data if isinstance(data, dict) else {"id": p.stem, "title": p.stem, "error": err or "vide"})
            out[-1]["_file"] = f"experiments/{p.name}"
            try:
                st["mtimes"][f"experiments/{p.name}"] = p.stat().st_mtime
            except OSError:
                pass
        return out

    def leads():
        rows = need("pipeline.json").get("leads") or []
        counts = {}
        for r in rows:
            counts[r.get("status", "?")] = counts.get(r.get("status", "?"), 0) + 1
        top = sorted(rows, key=lambda r: float(r.get("total") or 0), reverse=True)[:8]
        return {"top": top, "counts": counts, "count": len(rows)}

    def approvals():
        rows = need("approvals.json").get("approvals") or []
        return [r for r in rows if r.get("status") == "pending"]

    def tasks():
        rows = [t for t in need("tasks.json").get("tasks") or [] if t.get("status") == "open"]
        return {"open": rows, "est_hours": round(sum(float(t.get("est_minutes") or 0) for t in rows) / 60, 2)}

    def journal():
        p = MEM / "journal.md"
        return journal_entries(p.read_text(encoding="utf-8")) if p.exists() else []

    def sessions():
        out = []
        for p in sorted((MEM / "sessions").glob("*.md"), reverse=True)[:10]:
            try:
                first = next((l for l in p.read_text(encoding="utf-8").splitlines() if l.strip()), "")
            except OSError:
                first = ""
            out.append({"file": f"sessions/{p.name}", "name": p.stem, "title": first.lstrip("# ").strip(),
                        "mtime": p.stat().st_mtime})
        return out

    def runs():
        rows = [r for r in read_jsonl(tail_lines([RUNS], 40)) if r.get("goal") not in ("test", "locktest") and r.get("status") not in ("lock_test_done", "skipped_locked")]
        return rows[-10:][::-1]

    def state_md():
        p = MEM / "state.md"
        return p.read_text(encoding="utf-8")[:4000] if p.exists() else ""

    for name, fn in [("team", team), ("revenue", revenue), ("expenses", expenses),
                     ("experiments", experiments), ("leads", leads), ("approvals", approvals),
                     ("tasks", tasks), ("journal", journal), ("sessions", sessions), ("runs", runs),
                     ("state_md", state_md)]:
        section(name, fn)
    return st


def safe_doc(rel):
    """Chemin sûr dans memory/, sinon None."""
    if not rel or "\x00" in rel or rel.startswith(("/", "\\")) or re.match(r"^[A-Za-z]:", rel):
        return None
    if ".." in re.split(r"[\\/]", rel):
        return None
    p = (MEM / rel).resolve()
    if not p.is_relative_to(MEM.resolve()) or not p.is_file():
        return None
    return p


def png(size):
    """Icône PNG générée (pièce d'or pixel sur fond nuit), sans fichier image."""
    grid = ["................", "................", ".....######.....", "....#yyyyyy#....",
            "...#yyYYYYyy#...", "...#yYYyyYYy#...", "...#yYyyyyyy#...", "...#yYYYYYyy#...",
            "...#yyyyyYYy#...", "...#yYYYYYyy#...", "...#yyyYYyyy#...", "....#yyyyyy#....",
            ".....######.....", "................", "................", "................"]
    col = {".": (21, 19, 40), "#": (90, 52, 20), "y": (242, 184, 56), "Y": (255, 232, 140)}
    k = size // 16
    raw = b""
    for row in grid:
        line = b"".join(bytes(col[c]) * k for c in row)
        raw += (b"\x00" + line) * k
    def chunk(t, d):
        return struct.pack(">I", len(d)) + t + d + struct.pack(">I", zlib.crc32(t + d) & 0xffffffff)
    return (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", size, size, 8, 2, 0, 0, 0))
            + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b""))


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def log_message(self, *a):
        pass

    def send(self, code, body, ctype="application/json; charset=utf-8", cache="no-cache"):
        if isinstance(body, str):
            body = body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", cache)
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        u = urlparse(self.path)
        path = u.path
        try:
            if path == "/api/health":
                return self.send(200, '{"ok":true}')
            if path == "/api/state":
                return self.send(200, json.dumps(build_state(), ensure_ascii=False))
            if path == "/api/events":
                return self.events()
            if path == "/api/doc":
                p = safe_doc(parse_qs(u.query).get("path", [""])[0])
                if not p:
                    return self.send(403, '{"error":"chemin refusé"}')
                return self.send(200, p.read_bytes()[:2_000_000], "text/plain; charset=utf-8")
            m = re.fullmatch(r"/icon-(192|512)\.png", path)
            if m:
                return self.send(200, png(int(m.group(1))), "image/png", "max-age=86400")
            if path in STATIC:
                f = DASH / STATIC[path]
                return self.send(200, f.read_bytes(), TYPES[f.suffix])
            self.send(404, '{"error":"introuvable"}')
        except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError):
            pass

    def events(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream; charset=utf-8")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("X-Accel-Buffering", "no")
        self.end_headers()
        self.close_connection = True
        tail = Tail(ACT, ACT_OLD)
        last_ping = 0.0
        try:
            self.wfile.write(b"retry: 3000\n\n")
            while True:
                for line in tail.poll():
                    self.wfile.write(b"data: " + line.encode("utf-8") + b"\n\n")
                if time.time() - last_ping >= 15:
                    self.wfile.write(f"event: ping\ndata: {time.time():.0f}\n\n".encode())
                    last_ping = time.time()
                self.wfile.flush()
                time.sleep(1)
        except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError, OSError):
            pass


class Tail:
    """Suit activity.jsonl sans le garder ouvert (sinon Windows bloque la rotation du hook)."""

    def __init__(self, path, rotated):
        self.path, self.rotated = path, rotated
        st = self._stat(path)
        self.pos, self.ino, self.buf = (st.st_size, st.st_ino, b"") if st else (0, None, b"")

    @staticmethod
    def _stat(p):
        try:
            return p.stat()
        except OSError:
            return None

    def _read(self, p, start):
        try:
            with p.open("rb") as f:
                f.seek(start)
                return f.read()
        except OSError:
            return b""

    def poll(self):
        st = self._stat(self.path)
        if st is None:
            return []
        data = b""
        if st.st_ino != self.ino or st.st_size < self.pos:   # rotation : finir l'ancien fichier, repartir de 0
            old = self._stat(self.rotated)
            if old and self.ino is not None and old.st_ino == self.ino:
                data += self._read(self.rotated, self.pos)
            self.pos, self.ino = 0, st.st_ino
        if st.st_size > self.pos:
            chunk = self._read(self.path, self.pos)
            self.pos += len(chunk)
            data += chunk
        data = self.buf + data
        *lines, self.buf = data.split(b"\n")
        return [l.decode("utf-8", "replace").strip() for l in lines if l.strip()]


def selftest():
    import tempfile
    assert safe_doc("../.env") is None and safe_doc("/etc/passwd") is None and safe_doc("C:/x") is None
    assert safe_doc("..\\.env") is None and safe_doc("") is None
    j = journal_entries("# J\n## 2026-11-20 a\nx\n## 2026-11-22 b\ny\n## note\nz")
    assert [e["title"] for e in j][:2] == ["2026-11-22 b", "2026-11-20 a"], j
    now = time.time()
    iso = lambda t: datetime.fromtimestamp(t).astimezone().isoformat()
    assert live_status({"ts": iso(now - 10), "event": "PostToolUse"}, now) == "working"
    assert live_status({"ts": iso(now - 200), "event": "PostToolUse"}, now) == "idle"
    assert live_status({"ts": iso(now - 200), "event": "PreToolUse"}, now) == "working"
    assert live_status({"ts": iso(now - 5), "event": "Stop"}, now) == "idle"
    with tempfile.TemporaryDirectory() as d:
        a, b = Path(d) / "a.jsonl", Path(d) / "a.1.jsonl"
        a.write_text('{"x":0}\n')
        t = Tail(a, b)
        with a.open("a") as f:
            f.write('{"x":1}\n{"x":')
        assert t.poll() == ['{"x":1}']
        with a.open("a") as f:
            f.write('2}\n')
        a.replace(b)
        a.write_text('{"x":3}\n')
        assert t.poll() == ['{"x":2}', '{"x":3}'], "rotation"
    assert png(192)[:4] == b"\x89PNG"
    print("selftest ok")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        selftest()
    else:
        srv = ThreadingHTTPServer((HOST, PORT), Handler)
        srv.daemon_threads = True
        print(f"Dashboard : http://{HOST}:{PORT}", flush=True)
        srv.serve_forever()
