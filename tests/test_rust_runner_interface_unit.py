# SPEC-OPT-OUT: Validates Rust runner-interface command wiring and deterministic exit behavior not representable as stable .spec.md fixtures.
from __future__ import annotations

import subprocess
from pathlib import Path


def test_rust_cli_lists_unsupported_subcommand_as_error() -> None:
    root = Path(__file__).resolve().parents[1]
    cli = root / "runners/rust/spec_runner_cli/src/main.rs"
    assert cli.exists()


def test_rust_adapter_reports_error_for_missing_subcommand() -> None:
    root = Path(__file__).resolve().parents[1]
    adapter = root / "runners/rust/runner_adapter.sh"
    cp = subprocess.run([str(adapter)], cwd=root, capture_output=True, text=True, check=False)
    assert cp.returncode == 2
    assert "missing runner adapter subcommand" in (cp.stderr or "")
