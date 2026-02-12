from pathlib import Path

import pytest

from spec_runner.conformance_parity import ParityConfig, compare_parity_reports, run_parity_check


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


def test_run_parity_check_returns_report_shape_errors(monkeypatch, tmp_path):
    monkeypatch.setattr(
        "spec_runner.conformance_parity.run_python_report",
        lambda _cases: {"version": 2, "results": []},
    )
    monkeypatch.setattr(
        "spec_runner.conformance_parity.run_php_report",
        lambda _cases, _runner: {"version": 1, "results": []},
    )
    errs = run_parity_check(
        ParityConfig(
            cases_dir=tmp_path,
            php_runner=Path("scripts/php/conformance_runner.php"),
        )
    )
    assert errs
    assert "python report invalid: report.version must equal 1" in errs


def test_run_parity_check_surfaces_php_runner_failure(monkeypatch, tmp_path):
    monkeypatch.setattr(
        "spec_runner.conformance_parity.run_python_report",
        lambda _cases: {"version": 1, "results": []},
    )

    def _raise(_cases, _runner):
        raise RuntimeError("php conformance runner failed with exit 2")

    monkeypatch.setattr("spec_runner.conformance_parity.run_php_report", _raise)
    with pytest.raises(RuntimeError, match="php conformance runner failed with exit 2"):
        run_parity_check(
            ParityConfig(
                cases_dir=tmp_path,
                php_runner=Path("scripts/php/conformance_runner.php"),
            )
        )
