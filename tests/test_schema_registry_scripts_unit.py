# SPEC-OPT-OUT: Validates CLI command wiring/output shape for schema registry/report tooling.
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys


def test_schema_registry_report_script_writes_json(tmp_path: Path) -> None:
    repo_root = Path(__file__).resolve().parents[1]
    out = tmp_path / "schema_registry_report.json"
    cmd = [
        sys.executable,
        "-m",
        "spec_runner.spec_lang_commands",
        "schema-registry-report",
        "--format",
        "json",
        "--out",
        str(out),
    ]
    proc = subprocess.run(cmd, cwd=repo_root, capture_output=True, text=True, check=False)
    assert proc.returncode == 0, proc.stdout + proc.stderr
    payload = json.loads(out.read_text(encoding="utf-8"))
    assert payload["version"] == 1
    assert "summary" in payload
