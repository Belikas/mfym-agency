"""Enregistre les 3 videos de demo ComeUp (S1, S2, S3) en headless : commandes REELLEMENT executees, sortie streamee en direct.
Usage : python scripts/with_token.py python scripts/record_demos.py [S1 S2 S3]   (with_token : S2/S3 appellent Claude via la CLI)
Sortie : livrables/comeup/videos/S*.mp4 + frames/S*-{1,2,3}.png. Prerequis : pip install playwright && python -m playwright install chromium ; ffmpeg dans le PATH.
S2/S3 tournent dans une copie temporaire pour ne pas modifier unanswered.log / extraction.csv des demos."""
import sys, os, re, csv, html, time, shutil, tempfile, pathlib, subprocess, threading, queue, json, urllib.parse as up
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
DEMOS = ROOT / "livrables/comeup/demos"
OUT = ROOT / "livrables/comeup/videos"
BANNER = "Démo réelle — données fictives"
PAGE = """<meta charset=utf-8><style>
body{margin:0;background:#0d1117;color:#e6edf3;font:22px/1.35 Consolas,'Cascadia Mono',monospace;height:720px;overflow:hidden}
#bar{height:44px;background:#161b22;display:flex;align-items:center;padding:0 18px;font:18px 'Segoe UI',sans-serif;color:#8b949e;border-bottom:1px solid #30363d}
#t{padding:14px 22px;height:520px;overflow:hidden;white-space:pre-wrap;word-break:break-all}
#cap{position:fixed;left:0;right:0;bottom:56px;min-height:48px;background:#1f6feb;color:#fff;font:600 24px 'Segoe UI',sans-serif;padding:10px 22px;box-sizing:border-box}
#ban{position:fixed;left:0;right:0;bottom:0;height:56px;background:#facc15;color:#0f172a;font:700 26px 'Segoe UI',sans-serif;display:flex;align-items:center;justify-content:center}
.p{color:#7ee787}.hl{background:#5a1d1d;color:#ffb4b4;display:block;border-left:6px solid #f85149;padding-left:8px;font-weight:700}
table{word-break:normal;border-collapse:collapse;font-size:17px;width:100%}td,th{white-space:nowrap;border-bottom:1px solid #30363d;padding:4px 8px;text-align:left;vertical-align:top}th{color:#8b949e}
td:last-child{white-space:normal}tr.bad td{background:#3a2a0a}tr.err td{background:#5a1d1d;color:#ffb4b4;font-weight:700}
</style><div id=bar>{title}</div><div id=t></div><div id=cap></div><div id=ban>{banner}</div>"""
ANSI = re.compile(r"\x1b\[[0-9;?]*[A-Za-z]")


class Term:
    def __init__(self, page, title):
        self.p = page
        page.set_content(PAGE.replace("{title}", html.escape(title)).replace("{banner}", BANNER))

    def cap(self, s): self.p.evaluate("s=>document.getElementById('cap').textContent=s", s)
    def add(self, s, cls=""):
        self.p.evaluate("([s,c])=>{const t=document.getElementById('t'),e=document.createElement('span');e.className=c;e.textContent=s;t.appendChild(e);t.scrollTop=t.scrollHeight}", [s, cls])
    def html(self, h): self.p.evaluate("h=>{const t=document.getElementById('t');t.innerHTML=h;t.style.whiteSpace='normal'}", h)
    def clear(self): self.p.evaluate("()=>{const t=document.getElementById('t');t.innerHTML='';t.style.whiteSpace='pre-wrap'}")
    def type(self, cmd):
        self.add("$ ", "p")
        for ch in cmd: self.add(ch); self.p.wait_for_timeout(35)
        self.add("\n"); self.p.wait_for_timeout(500)

    def run(self, cmd, cwd, env=None, shell=False, pace=0.02):
        """Lance vraiment la commande, affiche chaque ligne des son arrivee. Renvoie (code, duree)."""
        t0 = time.time()
        pr = subprocess.Popen(cmd, cwd=cwd, shell=shell, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                              env={**os.environ, "PYTHONIOENCODING": "utf-8", "PYTHONUNBUFFERED": "1", **(env or {})})
        q = queue.Queue()
        threading.Thread(target=lambda: ([q.put(l) for l in iter(pr.stdout.readline, b"")], q.put(None)), daemon=True).start()
        while True:
            try: l = q.get(timeout=2)
            except queue.Empty: self.add("."); continue  # rien depuis 2 s : point de progression
            if l is None: break
            self.add(ANSI.sub("", l.decode("utf-8", "replace"))); self.p.wait_for_timeout(int(pace * 1000))
        return pr.wait(), time.time() - t0

    def show_file(self, path, hl=lambda l: False, per_line=0.25):
        for l in pathlib.Path(path).read_text(encoding="utf-8").splitlines(True):
            self.add(l, "hl" if hl(l) else ""); self.p.wait_for_timeout(int(per_line * 1000))


def capture(cmd, cwd):
    """Execute reellement la commande AVANT la video (sortie horodatee) : ([(offset_s, ligne)], duree, heure de debut, code)."""
    t0 = time.time(); stamp = time.strftime("%H:%M:%S"); pr = subprocess.Popen(cmd, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out = [(time.time() - t0, ANSI.sub("", l.decode("utf-8", "replace"))) for l in iter(pr.stdout.readline, b"")]
    return out, time.time() - t0, stamp, pr.wait()


def record(name, body):
    """Ouvre un contexte 1280x720 avec video, execute body(page), convertit en MP4 H.264, extrait 3 images cles."""
    OUT.mkdir(parents=True, exist_ok=True); (OUT / "frames").mkdir(exist_ok=True)
    tmp = pathlib.Path(tempfile.mkdtemp())
    with sync_playwright() as pw:
        br = pw.chromium.launch(); ctx = br.new_context(viewport={"width": 1280, "height": 720}, record_video_dir=str(tmp), record_video_size={"width": 1280, "height": 720})
        page = ctx.new_page(); body(page); page.wait_for_timeout(1500); ctx.close(); br.close()
    webm = next(tmp.glob("*.webm")); mp4 = OUT / f"{name}.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(webm), "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", "25", "-an", str(mp4)], check=True)
    dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(mp4)]))
    for i, f in enumerate((0.2, 0.55, 0.9), 1):
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{dur*f:.1f}", "-i", str(mp4), "-frames:v", "1", str(OUT / "frames" / f"{name}-{i}.png")], check=True)
    shutil.rmtree(tmp, ignore_errors=True); print(f"{name}: {dur:.1f} s -> {mp4}")


def copy_llm(tmp):
    """llm.py de la demo + --setting-sources '' et cwd neutre : sinon les hooks / CLAUDE.md utilisateur polluent la reponse de Claude."""
    src = (DEMOS / "llm.py").read_text(encoding="utf-8"); assert '"--output-format", "json"]' in src
    (tmp / "llm.py").write_text(src.replace('"--output-format", "json"]', '"--output-format", "json", "--setting-sources", ""]').replace("capture_output=True", "cwd=os.path.abspath(os.sep), capture_output=True"), encoding="utf-8")


def s1(page):
    d = DEMOS / "S1"; wf = json.loads((d / "n8n/workflow.json").read_text(encoding="utf-8"))
    n8n_out = N8N; prev = 0
    t = Term(page, "S1 — Logistique : workflow n8n")
    t.cap("Un vrai fichier de workflow n8n, pas une maquette."); t.type("cat n8n/workflow.json | nœuds")
    t.add(f"workflow « {wf['name']} » — {len(wf['nodes'])} nœuds :\n")
    for n in wf["nodes"]: t.add(f"  - {n['name']}  ({n['type'].split('.')[-1]})\n"); page.wait_for_timeout(250)
    page.wait_for_timeout(1500); t.clear()
    t.cap("Exécution réelle avec la CLI n8n 2.48.7 (sortie rejouée, attentes abrégées)."); t.type("sh n8n/run_n8n.sh")
    for off, l in n8n_out[0]:  # replay des lignes reelles, attentes plafonnees a 0,25 s
        t.add(l); page.wait_for_timeout(int(min(max(off - prev, 0.03), 0.25) * 1000)); prev = off
    t.add(f"\n[exécution réelle de {n8n_out[2]} : sortie {n8n_out[3]}, {n8n_out[1]:.0f} s ; attentes abrégées dans la vidéo]\n", "p"); page.wait_for_timeout(2500); t.clear()
    t.cap("Détection + messages générés par le script de référence (mêmes 4 colis)."); t.type("python run.py")
    t.run([sys.executable, "run.py"], d); page.wait_for_timeout(1000); t.type("cat out/alerte.txt")
    t.show_file(d / "out/alerte.txt", lambda l: l.startswith("- CMD"), 0.5); page.wait_for_timeout(5000); t.clear()
    t.cap("Messages clients prêts à envoyer (aucun e-mail envoyé dans la démo)."); t.type("cat out/messages.txt")
    t.show_file(d / "out/messages.txt", lambda l: l.startswith("Objet"), 0.18); page.wait_for_timeout(2500)


def s2(page):
    tmp = pathlib.Path(tempfile.mkdtemp()); shutil.copytree(DEMOS / "S2", tmp / "S2"); copy_llm(tmp)
    (tmp / "S2/unanswered.log").unlink(missing_ok=True)
    srv = subprocess.Popen([sys.executable, str(tmp / "S2/app.py")], env={**os.environ, "S2_LLM": "1", "PYTHONIOENCODING": "utf-8"}); time.sleep(1.5)
    ban = f"if(!document.getElementById('ban')){{const b=document.createElement('div');b.id='ban';b.textContent='{BANNER}';b.style.cssText='position:fixed;left:0;right:0;bottom:0;height:56px;background:#facc15;color:#0f172a;font:700 26px Segoe UI,sans-serif;display:flex;align-items:center;justify-content:center;z-index:99';document.body.appendChild(b)}}"
    try:
        page.goto("http://127.0.0.1:8765/"); page.evaluate(ban)
        for q in ("Combien coûte la livraison express ?", "Quelle est la durée de la garantie ?", "Avez-vous un magasin à Lyon ?"):
            n = page.locator("#log .m").count(); page.click("#q"); page.keyboard.type(q, delay=60); page.wait_for_timeout(400); page.keyboard.press("Enter")
            page.wait_for_function(f"document.querySelectorAll('#log .m').length>={n+2}", timeout=90000)
            page.wait_for_timeout(10000)
        page.goto("http://127.0.0.1:8765/log"); page.evaluate(ban); page.wait_for_timeout(8000)
        t = Term(page, "S2 — Assistant sur documents"); t.cap("Question hors périmètre : « je ne sais pas », journalisée pour l'équipe."); t.type("cat unanswered.log")
        t.show_file(tmp / "S2/unanswered.log", per_line=0.4); page.wait_for_timeout(6000)
    finally: srv.terminate(); shutil.rmtree(tmp, ignore_errors=True)


def s3(page):
    tmp = pathlib.Path(tempfile.mkdtemp()); shutil.copytree(DEMOS / "S3", tmp / "S3", ignore=shutil.ignore_patterns("_tmp")); copy_llm(tmp)
    try:
        t = Term(page, "S3 — Extraction de factures : Claude vs règles"); t.cap("8 factures PDF fictives lues par des règles ET relues par Claude."); t.type("python extract.py --ai")
        code, dur = t.run([sys.executable, "extract.py", "--ai"], tmp / "S3", pace=0.3); t.add(f"\n[sortie {code} — {dur:.0f} s, appels Claude réels]\n", "p"); page.wait_for_timeout(2500)
        rows = list(csv.DictReader(open(tmp / "S3/extraction.csv", encoding="utf-8"))); ok = sum(r["ia"] == "OK" for r in rows)
        def table(mark=None):
            return ("<table><tr><th>fichier<th>numéro<th>HT<th>TVA<th>TTC<th>IA<th>alertes</tr>" + "".join(
                f"<tr class='{'err' if r['fichier'] == mark else 'bad' if r['alertes'] else ''}'><td>{r['fichier']}<td>{html.escape(r['numero'])}<td>{r['ht']}<td>{r['tva']}<td>{r['ttc']}<td>{r['ia']}<td>{html.escape(r['alertes'])}</tr>" for r in rows) + "</table>")
        t.clear(); t.add("$ ", "p"); t.add("cat extraction.csv   (colonne ia = relecture Claude)\n"); t.cap(f"Claude relit chaque facture : {ok}/{len(rows)} identiques aux règles (ne mesure pas la précision réelle).")
        t.html("<div style='font-size:20px;margin-bottom:8px'><span class=p>$ </span>cat extraction.csv</div>" + table()); page.wait_for_timeout(8000)
        bad = next(r for r in rows if "HT+TVA" in r["alertes"] and "somme" not in r["alertes"])["fichier"]
        t.cap("Incohérence détectée automatiquement : HT + TVA ≠ TTC. Aucune correction silencieuse.")
        t.html("<div style='font-size:20px;margin-bottom:8px'><span class=p>$ </span>cat extraction.csv</div>" + table(bad)); page.wait_for_timeout(12000)
    finally: shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    for n in (sys.argv[1:] or ["S1", "S2", "S3"]):
        if n == "S1": N8N = capture([shutil.which("sh") or "C:/Program Files/Git/bin/sh.exe", "n8n/run_n8n.sh"], DEMOS / "S1")  # avant la video : sinon l'attente est filmee
        record(n, {"S1": s1, "S2": s2, "S3": s3}[n])
