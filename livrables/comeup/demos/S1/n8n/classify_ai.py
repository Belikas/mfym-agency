"""Étape IA du workflow n8n (palier Standard) : classe l'urgence d'un colis en retard.
Appelé par le Code node 'Classer l'urgence (IA)' via child_process (stdin = JSON {order, reason}).
Utilise la CLI Claude headless (abonnement), jamais de clé API.
"""
import sys, json, pathlib
here = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent.parent))
import llm
o = json.loads(sys.stdin.read())
mot = llm.ask(
    "Un colis e-commerce a ce motif de retard : \"" + o["reason"] + "\". "
    "Réponds uniquement par un mot : Urgent (incident transporteur ou plus de 2 jours de retard) ou Surveiller (sinon).",
    model="haiku")
print(mot.strip().split()[0])
