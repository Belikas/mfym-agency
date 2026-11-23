"""Logique du rapport de stock : lit un export WMS (CSV) et classe chaque
référence en rupture / sous seuil mini / à surveiller / surstock / écart
d'inventaire. Aucune dépendance externe (stdlib uniquement).

Colonnes attendues dans le CSV (en-têtes exacts, ordre libre) :
reference, designation, emplacement, stock_theorique,
stock_physique_inventaire, date_inventaire, stock_mini, stock_maxi,
sorties_30j, delai_reappro_jours, fournisseur
"""
from __future__ import annotations

import csv
import io
import sys
import unicodedata
from dataclasses import dataclass, field

ECART_SIGNIFICATIF_UNITES = 10  # ponytail: seuil fixe, affiner par métier si besoin

COLONNES_ATTENDUES = [
    "reference", "designation", "emplacement", "stock_theorique",
    "stock_physique_inventaire", "date_inventaire", "stock_mini", "stock_maxi",
    "sorties_30j", "delai_reappro_jours", "fournisseur",
]


class ColonnesManquantes(Exception):
    """Levée quand l'export n'a pas (au nom près) les colonnes attendues."""

    def __init__(self, attendues: list[str], trouvees: list[str]):
        manquantes = [c for c in attendues if c not in trouvees]
        super().__init__(
            "colonne(s) manquante(s) : " + ", ".join(manquantes) + ".\n"
            "Colonnes attendues : " + ", ".join(attendues) + ".\n"
            "Colonnes trouvées dans votre fichier : " + ", ".join(trouvees) + ".\n"
            "Renommez les en-têtes de votre export pour qu'ils correspondent "
            "(espaces, majuscules et accents sont tolérés, pas le nom lui-même), "
            "voir SKILL.md."
        )


class FichierIllisible(Exception):
    """Levée quand le fichier n'est pas un CSV texte exploitable (mauvais
    format ou encodage non reconnu)."""


# ponytail: 2 signatures binaires couvrent le cas le plus courant (Excel
# renommé en .csv), pas une détection générale de type de fichier.
_SIGNATURES_BINAIRES = {
    b"PK": "un classeur Excel (.xlsx)",
    b"\xd0\xcf": "un classeur Excel (.xls)",
}

_ENCODAGES_ESSAYES = ("utf-8-sig", "utf-8", "cp1252")


def _lire_texte(chemin_csv: str) -> str:
    """Lit le fichier en tolérant les encodages Windows FR courants et en
    détectant un fichier binaire renommé en .csv, pour qu'aucune lecture ne
    puisse faire remonter une trace Python brute à l'utilisateur."""
    donnees = open(chemin_csv, "rb").read()
    for signature, nom in _SIGNATURES_BINAIRES.items():
        if donnees.startswith(signature):
            raise FichierIllisible(
                f"ce fichier est {nom}, pas un CSV ; dans Excel, "
                "Fichier > Enregistrer sous > CSV UTF-8."
            )
    for encodage in _ENCODAGES_ESSAYES:
        try:
            return donnees.decode(encodage)
        except UnicodeDecodeError:
            continue
    raise FichierIllisible(
        "l'encodage de ce fichier n'est pas reconnu (ni UTF-8 ni Windows "
        "cp1252) ; réexportez-le en CSV UTF-8."
    )


def _normaliser_entete(entete: str) -> str:
    """Tolère espaces, majuscules et accents dans les en-têtes de colonnes."""
    sans_accents = unicodedata.normalize("NFKD", entete.strip().lower())
    sans_accents = "".join(c for c in sans_accents if not unicodedata.combining(c))
    return sans_accents.replace(" ", "_")


@dataclass
class LigneAnalysee:
    reference: str
    designation: str
    emplacement: str
    fournisseur: str
    stock_theorique: int
    stock_physique: int
    date_inventaire: str
    stock_mini: int
    stock_maxi: int
    sorties_30j: int
    delai_reappro_jours: int
    flags: list[str] = field(default_factory=list)
    couverture_jours: float | None = None
    ecart: int = 0


def _to_int(value: str, colonne: str) -> int:
    try:
        return int(float(str(value).strip().replace(",", ".")))
    except ValueError:
        raise ValueError(f"colonne {colonne} invalide : valeur '{value}' n'est pas un nombre") from None


def charger_lignes(chemin_csv: str) -> list[dict]:
    texte = _lire_texte(chemin_csv)
    premiere_ligne = texte.split("\n", 1)[0]
    delimiteur = ";" if premiere_ligne.count(";") > premiere_ligne.count(",") else ","

    reader = csv.DictReader(io.StringIO(texte), delimiter=delimiteur)
    entetes_brutes = reader.fieldnames or []
    mapping = {}
    for brute in entetes_brutes:
        normalisee = _normaliser_entete(brute)
        if normalisee in COLONNES_ATTENDUES:
            mapping[brute] = normalisee
    trouvees = sorted(set(mapping.values()))
    if any(c not in trouvees for c in COLONNES_ATTENDUES):
        raise ColonnesManquantes(COLONNES_ATTENDUES, entetes_brutes)
    return [{mapping[k]: v for k, v in row.items() if k in mapping} for row in reader]


def analyser_ligne(row: dict) -> LigneAnalysee:
    stock_theo = _to_int(row["stock_theorique"], "stock_theorique")
    stock_phys = _to_int(row["stock_physique_inventaire"], "stock_physique_inventaire")
    mini = _to_int(row["stock_mini"], "stock_mini")
    maxi = _to_int(row["stock_maxi"], "stock_maxi")
    sorties = _to_int(row["sorties_30j"], "sorties_30j")
    delai = _to_int(row["delai_reappro_jours"], "delai_reappro_jours")

    ligne = LigneAnalysee(
        reference=row["reference"],
        designation=row["designation"],
        emplacement=row["emplacement"],
        fournisseur=row["fournisseur"],
        stock_theorique=stock_theo,
        stock_physique=stock_phys,
        date_inventaire=row["date_inventaire"],
        stock_mini=mini,
        stock_maxi=maxi,
        sorties_30j=sorties,
        delai_reappro_jours=delai,
        ecart=stock_theo - stock_phys,
    )

    conso_jour = sorties / 30
    ligne.couverture_jours = (stock_theo / conso_jour) if conso_jour > 0 else None

    if stock_theo <= 0:
        ligne.flags.append("rupture")
    elif stock_theo <= mini:
        ligne.flags.append("sous_seuil")
    elif ligne.couverture_jours is not None and ligne.couverture_jours < delai:
        ligne.flags.append("a_surveiller")

    if stock_theo > maxi:
        ligne.flags.append("surstock_dormant" if sorties == 0 else "surstock")

    if abs(ligne.ecart) >= ECART_SIGNIFICATIF_UNITES:
        ligne.flags.append("ecart_inventaire")

    return ligne


def analyser_export(chemin_csv: str) -> tuple[list[LigneAnalysee], list[dict]]:
    """Retourne (lignes valides, lignes ignorées). Une ligne invalide (cellule
    vide ou non numérique) est ignorée et signalée, elle ne fait pas planter
    le reste du rapport."""
    lignes: list[LigneAnalysee] = []
    ignorees: list[dict] = []
    for numero, row in enumerate(charger_lignes(chemin_csv), start=2):
        try:
            lignes.append(analyser_ligne(row))
        except ValueError as e:
            ignorees.append({
                "ligne": numero,
                "reference": row.get("reference", "?"),
                "raison": str(e),
            })
    return lignes, ignorees


def _par_flag(lignes: list[LigneAnalysee], flag: str) -> list[LigneAnalysee]:
    return [l for l in lignes if flag in l.flags]


def resume_compact(lignes: list[LigneAnalysee]) -> str:
    ruptures = _par_flag(lignes, "rupture")
    surstocks = _par_flag(lignes, "surstock") + _par_flag(lignes, "surstock_dormant")
    ecarts = _par_flag(lignes, "ecart_inventaire")
    parts = [
        f"{len(ruptures)} réf. en rupture ({', '.join(l.reference for l in ruptures[:3])}{'…' if len(ruptures) > 3 else ''})",
        f"{len(surstocks)} surstocks à écouler ({', '.join(l.reference for l in surstocks[:2])}{'…' if len(surstocks) > 2 else ''})",
        f"{len(ecarts)} écart(s) d'inventaire à vérifier ({', '.join(l.reference for l in ecarts[:2])}{'…' if len(ecarts) > 2 else ''})",
    ]
    return " · ".join(parts)


def generer_rapport_markdown(
    lignes: list[LigneAnalysee],
    nom_fichier: str,
    date_generation: str,
    lignes_ignorees: list[dict] | None = None,
) -> str:
    ruptures = _par_flag(lignes, "rupture")
    sous_seuil = _par_flag(lignes, "sous_seuil")
    a_surveiller = _par_flag(lignes, "a_surveiller")
    surstock_dormant = _par_flag(lignes, "surstock_dormant")
    surstock = _par_flag(lignes, "surstock")
    ecarts = _par_flag(lignes, "ecart_inventaire")

    out = []
    out.append(f"# Rapport de stock — {nom_fichier}")
    out.append(f"*Généré le {date_generation}*\n")

    out.append("## Résumé")
    out.append(f"> {resume_compact(lignes)}\n")
    out.append(f"- {len(lignes)} références analysées")
    out.append(f"- {len(ruptures)} en rupture")
    out.append(f"- {len(sous_seuil)} sous le seuil mini (réappro à déclencher)")
    out.append(f"- {len(a_surveiller)} à surveiller (couverture sous le délai de réapprovisionnement)")
    out.append(f"- {len(surstock) + len(surstock_dormant)} surstocks, dont {len(surstock_dormant)} dormants (rotation nulle)")
    out.append(f"- {len(ecarts)} écarts d'inventaire significatifs\n")

    out.append("## Ruptures (stock théorique = 0)")
    if ruptures:
        for l in ruptures:
            out.append(f"- **{l.reference}** — {l.designation} ({l.emplacement}) — fournisseur {l.fournisseur}, délai réappro {l.delai_reappro_jours} j")
    else:
        out.append("- Aucune.")
    out.append("")

    out.append("## Sous le seuil mini — réappro à déclencher")
    if sous_seuil:
        for l in sous_seuil:
            out.append(f"- **{l.reference}** — stock {l.stock_theorique} / mini {l.stock_mini} ({l.emplacement}, {l.fournisseur}, délai {l.delai_reappro_jours} j)")
    else:
        out.append("- Aucune.")
    out.append("")

    out.append("## À surveiller — couverture inférieure au délai de réapprovisionnement")
    if a_surveiller:
        for l in a_surveiller:
            cj = f"{l.couverture_jours:.1f}" if l.couverture_jours is not None else "n/a"
            out.append(f"- **{l.reference}** — stock {l.stock_theorique} couvre ~{cj} j de vente, délai réappro {l.delai_reappro_jours} j ({l.fournisseur})")
    else:
        out.append("- Aucune.")
    out.append("")

    out.append("## Surstocks")
    out.append("### Dormants (0 sortie sur 30 jours)")
    if surstock_dormant:
        for l in surstock_dormant:
            out.append(f"- **{l.reference}** — stock {l.stock_theorique} vs maxi {l.stock_maxi} ({l.emplacement})")
    else:
        out.append("- Aucun.")
    out.append("### Avec rotation (sorties > 0 mais stock > maxi)")
    if surstock:
        for l in surstock:
            out.append(f"- **{l.reference}** — stock {l.stock_theorique} vs maxi {l.stock_maxi}, {l.sorties_30j} sorties/30j")
    else:
        out.append("- Aucun.")
    out.append("")

    out.append("## Écarts d'inventaire à vérifier")
    if ecarts:
        for l in ecarts:
            out.append(f"- **{l.reference}** — théorique {l.stock_theorique} vs physique {l.stock_physique} (écart {l.ecart:+d}) au {l.date_inventaire}")
    else:
        out.append("- Aucun.")
    out.append("")

    out.append("## Lignes ignorées (cellule vide ou valeur non numérique)")
    if lignes_ignorees:
        for ign in lignes_ignorees:
            out.append(f"- Ligne {ign['ligne']} (réf. {ign['reference']}) — {ign['raison']}")
    else:
        out.append("- Aucune.")
    out.append("")

    return "\n".join(out)


def _demo_autotest() -> None:
    """Auto-vérification : casse si la logique de classification régresse."""
    ligne_rupture = analyser_ligne({
        "reference": "T-1", "designation": "x", "emplacement": "A", "fournisseur": "F",
        "stock_theorique": "0", "stock_physique_inventaire": "0", "date_inventaire": "01/01/2026",
        "stock_mini": "10", "stock_maxi": "50", "sorties_30j": "20", "delai_reappro_jours": "7",
    })
    assert "rupture" in ligne_rupture.flags

    ligne_sous_seuil = analyser_ligne({
        "reference": "T-2", "designation": "x", "emplacement": "A", "fournisseur": "F",
        "stock_theorique": "5", "stock_physique_inventaire": "5", "date_inventaire": "01/01/2026",
        "stock_mini": "10", "stock_maxi": "50", "sorties_30j": "15", "delai_reappro_jours": "7",
    })
    assert "sous_seuil" in ligne_sous_seuil.flags
    assert "rupture" not in ligne_sous_seuil.flags

    ligne_surveiller = analyser_ligne({
        "reference": "T-3", "designation": "x", "emplacement": "A", "fournisseur": "F",
        "stock_theorique": "20", "stock_physique_inventaire": "20", "date_inventaire": "01/01/2026",
        "stock_mini": "10", "stock_maxi": "80", "sorties_30j": "60", "delai_reappro_jours": "14",
    })
    # couverture = 20 / (60/30) = 10 jours < délai 14 jours
    assert "a_surveiller" in ligne_surveiller.flags

    ligne_surstock_dormant = analyser_ligne({
        "reference": "T-4", "designation": "x", "emplacement": "A", "fournisseur": "F",
        "stock_theorique": "200", "stock_physique_inventaire": "200", "date_inventaire": "01/01/2026",
        "stock_mini": "10", "stock_maxi": "50", "sorties_30j": "0", "delai_reappro_jours": "7",
    })
    assert "surstock_dormant" in ligne_surstock_dormant.flags

    ligne_ecart = analyser_ligne({
        "reference": "T-5", "designation": "x", "emplacement": "A", "fournisseur": "F",
        "stock_theorique": "40", "stock_physique_inventaire": "10", "date_inventaire": "01/01/2026",
        "stock_mini": "10", "stock_maxi": "80", "sorties_30j": "10", "delai_reappro_jours": "7",
    })
    assert "ecart_inventaire" in ligne_ecart.flags

    ligne_ok = analyser_ligne({
        "reference": "T-6", "designation": "x", "emplacement": "A", "fournisseur": "F",
        "stock_theorique": "40", "stock_physique_inventaire": "40", "date_inventaire": "01/01/2026",
        "stock_mini": "10", "stock_maxi": "80", "sorties_30j": "10", "delai_reappro_jours": "7",
    })
    assert ligne_ok.flags == []

    import tempfile
    from pathlib import Path

    entetes = (
        "reference,designation,emplacement,stock_theorique,"
        "stock_physique_inventaire,date_inventaire,stock_mini,stock_maxi,"
        "sorties_30j,delai_reappro_jours,fournisseur\n"
    )

    with tempfile.TemporaryDirectory() as tmp:
        # Cas limite 1 : cellule vide -> ligne ignorée, pas de plantage.
        chemin = Path(tmp) / "vide.csv"
        chemin.write_text(
            entetes
            + "T-7,x,A,,0,01/01/2026,10,50,20,7,F\n"
            + "T-8,x,A,40,40,01/01/2026,10,80,10,7,F\n",
            encoding="utf-8",
        )
        lignes_v, ignorees_v = analyser_export(str(chemin))
        assert [l.reference for l in lignes_v] == ["T-8"]
        assert [i["reference"] for i in ignorees_v] == ["T-7"]

        # Cas limite 2 : valeur non numérique -> ligne ignorée, pas de plantage.
        chemin = Path(tmp) / "nonnum.csv"
        chemin.write_text(
            entetes
            + "T-9,x,A,abc,40,01/01/2026,10,50,20,7,F\n"
            + "T-10,x,A,40,40,01/01/2026,10,80,10,7,F\n",
            encoding="utf-8",
        )
        lignes_n, ignorees_n = analyser_export(str(chemin))
        assert [l.reference for l in lignes_n] == ["T-10"]
        assert [i["reference"] for i in ignorees_n] == ["T-9"]

        # Cas limite 3 : en-têtes différents du client -> erreur claire
        # (ColonnesManquantes), pas de trace Python.
        chemin = Path(tmp) / "entetes.csv"
        chemin.write_text(
            "sku,desc,loc,qty_theo,qty_phys,date_inv,mini,maxi,sorties,delai,fourn\n"
            "T-11,x,A,40,40,01/01/2026,10,80,10,7,F\n",
            encoding="utf-8",
        )
        try:
            analyser_export(str(chemin))
            raise AssertionError("ColonnesManquantes attendue, pas levée")
        except ColonnesManquantes as e:
            assert "reference" in str(e)

        # Variantes d'écriture tolérées (espaces, majuscules, accents).
        chemin = Path(tmp) / "variantes.csv"
        chemin.write_text(
            " Reference ,Designation,Emplacement,Stock Théorique,"
            "Stock Physique Inventaire,Date Inventaire,Stock Mini,Stock Maxi,"
            "Sorties_30J,Delai_Reappro_Jours,Fournisseur\n"
            "T-12,x,A,40,40,01/01/2026,10,80,10,7,F\n",
            encoding="utf-8",
        )
        lignes_var, ignorees_var = analyser_export(str(chemin))
        assert [l.reference for l in lignes_var] == ["T-12"] and not ignorees_var

        # Cas limite 5 : CSV encodé en cp1252 avec accents FR -> lu normalement.
        chemin = Path(tmp) / "cp1252.csv"
        chemin.write_bytes(
            (entetes + "T-13,Écran,Réserve,40,40,01/01/2026,10,80,10,7,F\n").encode("cp1252")
        )
        lignes_cp, ignorees_cp = analyser_export(str(chemin))
        assert [l.reference for l in lignes_cp] == ["T-13"] and not ignorees_cp
        assert lignes_cp[0].designation == "Écran"

        # Cas limite 6 : fichier Excel binaire renommé .csv -> erreur claire,
        # pas de trace Python.
        chemin = Path(tmp) / "classeur.csv"
        chemin.write_bytes(b"PK\x03\x04binaire-pas-du-csv")
        try:
            analyser_export(str(chemin))
            raise AssertionError("FichierIllisible attendue, pas levée")
        except FichierIllisible as e:
            assert "classeur Excel" in str(e)

        # Cas limite 7 : séparateur point-virgule (export Excel FR) -> lu
        # normalement, pas de message "colonne manquante" trompeur.
        chemin = Path(tmp) / "pointvirgule.csv"
        chemin.write_text(
            entetes.replace(",", ";") + "T-14,x,A,40,40,01/01/2026,10,80,10,7,F\n".replace(",", ";"),
            encoding="utf-8",
        )
        lignes_pv, ignorees_pv = analyser_export(str(chemin))
        assert [l.reference for l in lignes_pv] == ["T-14"] and not ignorees_pv

    print("Auto-test OK : 6 scénarios de classification + 7 cas limites corrects.")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        _demo_autotest()
    else:
        print(__doc__)
        print("Lancez plutôt run.py <export.csv> depuis la racine du skill.")
