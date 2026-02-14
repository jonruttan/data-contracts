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


def _env_bin() -> str | None:
    return shutil.which("env")


@pytest.mark.skipif(shutil.which("php") is None, reason="php is not installed")
@pytest.mark.skipif(not _php_has_yaml_extension(), reason="php yaml_parse extension is not installed")
def test_php_spec_runner_matches_pass_fixture_suite(tmp_path):
    repo_root = Path(__file__).resolve().parents[1]
    php_runner = repo_root / "scripts/php/spec_runner.php"
    fixtures_root = repo_root / "docs/spec/impl/php/cases"
    cases_dir = tmp_path / "cases"
    out_json = tmp_path / "php-report.json"
    cases_dir.mkdir(parents=True)
    pass_case = case_file_name("runner_pass")
    (cases_dir / pass_case).write_text(
        (fixtures_root / pass_case).read_text(encoding="utf-8"),
        encoding="utf-8",
    )
    (cases_dir / "fixtures").mkdir(parents=True)
    for name in ("sample.txt", "path_target.txt"):
        (cases_dir / "fixtures" / name).write_text(
            (fixtures_root / "fixtures" / name).read_text(encoding="utf-8"),
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
    assert compare_conformance_results(expected, actual) == []


@pytest.mark.skipif(shutil.which("php") is None, reason="php is not installed")
@pytest.mark.skipif(not _php_has_yaml_extension(), reason="php yaml_parse extension is not installed")
def test_php_spec_runner_matches_failure_fixture_suite(tmp_path):
    repo_root = Path(__file__).resolve().parents[1]
    php_runner = repo_root / "scripts/php/spec_runner.php"
    fixtures_root = repo_root / "docs/spec/impl/php/cases"
    cases_dir = tmp_path / "cases"
    out_json = tmp_path / "php-report.json"
    cases_dir.mkdir(parents=True)
    failures_case = case_file_name("runner_failures")
    (cases_dir / failures_case).write_text(
        (fixtures_root / failures_case).read_text(encoding="utf-8"),
        encoding="utf-8",
    )
    (cases_dir / "fixtures").mkdir(parents=True)
    (cases_dir / "fixtures" / "sample.txt").write_text(
        (fixtures_root / "fixtures" / "sample.txt").read_text(encoding="utf-8"),
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
    assert compare_conformance_results(expected, actual) == []


@pytest.mark.skipif(shutil.which("php") is None, reason="php is not installed")
@pytest.mark.skipif(not _php_has_yaml_extension(), reason="php yaml_parse extension is not installed")
def test_php_spec_runner_matches_assert_health_fixture_suite(tmp_path):
    repo_root = Path(__file__).resolve().parents[1]
    php_runner = repo_root / "scripts/php/spec_runner.php"
    fixtures_root = repo_root / "docs/spec/impl/php/cases"
    cases_dir = tmp_path / "cases"
    out_json = tmp_path / "php-report.json"
    cases_dir.mkdir(parents=True)
    assert_health_case = case_file_name("runner_assert_health")
    (cases_dir / assert_health_case).write_text(
        (fixtures_root / assert_health_case).read_text(encoding="utf-8"),
        encoding="utf-8",
    )

    env = os.environ.copy()
    env["SPEC_RUNNER_ASSERT_HEALTH"] = "warn"
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
        env=env,
        capture_output=True,
        text=True,
    )
    # Suite intentionally includes fail-status cases.
    assert cp.returncode == 1
    payload = json.loads(out_json.read_text(encoding="utf-8"))
    assert validate_conformance_report_payload(payload) == []
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
    assert compare_conformance_results(expected, actual) == []
    assert "WARN: ASSERT_HEALTH AH001" in cp.stderr
    assert "WARN: ASSERT_HEALTH AH005" not in cp.stderr


@pytest.mark.skipif(shutil.which("php") is None, reason="php is not installed")
@pytest.mark.skipif(not _php_has_yaml_extension(), reason="php yaml_parse extension is not installed")
def test_php_spec_runner_matches_portability_fixture_suite(tmp_path):
    repo_root = Path(__file__).resolve().parents[1]
    php_runner = repo_root / "scripts/php/spec_runner.php"
    fixtures_root = repo_root / "docs/spec/impl/php/cases"
    cases_dir = tmp_path / "cases"
    out_json = tmp_path / "php-report.json"
    cases_dir.mkdir(parents=True)
    portability_case = case_file_name("runner_portability")
    (cases_dir / portability_case).write_text(
        (fixtures_root / portability_case).read_text(encoding="utf-8"),
        encoding="utf-8",
    )
    (cases_dir / "fixtures").mkdir(parents=True)
    (cases_dir / "fixtures" / "path_target.txt").write_text(
        (fixtures_root / "fixtures" / "path_target.txt").read_text(encoding="utf-8"),
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
        check=True,
        cwd=repo_root,
        capture_output=True,
        text=True,
    )
    assert cp.returncode == 0
    payload = json.loads(out_json.read_text(encoding="utf-8"))
    assert validate_conformance_report_payload(payload) == []
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
    assert compare_conformance_results(expected, actual) == []


@pytest.mark.skipif(shutil.which("php") is None, reason="php is not installed")
@pytest.mark.skipif(not _php_has_yaml_extension(), reason="php yaml_parse extension is not installed")
@pytest.mark.skipif(_env_bin() is None, reason="env command is not available")
def test_php_spec_runner_env_allowlist_filters_ambient_env(tmp_path):
    repo_root = Path(__file__).resolve().parents[1]
    php_runner = repo_root / "scripts/php/spec_runner.php"
    cases_dir = tmp_path / "cases"
    out_json = tmp_path / "php-report.json"
    cases_dir.mkdir(parents=True)
    env_bin = _env_bin()
    assert env_bin

    cases_dir.joinpath(case_file_name("env-allowlist")).write_text(
        f"""# Env allowlist

```yaml spec-test
id: SR-PHP-ENV-ALLOWLIST-001
type: cli.run
argv: []
exit_code: 0
harness:
  entrypoint: {env_bin}
assert:
  - target: stdout
    must:
      - contain: ["CK_ALLOWED=ok"]
  - target: stdout
    cannot:
      - contain: ["CK_SECRET=shh"]
```
""",
        encoding="utf-8",
    )

    env = os.environ.copy()
    env["CK_ALLOWED"] = "ok"
    env["CK_SECRET"] = "shh"
    env["SPEC_RUNNER_ENV_ALLOWLIST"] = "CK_ALLOWED"

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
        {
            "id": "SR-PHP-ENV-ALLOWLIST-001",
            "status": "pass",
            "category": None,
            "message": None,
        }
    ]


@pytest.mark.skipif(shutil.which("php") is None, reason="php is not installed")
@pytest.mark.skipif(not _php_has_yaml_extension(), reason="php yaml_parse extension is not installed")
def test_php_spec_runner_rejects_empty_pattern_arg(tmp_path):
    repo_root = Path(__file__).resolve().parents[1]
    php_runner = repo_root / "scripts/php/spec_runner.php"
    cases_dir = tmp_path / "cases"
    out_json = tmp_path / "php-report.json"
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
def test_php_spec_runner_can_load_yaml_and_json_cases_with_opt_in_formats(tmp_path):
    repo_root = Path(__file__).resolve().parents[1]
    php_runner = repo_root / "scripts/php/spec_runner.php"
    cases_dir = tmp_path / "cases"
    out_json = tmp_path / "php-report.json"
    cases_dir.mkdir(parents=True)

    (cases_dir / "yaml_case.spec.yaml").write_text(
        """id: SR-PHP-FMT-001
type: text.file
assert:
  - target: text
    must:
      - contain: ["SR-PHP-FMT-001"]
""",
        encoding="utf-8",
    )
    (cases_dir / "json_case.spec.json").write_text(
        json.dumps(
            {
                "id": "SR-PHP-FMT-002",
                "type": "text.file",
                "assert": [{"target": "text", "must": [{"contain": ["SR-PHP-FMT-002"]}]}],
            }
        ),
        encoding="utf-8",
    )

    cp = subprocess.run(
        [
            "php",
            str(php_runner),
            "--cases",
            str(cases_dir),
            "--case-formats",
            "yaml,json",
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
    ids = [str(x["id"]) for x in payload.get("results", [])]
    assert sorted(ids) == ["SR-PHP-FMT-001", "SR-PHP-FMT-002"]
