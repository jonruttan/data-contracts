from pathlib import Path

import pytest

from spec_runner.conformance import (
    compare_conformance_results,
    load_expected_results,
    report_to_jsonable,
    results_to_jsonable,
    run_conformance_cases,
    validate_conformance_report_payload,
)
from spec_runner.dispatcher import SpecRunContext


def test_run_conformance_cases_matches_expected(tmp_path, monkeypatch, capsys):
    repo_root = Path(__file__).resolve().parents[3]
    cases_dir = repo_root / "tools/spec_runner/fixtures/conformance/cases"

    actual = run_conformance_cases(
        cases_dir,
        ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys),
    )
    expected = load_expected_results(cases_dir, implementation="python")
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
    report = report_to_jsonable(actual)
    errs = validate_conformance_report_payload(report)
    assert errs == []


def test_conformance_per_case_override_beats_global_assert_health_env(tmp_path, monkeypatch, capsys):
    cases_dir = tmp_path / "cases"
    cases_dir.mkdir(parents=True)
    (cases_dir / "override.spec.md").write_text(
        """```yaml spec-test
id: SRCONF-TMP-OVERRIDE
type: text.file
expect:
  portable:
    status: pass
    category: null
assert_health:
  mode: ignore
assert:
  - target: text
    must:
      - contain: [""]
```
""",
        encoding="utf-8",
    )
    monkeypatch.setenv("SPEC_RUNNER_ASSERT_HEALTH", "error")
    actual = run_conformance_cases(
        cases_dir,
        ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys),
    )
    assert len(actual) == 1
    assert actual[0].id == "SRCONF-TMP-OVERRIDE"
    assert actual[0].status == "pass"
    assert actual[0].category is None


def test_conformance_report_validator_rejects_invalid_payload():
    errs = validate_conformance_report_payload(
        {
            "version": 1,
            "results": [
                {"id": "", "status": "maybe", "category": "oops", "message": None},
                {"id": "X", "status": "pass", "category": "schema", "message": "bad"},
                {"id": "Y", "status": "fail", "category": None, "message": ""},
            ],
        }
    )
    assert errs
    assert any("status must be one of: pass, fail" in e for e in errs)
    assert any("category must be null when status=pass" in e for e in errs)


def test_conformance_inline_expect_merges_portable_and_impl_override(tmp_path, monkeypatch, capsys):
    cases_dir = tmp_path / "cases"
    cases_dir.mkdir(parents=True)
    (cases_dir / "inline.spec.md").write_text(
        """```yaml spec-test
id: SRCONF-TMP-INLINE
type: text.file
expect:
  portable:
    status: pass
    category: null
  impl:
    php:
      status: fail
      category: assertion
assert:
  - target: text
    must:
      - contain: ["version: 1"]
```
""",
        encoding="utf-8",
    )
    actual = run_conformance_cases(
        cases_dir,
        ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys),
    )
    exp_python = load_expected_results(cases_dir, implementation="python")
    assert compare_conformance_results(exp_python, actual) == []
    exp_php = load_expected_results(cases_dir, implementation="php")
    errs = compare_conformance_results(exp_php, actual)
    assert any("status mismatch for SRCONF-TMP-INLINE" in e for e in errs)


def test_conformance_inline_expect_requires_portable_status(tmp_path):
    cases_dir = tmp_path / "cases"
    cases_dir.mkdir(parents=True)
    (cases_dir / "bad.spec.md").write_text(
        """```yaml spec-test
id: SRCONF-TMP-BAD
type: text.file
expect:
  portable:
    category: assertion
```
""",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="expect.portable must include status"):
        load_expected_results(cases_dir)
