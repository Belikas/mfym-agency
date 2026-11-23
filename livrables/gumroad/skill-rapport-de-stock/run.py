"""Point d'entrée : python run.py <export.csv> [sortie.md]"""
import datetime
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

sys.path.insert(0, str(Path(__file__).parent / "scripts"))
from rapport_stock import (  # noqa: E402
    ColonneDupliquee,
    ColonnesManquantes,
    FichierIllisible,
    analyser_export,
    generer_rapport_markdown,
)


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage : python run.py <export.csv> [sortie.md]")
        sys.exit(1)

    chemin_csv = sys.argv[1]
    chemin_sortie = sys.argv[2] if len(sys.argv) > 2 else "rapport-stock.md"

    try:
        lignes, lignes_ignorees = analyser_export(chemin_csv)
    except (ColonnesManquantes, FichierIllisible, ColonneDupliquee) as e:
        print(f"Erreur : {e}")
        sys.exit(1)
    except Exception as e:
        print("Erreur : ce fichier n'a pas pu être traité. Contact direct "
              "indiqué sur la page de précommande si le problème persiste.")
        print(f"(détail technique : {type(e).__name__}: {e})")
        sys.exit(1)

    date_generation = datetime.date.today().strftime("%d/%m/%Y")
    rapport = generer_rapport_markdown(lignes, Path(chemin_csv).name, date_generation, lignes_ignorees)

    try:
        Path(chemin_sortie).write_text(rapport, encoding="utf-8")
    except Exception as e:
        print(f"Erreur : impossible d'écrire le rapport dans {chemin_sortie}. "
              "Vérifiez qu'il n'est pas ouvert dans Excel, que le dossier "
              "existe et n'est pas en lecture seule.")
        print(f"(détail technique : {type(e).__name__}: {e})")
        sys.exit(1)

    print(rapport)
    print(f"\n--- Rapport écrit dans {chemin_sortie} ---")


if __name__ == "__main__":
    main()
