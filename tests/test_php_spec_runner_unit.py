import json
import os
import shutil
import subprocess
from pathlib import Path

import pytest

from spec_runner.conformance import validate_conformance_report_payload


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
def test_php_spec_runner_executes_text_file_and_cli_run(tmp_path):
    repo_root = Path(__file__).resolve().parents[1]
    php_runner = repo_root / "scripts/php/spec_runner.php"
    cases_dir = tmp_path / "cases"
    out_json = tmp_path / "php-report.json"
    cases_dir.mkdir(parents=True)
    (cases_dir / "suite.spec.md").write_text(
        """# Suite

## SR-PHP-RUN-001

```yaml spec-test
id: SR-PHP-RUN-001
type: text.file
path: data/target.txt
assert:
  - target: text
    must:
      - contain: ["hello from target"]
```

## SR-PHP-RUN-002

```yaml spec-test
id: SR-PHP-RUN-002
type: cli.run
argv: ["hello-runner"]
exit_code: 0
harness:
  entrypoint: /bin/echo
assert:
  - target: stdout
    must:
      - contain: ["hello-runner"]
```
""",
        encoding="utf-8",
    )
    (cases_dir / "data").mkdir(parents=True)
    (cases_dir / "data" / "target.txt").write_text("hello from target\n", encoding="utf-8")

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
    assert cp.returncode == 0
    payload = json.loads(out_json.read_text(encoding="utf-8"))
    assert validate_conformance_report_payload(payload) == []
    assert payload["results"] == [
        {"id": "SR-PHP-RUN-001", "status": "pass", "category": None, "message": None},
        {"id": "SR-PHP-RUN-002", "status": "pass", "category": None, "message": None},
    ]


@pytest.mark.skipif(shutil.which("php") is None, reason="php is not installed")
@pytest.mark.skipif(not _php_has_yaml_extension(), reason="php yaml_parse extension is not installed")
def test_php_spec_runner_returns_nonzero_for_failed_case(tmp_path):
    repo_root = Path(__file__).resolve().parents[1]
    php_runner = repo_root / "scripts/php/spec_runner.php"
    cases_dir = tmp_path / "cases"
    out_json = tmp_path / "php-report.json"
    cases_dir.mkdir(parents=True)
    (cases_dir / "suite.spec.md").write_text(
        """# Suite

```yaml spec-test
id: SR-PHP-RUN-003
type: text.file
assert:
  - target: text
    must:
      - regex: ["\\\\A\\\\Z"]
```
""",
        encoding="utf-8",
    )

    cp = subprocess.run(
        [
            "php",
            str(php_runner),
            "--cases",
            str(cases_dir),
            "--out",
            str(out_json),
        ],
        check=False,
        cwd=repo_root,
        capture_output=True,
        text=True,
    )
    assert cp.returncode == 1
    payload = json.loads(out_json.read_text(encoding="utf-8"))
    assert validate_conformance_report_payload(payload) == []
    assert payload["results"] == [
        {
            "id": "SR-PHP-RUN-003",
            "status": "fail",
            "category": "assertion",
            "message": "[case_id=SR-PHP-RUN-003 assert_path=assert[0].must[0] target=text op=regex] regex assertion failed",
        }
    ]


@pytest.mark.skipif(shutil.which("php") is None, reason="php is not installed")
@pytest.mark.skipif(not _php_has_yaml_extension(), reason="php yaml_parse extension is not installed")
def test_php_spec_runner_uses_env_fallback_entrypoint(tmp_path):
    repo_root = Path(__file__).resolve().parents[1]
    php_runner = repo_root / "scripts/php/spec_runner.php"
    cases_dir = tmp_path / "cases"
    out_json = tmp_path / "php-report.json"
    cases_dir.mkdir(parents=True)
    (cases_dir / "suite.spec.md").write_text(
        """# Suite

```yaml spec-test
id: SR-PHP-RUN-004
type: cli.run
argv: ["from-env-entrypoint"]
exit_code: 0
harness: {}
assert:
  - target: stdout
    must:
      - contain: ["from-env-entrypoint"]
```
""",
        encoding="utf-8",
    )

    env = os.environ.copy()
    env["SPEC_RUNNER_ENTRYPOINT"] = "/bin/echo"
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
        env=env,
        capture_output=True,
        text=True,
    )
    assert cp.returncode == 0
    payload = json.loads(out_json.read_text(encoding="utf-8"))
    assert validate_conformance_report_payload(payload) == []
    assert payload["results"] == [
        {"id": "SR-PHP-RUN-004", "status": "pass", "category": None, "message": None}
    ]
