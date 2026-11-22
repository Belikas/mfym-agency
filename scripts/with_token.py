"""Lance une commande avec le token Claude de l'agence (forfait Max), jamais avec une clé API.
Usage : python scripts/with_token.py <commande...>"""
import os, shutil, subprocess, sys
import tg

env = {k: v for k, v in os.environ.items() if k not in ("ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN")}
env["CLAUDE_CODE_OAUTH_TOKEN"] = tg.env()["CLAUDE_CODE_OAUTH_TOKEN"]
cmd = [shutil.which(sys.argv[1]) or sys.argv[1], *sys.argv[2:]]
sys.exit(subprocess.call(cmd, env=env))
