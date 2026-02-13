# SPEC-OPT-OUT: Exercises behavior not yet representable as stable .spec.md coverage (unit-level API/diagnostic/infrastructure checks).
import shutil
import subprocess
import sys
from pathlib import Path

import pytest


def _required_flags() -> tuple[str, ...]:
    return ("--cases", "--out", "--case-file-pattern")


def test_python_conformance_runner_help_exposes_required_flags():
    repo_root = Path(__file__).resolve().parents[1]
    cp = subprocess.run(
        [
            sys.executable,
            str(repo_root / "scripts/python/conformance_runner.py"),
            "--help",
        ],
        check=True,
        capture_output=True,
        text=True,
        cwd=repo_root,
    )
    text = cp.stdout + cp.stderr
    for flag in _required_flags():
        assert flag in text


@pytest.mark.skipif(shutil.which("php") is None, reason="php is not installed")
def test_php_conformance_runner_help_exposes_required_flags():
    repo_root = Path(__file__).resolve().parents[1]
    cp = subprocess.run(
        [
            "php",
            str(repo_root / "scripts/php/conformance_runner.php"),
            "--help",
        ],
        check=True,
        capture_output=True,
        text=True,
        cwd=repo_root,
    )
    text = cp.stdout + cp.stderr
    for flag in _required_flags():
        assert flag in text
