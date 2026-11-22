import sys, csv, html, subprocess, pathlib, os
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from common import page, shot, shot_fit, ASSETS
A = "#1D4ED8"; here = pathlib.Path(__file__).parent
log = subprocess.run([sys.executable, str(here/"run.py")], capture_output=True, text=True, encoding="utf-8",
                     env={**os.environ, "PYTHONIOENCODING": "utf-8"}).stdout
def table(path, bad=lambda r: False):
    rows = list(csv.DictReader(open(path, encoding="utf-8")))
    h = "".join(f"<th>{k}</th>" for k in rows[0])
    return f"<table><tr>{h}</tr>" + "".join(f"<tr class='{'warn' if bad(r) else ''}'>" + "".join(f"<td>{html.escape(v)}</td>" for v in r.values()) + "</tr>" for r in rows) + "</table>"
tmp = here/"_tmp.html"
def make(name, title, body, h):
    tmp.write_text(page(title, body, A), encoding="utf-8"); shot_fit(tmp, ASSETS/name, 1280, 12)
make("S1-1-donnees-entree.png", "Automatisation logistique – données d'entrée",
     "<h1>1. Commandes (orders.csv)</h1>" + table(here/"orders.csv") + "<h1 style='margin-top:20px'>2. Statuts transporteur (tracking.csv)</h1>" + table(here/"tracking.csv"), 800)
make("S1-2-execution.png", "Automatisation logistique – exécution du script",
     "<h1>python run.py</h1><pre>" + html.escape(log) + "</pre>", 500)
msgs = (here/"out/messages.txt").read_text(encoding="utf-8").split("\n\n--------\n\n")
cards = "".join(f"<div class=card>{html.escape(m).replace(chr(10), '<br>')}</div>" for m in msgs[:3])
alerte = html.escape((here/"out/alerte.txt").read_text(encoding="utf-8"))
make("S1-3-sorties.png", "Automatisation logistique – messages clients et alerte",
     f"<div style='display:grid;grid-template-columns:1.25fr 1fr;gap:22px'><div><h1>Messages clients générés (3 sur 4)</h1>{cards}</div><div><h1>Résumé d'alerte</h1><pre>{alerte}</pre></div></div>", 800)
tmp.unlink()
