# SPEC-OPT-OUT: Exercises behavior not yet representable as stable .spec.md coverage (unit-level API/diagnostic/infrastructure checks).
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
from spec_runner.settings import case_file_name


def test_run_conformance_cases_matches_expected(tmp_path, monkeypatch, capsys):
    repo_root = Path(__file__).resolve().parents[1]
    cases_dir = repo_root / "docs/spec/conformance/cases"

    actual = run_conformance_cases(
        cases_dir,
        ctx=SpecRunContext(tmp_path=tmp_path, patcher=monkeypatch, capture=capsys),
    )
    expected = load_expected_results(cases_dir, implementation="python")
    errs = compare_conformance_results(expected, actual)
    assert errs == []


def test_conformance_results_are_jsonable(tmp_path, monkeypatch, capsys):
    repo_root = Path(__file__).resolve().parents[1]
    cases_dir = repo_root / "docs/spec/conformance/cases"
    actual = run_conformance_cases(
        cases_dir,
        ctx=SpecRunContext(tmp_path=tmp_path, patcher=monkeypatch, capture=capsys),
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
    (cases_dir / case_file_name("override")).write_text(
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
        ctx=SpecRunContext(tmp_path=tmp_path, patcher=monkeypatch, capture=capsys),
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
    assert any("status must be one of: pass, fail, skip" in e for e in errs)
    assert any("category must be null when status=pass" in e for e in errs)


def test_conformance_inline_expect_merges_portable_and_impl_override(tmp_path, monkeypatch, capsys):
    cases_dir = tmp_path / "cases"
    cases_dir.mkdir(parents=True)
    (cases_dir / case_file_name("inline")).write_text(
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
        ctx=SpecRunContext(tmp_path=tmp_path, patcher=monkeypatch, capture=capsys),
    )
    exp_python = load_expected_results(cases_dir, implementation="python")
    assert compare_conformance_results(exp_python, actual) == []
    exp_php = load_expected_results(cases_dir, implementation="php")
    errs = compare_conformance_results(exp_php, actual)
    assert any("status mismatch for SRCONF-TMP-INLINE" in e for e in errs)


def test_conformance_inline_expect_requires_portable_status(tmp_path):
    cases_dir = tmp_path / "cases"
    cases_dir.mkdir(parents=True)
    (cases_dir / case_file_name("bad")).write_text(
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


def test_conformance_requires_capabilities_skip_when_missing(tmp_path, monkeypatch, capsys):
    cases_dir = tmp_path / "cases"
    cases_dir.mkdir(parents=True)
    (cases_dir / case_file_name("requires")).write_text(
        """```yaml spec-test
id: SRCONF-TMP-REQ-SKIP
type: text.file
requires:
  capabilities: ["feature.x"]
  when_missing: skip
expect:
  portable:
    status: skip
    category: null
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
        ctx=SpecRunContext(tmp_path=tmp_path, patcher=monkeypatch, capture=capsys),
        implementation="python",
        capabilities=set(),
    )
    expected = load_expected_results(cases_dir, implementation="python")
    assert compare_conformance_results(expected, actual) == []


def test_conformance_requires_capabilities_fail_when_missing(tmp_path, monkeypatch, capsys):
    cases_dir = tmp_path / "cases"
    cases_dir.mkdir(parents=True)
    (cases_dir / case_file_name("requires-fail")).write_text(
        """```yaml spec-test
id: SRCONF-TMP-REQ-FAIL
type: text.file
requires:
  capabilities: ["feature.y"]
  when_missing: fail
expect:
  portable:
    status: fail
    category: runtime
    message_tokens: ["feature.y"]
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
        ctx=SpecRunContext(tmp_path=tmp_path, patcher=monkeypatch, capture=capsys),
        implementation="python",
        capabilities=set(),
    )
    expected = load_expected_results(cases_dir, implementation="python")
    assert compare_conformance_results(expected, actual) == []


def test_conformance_requires_rejects_invalid_when_missing(tmp_path, monkeypatch, capsys):
    cases_dir = tmp_path / "cases"
    cases_dir.mkdir(parents=True)
    (cases_dir / case_file_name("requires-invalid")).write_text(
        """```yaml spec-test
id: SRCONF-TMP-REQ-BAD
type: text.file
requires:
  capabilities: ["feature.z"]
  when_missing: maybe
expect:
  portable:
    status: fail
    category: schema
    message_tokens: ["requires.when_missing"]
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
        ctx=SpecRunContext(tmp_path=tmp_path, patcher=monkeypatch, capture=capsys),
        implementation="python",
        capabilities=set(),
    )
    expected = load_expected_results(cases_dir, implementation="python")
    assert compare_conformance_results(expected, actual) == []
