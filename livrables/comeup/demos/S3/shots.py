import sys, csv, html, pathlib, pymupdf
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from common import page, shot_fit, ASSETS
A = "#0F766E"; here = pathlib.Path(__file__).parent; tmp = here/"_tmp"; tmp.mkdir(exist_ok=True)
def img(n):
    pymupdf.open(here/f"invoices/facture-{n:02d}.pdf")[0].get_pixmap(dpi=110, clip=pymupdf.Rect(0, 0, 595, 520)).save(tmp/f"f{n}.png"); return f"f{n}.png"
fr = lambda v: f"{float(v):,.2f}".replace(",", " ").replace(".", ",") + " €"
rows = list(csv.DictReader(open(here/"extraction.csv", encoding="utf-8")))
def make(name, title, body, h):
    (tmp/"p.html").write_text(page(title, body, A), encoding="utf-8"); shot_fit(tmp/"p.html", ASSETS/name, 1280, 12)
im = "style='width:100%;border:1px solid #cbd5e1;box-shadow:0 2px 8px #0003'"
make("S3-1-pdf-entree.png", "Extraction de documents – PDF en entrée",
     f"<div style='display:grid;grid-template-columns:1fr 1fr;gap:24px'><div><h1>Facture PDF fictive (entrée)</h1><img src={img(2)} {im}></div>"
     f"<div><h1>Ce que les règles lisent (puis Claude en recoupement)</h1><pre>Fournisseur : Papeterie du Marais SAS\nSIRET       : 498 765 432 00027\nN° facture  : 2026/0187\nDate        : 05/11/2026\nTotal HT    : 163,20 €\nTVA         : 32,64 €\nTotal TTC   : 195,84 €\nContrôles   : OK\n\nClaude (IA) relit le même texte :\nmêmes 5 champs, aucun écart</pre></div></div>", 720)
th = "".join(f"<th>{k}</th>" for k in ("fichier","fournisseur","numero","date","ht","tva","ttc","Claude (IA)","contrôle"))
tr = "".join(f"<tr class='{'warn' if r['alertes'] else ''}'><td>{r['fichier']}</td><td>{html.escape(r['fournisseur'])}</td><td>{html.escape(r['numero'])}</td><td>{r['date']}</td><td>{fr(r['ht'])}</td><td>{fr(r['tva'])}</td><td>{fr(r['ttc'])}</td><td class='{'bad' if r['ia']!='OK' else 'ok'}'>{'OK, mêmes valeurs' if r['ia']=='OK' else 'écart'}</td><td class='{'bad' if r['alertes'] else 'ok'}'>{'À VÉRIFIER' if r['alertes'] else 'OK'}</td></tr>" for r in rows)
make("S3-2-tableau-extrait.png", "Extraction de documents – tableau obtenu (8 PDF)",
     f"<h1>extraction.csv : 8 factures, 4 à vérifier – Claude et les règles d'accord sur 8/8</h1><table><tr>{th}</tr>{tr}</table>", 520)
bad = rows[4]
make("S3-3-incoherence.png", "Extraction de documents – incohérence signalée",
     f"<div style='display:grid;grid-template-columns:1fr 1fr;gap:24px'><div><h1>Facture {bad['fichier']}</h1><img src={img(5)} {im}></div>"
     f"<div><h1>Signalement automatique (règles + relecture Claude : mêmes montants lus)</h1><div class=card style='border-color:#b91c1c'><b>{bad['numero']}</b> – {html.escape(bad['fournisseur'])}<br><br>"
     f"Total HT {fr(bad['ht'])} + TVA {fr(bad['tva'])} = <b>{fr(float(bad['ht'])+float(bad['tva']))}</b><br>Total TTC écrit sur la facture : <b>{fr(bad['ttc'])}</b><br><br><span class=bad>{html.escape(bad['alertes'])}</span></div>"
     f"<p>Le script ne corrige pas : il marque la ligne pour relecture humaine.</p></div></div>", 720)
