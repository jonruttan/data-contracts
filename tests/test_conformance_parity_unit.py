# SPEC-OPT-OUT: Exercises behavior not yet representable as stable .spec.md coverage (unit-level API/diagnostic/infrastructure checks).
from pathlib import Path
import subprocess

import pytest

from spec_runner.conformance_parity import (
    ParityConfig,
    build_parity_artifact,
    compare_parity_reports,
    run_parity_check,
)


def test_run_php_report_times_out_with_actionable_error(monkeypatch, tmp_path):
    from spec_runner.conformance_parity import run_php_report

    def _timeout(*_args, **_kwargs):
        raise subprocess.TimeoutExpired(cmd=["php"], timeout=1)

    monkeypatch.setattr("spec_runner.conformance_parity.subprocess.run", _timeout)
    with pytest.raises(RuntimeError, match="timed out after 1s"):
        run_php_report(tmp_path, tmp_path / "runner.php", timeout_seconds=1)


def test_run_python_report_times_out_with_actionable_error(monkeypatch, tmp_path):
    from spec_runner.conformance_parity import run_python_report

    def _timeout(*_args, **_kwargs):
        raise subprocess.TimeoutExpired(cmd=["python"], timeout=1)

    monkeypatch.setattr("spec_runner.conformance_parity.subprocess.run", _timeout)
    with pytest.raises(RuntimeError, match="python conformance runner timed out after 1s"):
        run_python_report(tmp_path, tmp_path / "runner.py", timeout_seconds=1)


def test_compare_parity_reports_matches_status_and_category_only():
    py = {
        "version": 1,
        "results": [
            {"id": "X", "status": "pass", "category": None, "message": "python text"},
        ],
    }
    php = {
        "version": 1,
        "results": [
            {"id": "X", "status": "pass", "category": None, "message": "php text"},
        ],
    }
    assert compare_parity_reports(py, php) == []


def test_compare_parity_reports_flags_mismatches_and_missing_ids():
    py = {
        "version": 1,
        "results": [
            {"id": "A", "status": "pass", "category": None, "message": None},
            {"id": "B", "status": "fail", "category": "assertion", "message": "x"},
        ],
    }
    php = {
        "version": 1,
        "results": [
            {"id": "B", "status": "fail", "category": "runtime", "message": "x"},
            {"id": "C", "status": "pass", "category": None, "message": None},
        ],
    }
    errs = compare_parity_reports(py, php)
    assert "missing in php report: A" in errs
    assert "missing in python report: C" in errs
    assert any(e.startswith("mismatch for B:") for e in errs)


def test_compare_parity_reports_respects_include_ids_filter():
    py = {
        "version": 1,
        "results": [
            {"id": "A", "status": "pass", "category": None, "message": None},
            {"id": "B", "status": "fail", "category": "assertion", "message": None},
        ],
    }
    php = {
        "version": 1,
        "results": [
            {"id": "A", "status": "fail", "category": "runtime", "message": None},
            {"id": "B", "status": "fail", "category": "assertion", "message": None},
        ],
    }
    errs = compare_parity_reports(py, php, include_ids={"B"})
    assert errs == []


def test_build_parity_artifact_schema_is_stable():
    artifact = build_parity_artifact(
        [
            "missing in php report: A",
            "mismatch for B: python(status=pass, category=None) != php(status=fail, category=runtime)",
            "python report invalid: report.version must equal 1",
            "php vs expected: status mismatch for X: expected=pass actual=fail",
        ]
    )
    assert set(artifact.keys()) == {"version", "missing", "mismatch", "shape_errors"}
    assert artifact["version"] == 1
    assert artifact["missing"] == ["missing in php report: A"]
    assert len(artifact["mismatch"]) == 2
    assert artifact["shape_errors"] == ["python report invalid: report.version must equal 1"]


def test_run_parity_check_returns_report_shape_errors(monkeypatch, tmp_path):
    monkeypatch.setattr(
        "spec_runner.conformance_parity.run_python_report",
        lambda _cases, _runner, **_kwargs: {"version": 2, "results": []},
    )
    monkeypatch.setattr(
        "spec_runner.conformance_parity.run_php_report",
        lambda _cases, _runner, **_kwargs: {"version": 1, "results": []},
    )
    errs = run_parity_check(
        ParityConfig(
            cases_dir=tmp_path,
            php_runner=Path("scripts/php/conformance_runner.php"),
            python_runner=Path("scripts/python/conformance_runner.py"),
        )
    )
    assert errs
    assert "python report invalid: report.version must equal 1" in errs


def test_run_parity_check_surfaces_php_runner_failure(monkeypatch, tmp_path):
    monkeypatch.setattr(
        "spec_runner.conformance_parity.run_python_report",
        lambda _cases, _runner, **_kwargs: {"version": 1, "results": []},
    )

    def _raise(_cases, _runner, **_kwargs):
        raise RuntimeError("php conformance runner failed with exit 2")

    monkeypatch.setattr("spec_runner.conformance_parity.run_php_report", _raise)
    with pytest.raises(RuntimeError, match="php conformance runner failed with exit 2"):
        run_parity_check(
            ParityConfig(
                cases_dir=tmp_path,
                php_runner=Path("scripts/php/conformance_runner.php"),
                python_runner=Path("scripts/python/conformance_runner.py"),
            )
        )


def test_run_parity_check_loads_expected_once_per_implementation(monkeypatch, tmp_path):
    monkeypatch.setattr(
        "spec_runner.conformance_parity.run_python_report",
        lambda _cases, _runner, **_kwargs: {"version": 1, "results": []},
    )
    monkeypatch.setattr(
        "spec_runner.conformance_parity.run_php_report",
        lambda _cases, _runner, **_kwargs: {"version": 1, "results": []},
    )

    calls = {"python": 0, "php": 0}

    class _Expected:
        def __init__(self, status: str, category):
            self.status = status
            self.category = category

    def _load_expected(_cases, *, implementation="python"):
        calls[implementation] += 1
        if implementation == "python":
            return {"X": _Expected("pass", None)}
        return {"X": _Expected("pass", None)}

    monkeypatch.setattr("spec_runner.conformance_parity.load_expected_results", _load_expected)
    monkeypatch.setattr("spec_runner.conformance_parity.compare_conformance_results", lambda _exp, _act: [])
    monkeypatch.setattr("spec_runner.conformance_parity.compare_parity_reports", lambda _py, _php, include_ids=None: [])

    errs = run_parity_check(
        ParityConfig(
            cases_dir=tmp_path,
            php_runner=Path("scripts/php/conformance_runner.php"),
            python_runner=Path("scripts/python/conformance_runner.py"),
        )
    )

    assert errs == []
    assert calls["python"] == 1
    assert calls["php"] == 1
