"""Point d'entrée : python run.py <export.csv> [sortie.md]"""
import datetime
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "scripts"))
from rapport_stock import analyser_export, generer_rapport_markdown  # noqa: E402


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage : python run.py <export.csv> [sortie.md]")
        sys.exit(1)

    chemin_csv = sys.argv[1]
    chemin_sortie = sys.argv[2] if len(sys.argv) > 2 else "rapport-stock.md"

    lignes = analyser_export(chemin_csv)
    date_generation = datetime.date.today().strftime("%d/%m/%Y")
    rapport = generer_rapport_markdown(lignes, Path(chemin_csv).name, date_generation)

    Path(chemin_sortie).write_text(rapport, encoding="utf-8")
    print(rapport)
    print(f"\n--- Rapport écrit dans {chemin_sortie} ---")


if __name__ == "__main__":
    main()
