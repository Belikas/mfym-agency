# S1 – Retards logistiques (données fictives)
- `python run.py` : version Python de référence, écrit out/messages.txt et out/alerte.txt (date fixée au 20/11/2026).
- `sh n8n/run_n8n.sh` : exécution réelle du workflow n8n (`n8n/workflow.json`, généré par `n8n/build_workflow.py`) avec la CLI n8n 2.48.7 épinglée, sans compte. Journal : n8n/out/n8n-execution.log. Premier lancement ~6 min (téléchargement), ensuite ~40 s.
- `python shots.py` puis `python n8n/shots_n8n.py` : régénèrent les 4 captures (Chrome requis, voir ../common.py). S1-4 est un schéma dessiné depuis workflow.json, pas l'éditeur n8n.
