# S2 – Assistant FAQ local (Python, données fictives)
`python app.py` puis http://127.0.0.1:8765 ; journal des questions sans réponse : /log (fichier unanswered.log).
Recherche par mots-clés pondérés (TF-IDF simplifié) dans faq.md, seuil THRESHOLD dans app.py. Sans API ni dépendance.
`python shots.py` régénère les captures.
Faux positif « cartes cadeaux » corrigé : une question dont moins de la moitié des mots est présente dans la FAQ est hors périmètre (COVERAGE).
Génération IA (non testée : CLI claude déconnectée au 22/11) : `S2_LLM=1 python app.py` fait rédiger la réponse par `claude -p` à partir du seul passage retrouvé (../llm.py).
