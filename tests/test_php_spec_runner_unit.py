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
def test_php_spec_runner_matches_pass_fixture_suite(tmp_path):
    repo_root = Path(__file__).resolve().parents[1]
    php_runner = repo_root / "scripts/php/spec_runner.php"
    fixtures_root = repo_root / "docs/spec/impl/php/cases"
    cases_dir = tmp_path / "cases"
    out_json = tmp_path / "php-report.json"
    cases_dir.mkdir(parents=True)
    (cases_dir / "runner-pass.spec.md").write_text(
        (fixtures_root / "runner-pass.spec.md").read_text(encoding="utf-8"),
        encoding="utf-8",
    )
    (cases_dir / "fixtures").mkdir(parents=True)
    for name in ("sample.txt", "path-target.txt"):
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
    (cases_dir / "runner-failures.spec.md").write_text(
        (fixtures_root / "runner-failures.spec.md").read_text(encoding="utf-8"),
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
    (cases_dir / "runner-assert-health.spec.md").write_text(
        (fixtures_root / "runner-assert-health.spec.md").read_text(encoding="utf-8"),
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


@pytest.mark.skipif(shutil.which("php") is None, reason="php is not installed")
@pytest.mark.skipif(not _php_has_yaml_extension(), reason="php yaml_parse extension is not installed")
def test_php_spec_runner_matches_portability_fixture_suite(tmp_path):
    repo_root = Path(__file__).resolve().parents[1]
    php_runner = repo_root / "scripts/php/spec_runner.php"
    fixtures_root = repo_root / "docs/spec/impl/php/cases"
    cases_dir = tmp_path / "cases"
    out_json = tmp_path / "php-report.json"
    cases_dir.mkdir(parents=True)
    (cases_dir / "runner-portability.spec.md").write_text(
        (fixtures_root / "runner-portability.spec.md").read_text(encoding="utf-8"),
        encoding="utf-8",
    )
    (cases_dir / "fixtures").mkdir(parents=True)
    (cases_dir / "fixtures" / "path-target.txt").write_text(
        (fixtures_root / "fixtures" / "path-target.txt").read_text(encoding="utf-8"),
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
