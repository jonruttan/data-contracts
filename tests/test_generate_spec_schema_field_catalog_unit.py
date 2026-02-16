# SPEC-OPT-OUT: Validates spec schema field catalog generation script output shape and sync behavior.
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys


def test_generate_spec_schema_field_catalog_check_passes() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    cp = subprocess.run(
        [sys.executable, "scripts/generate_spec_schema_field_catalog.py", "--check"],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=False,
    )
    assert cp.returncode == 0, cp.stdout + cp.stderr


def test_generate_spec_schema_field_catalog_json_shape() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    path = repo_root / ".artifacts/spec-schema-field-catalog.json"
    if not path.exists():
        cp = subprocess.run(
            [sys.executable, "scripts/generate_spec_schema_field_catalog.py"],
            cwd=repo_root,
            capture_output=True,
            text=True,
            check=False,
        )
        assert cp.returncode == 0, cp.stdout + cp.stderr
    payload = json.loads(path.read_text(encoding="utf-8"))
    assert payload["version"] == 1
    assert "summary" in payload
    assert isinstance(payload.get("top_level_fields"), list)
    assert isinstance(payload.get("type_profiles"), list)
