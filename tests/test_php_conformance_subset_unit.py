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
    repo_root = Path(__file__).resolve().parents[3]

    cases_src = repo_root / "tools/spec_runner/docs/spec/conformance/cases/php-text-file-subset.spec.md"
    php_runner = repo_root / "tools/spec_runner/scripts/php/conformance_runner.php"

    cases_dir = tmp_path / "cases"
    out_json = tmp_path / "php-report.json"
    cases_dir.mkdir(parents=True)
    (cases_dir / cases_src.name).write_text(cases_src.read_text(encoding="utf-8"), encoding="utf-8")

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
    report_errs = validate_conformance_report_payload(payload)
    assert report_errs == []

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
    repo_root = Path(__file__).resolve().parents[3]
    php_runner = repo_root / "tools/spec_runner/scripts/php/conformance_runner.php"
    cases_dir = tmp_path / "docs_spec"
    out_json = tmp_path / "php-md-report.json"
    cases_dir.mkdir(parents=True)
    (cases_dir / "sample.spec.md").write_text(
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
def test_php_bootstrap_runner_honors_requires_capabilities_skip(tmp_path):
    repo_root = Path(__file__).resolve().parents[3]
    php_runner = repo_root / "tools/spec_runner/scripts/php/conformance_runner.php"
    cases_dir = tmp_path / "docs_spec"
    out_json = tmp_path / "php-md-report.json"
    cases_dir.mkdir(parents=True)
    (cases_dir / "requires.spec.md").write_text(
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
