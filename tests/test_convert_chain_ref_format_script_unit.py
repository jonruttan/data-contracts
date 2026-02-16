# SPEC-OPT-OUT: Verifies codemod check/write behavior and idempotence for chain ref scalar normalization.
from __future__ import annotations

from pathlib import Path
import subprocess
import sys


def test_convert_chain_ref_format_write_and_check(tmp_path: Path) -> None:
    p = tmp_path / "x.spec.md"
    p.write_text(
        """harness:
  chain:
    steps:
    - id: one
      ref:
        path: /docs/spec/a.spec.md
        case_id: CASE-1
    - id: two
      ref:
        case_id: CASE-2
    - id: three
      ref:
        path: ../b.spec.md
""",
        encoding="utf-8",
    )

    cp = subprocess.run(
        [sys.executable, "scripts/convert_chain_ref_format.py", "--write", str(tmp_path)],
        cwd=Path(__file__).resolve().parents[1],
        capture_output=True,
        text=True,
        check=False,
    )
    assert cp.returncode == 0, cp.stdout + cp.stderr

    text = p.read_text(encoding="utf-8")
    assert "ref: /docs/spec/a.spec.md#CASE-1" in text
    assert "ref: #CASE-2" in text
    assert "ref: ../b.spec.md" in text

    cp2 = subprocess.run(
        [sys.executable, "scripts/convert_chain_ref_format.py", "--check", str(tmp_path)],
        cwd=Path(__file__).resolve().parents[1],
        capture_output=True,
        text=True,
        check=False,
    )
    assert cp2.returncode == 0, cp2.stdout + cp2.stderr


def test_convert_chain_ref_format_check_fails_on_legacy(tmp_path: Path) -> None:
    p = tmp_path / "x.spec.md"
    p.write_text(
        """harness:
  chain:
    steps:
    - id: one
      ref:
        path: /docs/spec/a.spec.md
        case_id: CASE-1
""",
        encoding="utf-8",
    )

    cp = subprocess.run(
        [sys.executable, "scripts/convert_chain_ref_format.py", "--check", str(tmp_path)],
        cwd=Path(__file__).resolve().parents[1],
        capture_output=True,
        text=True,
        check=False,
    )
    assert cp.returncode == 1
    assert "chain ref format drift" in (cp.stdout + cp.stderr)
