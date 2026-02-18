# SPEC-OPT-OUT: Exercises behavior not yet representable as stable .spec.md coverage (unit-level API/diagnostic/infrastructure checks).
from spec_runner.conformance_purpose import conformance_purpose_report_jsonable
from spec_runner.settings import case_file_name


def test_conformance_purpose_report_schema_and_fields(tmp_path):
    repo_root = tmp_path / "repo"
    repo_root.mkdir(parents=True)
    cases_dir = tmp_path / "cases"
    cases_dir.mkdir(parents=True)
    (cases_dir / case_file_name("sample")).write_text(
        """# Sample

## SRCONF-PURPOSE-REPORT-001

```yaml contract-spec
id: SRCONF-PURPOSE-REPORT-001
title: report row contains purpose metadata
purpose: Ensures purpose report exposes machine-readable case intent metadata.
type: text.file
expect:
  portable:
    status: pass
    category: null
```
""",
        encoding="utf-8",
    )

    payload = conformance_purpose_report_jsonable(cases_dir, repo_root=repo_root)
    assert payload["version"] == 1
    assert set(payload["summary"].keys()) == {
        "total_rows",
        "rows_with_warnings",
        "row_warning_count",
        "policy_error_count",
        "total_warning_count",
        "warning_code_counts",
        "warning_severity_counts",
    }
    assert set(payload["policy"].keys()) == {"path", "exists", "config", "errors"}
    assert payload["policy"]["path"].endswith("docs/spec/conformance/purpose_lint_v1.yaml")
    assert payload["policy"]["exists"] is False
    assert payload["policy"]["errors"] == []
    assert isinstance(payload["rows"], list)
    assert len(payload["rows"]) == 1
    row = payload["rows"][0]
    assert set(row.keys()) == {"id", "title", "purpose", "type", "file", "purpose_lint", "warnings"}
    assert row["id"] == "SRCONF-PURPOSE-REPORT-001"
    assert row["title"] == "report row contains purpose metadata"
    assert row["type"] == "text.file"
    assert "machine-readable case intent metadata" in row["purpose"]
    assert row["file"].endswith(case_file_name("sample"))
    assert row["purpose_lint"]["min_words"] == 8
    assert row["warnings"] == []
    assert payload["summary"]["warning_code_counts"] == {}
    assert payload["summary"]["warning_severity_counts"] == {}


def test_conformance_purpose_report_rows_are_sorted_by_id(tmp_path):
    repo_root = tmp_path / "repo"
    repo_root.mkdir(parents=True)
    cases_dir = tmp_path / "cases"
    cases_dir.mkdir(parents=True)
    (cases_dir / case_file_name("b")).write_text(
        """# B
## SRCONF-PURPOSE-REPORT-200
```yaml contract-spec
id: SRCONF-PURPOSE-REPORT-200
title: b title
purpose: Valid purpose text with enough words for sorted report output.
type: text.file
expect:
  portable: {status: pass, category: null}
```
""",
        encoding="utf-8",
    )
    (cases_dir / case_file_name("a")).write_text(
        """# A
## SRCONF-PURPOSE-REPORT-100
```yaml contract-spec
id: SRCONF-PURPOSE-REPORT-100
title: a title
purpose: Valid purpose text with enough words for sorted report output.
type: text.file
expect:
  portable: {status: pass, category: null}
```
""",
        encoding="utf-8",
    )

    rows = conformance_purpose_report_jsonable(cases_dir, repo_root=repo_root)["rows"]
    assert [r["id"] for r in rows] == ["SRCONF-PURPOSE-REPORT-100", "SRCONF-PURPOSE-REPORT-200"]


def test_conformance_purpose_report_uses_runtime_profile_and_override(tmp_path):
    repo_root = tmp_path / "repo"
    policy_path = repo_root / "docs/spec/conformance/purpose_lint_v1.yaml"
    policy_path.parent.mkdir(parents=True, exist_ok=True)
    policy_path.write_text(
        """version: 1
default:
  min_words: 8
  placeholders: [todo]
  forbid_title_copy: true
runtime:
  php:
    min_words: 3
""",
        encoding="utf-8",
    )
    cases_dir = tmp_path / "cases"
    cases_dir.mkdir(parents=True)
    (cases_dir / case_file_name("sample")).write_text(
        """# Sample
## SRCONF-PURPOSE-REPORT-300
```yaml contract-spec
id: SRCONF-PURPOSE-REPORT-300
title: sample
purpose: tiny words pass here
purpose_lint:
  runtime: php
  forbid_title_copy: false
type: text.file
expect:
  portable: {status: pass, category: null}
```
""",
        encoding="utf-8",
    )
    row = conformance_purpose_report_jsonable(cases_dir, repo_root=repo_root)["rows"][0]
    assert row["purpose_lint"]["runtime"] == "php"
    assert row["purpose_lint"]["min_words"] == 3
    assert row["purpose_lint"]["forbid_title_copy"] is False


def test_conformance_purpose_report_includes_warnings_even_when_case_lint_disabled(tmp_path):
    repo_root = tmp_path / "repo"
    repo_root.mkdir(parents=True)
    cases_dir = tmp_path / "cases"
    cases_dir.mkdir(parents=True)
    (cases_dir / case_file_name("sample")).write_text(
        """# Sample
## SRCONF-PURPOSE-REPORT-400
```yaml contract-spec
id: SRCONF-PURPOSE-REPORT-400
title: same text
purpose: same text
purpose_lint:
  enabled: false
type: text.file
expect:
  portable: {status: pass, category: null}
```
""",
        encoding="utf-8",
    )
    payload = conformance_purpose_report_jsonable(cases_dir, repo_root=repo_root)
    assert payload["summary"]["total_warning_count"] >= 1
    row = payload["rows"][0]
    assert any(
        w["code"] == "PUR001"
        and w["message"] == "purpose duplicates title"
        and w["severity"] == "warn"
        and "Rewrite purpose" in w["hint"]
        and "Rewrite `purpose`" in w["suggested_edit"]
        for w in row["warnings"]
    )


def test_conformance_purpose_report_warning_codes_are_grouped(tmp_path):
    repo_root = tmp_path / "repo"
    repo_root.mkdir(parents=True)
    cases_dir = tmp_path / "cases"
    cases_dir.mkdir(parents=True)
    (cases_dir / case_file_name("sample")).write_text(
        """# Sample
## SRCONF-PURPOSE-REPORT-500
```yaml contract-spec
id: SRCONF-PURPOSE-REPORT-500
title: TODO
purpose: TODO
type: text.file
expect:
  portable: {status: pass, category: null}
```
""",
        encoding="utf-8",
    )
    payload = conformance_purpose_report_jsonable(cases_dir, repo_root=repo_root)
    counts = payload["summary"]["warning_code_counts"]
    assert counts["PUR001"] == 1
    assert counts["PUR002"] == 1
    assert counts["PUR003"] == 1
    sev = payload["summary"]["warning_severity_counts"]
    assert sev["warn"] == 3


def test_conformance_purpose_report_uses_safe_default_hint_for_unknown_warning(monkeypatch, tmp_path):
    repo_root = tmp_path / "repo"
    repo_root.mkdir(parents=True)
    cases_dir = tmp_path / "cases"
    cases_dir.mkdir(parents=True)
    (cases_dir / case_file_name("sample")).write_text(
        """# Sample
## SRCONF-PURPOSE-REPORT-600
```yaml contract-spec
id: SRCONF-PURPOSE-REPORT-600
title: sample title
purpose: Purpose text with enough words to avoid quality warnings.
type: text.file
expect:
  portable: {status: pass, category: null}
```
""",
        encoding="utf-8",
    )
    monkeypatch.setattr(
        "spec_runner.conformance_purpose.purpose_quality_warnings",
        lambda *_a, **_k: ["some new warning shape"],
    )
    payload = conformance_purpose_report_jsonable(cases_dir, repo_root=repo_root)
    row = payload["rows"][0]
    assert row["warnings"][0]["code"] == "PUR004"
    assert row["warnings"][0]["message"] == "some new warning shape"
    assert row["warnings"][0]["severity"] == "error"
    assert row["warnings"][0]["hint"] == "Fix purpose_lint settings or policy file shape/version before rerunning."
    assert row["warnings"][0]["suggested_edit"] == "Fix `purpose_lint` configuration or policy schema/version before rerunning."


def test_conformance_purpose_report_severity_override_from_policy(tmp_path):
    repo_root = tmp_path / "repo"
    policy_path = repo_root / "docs/spec/conformance/purpose_lint_v1.yaml"
    policy_path.parent.mkdir(parents=True, exist_ok=True)
    policy_path.write_text(
        """version: 1
default:
  min_words: 8
  placeholders: [todo]
  forbid_title_copy: true
  severity_by_code:
    PUR002: info
runtime: {}
""",
        encoding="utf-8",
    )
    cases_dir = tmp_path / "cases"
    cases_dir.mkdir(parents=True)
    (cases_dir / case_file_name("sample")).write_text(
        """# Sample
## SRCONF-PURPOSE-REPORT-700
```yaml contract-spec
id: SRCONF-PURPOSE-REPORT-700
title: short purpose case
purpose: tiny purpose
type: text.file
expect:
  portable: {status: pass, category: null}
```
""",
        encoding="utf-8",
    )
    payload = conformance_purpose_report_jsonable(cases_dir, repo_root=repo_root)
    row = payload["rows"][0]
    assert any(w["code"] == "PUR002" and w["severity"] == "info" for w in row["warnings"])
    assert any("at least 8 words" in w["suggested_edit"] for w in row["warnings"] if w["code"] == "PUR002")
    assert payload["summary"]["warning_severity_counts"]["info"] >= 1
