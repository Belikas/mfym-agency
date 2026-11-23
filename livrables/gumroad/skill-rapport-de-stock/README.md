# Rapport de stock — installation

Assistant Claude Code qui transforme un export WMS (CSV) en rapport de stock
lisible : ruptures, surstocks, écarts d'inventaire, références à surveiller.

## Installation (4 étapes)

1. **Copiez ce dossier** entier (`skill-rapport-de-stock`) dans le dossier
   `.claude/skills/` de votre projet (créez `.claude/skills/` s'il n'existe
   pas encore).
2. **Vérifiez que Python est installé** : ouvrez un terminal et tapez
   `python --version`. Si rien ne s'affiche, installez Python depuis
   [python.org](https://python.org) (case « Add to PATH » cochée à
   l'installation).
3. **Testez avec l'exemple fourni** : dans un terminal, déplacez-vous dans
   le dossier du skill puis lancez :
   ```
   python run.py exemple-export-wms.csv
   ```
   Un rapport doit s'afficher à l'écran et être écrit dans
   `rapport-stock.md`.
4. **Utilisez votre propre export** : exportez votre WMS en CSV avec les
   colonnes listées dans `SKILL.md`, puis lancez
   `python run.py mon-export.csv`.

Dans Claude Code, une fois le dossier copié dans `.claude/skills/`, il
suffit de donner votre fichier d'export et de demander un rapport de stock :
le skill se déclenche automatiquement.

## En cas de problème

- `ModuleNotFoundError` : vous utilisez une version de Python trop ancienne
  ou incomplète — réinstallez depuis python.org.
- Le script affiche `Erreur : colonne(s) manquante(s) : ...` et s'arrête :
  une colonne attendue est absente de votre export. Le message liste les
  colonnes attendues et celles trouvées dans votre fichier — renommez vos
  en-têtes pour qu'ils correspondent (espaces, majuscules et accents sont
  tolérés, pas le nom lui-même, voir `SKILL.md`).
- Une référence a une case vide ou une valeur non numérique (stock, mini,
  maxi, sorties, délai…) : cette ligne est ignorée, pas le reste du rapport.
  Elle apparaît dans la section « Lignes ignorées » du rapport généré, avec
  la raison.
- Le rapport est vide ou faux : vérifiez que les en-têtes de colonnes de
  votre CSV correspondent à ceux listés dans `SKILL.md`.
- Tout autre souci : contact direct indiqué sur la page de précommande.
