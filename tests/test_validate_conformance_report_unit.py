import json
from pathlib import Path

from spec_runner.conformance import validate_conformance_report_payload


def test_validate_sample_php_bootstrap_report_shape(tmp_path):
    report = {
        "version": 1,
        "results": [
            {
                "id": "SRCONF-PHP-BOOT-001",
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
