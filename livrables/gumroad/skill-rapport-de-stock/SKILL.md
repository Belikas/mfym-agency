---
name: rapport-de-stock
description: Transforme un export WMS (CSV ou Excel) en rapport de stock lisible en français : ruptures, références sous le seuil de réapprovisionnement mini, surstocks dormants, écarts d'inventaire entre stock théorique et dernier comptage physique, et références à surveiller dont la couverture de stock tombe sous le délai de réapprovisionnement fournisseur. Déclencher ce skill quand l'utilisateur fournit un export d'inventaire ou de stock WMS et demande une synthèse, un résumé, ou un rapport exploitable sans reconstruire un tableau croisé dynamique à la main.
---

# Rapport de stock

Lit un export WMS et produit un rapport markdown classé par type d'alerte :
rupture, sous seuil mini, à surveiller (risque de rupture avant le prochain
réassort), surstock (dormant ou non), écart d'inventaire.

## Quand l'utiliser

L'utilisateur donne un fichier CSV (ou Excel exporté en CSV) issu d'un WMS
avec au minimum : référence, stock théorique, stock physique du dernier
inventaire, stock mini, stock maxi, sorties des 30 derniers jours, délai de
réapprovisionnement en jours. Il demande un résumé, un état des stocks, ou
« qu'est-ce qu'il faut surveiller ».

## Colonnes attendues (en-têtes exacts, ordre libre)

`reference, designation, emplacement, stock_theorique,
stock_physique_inventaire, date_inventaire, stock_mini, stock_maxi,
sorties_30j, delai_reappro_jours, fournisseur`

Si le fichier fourni a des colonnes différentes, les renommer (ou adapter
`scripts/rapport_stock.py`) avant de lancer le script — ne pas deviner le
mapping silencieusement.

## Utilisation

```bash
python run.py <export.csv> [rapport-sortie.md]
```

Si le fichier source est un `.xlsx`, demander à l'utilisateur de l'exporter
en CSV depuis Excel/son WMS (Fichier → Enregistrer sous → CSV), ou utiliser
`openpyxl` s'il est déjà installé pour le convertir au préalable — ne pas
ajouter de dépendance pour ce cas.

Le script écrit le rapport dans le fichier de sortie (`rapport-stock.md` par
défaut) et l'affiche aussi à l'écran.

## Logique de détection (dans `scripts/rapport_stock.py`)

- **Rupture** : stock théorique ≤ 0.
- **Sous le seuil mini** : 0 < stock théorique ≤ stock mini.
- **À surveiller** : stock théorique au-dessus du mini, mais la couverture
  (stock théorique ÷ consommation journalière moyenne sur 30j) est
  inférieure au délai de réapprovisionnement — la référence risque la
  rupture avant le prochain réassort si rien n'est fait.
- **Surstock** : stock théorique > stock maxi. Sous-catégorie « dormant » si
  0 sortie sur les 30 derniers jours (rotation nulle).
- **Écart d'inventaire** : écart entre stock théorique et stock physique du
  dernier inventaire ≥ 10 unités (seuil fixe, à ajuster dans le code si le
  métier du client a des volumes très différents).

## Vérifier que la logique n'a pas régressé

```bash
python scripts/rapport_stock.py --test
```

Doit afficher `Auto-test OK`. À relancer après toute modification du script.

## Fichiers

- `scripts/rapport_stock.py` — logique de classification + auto-test.
- `run.py` — point d'entrée en ligne de commande.
- `exemple-export-wms.csv` — export d'exemple pour tester l'installation.
- `sortie-reelle.md` — rapport réellement généré à partir de l'exemple.
