"""Valide les fichiers de memory/ contre memory/schemas/. Code de sortie 1 si une erreur."""
import json, sys, glob
from pathlib import Path
from jsonschema import Draft202012Validator

M = Path(__file__).resolve().parent.parent / "memory"
S = M / "schemas"

def check(data, schema_name, label):
    v = Draft202012Validator(json.loads((S / schema_name).read_text(encoding="utf-8")))
    return [f"{label}: {'/'.join(map(str, e.path))} {e.message}" for e in v.iter_errors(data)]

errors = []
for name in ["pipeline", "team", "tasks", "approvals", "revenue", "expenses"]:
    try:
        errors += check(json.loads((M / f"{name}.json").read_text(encoding="utf-8")), f"{name}.schema.json", name)
    except json.JSONDecodeError as e:
        errors.append(f"{name}: JSON invalide {e}")
for f in glob.glob(str(M / "experiments" / "*.json")):
    errors += check(json.loads(Path(f).read_text(encoding="utf-8")), "experiment.schema.json", Path(f).name)
for name, schema in [("inbox.jsonl", "inbox.line.schema.json")]:
    for i, line in enumerate((M / name).read_text(encoding="utf-8").splitlines(), 1):
        if line.strip():
            errors += check(json.loads(line), schema, f"{name}:{i}")

print("\n".join(errors) or "OK")
sys.exit(1 if errors else 0)
