# Stock Report — installation

Claude Code assistant that turns a WMS export (CSV) into a readable stock
report: stockouts, overstocks, inventory discrepancies, SKUs to watch.

Note: the assistant's reports, error messages, and expected column headers
are currently in French (see `SKILL.md`) — this first version was built for
the French market and hasn't been localized yet.

## Installation (4 steps)

1. **Copy this entire folder** (`skill-rapport-de-stock`) into your
   project's `.claude/skills/` folder (create `.claude/skills/` if it
   doesn't exist yet).
2. **Check that Python is installed**: open a terminal and type
   `python --version`. If nothing shows up, install Python from
   [python.org](https://python.org) (check the "Add to PATH" box during
   installation).
3. **Test it with the sample file provided**: in a terminal, go to the
   skill's folder, then run:
   ```
   python run.py exemple-export-wms.csv
   ```
   A report should print to the screen and be written to
   `rapport-stock.md`.
4. **Use your own export**: export your WMS to CSV with the columns listed
   in `SKILL.md`, then run `python run.py mon-export.csv`.

In Claude Code, once the folder is copied into `.claude/skills/`, just
hand it your export file and ask for a stock report: the skill triggers
automatically.

## Troubleshooting

- `ModuleNotFoundError`: you're using a Python version that's too old or
  incomplete — reinstall from python.org.
- The script prints `Erreur : colonne(s) manquante(s) : ...` ("missing
  column(s)") and stops: an expected column is missing from your export.
  The message lists the expected columns and the ones found in your file —
  rename your headers to match (spaces, capitalization, and accents are
  tolerated, not the name itself, see `SKILL.md`).
- A SKU has an empty cell or a non-numeric value (stock, min, max,
  outbound, lead time…): that row is skipped, not the rest of the report.
  It shows up in the "Lignes ignorées" ("Skipped rows") section of the
  generated report, with the reason.
- The report is empty or wrong: check that your CSV's column headers match
  the ones listed in `SKILL.md`.
- The script prints `Erreur : colonne en double : ...` ("duplicate
  column") and stops: your export contains the same column twice. The
  script refuses the file instead of choosing for you, because it can't
  know which of the two holds the right value — and a wrong value would
  produce a false report without saying so. Delete the extra column in
  Excel, then run it again.
- The script prints a report-writing error: the output file is probably
  still open in Excel, or the folder is read-only. Close the file, or
  point to a different output folder.
- The script prints "ce fichier est un classeur Excel, pas un CSV" ("this
  file is an Excel workbook, not a CSV") or an encoding error: your file
  isn't a standard text CSV (often an Excel file renamed to `.csv` without
  re-exporting) — in Excel, go to File > Save As > CSV UTF-8, then run it
  again.
- Anything else: direct contact listed on the presale page.
