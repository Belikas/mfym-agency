# S2 – Assistant FAQ local (Python, données fictives)
`python app.py` puis http://127.0.0.1:8765 ; journal des questions sans réponse : /log (fichier unanswered.log).
Recherche par mots-clés pondérés (TF-IDF simplifié) dans faq.md, seuil THRESHOLD dans app.py. Sans API ni dépendance.
`python shots.py` régénère les captures (avec `S2_LLM=1` pour les réponses Claude).
Faux positif « cartes cadeaux » corrigé : une question dont moins de la moitié des mots est présente dans la FAQ est hors périmètre (COVERAGE).
Génération IA (testée le 22/11 : réponses rédigées, source citée, « je ne sais pas » hors périmètre) : `S2_LLM=1` lancé via le script with_token du dossier scripts du projet fait rédiger la réponse par `claude -p` à partir du seul passage retrouvé (../llm.py).
