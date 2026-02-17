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
type: spec_lang.export
defines:
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
type: spec_lang.export
imports: ["/libs/b.spec.md"]
defines:
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
type: spec_lang.export
imports: ["/libs/a.spec.md"]
defines:
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
type: spec_lang.export
defines:
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
type: spec_lang.export
defines:
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
type: spec_lang.export
defines:
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


def test_harness_exports_keeps_private_dependencies(tmp_path: Path) -> None:
    case_doc = tmp_path / "cases" / "sample.spec.md"
    _write(case_doc, "# Case\n")
    _write(
        tmp_path / "libs" / "a.spec.md",
        """```yaml spec-test
id: LIB-A
type: spec_lang.export
defines:
  public:
    keep:
      fn:
      - [x]
      - call:
        - {var: helper}
        - {var: x}
  private:
    helper:
      fn:
      - [x]
      - std.logic.eq:
        - {var: x}
        - ok
```
""",
    )

    symbols = load_spec_lang_symbols_for_case(
        doc_path=case_doc,
        harness={"spec_lang": {"includes": ["/libs/a.spec.md"], "exports": ["keep"]}},
        limits=SpecLangLimits(timeout_ms=0),
    )
    expr = ["call", ["var", "keep"], "ok"]
    assert eval_predicate(expr, subject=None, symbols=symbols) is True


def test_library_function_rejects_list_s_expr_authoring(tmp_path: Path) -> None:
    case_doc = tmp_path / "cases" / "sample.spec.md"
    _write(case_doc, "# Case\n")
    _write(
        tmp_path / "libs" / "bad.spec.md",
        """```yaml spec-test
id: LIB-BAD
type: spec_lang.export
defines:
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


def test_markdown_domain_library_rejects_spec_export_only_surface() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    case_doc = repo_root / "docs/spec/conformance/cases/core/domain_libraries.spec.md"
    with pytest.raises(ValueError, match="no spec_lang.export defines"):
        load_spec_lang_symbols_for_case(
            doc_path=case_doc,
            harness={"spec_lang": {"includes": ["/docs/spec/libraries/domain/markdown_core.spec.md"]}},
            limits=SpecLangLimits(timeout_ms=0),
        )
