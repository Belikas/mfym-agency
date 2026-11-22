"""Hook d'activité : une ligne par événement dans memory/activity.jsonl (lu par le dashboard).
Ne bloque jamais (exit 0 même en erreur)."""
import json, os, re, sys
from datetime import datetime, timezone
from pathlib import Path

LOG = Path(__file__).resolve().parents[2] / "memory" / "activity.jsonl"
MAX_BYTES = 5_000_000

def redact(s: str) -> str:
    return re.sub(r"[A-Za-z0-9_\-:]{32,}", "***", s)

def summarize(tool: str, ti: dict) -> str:
    for k in ("description", "file_path", "notebook_path", "pattern", "query", "url", "prompt", "command", "skill"):
        if ti.get(k):
            v = str(ti[k]).replace("\n", " ")
            if k.endswith("path"):
                v = v.replace(str(LOG.parents[1]), "").lstrip("\/")
            return redact(v)[:140]
    return tool

def main():
    d = json.load(sys.stdin)
    ev = d.get("hook_event_name", "")
    tool = d.get("tool_name", "")
    ti = d.get("tool_input") or {}
    line = {
        "ts": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
        "session_id": d.get("session_id", ""),
        "run_id": os.environ.get("MFYM_RUN_ID", "interactive"),
        "agent": d.get("agent_type") or os.environ.get("MFYM_AGENT", "directeur"),
        "agent_id": d.get("agent_id", ""),
        "event": ev,
    }
    if tool:
        line["tool"] = tool
    if ev in ("PreToolUse", "PostToolUse", "PostToolUseFailure"):
        line["summary"] = summarize(tool, ti)
        if ev == "PostToolUseFailure":
            line["status"] = "error"
    elif ev == "SubagentStop":
        line["summary"] = redact(str(d.get("last_assistant_message", ""))[:200])
    elif ev == "SessionStart":
        line["summary"] = f"démarrage ({d.get('source', '')})"
    else:
        line["summary"] = ev
    if LOG.exists() and LOG.stat().st_size > MAX_BYTES:
        LOG.replace(LOG.with_suffix(".1.jsonl"))
    with LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(line, ensure_ascii=False) + "\n")

try:
    main()
except Exception:
    pass
