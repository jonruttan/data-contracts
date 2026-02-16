# SPEC-OPT-OUT: Validates harness type catalog generation script output shape and sync behavior.
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys


def test_generate_harness_type_catalog_check_passes() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    cp = subprocess.run(
        [sys.executable, "scripts/generate_harness_type_catalog.py", "--check"],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=False,
    )
    assert cp.returncode == 0, cp.stdout + cp.stderr


def test_generate_harness_type_catalog_json_has_profiles() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    path = repo_root / ".artifacts/harness-type-catalog.json"
    if not path.exists():
        cp = subprocess.run(
            [sys.executable, "scripts/generate_harness_type_catalog.py"],
            cwd=repo_root,
            capture_output=True,
            text=True,
            check=False,
        )
        assert cp.returncode == 0, cp.stdout + cp.stderr
    payload = json.loads(path.read_text(encoding="utf-8"))
    assert payload["version"] == 2
    assert "quality" in payload
    assert isinstance(payload.get("type_profiles"), list)
