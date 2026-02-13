# SPEC-OPT-OUT: Exercises behavior not yet representable as stable .spec.md coverage (unit-level API/diagnostic/infrastructure checks).
import importlib.util
import json
from pathlib import Path

from spec_runner.conformance import ConformanceResult


def _load_script_module():
    repo_root = Path(__file__).resolve().parents[1]
    script_path = repo_root / "scripts/python/conformance_runner.py"
    spec = importlib.util.spec_from_file_location("python_conformance_runner_script", script_path)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_script_writes_report_and_returns_zero_when_all_pass(monkeypatch, tmp_path):
    mod = _load_script_module()
    out_path = tmp_path / "report.json"
    cases_path = tmp_path / "cases"
    cases_path.mkdir(parents=True)

    monkeypatch.setattr(
        mod,
        "run_conformance_cases",
        lambda *_a, **_k: [
            ConformanceResult(id="A", status="pass", category=None, message=None),
            ConformanceResult(id="B", status="skip", category=None, message=None),
        ],
    )

    code = mod.main(["--cases", str(cases_path), "--out", str(out_path)])
    assert code == 0
    payload = json.loads(out_path.read_text(encoding="utf-8"))
    assert payload["version"] == 1
    assert payload["results"] == [
        {"id": "A", "status": "pass", "category": None, "message": None},
        {"id": "B", "status": "skip", "category": None, "message": None},
    ]


def test_script_returns_one_when_any_case_fails(monkeypatch, tmp_path):
    mod = _load_script_module()
    out_path = tmp_path / "report.json"
    cases_path = tmp_path / "cases"
    cases_path.mkdir(parents=True)

    monkeypatch.setattr(
        mod,
        "run_conformance_cases",
        lambda *_a, **_k: [
            ConformanceResult(id="A", status="fail", category="assertion", message="boom"),
        ],
    )

    code = mod.main(["--cases", str(cases_path), "--out", str(out_path)])
    assert code == 1
    payload = json.loads(out_path.read_text(encoding="utf-8"))
    assert payload["results"][0]["id"] == "A"


def test_script_rejects_empty_case_pattern(tmp_path):
    mod = _load_script_module()
    out_path = tmp_path / "report.json"
    cases_path = tmp_path / "cases"
    cases_path.mkdir(parents=True)

    code = mod.main(["--cases", str(cases_path), "--out", str(out_path), "--case-file-pattern", ""])
    assert code == 2
    assert not out_path.exists()
