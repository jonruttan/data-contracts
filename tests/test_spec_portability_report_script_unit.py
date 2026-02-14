# SPEC-OPT-OUT: Script wiring/IO behavior for portability metric reporting utility.
from __future__ import annotations

import importlib.util
import json
from pathlib import Path


def _load_module():
    path = Path(__file__).resolve().parents[1] / "scripts/spec_portability_report.py"
    spec = importlib.util.spec_from_file_location("spec_portability_report_script", path)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_script_writes_json(monkeypatch, tmp_path: Path) -> None:
    mod = _load_module()
    out = tmp_path / "portability.json"

    monkeypatch.setattr(
        mod,
        "spec_portability_report_jsonable",
        lambda *_a, **_k: {
            "version": 1,
            "summary": {
                "total_cases": 2,
                "overall_self_contained_ratio": 0.8,
                "overall_implementation_reliance_ratio": 0.2,
                "overall_logic_self_contained_ratio": 0.9,
                "overall_logic_reliance_ratio": 0.1,
                "overall_execution_portability_ratio": 0.7,
                "overall_execution_coupling_ratio": 0.3,
            },
            "segments": {
                "conformance": {
                    "case_count": 2,
                    "mean_self_contained_ratio": 0.8,
                    "mean_implementation_reliance_ratio": 0.2,
                    "mean_logic_self_contained_ratio": 0.9,
                    "mean_logic_reliance_ratio": 0.1,
                    "mean_execution_portability_ratio": 0.7,
                    "mean_execution_coupling_ratio": 0.3,
                    "penalty_counts": {},
                }
            },
            "worst_cases": [],
            "cases": [],
            "config": {},
            "errors": [],
        },
    )

    code = mod.main(["--out", str(out)])
    assert code == 0
    payload = json.loads(out.read_text(encoding="utf-8"))
    assert payload["summary"]["total_cases"] == 2


def test_script_writes_markdown(monkeypatch, tmp_path: Path) -> None:
    mod = _load_module()
    out = tmp_path / "portability.md"

    monkeypatch.setattr(
        mod,
        "spec_portability_report_jsonable",
        lambda *_a, **_k: {
            "version": 1,
            "summary": {
                "total_cases": 1,
                "overall_self_contained_ratio": 1.0,
                "overall_implementation_reliance_ratio": 0.0,
                "overall_logic_self_contained_ratio": 1.0,
                "overall_logic_reliance_ratio": 0.0,
                "overall_execution_portability_ratio": 1.0,
                "overall_execution_coupling_ratio": 0.0,
            },
            "segments": {
                "conformance": {
                    "case_count": 1,
                    "mean_self_contained_ratio": 1.0,
                    "mean_implementation_reliance_ratio": 0.0,
                    "mean_logic_self_contained_ratio": 1.0,
                    "mean_logic_reliance_ratio": 0.0,
                    "mean_execution_portability_ratio": 1.0,
                    "mean_execution_coupling_ratio": 0.0,
                    "penalty_counts": {},
                }
            },
            "worst_cases": [
                {
                    "id": "C1",
                    "type": "text.file",
                    "segment": "conformance",
                    "self_contained_ratio": 1.0,
                    "file": "docs/spec/conformance/cases/a.spec.md",
                    "reasons": [],
                }
            ],
            "cases": [],
            "config": {},
            "errors": [],
        },
    )

    code = mod.main(["--format", "md", "--out", str(out)])
    assert code == 0
    text = out.read_text(encoding="utf-8")
    assert text.startswith("# Spec Portability Report")
    assert "| conformance | 1 | 1.0000 | 0.0000 | 1.0000 | 1.0000 |" in text


def test_script_top_n_override_and_external_config(monkeypatch, tmp_path: Path) -> None:
    mod = _load_module()
    out = tmp_path / "portability.json"
    cfg_path = tmp_path / "cfg.yaml"
    cfg_path.write_text(
        """
roots: ["docs/spec/conformance/cases"]
report:
  top_n: 3
""",
        encoding="utf-8",
    )

    seen: dict = {}

    def _fake(_repo_root, config=None):
        seen["config"] = config
        return {
            "version": 1,
            "summary": {
                "total_cases": 0,
                "overall_self_contained_ratio": 0.0,
                "overall_implementation_reliance_ratio": 0.0,
                "overall_logic_self_contained_ratio": 0.0,
                "overall_logic_reliance_ratio": 0.0,
                "overall_execution_portability_ratio": 0.0,
                "overall_execution_coupling_ratio": 0.0,
            },
            "segments": {},
            "worst_cases": [],
            "cases": [],
            "config": config or {},
            "errors": [],
        }

    monkeypatch.setattr(mod, "spec_portability_report_jsonable", _fake)

    code = mod.main(["--config", str(cfg_path), "--top-n", "7", "--out", str(out)])
    assert code == 0
    assert isinstance(seen.get("config"), dict)
    assert seen["config"]["report"]["top_n"] == 7
