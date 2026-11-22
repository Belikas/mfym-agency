# Journal des décisions

## 2026-11-22 — Kickoff
- **Structure** : mémoire en JSON validé par schémas (`scripts/validate.py`, jsonschema installé via pip).
- **Mode sans surveillance** : `claude -p --permission-mode dontAsk` + liste d'outils + hook PreToolUse Python (`guard.py`) qui bloque écritures hors projet, commandes destructrices, lecture de secrets. Raison : les règles deny seules se contournent.
- **Planification** : Planificateur de tâches Windows (les crons de session Claude expirent après 7 j). 3 runs/jour : opus le matin, sonnet midi et soir pour ménager le forfait Max 5x (pool partagé avec l'usage interactif de Baptiste). À ajuster selon les lignes `quota` de logs/runs.jsonl.
- **Telegram** : bot autonome en long polling ; les runs n'envoient rien directement, ils écrivent approvals.json/tasks.json et le bot envoie. Une réponse déclenche le run `reponses` (verrou respecté via run/trigger.flag).
- **Dashboard** : construit maison (serveur Python stdlib + canvas + SSE) plutôt que fork de pixel-agents : aucun ne gère mobile + données business, forker traînerait du code VS Code/Electron. Voir memory/benchmarks/dashboard.md.
- **Recherche large** : 35 pistes (3 chercheurs sonnet en parallèle). Écartées : intérim logistique (conflit employeur probable), parking (actif non confirmé), KDP low-content (risque compte existant), YouTube sans visage (délai), scraping LBC/Vinted (CGU), bug bounty (pas d'avantage).
- **Tests choisis** : exp-01 clipping (déjà en place, 0 €, on mesure les vrais paiements), exp-02 ComeUp n8n/IA (meilleur total à 0 €, avantage dev), exp-03 skills Claude Code sur Gumroad (0 €, compte Gumroad existant, presque tout faisable par agents). Primes bancaires gardées en réserve.
- **Équipe** : embauche chercheur, critique, rédacteur, atelier (tous sonnet) ; le Directeur = run planifié (opus/sonnet).
- **Installs** : pip jsonschema.
- **Micro-entreprise reportée** (Baptiste, 22/11) : on la crée quand elle devient indispensable, c'est-à-dire quand une offre est prête à vendre (fiches ComeUp validées par le critique). Conséquence : on prépare tout pour publier le jour même ; les pistes sans statut (pré-vente, liste d'attente) passent avant.
