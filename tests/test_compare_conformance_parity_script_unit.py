import importlib.util
import json
from pathlib import Path


def _load_script_module():
    repo_root = Path(__file__).resolve().parents[1]
    script_path = repo_root / "scripts/compare_conformance_parity.py"
    spec = importlib.util.spec_from_file_location("compare_conformance_parity_script", script_path)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_script_writes_stable_artifact_on_failure(monkeypatch, tmp_path):
    mod = _load_script_module()
    out_path = tmp_path / "parity.json"

    monkeypatch.setattr(mod.shutil, "which", lambda _name: "/usr/bin/php")
    monkeypatch.setattr(
        mod,
        "run_parity_check",
        lambda _cfg: [
            "missing in php report: A",
            "mismatch for B: python(status=pass, category=None) != php(status=fail, category=runtime)",
            "python report invalid: report.version must equal 1",
        ],
    )

    code = mod.main(
        [
            "--cases",
            str(tmp_path / "cases"),
            "--python-runner",
            str(tmp_path / "runner.py"),
            "--php-runner",
            str(tmp_path / "runner.php"),
            "--python-timeout-seconds",
            "45",
            "--php-timeout-seconds",
            "45",
            "--out",
            str(out_path),
        ]
    )
    assert code == 1
    payload = json.loads(out_path.read_text(encoding="utf-8"))
    assert payload == {
        "missing": ["missing in php report: A"],
        "mismatch": [
            "mismatch for B: python(status=pass, category=None) != php(status=fail, category=runtime)"
        ],
        "shape_errors": ["python report invalid: report.version must equal 1"],
        "version": 1,
    }


def test_script_writes_empty_artifact_on_success(monkeypatch, tmp_path):
    mod = _load_script_module()
    out_path = tmp_path / "parity.json"

    monkeypatch.setattr(mod.shutil, "which", lambda _name: "/usr/bin/php")
    monkeypatch.setattr(mod, "run_parity_check", lambda _cfg: [])

    code = mod.main(
        [
            "--cases",
            str(tmp_path / "cases"),
            "--python-runner",
            str(tmp_path / "runner.py"),
            "--php-runner",
            str(tmp_path / "runner.php"),
            "--python-timeout-seconds",
            "45",
            "--php-timeout-seconds",
            "45",
            "--out",
            str(out_path),
        ]
    )
    assert code == 0
    payload = json.loads(out_path.read_text(encoding="utf-8"))
    assert payload == {"missing": [], "mismatch": [], "shape_errors": [], "version": 1}
