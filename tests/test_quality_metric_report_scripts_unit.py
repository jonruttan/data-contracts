# SPEC-OPT-OUT: Script wiring/IO behavior for multi-family quality metric reporting utilities.
from __future__ import annotations

import importlib.util
import json
from pathlib import Path


def _load(path: str, name: str):
    p = Path(__file__).resolve().parents[1] / path
    spec = importlib.util.spec_from_file_location(name, p)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _fake_payload(summary_key: str) -> dict:
    return {
        "version": 1,
        "summary": {summary_key: 0.5},
        "segments": {},
        "errors": [],
    }


def test_spec_lang_adoption_report_script_writes_json(monkeypatch, tmp_path: Path) -> None:
    mod = _load("scripts/spec_lang_adoption_report.py", "sla_report")
    monkeypatch.setattr(mod, "spec_lang_adoption_report_jsonable", lambda *_a, **_k: _fake_payload("overall_logic_self_contained_ratio"))
    out = tmp_path / "sla.json"
    code = mod.main(["--out", str(out)])
    assert code == 0
    assert "overall_logic_self_contained_ratio" in json.loads(out.read_text(encoding="utf-8"))["summary"]


def test_runner_independence_report_script_writes_json(monkeypatch, tmp_path: Path) -> None:
    mod = _load("scripts/runner_independence_report.py", "ri_report")
    monkeypatch.setattr(mod, "runner_independence_report_jsonable", lambda *_a, **_k: _fake_payload("overall_runner_independence_ratio"))
    out = tmp_path / "ri.json"
    code = mod.main(["--out", str(out)])
    assert code == 0
    assert "overall_runner_independence_ratio" in json.loads(out.read_text(encoding="utf-8"))["summary"]


def test_docs_operability_report_script_writes_json(monkeypatch, tmp_path: Path) -> None:
    mod = _load("scripts/docs_operability_report.py", "do_report")
    monkeypatch.setattr(mod, "docs_operability_report_jsonable", lambda *_a, **_k: _fake_payload("overall_docs_operability_ratio"))
    out = tmp_path / "do.json"
    code = mod.main(["--out", str(out)])
    assert code == 0
    assert "overall_docs_operability_ratio" in json.loads(out.read_text(encoding="utf-8"))["summary"]


def test_contract_assertions_report_script_writes_json(monkeypatch, tmp_path: Path) -> None:
    mod = _load("scripts/contract_assertions_report.py", "ca_report")
    monkeypatch.setattr(mod, "contract_assertions_report_jsonable", lambda *_a, **_k: _fake_payload("overall_contract_assertions_ratio"))
    out = tmp_path / "ca.json"
    code = mod.main(["--out", str(out)])
    assert code == 0
    assert "overall_contract_assertions_ratio" in json.loads(out.read_text(encoding="utf-8"))["summary"]


def test_objective_scorecard_report_script_writes_json(monkeypatch, tmp_path: Path) -> None:
    mod = _load("scripts/objective_scorecard_report.py", "obj_report")
    monkeypatch.setattr(
        mod,
        "objective_scorecard_report_jsonable",
        lambda *_a, **_k: {
            "version": 1,
            "summary": {"overall_min_score": 0.5},
            "objectives": [],
            "tripwire_hits": [],
            "errors": [],
        },
    )
    out = tmp_path / "objective.json"
    code = mod.main(["--out", str(out)])
    assert code == 0
    assert "overall_min_score" in json.loads(out.read_text(encoding="utf-8"))["summary"]
