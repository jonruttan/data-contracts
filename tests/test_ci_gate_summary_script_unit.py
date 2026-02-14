# SPEC-OPT-OUT: Exercises behavior not yet representable as stable .spec.md coverage (unit-level API/diagnostic/infrastructure checks).
import importlib.util
import json
from pathlib import Path


def _load_script_module():
    repo_root = Path(__file__).resolve().parents[1]
    script_path = repo_root / "scripts/ci_gate_summary.py"
    spec = importlib.util.spec_from_file_location("ci_gate_summary_script", script_path)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_script_writes_pass_summary(monkeypatch, tmp_path):
    mod = _load_script_module()
    out = tmp_path / "gate-summary.json"

    monkeypatch.setattr(
        mod,
        "_default_steps",
        lambda _python_bin: [
            ("a", ["echo", "a"]),
            ("b", ["echo", "b"]),
        ],
    )
    monkeypatch.setattr(mod, "_run_command", lambda _cmd: 0)

    code = mod.main(["--out", str(out), "--runner-bin", "./scripts/runner_adapter.sh"])
    assert code == 0
    payload = json.loads(out.read_text(encoding="utf-8"))
    assert payload["version"] == 1
    assert payload["status"] == "pass"
    assert [x["name"] for x in payload["steps"]] == ["a", "b"]
    assert all(x["status"] == "pass" for x in payload["steps"])


def test_script_stops_at_first_failure_and_writes_summary(monkeypatch, tmp_path):
    mod = _load_script_module()
    out = tmp_path / "gate-summary.json"

    monkeypatch.setattr(
        mod,
        "_default_steps",
        lambda _python_bin: [
            ("a", ["echo", "a"]),
            ("b", ["echo", "b"]),
            ("c", ["echo", "c"]),
        ],
    )
    codes = iter((0, 3, 0))
    monkeypatch.setattr(mod, "_run_command", lambda _cmd: next(codes))

    code = mod.main(["--out", str(out), "--runner-bin", "./scripts/runner_adapter.sh"])
    assert code == 3
    payload = json.loads(out.read_text(encoding="utf-8"))
    assert payload["status"] == "fail"
    assert [x["name"] for x in payload["steps"]] == ["a", "b"]
    assert payload["steps"][1]["status"] == "fail"
    assert payload["steps"][1]["exit_code"] == 3
