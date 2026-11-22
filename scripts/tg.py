"""Telegram : envoi + règles de bruit. Sans token, tout va dans logs/alerts.log.
CLI : python scripts/tg.py alert|info|digest "texte"   (digest sans texte = calculé)"""
import json, sys, urllib.parse, urllib.request
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
M = ROOT / "memory"
LOGS = ROOT / "logs"
ENV = ROOT / ".env"


def env() -> dict:
    out = {}
    for line in ENV.read_text(encoding="utf-8").splitlines():
        if "=" in line and not line.lstrip().startswith("#"):
            k, v = line.split("=", 1)
            out[k.strip()] = v.strip()
    return out


def set_env(key: str, value: str):
    lines, found = ENV.read_text(encoding="utf-8").splitlines(), False
    for i, line in enumerate(lines):
        if line.split("=", 1)[0].strip() == key:
            lines[i], found = f"{key}={value}", True
    if not found:
        lines.append(f"{key}={value}")
    ENV.write_text("\n".join(lines) + "\n", encoding="utf-8")


def api(method: str, **params):
    token = env().get("TELEGRAM_BOT_TOKEN")
    if not token:
        raise RuntimeError("pas de token")
    data = urllib.parse.urlencode({k: json.dumps(v) if isinstance(v, (dict, list)) else v
                                   for k, v in params.items()}).encode()
    with urllib.request.urlopen(f"https://api.telegram.org/bot{token}/{method}", data, timeout=70) as r:
        return json.loads(r.read())["result"]


def log_local(kind: str, text: str):
    LOGS.mkdir(exist_ok=True)
    with (LOGS / "alerts.log").open("a", encoding="utf-8") as f:
        f.write(f"{datetime.now().isoformat(timespec='seconds')} [{kind}] {text}\n")


def send(text: str, kind: str = "info", buttons=None) -> int | None:
    """kind : alert | approval | task | digest | info. 'info' : 1 par jour max (CLAUDE.md)."""
    if kind == "info":
        flag = ROOT / "run" / f"info-{date.today()}.flag"
        if flag.exists():
            log_local("info-dropped", text)
            return None
        flag.parent.mkdir(exist_ok=True)
        flag.touch()
    e = env()
    if not (e.get("TELEGRAM_BOT_TOKEN") and e.get("TELEGRAM_CHAT_ID")):
        log_local(kind, text)
        return None
    params = {"chat_id": e["TELEGRAM_CHAT_ID"], "text": text[:4000]}
    if buttons:
        params["reply_markup"] = {"inline_keyboard": buttons}
    try:
        return api("sendMessage", **params)["message_id"]
    except Exception as ex:
        log_local(kind, f"{text} (échec envoi : {ex})")
        return None


def load(name):
    return json.loads((M / name).read_text(encoding="utf-8"))


def digest() -> str:
    """5 lignes max : revenu vs cible, tests, ce qui attend Baptiste."""
    rev = load("revenue.json")["entries"]
    month = date.today().strftime("%Y-%m")
    net = sum(e["net_eur"] for e in rev if e["date"].startswith(month))
    exps = [json.loads(p.read_text(encoding="utf-8")) for p in (M / "experiments").glob("*.json")]
    running = [x for x in exps if x["status"] in ("running", "blocked", "ready")]
    appr = [a for a in load("approvals.json")["approvals"] if a["status"] == "pending"]
    tasks = [t for t in load("tasks.json")["tasks"] if t["status"] == "open"]
    h = sum(t["est_minutes"] for t in tasks) / 60
    lines = [f"Revenu net {month} : {net:.0f} € / 1000 €",
             f"Tests : " + (", ".join(f"{x['title']} ({x['status']}, kill {x['kill_date']})" for x in running[:3]) or "aucun")]
    lines.append(f"Pour toi : {len(appr)} approbation(s), {len(tasks)} tâche(s) (~{h:.1f} h)" if appr or tasks
                 else "Rien n'attend ta réponse.")
    return "\n".join(lines)


if __name__ == "__main__":
    kind = sys.argv[1]
    text = sys.argv[2] if len(sys.argv) > 2 else (digest() if kind == "digest" else "")
    send(text, kind)
