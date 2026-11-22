"""PreToolUse : bloque écritures hors projet, commandes destructrices, fuite de secrets.
Exit 2 + stderr = refus (doc hooks Claude Code)."""
import json, os, re, sys, tempfile
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[2]
ALLOWED_ROOTS = [PROJECT, Path(tempfile.gettempdir()).resolve()]

DESTRUCTIVE = [
    r"\bgit\s+push\b.*(--force|-f\b|--mirror|--delete)",
    r"\bgit\s+(reset\s+--hard|clean\s+-[a-z]*f|filter-branch|reflog\s+expire)",
    r"(^|[;&|]\s*)format(\.com)?\s+[A-Za-z]:|\b(diskpart|mkfs\w*|bcdedit|vssadmin|cipher\s+/w)\b|Format-Volume|Clear-Disk",
    r"\bdd\s+if=",
    r"\b(shutdown|restart-computer|stop-computer)\b",
    r"\breg(\.exe)?\s+(delete|add)\b|Remove-ItemProperty|Set-ItemProperty\s+.*HK",
    r"\bdel\s+/[sq]|\brd\s+/s|\brmdir\s+/s",
    r"Remove-Item\b.*-Recurse",
    r"Set-ExecutionPolicy|Disable-WindowsOptionalFeature|Set-MpPreference|netsh\s+advfirewall",
    r"(curl|wget|iwr|Invoke-WebRequest|irm|Invoke-RestMethod)\b[^|]*\|\s*(ba|z)?sh\b|\|\s*iex\b",
    r"\bschtasks\s+/delete\b|Unregister-ScheduledTask",
    r"\bchmod\s+-R\s+777\s+/",
    r"tailscale\s+funnel",
]
SECRETS = [
    r"(cat|type|more|less|head|tail|Get-Content|gc|bat|strings|xxd|od)\b[^|;&]*\.env\b",
    r"^\s*(env|printenv|set)\s*$|\b(printenv|Get-ChildItem\s+env:|gci\s+env:|dir\s+env:)",
    r"ANTHROPIC_API_KEY\s*=",
    r"\$env:ANTHROPIC_API_KEY\s*=",
]

def inside(p: str) -> bool:
    try:
        rp = Path(p.replace("/c/", "C:/", 1) if re.match(r"^/[a-z]/", p) else p)
        rp = (Path(os.environ.get("CLAUDE_PROJECT_DIR", PROJECT)) / rp).resolve() if not rp.is_absolute() else rp.resolve()
    except Exception:
        return False
    return any(rp == r or r in rp.parents for r in ALLOWED_ROOTS)

def abs_targets(cmd: str):
    """Cibles d'écriture absolues visibles dans une commande shell (heuristique)."""
    pats = [r">>?\s*['\"]?((?:/[a-z]/|[A-Za-z]:[\/]|/|~)[^'\"\s;|&]*)",
            r"\b(?:tee|Out-File|Set-Content|Add-Content|New-Item|cp|mv|Copy-Item|Move-Item)\b[^;|&]*?\s['\"]?((?:/[a-z]/|[A-Za-z]:[\/]|~)[^'\"\s;|&]*)['\"]?\s*(?:$|[;|&])"]
    out = []
    for p in pats:
        out += re.findall(p, cmd)
    return [t for t in out if t not in ("/dev/null", "NUL", "$null")]

def rm_targets(cmd: str):
    """Arguments des rm récursifs ; un seul hors projet suffit à bloquer.
    ponytail: heuristique (ignore les cd préalables), le refus de toute écriture absolue hors projet couvre le reste."""
    out = []
    for seg in re.split(r"[;&|]+", cmd):
        toks = seg.split()
        if toks and toks[0] in ("rm", "sudo") and any(re.match(r"^-[a-zA-Z]*r", t) for t in toks):
            out += [t.strip("'\"") for t in toks[1:] if not t.startswith("-") and t != "rm"]
    return out

def deny(msg):
    print(f"BLOQUÉ par guard.py : {msg}", file=sys.stderr)
    sys.exit(2)

def main():
    sys.stderr.reconfigure(encoding="utf-8")
    d = json.load(sys.stdin)
    tool, ti = d.get("tool_name", ""), d.get("tool_input", {}) or {}
    if tool in ("Write", "Edit", "MultiEdit", "NotebookEdit"):
        p = ti.get("file_path") or ti.get("notebook_path") or ""
        if not inside(p):
            deny(f"écriture hors du projet ({p})")
    if tool in ("Read", "Write", "Edit") and Path(ti.get("file_path", "")).name == ".env":
        deny(".env contient des secrets : lis-le depuis un script, jamais dans la conversation")
    if tool in ("Bash", "PowerShell"):
        cmd = ti.get("command", "")
        for pat in DESTRUCTIVE:
            if re.search(pat, cmd, re.I | re.M):
                deny(f"commande destructrice ({pat})")
        for pat in SECRETS:
            if re.search(pat, cmd, re.I | re.M):
                deny("exposition de secrets")
        for t in rm_targets(cmd):
            if t in ("*", "/", "~") or ".." in t or not inside(t.replace("~", str(Path.home()), 1)):
                deny(f"rm récursif hors du projet ({t})")
        for t in abs_targets(cmd):
            if t.startswith("~") or not inside(t.replace("~", str(Path.home()), 1)):
                deny(f"écriture hors du projet ({t})")
    sys.exit(0)

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as e:  # garde-fou en échec = refus
        deny(f"erreur du hook ({e})")
