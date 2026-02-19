# SPEC-OPT-OUT: Objective scorecard composition and baseline-note integrity checks are script/metrics internals not representable as stable .spec.md coverage.
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import yaml

import spec_runner.quality_metrics as qm


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _fake_report(summary_key: str, value: float) -> dict:
    return {
        "version": 1,
        "summary": {summary_key: value},
        "segments": {},
        "cases": [],
        "errors": [],
    }


def test_objective_scorecard_deterministic_scoring(monkeypatch, tmp_path: Path) -> None:
    _write(
        tmp_path / "specs/governance/metrics/objective_manifest.yaml",
        yaml.safe_dump(
            {
                "version": 1,
                "objectives": [
                    {
                        "id": "OBJ-A",
                        "name": "A",
                        "primary": {
                            "source": "spec_portability",
                            "field": "summary.overall_self_contained_ratio",
                            "mode": "direct",
                            "scale": 1.0,
                        },
                        "counters": [
                            {
                                "id": "counter-a",
                                "source": "spec_lang_adoption",
                                "field": "summary.native_logic_escape_case_ratio",
                                "mode": "one_minus",
                                "scale": 1.0,
                            }
                        ],
                        "tripwires": [],
                    }
                ],
            },
            sort_keys=False,
        ),
    )

    monkeypatch.setattr(qm, "spec_portability_report_jsonable", lambda *_a, **_k: _fake_report("overall_self_contained_ratio", 0.8))
    monkeypatch.setattr(qm, "spec_lang_adoption_report_jsonable", lambda *_a, **_k: _fake_report("native_logic_escape_case_ratio", 0.2))
    monkeypatch.setattr(qm, "runner_independence_report_jsonable", lambda *_a, **_k: _fake_report("overall_runner_independence_ratio", 0.5))
    monkeypatch.setattr(qm, "docs_operability_report_jsonable", lambda *_a, **_k: _fake_report("overall_docs_operability_ratio", 0.5))
    monkeypatch.setattr(qm, "contract_assertions_report_jsonable", lambda *_a, **_k: _fake_report("contract_must_coverage_ratio", 1.0))

    payload = qm.objective_scorecard_report_jsonable(tmp_path)
    assert payload["errors"] == []
    assert payload["summary"]["objective_count"] == 1
    assert payload["summary"]["overall_status"] == "green"
    assert payload["summary"]["overall_min_score"] > 0.7


def test_objective_scorecard_tripwire_sets_red(monkeypatch, tmp_path: Path) -> None:
    _write(
        tmp_path / "specs/governance/metrics/objective_manifest.yaml",
        yaml.safe_dump(
            {
                "version": 1,
                "objectives": [
                    {
                        "id": "OBJ-TW",
                        "name": "TW",
                        "primary": {
                            "source": "spec_portability",
                            "field": "summary.overall_self_contained_ratio",
                        },
                        "tripwires": [{"check_id": "x.check", "reason": "x"}],
                    }
                ],
            },
            sort_keys=False,
        ),
    )
    monkeypatch.setattr(qm, "spec_portability_report_jsonable", lambda *_a, **_k: _fake_report("overall_self_contained_ratio", 0.9))
    monkeypatch.setattr(qm, "spec_lang_adoption_report_jsonable", lambda *_a, **_k: _fake_report("overall_logic_self_contained_ratio", 0.9))
    monkeypatch.setattr(qm, "runner_independence_report_jsonable", lambda *_a, **_k: _fake_report("overall_runner_independence_ratio", 0.9))
    monkeypatch.setattr(qm, "docs_operability_report_jsonable", lambda *_a, **_k: _fake_report("overall_docs_operability_ratio", 0.9))
    monkeypatch.setattr(qm, "contract_assertions_report_jsonable", lambda *_a, **_k: _fake_report("contract_must_coverage_ratio", 1.0))

    payload = qm.objective_scorecard_report_jsonable(tmp_path, config={"tripwire_status": {"x.check": "fail"}})
    assert payload["summary"]["overall_status"] == "red"
    assert payload["summary"]["tripwire_hit_count"] == 1


def test_objective_scorecard_missing_source_reports_error(monkeypatch, tmp_path: Path) -> None:
    _write(
        tmp_path / "specs/governance/metrics/objective_manifest.yaml",
        yaml.safe_dump(
            {
                "version": 1,
                "objectives": [
                    {
                        "id": "OBJ-MISS",
                        "name": "MISS",
                        "primary": {"source": "spec_portability", "field": "summary.not_there"},
                        "tripwires": [],
                    }
                ],
            },
            sort_keys=False,
        ),
    )
    monkeypatch.setattr(qm, "spec_portability_report_jsonable", lambda *_a, **_k: _fake_report("overall_self_contained_ratio", 0.2))
    monkeypatch.setattr(qm, "spec_lang_adoption_report_jsonable", lambda *_a, **_k: _fake_report("overall_logic_self_contained_ratio", 0.2))
    monkeypatch.setattr(qm, "runner_independence_report_jsonable", lambda *_a, **_k: _fake_report("overall_runner_independence_ratio", 0.2))
    monkeypatch.setattr(qm, "docs_operability_report_jsonable", lambda *_a, **_k: _fake_report("overall_docs_operability_ratio", 0.2))
    monkeypatch.setattr(qm, "contract_assertions_report_jsonable", lambda *_a, **_k: _fake_report("contract_must_coverage_ratio", 0.2))

    payload = qm.objective_scorecard_report_jsonable(tmp_path)
    assert payload["summary"]["objective_count"] == 1
    assert payload["objectives"][0]["primary"]["value"] is None
    assert payload["objectives"][0]["status"] in {"yellow", "red"}


def test_validate_metric_baseline_notes_hashes(tmp_path: Path) -> None:
    baseline = tmp_path / "specs/governance/metrics/a.json"
    _write(baseline, json.dumps({"x": 1}) + "\n")
    digest = hashlib.sha256(baseline.read_bytes()).hexdigest()
    notes = tmp_path / "specs/governance/metrics/baseline_update_notes.yaml"
    _write(
        notes,
        yaml.safe_dump(
            {
                "version": 1,
                "entries": [
                    {
                        "baseline": "specs/governance/metrics/a.json",
                        "sha256": digest,
                        "rationale": "update",
                        "measurement_model_change": "no",
                    }
                ],
            },
            sort_keys=False,
        ),
    )

    violations = qm.validate_metric_baseline_notes(
        tmp_path,
        notes_path="specs/governance/metrics/baseline_update_notes.yaml",
        baseline_paths=["specs/governance/metrics/a.json"],
    )
    assert violations == []

    _write(baseline, json.dumps({"x": 2}) + "\n")
    violations = qm.validate_metric_baseline_notes(
        tmp_path,
        notes_path="specs/governance/metrics/baseline_update_notes.yaml",
        baseline_paths=["specs/governance/metrics/a.json"],
    )
    assert any("sha256 mismatch" in v for v in violations)
