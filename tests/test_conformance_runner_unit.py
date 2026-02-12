from pathlib import Path

from spec_runner.conformance import (
    compare_conformance_results,
    load_expected_results,
    results_to_jsonable,
    run_conformance_cases,
)
from spec_runner.dispatcher import SpecRunContext


def test_run_conformance_cases_matches_expected(tmp_path, monkeypatch, capsys):
    repo_root = Path(__file__).resolve().parents[3]
    cases_dir = repo_root / "tools/spec_runner/fixtures/conformance/cases"
    expected_dir = repo_root / "tools/spec_runner/fixtures/conformance/expected"

    actual = run_conformance_cases(
        cases_dir,
        ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys),
    )
    expected = load_expected_results(expected_dir)
    errs = compare_conformance_results(expected, actual)
    assert errs == []


def test_conformance_results_are_jsonable(tmp_path, monkeypatch, capsys):
    repo_root = Path(__file__).resolve().parents[3]
    cases_dir = repo_root / "tools/spec_runner/fixtures/conformance/cases"
    actual = run_conformance_cases(
        cases_dir,
        ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys),
    )
    payload = results_to_jsonable(actual)
    assert isinstance(payload, list)
    assert all(isinstance(x, dict) for x in payload)
    assert all({"id", "status", "category", "message"} <= set(x.keys()) for x in payload)
