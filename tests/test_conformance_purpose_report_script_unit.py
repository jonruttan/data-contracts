import importlib.util
import json
from pathlib import Path


def _load_script_module():
    repo_root = Path(__file__).resolve().parents[3]
    script_path = repo_root / "tools/spec_runner/scripts/conformance_purpose_report.py"
    spec = importlib.util.spec_from_file_location("conformance_purpose_report_script", script_path)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_script_json_mode_and_fail_on_warn(monkeypatch, tmp_path):
    mod = _load_script_module()
    out = tmp_path / "purpose.json"
    monkeypatch.setattr(
        mod,
        "conformance_purpose_report_jsonable",
        lambda *_a, **_k: {
            "version": 1,
            "summary": {
                "total_rows": 1,
                "rows_with_warnings": 1,
                "row_warning_count": 1,
                "policy_error_count": 0,
                "total_warning_count": 1,
                "warning_code_counts": {"PUR001": 1},
            },
            "policy": {"path": "x", "exists": False, "config": {}, "errors": []},
            "rows": [
                {
                    "id": "A",
                    "title": "t",
                    "purpose": "p",
                    "type": "text.file",
                    "file": "a.spec.md",
                    "purpose_lint": {"enabled": True},
                    "warnings": [
                        {
                            "code": "PUR001",
                            "message": "purpose duplicates title",
                            "hint": "Rewrite purpose to explain intent or risk not already stated in title.",
                        }
                    ],
                }
            ],
        },
    )
    code = mod.main(["--out", str(out), "--fail-on-warn"])
    assert code == 1
    payload = json.loads(out.read_text(encoding="utf-8"))
    assert payload["summary"]["total_warning_count"] == 1


def test_script_markdown_mode(monkeypatch, tmp_path):
    mod = _load_script_module()
    out = tmp_path / "purpose.md"
    monkeypatch.setattr(
        mod,
        "conformance_purpose_report_jsonable",
        lambda *_a, **_k: {
            "version": 1,
            "summary": {
                "total_rows": 1,
                "rows_with_warnings": 1,
                "row_warning_count": 1,
                "policy_error_count": 0,
                "total_warning_count": 1,
                "warning_code_counts": {"PUR002": 1},
            },
            "policy": {"path": "x", "exists": True, "config": {}, "errors": []},
            "rows": [
                {
                    "id": "SRCONF-X",
                    "title": "t",
                    "purpose": "p",
                    "type": "text.file",
                    "file": "x.spec.md",
                    "purpose_lint": {"enabled": False},
                    "warnings": [
                        {
                            "code": "PUR002",
                            "message": "purpose word count 2 below minimum 8",
                            "hint": "Expand purpose to meet the configured minimum word count.",
                        }
                    ],
                }
            ],
        },
    )
    code = mod.main(["--format", "md", "--out", str(out)])
    assert code == 0
    text = out.read_text(encoding="utf-8")
    assert text.startswith("# Conformance Purpose Report")
    assert (
        "| SRCONF-X | text.file | PUR002 | purpose word count 2 below minimum 8 | "
        "Expand purpose to meet the configured minimum word count. | x.spec.md |"
    ) in text


def test_script_only_warnings_filters_rows(monkeypatch, tmp_path):
    mod = _load_script_module()
    out = tmp_path / "purpose.json"
    monkeypatch.setattr(
        mod,
        "conformance_purpose_report_jsonable",
        lambda *_a, **_k: {
            "version": 1,
            "summary": {
                "total_rows": 2,
                "rows_with_warnings": 1,
                "row_warning_count": 1,
                "policy_error_count": 0,
                "total_warning_count": 1,
                "warning_code_counts": {"PUR001": 1},
            },
            "policy": {"path": "x", "exists": False, "config": {}, "errors": []},
            "rows": [
                {
                    "id": "A",
                    "title": "t",
                    "purpose": "p",
                    "type": "text.file",
                    "file": "a.spec.md",
                    "purpose_lint": {"enabled": True},
                    "warnings": [
                        {
                            "code": "PUR001",
                            "message": "purpose duplicates title",
                            "hint": "Rewrite purpose to explain intent or risk not already stated in title.",
                        }
                    ],
                },
                {
                    "id": "B",
                    "title": "u",
                    "purpose": "v",
                    "type": "text.file",
                    "file": "b.spec.md",
                    "purpose_lint": {"enabled": True},
                    "warnings": [],
                },
            ],
        },
    )
    code = mod.main(["--out", str(out), "--only-warnings"])
    assert code == 0
    payload = json.loads(out.read_text(encoding="utf-8"))
    assert payload["summary"]["only_warnings"] is True
    assert payload["summary"]["total_rows"] == 1
    assert [r["id"] for r in payload["rows"]] == ["A"]
