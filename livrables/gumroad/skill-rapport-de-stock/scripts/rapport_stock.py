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
import sys
from dataclasses import dataclass, field

ECART_SIGNIFICATIF_UNITES = 10  # ponytail: seuil fixe, affiner par métier si besoin


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


def _to_int(value: str) -> int:
    return int(float(str(value).strip().replace(",", ".")))


def charger_lignes(chemin_csv: str) -> list[dict]:
    with open(chemin_csv, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def analyser_ligne(row: dict) -> LigneAnalysee:
    stock_theo = _to_int(row["stock_theorique"])
    stock_phys = _to_int(row["stock_physique_inventaire"])
    mini = _to_int(row["stock_mini"])
    maxi = _to_int(row["stock_maxi"])
    sorties = _to_int(row["sorties_30j"])
    delai = _to_int(row["delai_reappro_jours"])

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


def analyser_export(chemin_csv: str) -> list[LigneAnalysee]:
    return [analyser_ligne(row) for row in charger_lignes(chemin_csv)]


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


def generer_rapport_markdown(lignes: list[LigneAnalysee], nom_fichier: str, date_generation: str) -> str:
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

    print("Auto-test OK : les 6 scénarios de classification sont corrects.")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        _demo_autotest()
    else:
        print(__doc__)
        print("Lancez plutôt run.py <export.csv> depuis la racine du skill.")
