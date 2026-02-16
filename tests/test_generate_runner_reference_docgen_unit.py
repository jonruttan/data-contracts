# SPEC-OPT-OUT: Verifies generated runner reference includes semantic docs sections for each command.
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys


def test_runner_reference_catalog_has_semantics_fields() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    cp = subprocess.run(
        [sys.executable, "scripts/generate_runner_api_catalog.py"],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=False,
    )
    assert cp.returncode == 0, cp.stdout + cp.stderr
    payload = json.loads((repo_root / ".artifacts/runner-api-catalog.json").read_text(encoding="utf-8"))
    rows = payload.get("commands") or []
    assert rows
    row = rows[0]
    assert isinstance(row.get("summary"), str) and row["summary"].strip()
    assert isinstance(row.get("defaults"), list)
    assert isinstance(row.get("failure_modes"), list)
    assert isinstance(row.get("examples"), list) and row["examples"]
