# SPEC-OPT-OUT: Exercises behavior not yet representable as stable .spec.md coverage (unit-level API/diagnostic/infrastructure checks).
import json
import os
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
from spec_runner.doc_parser import iter_spec_doc_tests
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
def test_php_bootstrap_runner_rejects_empty_pattern_arg(tmp_path):
    repo_root = Path(__file__).resolve().parents[1]
    php_runner = repo_root / "scripts/php/conformance_runner.php"
    cases_dir = tmp_path / "docs_spec"
    out_json = tmp_path / "php-md-report.json"
    cases_dir.mkdir(parents=True)

    cp = subprocess.run(
        [
            "php",
            str(php_runner),
            "--cases",
            str(cases_dir),
            "--out",
            str(out_json),
            "--case-file-pattern",
            "",
        ],
        check=False,
        cwd=repo_root,
        capture_output=True,
        text=True,
    )
    assert cp.returncode == 2
    assert "case-file-pattern requires a non-empty value" in cp.stderr


@pytest.mark.skipif(shutil.which("php") is None, reason="php is not installed")
@pytest.mark.skipif(not _php_has_yaml_extension(), reason="php yaml_parse extension is not installed")
def test_default_case_pattern_parity_between_python_and_php(tmp_path):
    repo_root = Path(__file__).resolve().parents[1]
    php_runner = repo_root / "scripts/php/conformance_runner.php"
    cases_dir = tmp_path / "docs_spec"
    out_json = tmp_path / "php-md-report.json"
    cases_dir.mkdir(parents=True)

    (cases_dir / case_file_name("match")).write_text(
        """# Match

```yaml spec-test
id: SRCONF-PATTERN-PARITY-001
type: text.file
assert:
  - target: text
    must:
      - contain: ["SRCONF-PATTERN-PARITY-001"]
```
""",
        encoding="utf-8",
    )
    (cases_dir / "plain.md").write_text(
        """# Plain

```yaml spec-test
id: SRCONF-PATTERN-PARITY-002
type: text.file
assert:
  - target: text
    must:
      - contain: ["SRCONF-PATTERN-PARITY-002"]
```
""",
        encoding="utf-8",
    )

    python_ids = [c.test["id"] for c in iter_spec_doc_tests(cases_dir)]

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
    php_ids = [str(r["id"]) for r in payload.get("results", [])]

    assert python_ids == ["SRCONF-PATTERN-PARITY-001"]
    assert php_ids == python_ids


@pytest.mark.skipif(shutil.which("php") is None, reason="php is not installed")
@pytest.mark.skipif(not _php_has_yaml_extension(), reason="php yaml_parse extension is not installed")
def test_php_bootstrap_runner_honors_global_assert_health_env_warn(tmp_path):
    repo_root = Path(__file__).resolve().parents[1]
    php_runner = repo_root / "scripts/php/conformance_runner.php"
    cases_dir = tmp_path / "docs_spec"
    out_json = tmp_path / "php-md-report.json"
    cases_dir.mkdir(parents=True)
    (cases_dir / case_file_name("warn")).write_text(
        """# Example

```yaml spec-test
id: SRCONF-PHP-AH-ENV-001
type: text.file
assert:
  - target: text
    must:
      - contain: [""]
```
""",
        encoding="utf-8",
    )
    proc_env = os.environ.copy()
    proc_env["SPEC_RUNNER_ASSERT_HEALTH"] = "warn"
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
        env=proc_env,
        capture_output=True,
        text=True,
    )
    payload = json.loads(out_json.read_text(encoding="utf-8"))
    assert validate_conformance_report_payload(payload) == []
    assert payload["results"] == [
        {"id": "SRCONF-PHP-AH-ENV-001", "status": "pass", "category": None, "message": None}
    ]
    assert "WARN: ASSERT_HEALTH AH001" in cp.stderr


@pytest.mark.skipif(shutil.which("php") is None, reason="php is not installed")
@pytest.mark.skipif(not _php_has_yaml_extension(), reason="php yaml_parse extension is not installed")
def test_php_bootstrap_runner_per_case_ignore_overrides_global_error_env(tmp_path):
    repo_root = Path(__file__).resolve().parents[1]
    php_runner = repo_root / "scripts/php/conformance_runner.php"
    cases_dir = tmp_path / "docs_spec"
    out_json = tmp_path / "php-md-report.json"
    cases_dir.mkdir(parents=True)
    (cases_dir / case_file_name("override")).write_text(
        """# Example

```yaml spec-test
id: SRCONF-PHP-AH-ENV-002
type: text.file
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
    proc_env = os.environ.copy()
    proc_env["SPEC_RUNNER_ASSERT_HEALTH"] = "error"
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
        env=proc_env,
        capture_output=True,
        text=True,
    )
    payload = json.loads(out_json.read_text(encoding="utf-8"))
    assert validate_conformance_report_payload(payload) == []
    assert payload["results"] == [
        {"id": "SRCONF-PHP-AH-ENV-002", "status": "pass", "category": None, "message": None}
    ]
    assert "ASSERT_HEALTH" not in cp.stderr


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
