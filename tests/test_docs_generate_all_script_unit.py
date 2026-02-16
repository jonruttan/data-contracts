# SPEC-OPT-OUT: Validates docs generator orchestration script wiring and drift detection behavior.
from __future__ import annotations

from pathlib import Path
import subprocess
import sys


def test_docs_generate_all_check_passes_on_repo() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    cp = subprocess.run(
        [sys.executable, "scripts/docs_generate_all.py", "--check"],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=False,
    )
    assert cp.returncode == 0, cp.stdout + cp.stderr


def test_docs_generate_all_unknown_surface_fails() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    cp = subprocess.run(
        [sys.executable, "scripts/docs_generate_all.py", "--check", "--surface", "nope"],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=False,
    )
    assert cp.returncode == 1
    text = (cp.stdout or "") + (cp.stderr or "")
    assert "unknown surface_id: nope" in text
