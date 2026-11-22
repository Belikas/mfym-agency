"""Extrait les champs des PDF (texte + regex, déterministe, sans API) vers extraction.csv et signale les incohérences."""
import pymupdf, re, csv, pathlib, collections, sys
sys.stdout.reconfigure(encoding="utf-8")
here = pathlib.Path(__file__).parent
num = lambda s: float(s.replace(" ", "").replace(" ", "").replace(",", "."))
fr = lambda v: f"{v:,.2f}".replace(",", " ").replace(".", ",") + " €"
AI = "--ai" in sys.argv   # étape IA : Claude (CLI headless) relit le texte du PDF et renvoie les champs en JSON ; écart avec les règles = alerte
if AI:
    import json; sys.path.insert(0, str(here.parent)); import llm
rows = []
for p in sorted((here/"invoices").glob("*.pdf")):
    t = "\n".join(pg.get_text() for pg in pymupdf.open(p)).replace("\xa0", " ")
    g = lambda rx: (m.group(1).strip() if (m := re.search(rx, t)) else "")
    ht, tva, ttc = (num(g(rf"{k}[^:\n]*:\s*([\d ]+,\d{{2}})")) for k in ("Total HT", "TVA", "Total TTC"))
    block = t.split("Total HT :")[0]
    nums = re.findall(r"\n(\d+)\n([\d ]+,\d{2})\n([\d ]+,\d{2})", block)
    lines_sum = round(sum(num(c) for _, _, c in nums), 2)
    ai_alert = []
    if AI:
        raw = llm.ask("Extrais de cette facture le numéro, la date (JJ/MM/AAAA), le total HT, la TVA et le total TTC (nombres avec point décimal). Réponds uniquement par un objet JSON de clés numero, date, ht, tva, ttc.\n\n" + t)
        a = json.loads(raw[raw.index("{"):raw.rindex("}") + 1])
        ai_alert = [f"IA ≠ règles sur {k}" for k, v in (("numero", g(r"Facture n° (\S+)")), ("date", g(r"Date : (\S+)")), ("ht", ht), ("tva", tva), ("ttc", ttc)) if str(a[k]).strip() != str(v)]
    rows.append(dict(fichier=p.name, fournisseur=t.split("\n")[0].strip(), siret=g(r"SIRET ([\d ]+)"), numero=g(r"Facture n° (\S+)"),
                     date=g(r"Date : (\S+)"), ht=ht, tva=tva, ttc=ttc, somme_lignes=lines_sum, alertes=ai_alert))
cnt = collections.Counter((r["fournisseur"], r["numero"]) for r in rows)
for r in rows:
    if abs(r["somme_lignes"] - r["ht"]) > 0.01: r["alertes"].append(f"somme des lignes {fr(r['somme_lignes'])} ≠ Total HT {fr(r['ht'])}")
    if abs(r["ht"]*0.2 - r["tva"]) > 0.01: r["alertes"].append("TVA ≠ 20 % du HT")
    if abs(r["ht"] + r["tva"] - r["ttc"]) > 0.01: r["alertes"].append(f"HT+TVA = {fr(r['ht']+r['tva'])} ≠ TTC {fr(r['ttc'])}")
    if any(c > 1 and r["numero"] == k[1] for k, c in cnt.items()): r["alertes"].append("numéro de facture en doublon")
with open(here/"extraction.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, rows[0].keys()); w.writeheader()
    for r in rows: w.writerow({**r, "alertes": " ; ".join(r["alertes"])})
for r in rows: print(r["fichier"], r["numero"], r["ttc"], "OK" if not r["alertes"] else "A VERIFIER: " + " ; ".join(r["alertes"]))
