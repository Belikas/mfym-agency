# Script des 3 vidéos ComeUp (T-04) — prêt à l'avance

À utiliser le jour où A-07 (micro-entreprise) est répondu « oui » et où on publie exp-02. Chaque vidéo : Win+Alt+R pour démarrer/arrêter l'enregistrement, 60-90 s, écran uniquement (pas besoin de voix — les légendes ci-dessous servent de sous-titre à ajouter sur ComeUp, pas à lire à l'oral). Terminal avec police large recommandé. Dossier de travail pour les 3 : `livrables/comeup/demos/`.

Honnêteté à respecter (déjà actée dans `livrables/comeup/assets/captions.md`) : données fictives partout, le dire à l'écran ou en légende ComeUp ; ne jamais couper le passage qui montre une incohérence détectée (S3) — c'est une preuve de fiabilité, pas un défaut à cacher.

## Vidéo 1 — S1 Logistique (workflow n8n réel)
1. Ouvrir `livrables/comeup/demos/S1/n8n/workflow.json` dans VS Code 2 s (montrer que c'est un vrai fichier de workflow n8n, pas une maquette).
2. Terminal : `cd livrables/comeup/demos/S1 && sh n8n/run_n8n.sh` (déjà testé, ~40 s après le premier lancement — lancer une fois avant l'enregistrement pour éviter les 6 min de téléchargement, puis relancer pendant l'enregistrement).
3. Laisser défiler le log jusqu'à `success`, 7 nœuds exécutés.
4. `cat out/alerte.txt` puis `cat out/messages.txt` : montrer les 4 expéditions à risque détectées et les messages clients générés.
5. Couper. Durée visée : 60-75 s.

## Vidéo 2 — S2 Assistant sur documents (Claude réel)
1. Terminal : `cd livrables/comeup/demos/S2 && python app.py`.
2. Navigateur : ouvrir `http://127.0.0.1:8765`, poser une question couverte par la FAQ (ex. celle utilisée dans S2-1-reponse-sourcee.png) : montrer la réponse avec la source citée.
3. Poser une question hors périmètre (ex. celle de S2-2-hors-perimetre.png) : montrer le « je ne sais pas » honnête, pas une réponse inventée.
4. `cat unanswered.log` : montrer que la question hors périmètre est journalisée.
5. Couper. Durée visée : 60-90 s.

## Vidéo 3 — S3 Extraction de factures (Claude vs règles)
1. Terminal : `cd livrables/comeup/demos/S3 && python extract.py --ai`.
2. Ouvrir `extraction.csv` (Excel ou éditeur) : montrer la colonne `ia` à côté des règles, 8/8 identiques.
3. Faire défiler jusqu'à la ligne où HT+TVA ≠ TTC (S3-3-incoherence.png) : montrer l'alerte, dire/sous-titrer « incohérence détectée automatiquement, aucune correction silencieuse ».
4. Couper. Durée visée : 60-80 s.

## Après l'enregistrement
Envoyer les 3 fichiers au bot (comme prévu dans T-04). Le rédacteur les associe aux fiches S1/S2/S3 et relance une passe de critique courte (preuve uniquement, pas toute la grille) avant publication.
