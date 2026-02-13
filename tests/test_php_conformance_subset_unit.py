import json
import shutil
import subprocess
from pathlib import Path

import pytest

from spec_runner.conformance import (
    ConformanceResult,
    compare_conformance_results,
    load_expected_results,
    validate_conformance_report_payload,
)
from spec_runner.settings import case_file_name


def _php_has_yaml_extension() -> bool:
    if shutil.which("php") is None:
        return False
    cp = subprocess.run(
        ["php", "-r", "echo function_exists('yaml_parse') ? '1' : '0';"],
        check=True,
        capture_output=True,
        text=True,
    )
    return cp.stdout.strip() == "1"


@pytest.mark.skipif(shutil.which("php") is None, reason="php is not installed")
@pytest.mark.skipif(not _php_has_yaml_extension(), reason="php yaml_parse extension is not installed")
def test_php_bootstrap_runner_matches_text_file_subset_expected(tmp_path):
    repo_root = Path(__file__).resolve().parents[1]

    cases_src = repo_root / "docs/spec/conformance/cases" / case_file_name("php-text-file-subset")
    php_runner = repo_root / "scripts/php/conformance_runner.php"

    cases_dir = tmp_path / "cases"
    out_json = tmp_path / "php-report.json"
    cases_dir.mkdir(parents=True)
    (cases_dir / cases_src.name).write_text(cases_src.read_text(encoding="utf-8"), encoding="utf-8")

    cp = subprocess.run(
        [
            "php",
            str(php_runner),
            "--cases",
            str(cases_dir),
            "--out",
            str(out_json),
        ],
        check=True,
        cwd=repo_root,
        capture_output=True,
        text=True,
    )

    payload = json.loads(out_json.read_text(encoding="utf-8"))
    report_errs = validate_conformance_report_payload(payload)
    assert report_errs == []
    assert "WARN: ASSERT_HEALTH AH001" in cp.stderr

    actual = [
        ConformanceResult(
            id=str(r.get("id", "")),
            status=str(r.get("status", "")),
            category=None if r.get("category") is None else str(r.get("category")),
            message=None if r.get("message") is None else str(r.get("message")),
        )
        for r in payload.get("results", [])
    ]
    expected = load_expected_results(cases_dir, implementation="php")
    errs = compare_conformance_results(expected, actual)
    assert errs == []


@pytest.mark.skipif(shutil.which("php") is None, reason="php is not installed")
@pytest.mark.skipif(not _php_has_yaml_extension(), reason="php yaml_parse extension is not installed")
def test_php_bootstrap_runner_can_parse_markdown_spec_test_blocks(tmp_path):
    repo_root = Path(__file__).resolve().parents[1]
    php_runner = repo_root / "scripts/php/conformance_runner.php"
    cases_dir = tmp_path / "docs_spec"
    out_json = tmp_path / "php-md-report.json"
    cases_dir.mkdir(parents=True)
    (cases_dir / case_file_name("sample")).write_text(
        """# Example

```yaml spec-test
id: SRCONF-PHP-MD-001
type: text.file
assert:
  - target: text
    must:
      - contain: ["SRCONF-PHP-MD-001"]
```
""",
        encoding="utf-8",
    )

    subprocess.run(
        [
            "php",
            str(php_runner),
            "--cases",
            str(cases_dir),
            "--out",
            str(out_json),
        ],
        check=True,
        cwd=repo_root,
        capture_output=True,
        text=True,
    )
    payload = json.loads(out_json.read_text(encoding="utf-8"))
    errs = validate_conformance_report_payload(payload)
    assert errs == []
    assert payload["results"] == [
        {"id": "SRCONF-PHP-MD-001", "status": "pass", "category": None, "message": None}
    ]


@pytest.mark.skipif(shutil.which("php") is None, reason="php is not installed")
@pytest.mark.skipif(not _php_has_yaml_extension(), reason="php yaml_parse extension is not installed")
def test_php_bootstrap_runner_ignores_plain_md_case_file(tmp_path):
    repo_root = Path(__file__).resolve().parents[1]
    php_runner = repo_root / "scripts/php/conformance_runner.php"
    cases_dir = tmp_path / "docs_spec"
    out_json = tmp_path / "php-md-report.json"
    cases_dir.mkdir(parents=True)
    (cases_dir / "sample.md").write_text(
        """# Example

```yaml spec-test
id: SRCONF-PHP-MD-002
type: text.file
assert:
  - target: text
    must:
      - contain: ["SRCONF-PHP-MD-002"]
```
""",
        encoding="utf-8",
    )

    subprocess.run(
        [
            "php",
            str(php_runner),
            "--cases",
            str(cases_dir),
            "--out",
            str(out_json),
        ],
        check=True,
        cwd=repo_root,
        capture_output=True,
        text=True,
    )
    payload = json.loads(out_json.read_text(encoding="utf-8"))
    errs = validate_conformance_report_payload(payload)
    assert errs == []
    assert payload["results"] == []


@pytest.mark.skipif(shutil.which("php") is None, reason="php is not installed")
@pytest.mark.skipif(not _php_has_yaml_extension(), reason="php yaml_parse extension is not installed")
def test_php_bootstrap_runner_allows_pattern_override(tmp_path):
    repo_root = Path(__file__).resolve().parents[1]
    php_runner = repo_root / "scripts/php/conformance_runner.php"
    cases_dir = tmp_path / "docs_spec"
    out_json = tmp_path / "php-md-report.json"
    cases_dir.mkdir(parents=True)
    (cases_dir / "sample.md").write_text(
        """# Example

```yaml spec-test
id: SRCONF-PHP-MD-003
type: text.file
assert:
  - target: text
    must:
      - contain: ["SRCONF-PHP-MD-003"]
```
""",
        encoding="utf-8",
    )

    subprocess.run(
        [
            "php",
            str(php_runner),
            "--cases",
            str(cases_dir),
            "--out",
            str(out_json),
            "--case-file-pattern",
            "*.md",
        ],
        check=True,
        cwd=repo_root,
        capture_output=True,
        text=True,
    )
    payload = json.loads(out_json.read_text(encoding="utf-8"))
    errs = validate_conformance_report_payload(payload)
    assert errs == []
    assert payload["results"] == [
        {"id": "SRCONF-PHP-MD-003", "status": "pass", "category": None, "message": None}
    ]


@pytest.mark.skipif(shutil.which("php") is None, reason="php is not installed")
@pytest.mark.skipif(not _php_has_yaml_extension(), reason="php yaml_parse extension is not installed")
def test_php_bootstrap_runner_honors_requires_capabilities_skip(tmp_path):
    repo_root = Path(__file__).resolve().parents[1]
    php_runner = repo_root / "scripts/php/conformance_runner.php"
    cases_dir = tmp_path / "docs_spec"
    out_json = tmp_path / "php-md-report.json"
    cases_dir.mkdir(parents=True)
    (cases_dir / case_file_name("requires")).write_text(
        """# Example

## SRCONF-PHP-MD-REQ-001

```yaml spec-test
id: SRCONF-PHP-MD-REQ-001
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
      - contain: ["feature.x"]
```
""",
        encoding="utf-8",
    )
    subprocess.run(
        [
            "php",
            str(php_runner),
            "--cases",
            str(cases_dir),
            "--out",
            str(out_json),
        ],
        check=True,
        cwd=repo_root,
        capture_output=True,
        text=True,
    )
    payload = json.loads(out_json.read_text(encoding="utf-8"))
    errs = validate_conformance_report_payload(payload)
    assert errs == []
    assert payload["results"] == [
        {"id": "SRCONF-PHP-MD-REQ-001", "status": "skip", "category": None, "message": None}
    ]


@pytest.mark.skipif(shutil.which("php") is None, reason="php is not installed")
@pytest.mark.skipif(not _php_has_yaml_extension(), reason="php yaml_parse extension is not installed")
def test_php_bootstrap_runner_applies_requires_before_type_support_check(tmp_path):
    repo_root = Path(__file__).resolve().parents[1]
    php_runner = repo_root / "scripts/php/conformance_runner.php"
    cases_dir = tmp_path / "docs_spec"
    out_json = tmp_path / "php-md-report.json"
    cases_dir.mkdir(parents=True)
    (cases_dir / case_file_name("requires-cli")).write_text(
        """# Example

```yaml spec-test
id: SRCONF-PHP-MD-REQ-CLI
type: cli.run
requires:
  capabilities: ["cli.run"]
  when_missing: skip
expect:
  portable:
    status: skip
    category: null
```
""",
        encoding="utf-8",
    )
    subprocess.run(
        [
            "php",
            str(php_runner),
            "--cases",
            str(cases_dir),
            "--out",
            str(out_json),
        ],
        check=True,
        cwd=repo_root,
        capture_output=True,
        text=True,
    )
    payload = json.loads(out_json.read_text(encoding="utf-8"))
    errs = validate_conformance_report_payload(payload)
    assert errs == []
    assert payload["results"] == [
        {"id": "SRCONF-PHP-MD-REQ-CLI", "status": "skip", "category": None, "message": None}
    ]


@pytest.mark.skipif(shutil.which("php") is None, reason="php is not installed")
@pytest.mark.skipif(not _php_has_yaml_extension(), reason="php yaml_parse extension is not installed")
def test_php_bootstrap_runner_supports_text_file_relative_path_and_escape_guard(tmp_path):
    repo_root = Path(__file__).resolve().parents[1]
    php_runner = repo_root / "scripts/php/conformance_runner.php"
    cases_dir = tmp_path / "docs_spec"
    out_json = tmp_path / "php-md-report.json"
    (cases_dir / ".git").mkdir(parents=True)
    (cases_dir / "sub").mkdir(parents=True)
    (cases_dir / "data").mkdir(parents=True)
    (cases_dir / "data" / "target.txt").write_text("hello from path fixture\n", encoding="utf-8")
    (cases_dir.parent / "outside.txt").write_text("outside\n", encoding="utf-8")
    (cases_dir / "sub" / case_file_name("path")).write_text(
        """# Path Cases

## SRCONF-PHP-MD-PATH-001

```yaml spec-test
id: SRCONF-PHP-MD-PATH-001
type: text.file
path: ../data/target.txt
assert:
  - target: text
    must:
      - contain: ["hello from path fixture"]
```

## SRCONF-PHP-MD-PATH-002

```yaml spec-test
id: SRCONF-PHP-MD-PATH-002
type: text.file
path: ../../outside.txt
assert:
  - target: text
    must:
      - contain: ["outside"]
```
""",
        encoding="utf-8",
    )

    subprocess.run(
        [
            "php",
            str(php_runner),
            "--cases",
            str(cases_dir / "sub"),
            "--out",
            str(out_json),
        ],
        check=True,
        cwd=repo_root,
        capture_output=True,
        text=True,
    )
    payload = json.loads(out_json.read_text(encoding="utf-8"))
    errs = validate_conformance_report_payload(payload)
    assert errs == []
    assert payload["results"] == [
        {"id": "SRCONF-PHP-MD-PATH-001", "status": "pass", "category": None, "message": None},
        {
            "id": "SRCONF-PHP-MD-PATH-002",
            "status": "fail",
            "category": "schema",
            "message": "text.file path escapes contract root",
        },
    ]
