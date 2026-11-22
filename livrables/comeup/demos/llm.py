"""LLM local = CLI Claude Code en mode headless (abonnement, pas d'API payante). Lève RuntimeError si la CLI n'est pas connectée."""
import subprocess, json, os, shutil
def ask(prompt, model="haiku", timeout=180):
    env = {k: v for k, v in os.environ.items() if not k.startswith(("CLAUDE", "ANTHROPIC_"))}  # jamais de clé API
    p = subprocess.run([shutil.which("claude") or "claude", "-p", "--model", model, "--output-format", "json"], input=prompt,
                       capture_output=True, text=True, encoding="utf-8", timeout=timeout, env=env)
    r = json.loads(p.stdout)
    if r.get("is_error"): raise RuntimeError(r.get("result", "erreur claude"))
    return r["result"].strip()
if __name__ == "__main__": print(ask("Réponds uniquement : OK"))
