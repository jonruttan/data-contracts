# SPEC-OPT-OUT: Library loading/import resolution behavior for spec-lang symbol reuse.
from __future__ import annotations

from pathlib import Path

import pytest

from spec_runner.spec_lang import SpecLangLimits, eval_predicate
from spec_runner.spec_lang_libraries import load_spec_lang_symbols_for_case


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def test_load_spec_lang_symbols_from_library_paths(tmp_path: Path) -> None:
    case_doc = tmp_path / "cases" / "sample.spec.md"
    _write(case_doc, "# Case\n")
    lib_doc = tmp_path / "libs" / "common.spec.md"
    _write(
        lib_doc,
        """# Common

## LIB-1

```yaml spec-test
id: LIB-1
type: spec_lang.library
definitions:
  public:
    is_warn:
      fn:
      - [text]
      - std.string.contains:
        - {var: text}
        - WARN
    is_error:
      fn:
      - [text]
      - std.string.contains:
        - {var: text}
        - ERROR
```
""",
    )

    symbols = load_spec_lang_symbols_for_case(
        doc_path=case_doc,
        harness={"spec_lang": {"includes": ["/libs/common.spec.md"]}},
        limits=SpecLangLimits(timeout_ms=0),
    )
    expr = [
        "std.logic.and",
        ["call", ["var", "is_warn"], ["std.core.subject"]],
        ["std.logic.not", ["call", ["var", "is_error"], ["std.core.subject"]]],
    ]
    assert eval_predicate(expr, subject="WARN: sample", symbols=symbols) is True


def test_library_import_cycle_is_rejected(tmp_path: Path) -> None:
    case_doc = tmp_path / "cases" / "sample.spec.md"
    _write(case_doc, "# Case\n")
    _write(
        tmp_path / "libs" / "a.spec.md",
        """```yaml spec-test
id: LIB-A
type: spec_lang.library
imports: ["/libs/b.spec.md"]
definitions:
  public:
    a:
      fn:
      - [x]
      - {var: x}
```
""",
    )
    _write(
        tmp_path / "libs" / "b.spec.md",
        """```yaml spec-test
id: LIB-B
type: spec_lang.library
imports: ["/libs/a.spec.md"]
definitions:
  public:
    b:
      fn:
      - [x]
      - {var: x}
```
""",
    )

    with pytest.raises(ValueError, match="cycle"):
        load_spec_lang_symbols_for_case(
            doc_path=case_doc,
            harness={"spec_lang": {"includes": ["/libs/a.spec.md"]}},
            limits=SpecLangLimits(timeout_ms=0),
        )


def test_duplicate_library_symbol_is_rejected(tmp_path: Path) -> None:
    case_doc = tmp_path / "cases" / "sample.spec.md"
    _write(case_doc, "# Case\n")
    _write(
        tmp_path / "libs" / "a.spec.md",
        """```yaml spec-test
id: LIB-A
type: spec_lang.library
definitions:
  public:
    same:
      fn:
      - [x]
      - {var: x}
```
""",
    )
    _write(
        tmp_path / "libs" / "b.spec.md",
        """```yaml spec-test
id: LIB-B
type: spec_lang.library
definitions:
  public:
    same:
      fn:
      - [x]
      - {var: x}
```
""",
    )

    with pytest.raises(ValueError, match="duplicate exported library symbol"):
        load_spec_lang_symbols_for_case(
            doc_path=case_doc,
            harness={"spec_lang": {"includes": ["/libs/a.spec.md", "/libs/b.spec.md"]}},
            limits=SpecLangLimits(timeout_ms=0),
        )


def test_harness_exports_filters_symbols(tmp_path: Path) -> None:
    case_doc = tmp_path / "cases" / "sample.spec.md"
    _write(case_doc, "# Case\n")
    _write(
        tmp_path / "libs" / "a.spec.md",
        """```yaml spec-test
id: LIB-A
type: spec_lang.library
definitions:
  public:
    keep:
      fn:
      - [x]
      - {var: x}
  private:
    drop:
      fn:
      - [x]
      - {var: x}
```
""",
    )

    symbols = load_spec_lang_symbols_for_case(
        doc_path=case_doc,
        harness={"spec_lang": {"includes": ["/libs/a.spec.md"], "exports": ["keep"]}},
        limits=SpecLangLimits(timeout_ms=0),
    )
    assert "keep" in symbols
    assert "drop" not in symbols


def test_library_function_rejects_list_s_expr_authoring(tmp_path: Path) -> None:
    case_doc = tmp_path / "cases" / "sample.spec.md"
    _write(case_doc, "# Case\n")
    _write(
        tmp_path / "libs" / "bad.spec.md",
        """```yaml spec-test
id: LIB-BAD
type: spec_lang.library
definitions:
  public:
    bad: ["fn", ["x"], ["var", "x"]]
```
""",
    )
    with pytest.raises(ValueError, match="list expressions are not allowed"):
        load_spec_lang_symbols_for_case(
            doc_path=case_doc,
            harness={"spec_lang": {"includes": ["/libs/bad.spec.md"]}},
            limits=SpecLangLimits(timeout_ms=0),
        )


def test_markdown_domain_library_exports_full_core_helpers() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    case_doc = repo_root / "docs/spec/conformance/cases/core/domain_libraries.spec.md"
    symbols = load_spec_lang_symbols_for_case(
        doc_path=case_doc,
        harness={"spec_lang": {"includes": ["/docs/spec/libraries/domain/markdown_core.spec.md"]}},
        limits=SpecLangLimits(timeout_ms=0),
    )

    profile = {
        "value": "# Contract\n\n## Usage\n\n```yaml spec-test\nid: A\n```\n",
        "meta": {},
        "context": {
            "headings": [
                {"text": "Contract", "level": 1},
                {"text": "Usage", "level": 2},
            ],
            "heading_positions": {"Contract": 1, "Usage": 2},
            "links": [{"target": "/docs/spec/current.md", "resolved": True}],
            "tokens": {"DOCS_ONE": True, "DOCS_TWO": True},
            "token_owners": {"DOCS_ONE": ["/docs/book/index.md"]},
            "token_dependencies": [{"token": "DOCS_ONE", "depends_on": "DOCS_BASE", "resolved": True}],
        },
    }
    lit_profile = ["lit", profile]

    assert eval_predicate(["call", ["var", "md.has_heading"], lit_profile, "Contract"], subject=None, symbols=symbols) is True
    assert (
        eval_predicate(["call", ["var", "domain.markdown.has_heading"], lit_profile, "Usage"], subject=None, symbols=symbols)
        is True
    )
    assert eval_predicate(["call", ["var", "md.heading_level_exists"], lit_profile, 2], subject=None, symbols=symbols) is True
    assert eval_predicate(
        ["call", ["var", "md.required_sections_present"], lit_profile, ["lit", ["Contract", "Usage"]]],
        subject=None,
        symbols=symbols,
    ) is True
    assert eval_predicate(
        ["call", ["var", "md.section_order_valid"], lit_profile, ["lit", ["Contract", "Usage"]]],
        subject=None,
        symbols=symbols,
    ) is True
    assert eval_predicate(["call", ["var", "md.link_targets_all_resolve"], lit_profile], subject=None, symbols=symbols) is True
    assert eval_predicate(["call", ["var", "md.has_broken_links"], lit_profile], subject=None, symbols=symbols) is False
    assert eval_predicate(["call", ["var", "md.has_yaml_spec_test_fence"], lit_profile], subject=None, symbols=symbols) is True
    assert eval_predicate(
        ["call", ["var", "md.code_fence_language_exists"], lit_profile, "yaml"], subject=None, symbols=symbols
    ) is True
    assert eval_predicate(["call", ["var", "md.token_present"], lit_profile, "DOCS_ONE"], subject=None, symbols=symbols) is True
    assert eval_predicate(
        ["call", ["var", "md.tokens_all_present"], lit_profile, ["lit", ["DOCS_ONE", "DOCS_TWO"]]],
        subject=None,
        symbols=symbols,
    ) is True
    assert eval_predicate(["call", ["var", "md.token_ownership_unique"], lit_profile], subject=None, symbols=symbols) is True
    assert eval_predicate(
        ["call", ["var", "md.token_dependencies_resolved"], lit_profile], subject=None, symbols=symbols
    ) is True
    assert eval_predicate(
        ["call", ["var", "md.has_heading"], "# Contract\n\nText", "Contract"],
        subject=None,
        symbols=symbols,
    ) is True
