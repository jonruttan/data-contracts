# SPEC-OPT-OUT: Exercises script wiring and formatter/linter behavior for markdown-yaml text rewriting.
from __future__ import annotations

import importlib.util
from pathlib import Path


def _load_script_module():
    repo_root = Path(__file__).resolve().parents[1]
    script_path = repo_root / "scripts/evaluate_style.py"
    spec = importlib.util.spec_from_file_location("evaluate_style_script", script_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("failed to load evaluate_style.py module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_evaluate_style_check_and_write(tmp_path):
    mod = _load_script_module()
    case = tmp_path / "sample.spec.md"
    case.write_text(
        """# Case\n\n```yaml spec-test\nid: EVAL-FMT-001\ntype: text.file\nassert:\n  - target: text\n    must:\n      - evaluate:\n          - [\"let\", [[\"loop\", [\"fn\", [\"n\", \"acc\"], [\"if\", [\"eq\", [\"var\", \"n\"], 0], [\"var\", \"acc\"], [\"call\", [\"var\", \"loop\"], [\"sub\", [\"var\", \"n\"], 1], [\"add\", [\"var\", \"acc\"], 1]]]]]], [\"eq\", [\"call\", [\"var\", \"loop\"], 1000, 0], 1000]]\n```\n""",
        encoding="utf-8",
    )

    code = mod.main(["--check", str(case)])
    assert code == 1

    code = mod.main(["--write", str(case)])
    assert code == 0

    code = mod.main(["--check", str(case)])
    assert code == 0

    updated = case.read_text(encoding="utf-8")
    assert "evaluate:" in updated
    assert '["let",' in updated
    assert '["fn"' in updated
    assert "\n" in updated


def test_evaluate_style_ignores_non_spec_fences(tmp_path):
    mod = _load_script_module()
    doc = tmp_path / "note.spec.md"
    doc.write_text(
        """# Note\n\n```yaml\na: [1,2,3]\n```\n""",
        encoding="utf-8",
    )

    code = mod.main(["--check", str(doc)])
    assert code == 0


def test_evaluate_style_does_not_reformat_blocks_without_evaluate(tmp_path):
    mod = _load_script_module()
    case = tmp_path / "plain.spec.md"
    original = (
        "# Plain\\n\\n"
        "```yaml spec-test\\n"
        "id: EVAL-FMT-PLAIN-001\\n"
        "type: text.file\\n"
        "assert:\\n"
        "  - target: text\\n"
        "    must:\\n"
        "      - contain: [\\\"ok\\\"]\\n"
        "```\\n"
    )
    case.write_text(original, encoding="utf-8")

    code = mod.main(["--check", str(case)])
    assert code == 0
    assert case.read_text(encoding="utf-8") == original
