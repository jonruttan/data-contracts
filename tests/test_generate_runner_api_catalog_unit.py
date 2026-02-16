# SPEC-OPT-OUT: Validates runner API catalog generation script output shape and sync behavior.
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys


def test_generate_runner_api_catalog_check_passes() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    cp = subprocess.run(
        [sys.executable, "scripts/generate_runner_api_catalog.py", "--check"],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=False,
    )
    assert cp.returncode == 0, cp.stdout + cp.stderr


def test_generate_runner_api_catalog_json_shape(tmp_path: Path) -> None:
    repo_root = Path(__file__).resolve().parents[1]
    out = tmp_path / "runner-api-catalog.json"
    doc = tmp_path / "runner_api_reference.md"
    doc.write_text(
        "# x\n\n<!-- GENERATED:START runner_api_catalog -->\nold\n<!-- GENERATED:END runner_api_catalog -->\n",
        encoding="utf-8",
    )
    cp = subprocess.run(
        [
            sys.executable,
            "scripts/generate_runner_api_catalog.py",
            "--out",
            str(out),
            "--doc-out",
            str(doc),
        ],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=False,
    )
    assert cp.returncode == 0, cp.stdout + cp.stderr
    payload = json.loads(out.read_text(encoding="utf-8"))
    assert payload["version"] == 2
    assert "quality" in payload
    assert "summary" in payload
    assert isinstance(payload.get("commands"), list)
