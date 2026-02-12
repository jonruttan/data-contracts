from pathlib import Path

from spec_runner.conformance_purpose import conformance_purpose_report_jsonable


def test_conformance_purpose_report_schema_and_fields(tmp_path):
    cases_dir = tmp_path / "cases"
    cases_dir.mkdir(parents=True)
    (cases_dir / "sample.spec.md").write_text(
        """# Sample

## SRCONF-PURPOSE-REPORT-001

```yaml spec-test
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

    payload = conformance_purpose_report_jsonable(cases_dir)
    assert payload["version"] == 1
    assert isinstance(payload["rows"], list)
    assert len(payload["rows"]) == 1
    row = payload["rows"][0]
    assert set(row.keys()) == {"id", "title", "purpose", "type", "file"}
    assert row["id"] == "SRCONF-PURPOSE-REPORT-001"
    assert row["title"] == "report row contains purpose metadata"
    assert row["type"] == "text.file"
    assert "machine-readable case intent metadata" in row["purpose"]
    assert row["file"].endswith("sample.spec.md")


def test_conformance_purpose_report_rows_are_sorted_by_id(tmp_path):
    cases_dir = tmp_path / "cases"
    cases_dir.mkdir(parents=True)
    (cases_dir / "b.spec.md").write_text(
        """# B
## SRCONF-PURPOSE-REPORT-200
```yaml spec-test
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
    (cases_dir / "a.spec.md").write_text(
        """# A
## SRCONF-PURPOSE-REPORT-100
```yaml spec-test
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

    rows = conformance_purpose_report_jsonable(cases_dir)["rows"]
    assert [r["id"] for r in rows] == ["SRCONF-PURPOSE-REPORT-100", "SRCONF-PURPOSE-REPORT-200"]
