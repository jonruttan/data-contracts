# SPEC-OPT-OUT: Verifies codemod check/write behavior and idempotence for ops symbol normalization.
from __future__ import annotations

from pathlib import Path
import subprocess
import sys


def test_convert_ops_symbol_names_write_and_check(tmp_path: Path) -> None:
    p = tmp_path / "x.spec.md"
    p.write_text("ops.fs.read_file\nops.proc.exec\n", encoding="utf-8")

    cp = subprocess.run(
        [sys.executable, "scripts/convert_ops_symbol_names.py", "--write", str(tmp_path)],
        cwd=Path(__file__).resolve().parents[1],
        capture_output=True,
        text=True,
        check=False,
    )
    assert cp.returncode == 0, cp.stdout + cp.stderr

    text = p.read_text(encoding="utf-8")
    assert "ops.fs.file.read" in text
    assert "ops.proc.command.exec" in text

    cp2 = subprocess.run(
        [sys.executable, "scripts/convert_ops_symbol_names.py", "--check", str(tmp_path)],
        cwd=Path(__file__).resolve().parents[1],
        capture_output=True,
        text=True,
        check=False,
    )
    assert cp2.returncode == 0, cp2.stdout + cp2.stderr


def test_convert_ops_symbol_names_check_fails_on_legacy(tmp_path: Path) -> None:
    p = tmp_path / "x.spec.md"
    p.write_text("ops.fs.path_exists\n", encoding="utf-8")

    cp = subprocess.run(
        [sys.executable, "scripts/convert_ops_symbol_names.py", "--check", str(tmp_path)],
        cwd=Path(__file__).resolve().parents[1],
        capture_output=True,
        text=True,
        check=False,
    )
    assert cp.returncode == 1
    assert "ops symbol normalization drift" in (cp.stdout + cp.stderr)
