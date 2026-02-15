# SPEC-OPT-OUT: Script wiring/IO behavior for objective scorecard reporting utility.
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


def test_objective_scorecard_report_script_writes_json(monkeypatch, tmp_path: Path) -> None:
    mod = _load("scripts/objective_scorecard_report.py", "objective_report")
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
