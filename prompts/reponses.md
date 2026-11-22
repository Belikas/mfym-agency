Run déclenché par le bot Telegram : Baptiste vient de répondre (approbation, tâche faite, message ou fichier). Limites : 40 tours, 30 minutes. Run COURT : traite les réponses et ce qu'elles débloquent directement, puis termine. Pas de travail business long ici (il revient aux runs quotidiens). Vise 10 minutes.

1. Traite chaque ligne non traitée de memory/inbox.jsonl et chaque approbation répondue non traitée : enregistre l'information là où elle fait foi (tasks.json : reply, actual_minutes si donné ; experiments ; pipeline ; state.md).
2. Agis tout de suite sur ce que la réponse débloque (ex. approbation oui → exécute la décision ; tâche faite → reprends le test qu'elle bloquait).
3. Une approbation "no" : note la raison si donnée, choisis l'alternative et continue.
4. Si une réponse contient un secret par erreur, ne le recopie nulle part ; demande à Baptiste d'utiliser /secret.
