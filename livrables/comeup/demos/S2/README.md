# S2 – Assistant FAQ local (Python, données fictives)
`python app.py` puis http://127.0.0.1:8765 ; journal des questions sans réponse : /log (fichier unanswered.log).
Recherche par mots-clés pondérés (TF-IDF simplifié) dans faq.md, seuil THRESHOLD dans app.py. Sans API ni dépendance.
Limite connue : un mot commun peut produire une fausse réponse (« cartes cadeaux » tombe sur Paiement via « carte ») ; une vraie version utiliserait un LLM + citation.
`python shots.py` régénère les captures.
