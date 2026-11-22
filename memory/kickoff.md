# Kickoff — checklist (source : KICKOFF.md)

Tant qu'une case reste ouverte, chaque run avance le kickoff avant le business (sauf ce qui attend Baptiste).

| # | Critère | Statut | Preuve |
|---|---|---|---|
| 1 | Le hook garde-fou a bloqué les 3 commandes de test | ✅ 22/11 | `python scripts/tests/guard_cases.py` → « guard OK » (10 cas bloqués : rm -rf hors projet, Remove-Item -Recurse, écriture C:\Windows, cat .env, push --force…, 4 cas autorisés). En vrai run headless : `logs/test-run.txt` « guard: bloqué » (run 20261122-0921-test). |
| 2 | Un run planifié s'est lancé seul, a travaillé et journalisé, sans personne | ⏳ | Lanceur validé à la main (`logs/runs.jsonl` run 20261122-0921-test status ok). Attendu : MFYM-quotidien-1300 du 22/11 → ligne `goal: quotidien, status: ok` dans logs/runs.jsonl. |
| 3 | Un run qui trouve le verrou pris sort proprement | ✅ 22/11 | `logs/runs.jsonl` : `{"status":"skipped_locked","holder":"37952","goal":"quotidien","ts":"2026-11-22T09:19:22"}`, code de sortie 0. |
| 4 | Après un vrai redémarrage, planificateur, bot, dashboard, Tailscale reviennent seuls | ⏳ Baptiste | Mode admin à appliquer (T-03, `schedule.ps1` en admin), puis redémarrage ; preuve = ligne `startup:` tout à true dans logs/maint.log. |
| 5 | Heartbeat healthchecks.io vert | ⏳ Baptiste | Tâche MFYM-heartbeat toutes les 5 min prête ; attend HC_PING_URL dans .env. |
| 6 | Aller-retour Telegram complet : envoyé → tapé → enregistré → run déclenché → exécuté | ⏳ Baptiste | Bot en service (MFYM-bot) ; attend TELEGRAM_BOT_TOKEN + /start. |
| 7 | Dashboard : activité live + business, sur PC et téléphone | 🔨 en cours | Construction par l'atelier ; puis `tailscale serve` port 8445, puis critique ≥4/5. |
| 8 | Sauvegarde quotidienne poussée sur GitHub | ⏳ Baptiste | MFYM-backup 03:00 prêt (commit local OK) ; attend GITHUB_REPO + GITHUB_TOKEN. |
| 9 | pipeline.json : 30+ pistes notées avec sources | ✅ 22/11 | 35 pistes, 14 catégories, 5 types de sources ; `python scripts/validate.py` → OK. |
| 10 | Premiers tests lancés ou prêts, avec kill dates | ✅ 22/11 | exp-01 clipping (kill 06/12, attend T-02), exp-02 ComeUp (kill 20/12, attend T-01), exp-03 skills Gumroad (en cours, kill 20/12). |
| 11 | Tâches de Baptiste en une liste groupée avec temps estimés | ✅ 22/11 | memory/tasks.json : T-01 (15 min), T-02 (5 min/sem), T-03 (45 min). |

Quand tout est coché : message Telegram final (ce qui marche, lien dashboard, ce qui attend Baptiste), puis runs business normaux.
