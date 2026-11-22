"""Lance app.py, capture 3 écrans (réponse sourcée, hors périmètre, journal des questions sans réponse)."""
import sys, subprocess, time, pathlib, urllib.parse as up
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from common import shot, ASSETS
here = pathlib.Path(__file__).parent; (here/"unanswered.log").unlink(missing_ok=True)
srv = subprocess.Popen([sys.executable, str(here/"app.py")]); time.sleep(1.5)
u = lambda *qs: "http://127.0.0.1:8765/?" + "&".join("q=" + up.quote(q) for q in qs)
try:
    shot(u("Combien coûte la livraison express ?"), ASSETS/"S2-1-reponse-sourcee.png", 1280, 520)
    shot(u("Vendez-vous des cartes cadeaux ?", "Avez-vous un magasin à Lyon ?"), ASSETS/"S2-2-hors-perimetre.png", 1280, 620)
    shot("http://127.0.0.1:8765/log", ASSETS/"S2-3-questions-sans-reponse.png", 1280, 300)
finally: srv.terminate()
