# Benchmark — dashboard « bureau pixel » (22/11/2026)

Sources : GitHub API + README (22/11). Captures non vues par le sous-agent : à revoir en ouvrant les démos.

| Réf. | Étoiles / licence | Web autonome | Données | Idées à reprendre |
|---|---|---|---|---|
| pixel-agents-hq/pixel-agents | 10.3k / MIT | oui (`npx pixel-agents`) | hooks + repli transcripts JSONL | poses typing/reading/running, bulle « attend » |
| paulrobello/claude-office | 626 / MIT | oui (2 serveurs) | hooks → FastAPI → WS | Command Center : À toi / En cours / Fini ; métaphores (poubelle = contexte) |
| IvanWng97/pixtuoid | 576 / MIT | non (TUI) | hooks + logs | écran coloré par outil (Edit bleu, Bash orange, Read cyan), Zzz = fini |
| zep-ia/pixel-agent-desk | 141 / art non redistribuable | non | hooks | — |
| disler/…-observability | 1.6k / sans licence | oui | hooks → Bun → WS | timeline filtrable |

**Décision : construire léger** (un serveur Python stdlib + une page statique + SSE), en reprenant les idées ci-dessus. Aucun ne règle le mobile ni les données business ; forker traînerait du code VS Code/Electron à jeter.
Sprites : MetroCity (JIK-A-4, CC0) https://jik-a-4.itch.io/metrocity-free-topdown-character-pack — sinon dessin pixel maison en CSS/canvas.

## Grille (1–5, critères maîtrisés) — barre : ≥4 partout (critique indépendant)
1. **Lisibilité éclair** : en <5 s sur téléphone, revenu vs objectif, qui travaille, ce qui attend Baptiste. 5 = bandeau sans défilement.
2. **Fidélité de l'activité** : pose/bulle de chaque agent = vrais événements hooks en ≤2 s ; aucun état inventé ; pas d'agent fantôme.
3. **Identité des agents** : sprite, nom, couleur distincts ; rôle et tâche lisibles sans toucher ; tient à 8 agents sur 390 px.
4. **Clarté business** : revenu, budget, tests (kill date), pistes, approbations, tâches = une carte chacun, valeur + horodatage de fraîcheur.
5. **Mobile** : 360–430 px portrait, zéro défilement horizontal, cibles ≥44 px, installable écran d'accueil.
6. **Détail à la demande** : ≤2 taps pour le rapport complet d'un agent, test, décision ou session.
7. **Finition visuelle** : une palette, une échelle pixel (rendu net), salles lisibles, mode sombre.
8. **Robustesse** : CPU au repos faible, reconnexion après coupure, JSON manquant/cassé = état vide clair.
