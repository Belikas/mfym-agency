"""Détecte les expéditions en retard (CSV commandes + CSV suivi transporteur) et génère messages clients + résumé d'alerte.
Usage : python run.py   (date de référence fixée pour une sortie reproductible)"""
import csv, datetime as dt, pathlib, sys
TODAY = dt.date(2026, 11, 20)
STALE_DAYS = 3          # aucun scan depuis N jours = suspect
here = pathlib.Path(__file__).parent
d = lambda s: dt.date.fromisoformat(s)

orders = list(csv.DictReader(open(here/"orders.csv", encoding="utf-8")))
track = {r["tracking"]: r for r in csv.DictReader(open(here/"tracking.csv", encoding="utf-8"))}
print(f"[1/3] {len(orders)} commandes lues, {len(track)} statuts de suivi")

late = []
for o in orders:
    t = track.get(o["tracking"])
    if t is None: reason = "aucun statut de suivi"
    elif t["status"] == "delivered": continue
    elif t["status"] == "exception": reason = "incident transporteur"
    elif d(o["promised"]) < TODAY: reason = f"{(TODAY-d(o['promised'])).days} j de retard sur la date promise"
    elif (TODAY-d(t["last_scan"])).days >= STALE_DAYS: reason = f"aucun scan depuis {(TODAY-d(t['last_scan'])).days} j"
    else: continue
    late.append((o, reason))
print(f"[2/3] {len(late)} expéditions à risque détectées")

out = here/"out"; out.mkdir(exist_ok=True)
msgs = []
for o, reason in late:
    msgs.append(f"À : {o['email']}\nObjet : Votre commande {o['order_id']} – point sur la livraison\n\n"
        f"Bonjour {o['customer'].split()[0]},\nvotre colis ({o['carrier']}, suivi {o['tracking']}) devait arriver le {d(o['promised']):%d/%m}. "
        f"Il connaît un retard ({reason}). Nous suivons le dossier auprès du transporteur et revenons vers vous sous 24 h.\nL'équipe boutique")
(out/"messages.txt").write_text("\n\n--------\n\n".join(msgs), encoding="utf-8")
summary = [f"ALERTE LOGISTIQUE – {TODAY:%d/%m/%Y} – {len(late)} colis à risque sur {len(orders)}"] + \
          [f"- {o['order_id']} | {o['carrier']} | {o['customer']} | {reason}" for o, reason in late]
(out/"alerte.txt").write_text("\n".join(summary), encoding="utf-8")
print(f"[3/3] {len(msgs)} messages écrits dans out/messages.txt, résumé dans out/alerte.txt")
print("\n".join(summary))
