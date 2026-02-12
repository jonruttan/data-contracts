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


@pytest.mark.skipif(shutil.which("php") is None, reason="php is not installed")
def test_php_bootstrap_runner_matches_text_file_subset_expected(tmp_path):
    repo_root = Path(__file__).resolve().parents[3]

    cases_src = repo_root / "tools/spec_runner/fixtures/conformance/cases/php-text-file-subset.yaml"
    expected_src = repo_root / "tools/spec_runner/fixtures/conformance/expected/php-text-file-subset.yaml"
    php_runner = repo_root / "tools/spec_runner/scripts/php/conformance_runner.php"

    cases_dir = tmp_path / "cases"
    expected_dir = tmp_path / "expected"
    out_json = tmp_path / "php-report.json"
    cases_dir.mkdir(parents=True)
    expected_dir.mkdir(parents=True)
    (cases_dir / cases_src.name).write_text(cases_src.read_text(encoding="utf-8"), encoding="utf-8")
    (expected_dir / expected_src.name).write_text(expected_src.read_text(encoding="utf-8"), encoding="utf-8")

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
    expected = load_expected_results(expected_dir)
    errs = compare_conformance_results(expected, actual)
    assert errs == []
