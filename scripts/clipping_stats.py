"""Lit en SEULE LECTURE la base du projet CLIPPING MONEY pour mesurer exp-01.

Le projet clipping ne remplit pas posts.earnings : les euros restent a confirmer
depuis Whop (T-02). Ce que la base donne quand meme : volume, vues, distribution,
et donc le plafond de gain possible.
"""
import json
import sqlite3
import sys
from pathlib import Path

DB = Path(r"C:\Users\Baptiste\Desktop\CLAUDE CODE\CLIPPING MONEY\data\clipping.db")
# Seuil de vues en dessous duquel un clip ne declenche aucun paiement en pratique
# (min_payout 2-35 $ pour un CPM de 0,5-2,5 $/1k vues).
SEUIL_PAYANT = 1000


def stats(db=DB):
    con = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    try:
        vues = [r[0] or 0 for r in con.execute("select views from posts")]
        gains = con.execute("select coalesce(sum(earnings), 0) from posts").fetchone()[0]
        par_statut = dict(con.execute("select status, count(*) from posts group by status"))
        cpm_median = con.execute(
            "select cpm from campaigns where active = 1 and cpm is not null "
            "order by cpm limit 1 offset (select count(*) / 2 from campaigns "
            "where active = 1 and cpm is not null)"
        ).fetchone()
    finally:
        con.close()

    vues.sort(reverse=True)
    payants = [v for v in vues if v > SEUIL_PAYANT]
    cpm = cpm_median[0] if cpm_median else 0
    return {
        "clips": len(vues),
        "vues_total": sum(vues),
        "vues_mediane": vues[len(vues) // 2] if vues else 0,
        "vues_max": max(vues, default=0),
        "clips_au_dessus_du_seuil": len(payants),
        "vues_eligibles": sum(payants),
        "cpm_median_usd": cpm,
        "plafond_gain_usd": round(sum(payants) / 1000 * cpm, 2),
        "gains_enregistres_eur": gains,
        "par_statut": par_statut,
    }


def demo():
    s = stats()
    assert s["clips"] > 0, "aucun clip lu : chemin de base invalide ?"
    assert s["vues_eligibles"] <= s["vues_total"]
    assert s["clips_au_dessus_du_seuil"] <= s["clips"]
    print("ok")


if __name__ == "__main__":
    if "--demo" in sys.argv:
        demo()
    else:
        print(json.dumps(stats(), ensure_ascii=False, indent=1))
