# S3 – Extraction de factures PDF (Python, données fictives)
`pip install pymupdf` puis : `python gen_pdfs.py` (8 PDF dans invoices/, Chrome requis), `python extract.py` (extraction.csv + contrôles HT/TVA/TTC, somme des lignes, doublons), `python shots.py` (captures).
Extraction déterministe (texte + regex) : fonctionne sur PDF texte au gabarit connu, pas sur scans. 3 factures ont une erreur volontaire, la 4e alerte est un numéro en doublon.
Étape IA (testée le 22/11, 8/8 factures identiques aux règles) : `python extract.py --ai` (via scripts/with_token.py) compare l'extraction de `claude -p` (../llm.py) aux règles, colonne `ia` de extraction.csv, et signale les écarts. Pas testée sur scans.
