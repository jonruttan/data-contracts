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
        """# Case\n\n```yaml contract-spec\nid: EVAL-FMT-001\ntype: text.file\nassert:\n  - target: text\n    must:\n      - evaluate:\n          - [\"let\", [[\"loop\", [\"fn\", [\"n\", \"acc\"], [\"if\", [\"eq\", [\"var\", \"n\"], 0], [\"var\", \"acc\"], [\"call\", [\"var\", \"loop\"], [\"sub\", [\"var\", \"n\"], 1], [\"add\", [\"var\", \"acc\"], 1]]]]]], [\"eq\", [\"call\", [\"var\", \"loop\"], 1000, 0], 1000]]\n```\n""",
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
    assert "let:" in updated
    assert "\n" in updated


def test_evaluate_style_formats_nested_mapping_ast_args_block_first(tmp_path):
    mod = _load_script_module()
    case = tmp_path / "compact.spec.md"
    case.write_text(
        """# Compact\n\n```yaml contract-spec\nid: EVAL-FMT-002\ntype: text.file\nassert:\n  - target: text\n    must:\n      - evaluate:\n          - eq:\n              - add:\n                  - 1\n                  - 2\n              - 3\n```\n""",
        encoding="utf-8",
    )
    code = mod.main(["--write", str(case)])
    assert code == 0
    updated = case.read_text(encoding="utf-8")
    assert "eq:\n" in updated
    assert "  - add:\n" in updated
    assert "    - 1\n" in updated
    assert "    - 2\n" in updated
    assert "  - 3\n" in updated


def test_evaluate_style_canonicalizes_ref_node_layout(tmp_path):
    mod = _load_script_module()
    case = tmp_path / "subject.spec.md"
    case.write_text(
        """# Subject\n\n```yaml contract-spec\nid: EVAL-FMT-003\ntype: text.file\nassert:\n  - target: text\n    must:\n      - evaluate:\n          - contains:\n              - var: subject\n              - ok\n```\n""",
        encoding="utf-8",
    )

    code = mod.main(["--write", str(case)])
    assert code == 0
    updated = case.read_text(encoding="utf-8")
    assert "contains:\n" in updated
    assert "- {var: subject}\n" in updated
    assert "- ok\n" in updated


def test_evaluate_style_write_is_idempotent(tmp_path):
    mod = _load_script_module()
    case = tmp_path / "idempotent.spec.md"
    case.write_text(
        """# Idempotent\n\n```yaml contract-spec\nid: EVAL-FMT-004\ntype: text.file\nassert:\n  - target: text\n    must:\n      - evaluate:\n          - eq:\n              - add:\n                  - 1\n                  - 2\n              - 3\n```\n""",
        encoding="utf-8",
    )
    code = mod.main(["--write", str(case)])
    assert code == 0
    first = case.read_text(encoding="utf-8")
    code = mod.main(["--write", str(case)])
    assert code == 0
    second = case.read_text(encoding="utf-8")
    assert first == second


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
        "```yaml contract-spec\\n"
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
