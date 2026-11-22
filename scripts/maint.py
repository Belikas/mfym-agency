"""Maintenance sans Claude : python scripts/maint.py heartbeat|backup|startup"""
import base64, json, subprocess, sys, time, urllib.request
from datetime import datetime
from pathlib import Path
import tg

ROOT = tg.ROOT
LOG = ROOT / "logs" / "maint.log"


def log(msg):
    LOG.parent.mkdir(exist_ok=True)
    with LOG.open("a", encoding="utf-8") as f:
        f.write(f"{datetime.now().isoformat(timespec='seconds')} {msg}\n")


def heartbeat():
    url = tg.env().get("HC_PING_URL")
    if not url:
        return log("heartbeat: pas d'URL HC_PING_URL")
    urllib.request.urlopen(url, timeout=15).read()


def git(*args, check=True):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, encoding="utf-8", check=check)


def backup():
    e = tg.env()
    git("add", "-A")
    if git("diff", "--cached", "--quiet", check=False).returncode:
        git("commit", "-m", f"sauvegarde {datetime.now():%Y-%m-%d}")
    repo, token = e.get("GITHUB_REPO"), e.get("GITHUB_TOKEN")
    if not (repo and token):
        return log("backup: commit local fait, push en attente (GITHUB_REPO/GITHUB_TOKEN vides)")
    url = repo if repo.endswith(".git") else repo + ".git"
    auth = base64.b64encode(f"x-access-token:{token}".encode()).decode()
    r = git("-c", f"http.extraHeader=Authorization: Basic {auth}", "push", url, "HEAD:main", check=False)
    if r.returncode:
        log(f"backup: push ÉCHEC {r.stderr.strip()[-300:]}")
        tg.send("Sauvegarde GitHub en échec (voir logs/maint.log).", "alert")
    else:
        log(f"backup: push OK {git('rev-parse', '--short', 'HEAD').stdout.strip()}")


def startup():
    time.sleep(120)
    checks = {}
    alive = ROOT / "run" / "bot_alive.txt"
    checks["bot"] = alive.exists() and time.time() - alive.stat().st_mtime < 180
    try:
        urllib.request.urlopen("http://127.0.0.1:8700/api/health", timeout=5)
        checks["dashboard"] = True
    except Exception:
        checks["dashboard"] = False
    ts = subprocess.run(["tailscale", "status", "--json"], capture_output=True, text=True, encoding="utf-8")
    checks["tailscale"] = ts.returncode == 0 and json.loads(ts.stdout or "{}").get("BackendState") == "Running"
    st = subprocess.run(["schtasks", "/query", "/fo", "csv", "/nh"], capture_output=True, text=True, encoding="cp850", errors="replace")
    checks["planificateur"] = "MFYM-quotidien-0730" in st.stdout
    log(f"startup: {json.dumps(checks)}")
    if not all(checks.values()):
        tg.send(f"Redémarrage du PC : services KO {[k for k, v in checks.items() if not v]}", "alert")


if __name__ == "__main__":
    try:
        {"heartbeat": heartbeat, "backup": backup, "startup": startup}[sys.argv[1]]()
    except Exception as ex:
        log(f"{sys.argv[1]}: erreur {ex}")
        raise
