# SPEC-OPT-OUT: Verifies generated spec-lang reference catalog semantic payload shape and completeness checks.
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys


def test_spec_lang_reference_catalog_has_semantic_fields() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    cp = subprocess.run(
        [sys.executable, "scripts/generate_spec_lang_builtin_catalog.py"],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=False,
    )
    assert cp.returncode == 0, cp.stdout + cp.stderr
    payload = json.loads((repo_root / ".artifacts/spec-lang-builtin-catalog.json").read_text(encoding="utf-8"))
    builtins = payload.get("builtins") or []
    assert builtins
    row = builtins[0]
    assert isinstance(row.get("summary"), str) and row["summary"].strip()
    assert isinstance(row.get("params"), list) and row["params"]
    assert isinstance(row.get("returns"), dict) and str(row["returns"].get("description", "")).strip()
    assert isinstance(row.get("errors"), list) and row["errors"]
    assert isinstance(row.get("examples"), list) and row["examples"]
