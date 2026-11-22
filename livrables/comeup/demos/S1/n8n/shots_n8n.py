"""S1-2 et S1-4 : vraies captures de l'interface n8n (pas un schéma dessiné).
Démarre un vrai serveur n8n local, exécute colisRetard01 (7 nœuds) via l'éditeur et capture
le panneau Executions réel (S1-2), puis capture l'éditeur de colisRetard01Standard (8 nœuds,
+ étape IA 'Classer l'urgence') sans l'exécuter (S1-4 : la CLI Claude headless utilisée par
cette étape n'est pas connectée sur cette machine au moment de la capture).
Chrome headless ne sait pas poser de cookie de session : on parle au vrai Chrome via DevTools
Protocol (CDP, pip install websocket-client) pour injecter le cookie puis piloter la page.
Lancer : python shots_n8n.py   (Chrome + npx + .n8n-home requis, ~1-2 min)
"""
import json, subprocess, time, pathlib, tempfile, sys, base64, os
import requests
from websocket import create_connection

here = pathlib.Path(__file__).parent
sys.path.insert(0, str(here.parent.parent))
from common import ASSETS
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PORT = 5680
BASE = f"http://127.0.0.1:{PORT}"
EMAIL, PASSWORD = "demo@example.com", "Demo1234!demo"

def n8n_cli():
    """Résout bin/n8n (installé par npx dans le cache local) pour le lancer via node directement :
    avec npx + shell=True, terminate() ne tue que le wrapper cmd.exe et laisse le serveur orphelin."""
    for pkg in pathlib.Path(os.environ["LOCALAPPDATA"], "npm-cache/_npx").glob("*/node_modules/n8n/package.json"):
        if '"2.48.7"' in pkg.read_text(encoding="utf-8"): return ["node", str(pkg.parent/"bin"/"n8n")]
    raise RuntimeError("n8n@2.48.7 introuvable dans le cache npx : lancer d'abord `npx -y n8n@2.48.7 --version`")

env = {**os.environ, "N8N_USER_FOLDER": str(here/".n8n-home"), "N8N_RESTRICT_FILE_ACCESS_TO": str(here.parent),
       "N8N_DIAGNOSTICS_ENABLED": "false", "N8N_VERSION_NOTIFICATIONS_ENABLED": "false",
       "N8N_PORT": str(PORT), "N8N_SECURE_COOKIE": "false"}

def wait_http(path, tries=40):
    for _ in range(tries):
        try:
            r = requests.get(BASE + path, timeout=1)
            if r.status_code in (200, 401): return r
        except Exception: pass
        time.sleep(1.5)
    raise RuntimeError(f"n8n ne répond pas sur {path}")

def login():
    r = requests.post(BASE + "/rest/login", json={"emailOrLdapLoginId": EMAIL, "password": PASSWORD})
    if r.status_code != 200:
        r = requests.post(BASE + "/rest/owner/setup", json={"email": EMAIL, "firstName": "Demo", "lastName": "Local", "password": PASSWORD})
        r.raise_for_status()
        r = requests.post(BASE + "/rest/login", json={"emailOrLdapLoginId": EMAIL, "password": PASSWORD}); r.raise_for_status()
    return r.cookies["n8n-auth"]

class Browser:
    """Une seule session Chrome headless pilotée via CDP (Chrome ne pose pas de cookie de
    session tout seul : on l'injecte via Network.setCookie, le reste est une vraie navigation)."""
    def __init__(self, token):
        self.profile = tempfile.mkdtemp()
        self.proc = subprocess.Popen([CHROME, "--headless=new", "--disable-gpu", "--remote-debugging-port=9333",
                                       f"--user-data-dir={self.profile}", "--window-size=1280,800",
                                       "--force-device-scale-factor=2", "about:blank"])  # capture nette pour un affichage réduit (200-375 px)
        for _ in range(50):
            try:
                tabs = requests.get("http://127.0.0.1:9333/json", timeout=1).json(); break
            except Exception: time.sleep(0.3)
        self.ws = create_connection(tabs[0]["webSocketDebuggerUrl"], timeout=20)
        self.rid = 0
        self.send("Network.enable")
        self.send("Network.setCookie", {"name": "n8n-auth", "value": token, "domain": "127.0.0.1", "path": "/", "httpOnly": True, "secure": False})
        self.send("Page.enable")
    def send(self, method, params=None):
        self.rid += 1
        self.ws.send(json.dumps({"id": self.rid, "method": method, "params": params or {}}))
        while True:
            m = json.loads(self.ws.recv())
            if m.get("id") == self.rid: return m
    def goto(self, url, wait_s=6):
        self.send("Page.navigate", {"url": url}); time.sleep(wait_s)
    def click(self, x, y, wait_s=4):
        self.send("Input.dispatchMouseEvent", {"type": "mousePressed", "x": x, "y": y, "button": "left", "clickCount": 1})
        self.send("Input.dispatchMouseEvent", {"type": "mouseReleased", "x": x, "y": y, "button": "left", "clickCount": 1})
        time.sleep(wait_s)
    def shot(self, out):
        r = self.send("Page.captureScreenshot", {"format": "png"})
        pathlib.Path(out).write_bytes(base64.b64decode(r["result"]["data"]))
    def close(self):
        self.ws.close(); self.proc.terminate()

CLI = n8n_cli()
server = subprocess.Popen([*CLI, "start"], env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
try:
    wait_http("/rest/settings")
    token = login()
    for wf in ("workflow.json", "workflow-standard.json"):
        subprocess.run([*CLI, "import:workflow", f"--input={wf}"], cwd=here, env=env, check=True)

    b = Browser(token)
    # S1-2 : exécution réelle (bouton Execute) puis onglet Executions, capturé dans l'éditeur n8n
    b.goto(f"{BASE}/workflow/colisRetard01", wait_s=8)
    b.click(652, 634, wait_s=8)   # bouton "Execute"
    b.click(637, 65, wait_s=3)    # onglet "Executions"
    b.shot(ASSETS/"S1-2-execution.png")

    # S1-4 : éditeur du workflow + étape IA (non exécuté : CLI Claude non connectée sur cette machine)
    b.goto(f"{BASE}/workflow/colisRetard01Standard", wait_s=6)
    b.shot(ASSETS/"S1-4-workflow-n8n.png")
    b.close()
    print("S1-2-execution.png et S1-4-workflow-n8n.png écrits dans", ASSETS)
finally:
    server.kill()  # node lancé directement (pas via npx/cmd.exe) : kill() l'atteint vraiment
    server.wait(timeout=10)
