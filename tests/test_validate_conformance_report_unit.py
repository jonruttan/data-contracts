# SPEC-OPT-OUT: Exercises behavior not yet representable as stable .spec.md coverage (unit-level API/diagnostic/infrastructure checks).
import json

from spec_runner.conformance import validate_conformance_report_payload


def test_validate_sample_php_bootstrap_report_shape(tmp_path):
    report = {
        "version": 1,
        "results": [
            {
                "id": "DCCONF-PHP-BOOT-001",
                "status": "fail",
                "category": "runtime",
                "message": "PHP conformance runner bootstrap placeholder",
            }
        ],
    }
    p = tmp_path / "php-report.json"
    p.write_text(json.dumps(report), encoding="utf-8")
    loaded = json.loads(p.read_text(encoding="utf-8"))
    errs = validate_conformance_report_payload(loaded)
    assert errs == []


def test_validate_report_accepts_skip_status():
    report = {
        "version": 1,
        "results": [
            {
                "id": "DCCONF-SKIP-001",
                "status": "skip",
                "category": None,
                "message": None,
            }
        ],
    }
    errs = validate_conformance_report_payload(report)
    assert errs == []
