# SPEC-OPT-OUT: Packaging metadata contract check not yet representable as stable .spec.md coverage.
from pathlib import Path


def test_pyproject_declares_core_cli_entrypoints():
    repo_root = Path(__file__).resolve().parents[1]
    raw = (repo_root / "pyproject.toml").read_text(encoding="utf-8")

    assert "[project.scripts]" in raw
    assert 'spec-runner-conformance = "spec_runner.cli:conformance_runner_main"' in raw
    assert 'spec-runner-parity = "spec_runner.cli:compare_parity_main"' in raw
    assert 'spec-runner-validate-report = "spec_runner.cli:validate_report_main"' in raw
