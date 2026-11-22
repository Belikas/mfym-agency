"""Génère 8 factures PDF fictives (dossier invoices/). 3 contiennent une incohérence volontaire."""
import subprocess, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from common import CHROME
here = pathlib.Path(__file__).parent; out = here/"invoices"; out.mkdir(exist_ok=True)
SUP = [("Atelier Bois Lumière SARL","512 345 678 00019"),("Papeterie du Marais SAS","498 765 432 00027"),
       ("Nordik Emballages SARL","823 456 789 00011"),("Ferme des Trois Chênes EARL","401 234 567 00035"),
       ("Studio Cadrage SAS","790 123 456 00042"),("Mécano Services SARL","355 666 777 00058"),
       ("Atelier Bois Lumière SARL","512 345 678 00019"),("Verre & Fils SAS","612 987 654 00063")]
# (n°, date, lignes[(désignation, qté, pu)], override ttc, override ht)
INV = [("F-2026-0412","03/11/2026",[("Planches chêne 2 m",20,14.5),("Vernis mat 1 L",4,19.9)],None,None),
 ("2026/0187","05/11/2026",[("Ramettes A4 500 f.",30,4.2),("Classeurs",12,3.1)],None,None),
 ("NE-77120","06/11/2026",[("Cartons 40x30",200,0.85),("Ruban adhésif",24,1.6)],None,None),
 ("FT-0931","08/11/2026",[("Panier légumes",15,18.0),("Œufs (boîte 12)",40,3.2)],None,None),
 ("SC-2026-064","10/11/2026",[("Séance photo produits",1,420.0),("Retouches",10,12.0)],"612,00",None),
 ("MS-5520","12/11/2026",[("Révision chariot",2,85.0),("Pièces",1,64.5)],None,"250,00"),
 ("F-2026-0412","14/11/2026",[("Étagères",6,32.0)],None,None),
 ("VF-3308","17/11/2026",[("Bocaux 500 ml",120,0.74),("Couvercles",120,0.18)],None,None)]
f = lambda x: f"{x:,.2f}".replace(",", " ").replace(".", ",")
for i, (n, date, lines, ttc_o, ht_o) in enumerate(INV, 1):
    name, siret = SUP[i-1]
    ht = sum(q*p for _, q, p in lines); tva = round(ht*0.2, 2); ttc = ht+tva
    ht_s = ht_o or f(ht); ttc_s = ttc_o or f(ttc)
    rows = "".join(f"<tr><td>{d}</td><td>{q}</td><td>{f(p)}</td><td>{f(q*p)}</td></tr>" for d, q, p in lines)
    (out/f"facture-{i:02d}.html").write_text(f"""<!doctype html><meta charset=utf-8><style>
body{{font:14px Arial;margin:50px;color:#222}}h1{{font-size:26px;margin:0}}table{{width:100%;border-collapse:collapse;margin:30px 0}}
th{{background:#eee;text-align:left;padding:8px}}td{{padding:8px;border-bottom:1px solid #ddd}}.r{{text-align:right}}
.wm{{color:#b91c1c;font-weight:bold;border:2px solid #b91c1c;display:inline-block;padding:3px 10px}}</style>
<h1>{name}</h1><p>SIRET {siret}<br>12 rue de l'Exemple, 75000 Ville</p><span class=wm>EXEMPLE – DONNÉES FICTIVES</span>
<h2>Facture n° {n}</h2><p>Date : {date}<br>Client : Boutique Démo SARL</p>
<table><tr><th>Désignation</th><th>Qté</th><th>PU HT</th><th>Total HT</th></tr>{rows}</table>
<p class=r>Total HT : {ht_s} €<br>TVA 20 % : {f(tva)} €<br><b>Total TTC : {ttc_s} €</b></p>""", encoding="utf-8")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
        f"--print-to-pdf={out/f'facture-{i:02d}.pdf'}", (out/f"facture-{i:02d}.html").resolve().as_uri()], check=True, capture_output=True)
    (out/f"facture-{i:02d}.html").unlink()
print(len(INV), "PDF générés")
