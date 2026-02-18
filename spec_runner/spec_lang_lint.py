from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from spec_runner.codecs import load_external_cases
from spec_runner.settings import SETTINGS
from spec_runner.spec_lang_yaml_ast import SpecLangYamlAstError, compile_yaml_expr_to_sexpr

_GROUP_KEYS = {"MUST", "MAY", "MUST_NOT"}
_LEGACY_GROUP_KEYS = {"must", "can", "cannot"}
_WHEN_KEYS = {"must", "can", "cannot", "fail", "complete"}


@dataclass(frozen=True)
class SpecLangLintIssue:
    path: Path
    case_id: str
    field: str
    code: str
    message: str

    def render(self) -> str:
        rel = self.path.as_posix()
        return f"{rel}: case {self.case_id}: {self.code}: {self.field}: {self.message}"


def _append_issue(
    issues: list[SpecLangLintIssue],
    *,
    path: Path,
    case_id: str,
    field: str,
    code: str,
    message: str,
) -> None:
    issues.append(
        SpecLangLintIssue(path=path, case_id=case_id, field=field, code=code, message=message)
    )


def _lint_nested_lit(
    node: Any,
    *,
    issues: list[SpecLangLintIssue],
    path: Path,
    case_id: str,
    field: str,
    lit_depth: int = 0,
) -> None:
    if isinstance(node, list):
        for idx, child in enumerate(node):
            _lint_nested_lit(
                child,
                issues=issues,
                path=path,
                case_id=case_id,
                field=f"{field}[{idx}]",
                lit_depth=lit_depth,
            )
        return
    if not isinstance(node, dict):
        return

    if set(node.keys()) == {"lit"}:
        if lit_depth >= 1:
            _append_issue(
                issues,
                path=path,
                case_id=case_id,
                field=field,
                code="SLINT002",
                message="nested lit wrapper is forbidden",
            )
        _lint_nested_lit(
            node.get("lit"),
            issues=issues,
            path=path,
            case_id=case_id,
            field=f"{field}.lit",
            lit_depth=lit_depth + 1,
        )
        return

    for raw_key, value in node.items():
        key = str(raw_key)
        if key in _GROUP_KEYS or key in _LEGACY_GROUP_KEYS:
            _append_issue(
                issues,
                path=path,
                case_id=case_id,
                field=f"{field}.{key}",
                code="SLINT003",
                message="assertion group key is not a valid spec-lang operator in expression context",
            )
        _lint_nested_lit(
            value,
            issues=issues,
            path=path,
            case_id=case_id,
            field=f"{field}.{key}",
            lit_depth=lit_depth,
        )


def _lint_expression_mapping(
    expr: Any,
    *,
    issues: list[SpecLangLintIssue],
    path: Path,
    case_id: str,
    field: str,
) -> None:
    if not isinstance(expr, dict) or not expr:
        _append_issue(
            issues,
            path=path,
            case_id=case_id,
            field=field,
            code="SLINT004",
            message="expression leaf must be a non-empty operator mapping",
        )
        return
    if "evaluate" in expr:
        _append_issue(
            issues,
            path=path,
            case_id=case_id,
            field=field,
            code="SLINT001",
            message="evaluate wrapper is forbidden; place operator mapping directly in asserts",
        )

    _lint_nested_lit(
        expr,
        issues=issues,
        path=path,
        case_id=case_id,
        field=field,
    )
    try:
        compile_yaml_expr_to_sexpr(expr, field_path=f"{path.as_posix()}::{case_id}.{field}")
    except SpecLangYamlAstError as exc:
        _append_issue(
            issues,
            path=path,
            case_id=case_id,
            field=field,
            code="SLINT005",
            message=str(exc),
        )


def _lint_assert_node(
    node: Any,
    *,
    issues: list[SpecLangLintIssue],
    path: Path,
    case_id: str,
    field: str,
) -> None:
    if isinstance(node, list):
        for idx, child in enumerate(node):
            _lint_assert_node(
                child,
                issues=issues,
                path=path,
                case_id=case_id,
                field=f"{field}[{idx}]",
            )
        return
    if not isinstance(node, dict):
        _append_issue(
            issues,
            path=path,
            case_id=case_id,
            field=field,
            code="SLINT006",
            message="assert node must be a mapping or list",
        )
        return

    step_class = str(node.get("class", "")).strip() if "class" in node else ""
    if step_class in _GROUP_KEYS and "asserts" in node:
        asserts = node.get("asserts")
        if not isinstance(asserts, list) or not asserts:
            _append_issue(
                issues,
                path=path,
                case_id=case_id,
                field=f"{field}.asserts",
                code="SLINT007",
                message="contract step asserts must be a non-empty list",
            )
            return
        for idx, child in enumerate(asserts):
            _lint_assert_node(
                child,
                issues=issues,
                path=path,
                case_id=case_id,
                field=f"{field}.asserts[{idx}]",
            )
        return

    present = [k for k in _GROUP_KEYS if k in node]
    legacy_present = [k for k in _LEGACY_GROUP_KEYS if k in node]
    if present or legacy_present:
        for bad in legacy_present:
            _append_issue(
                issues,
                path=path,
                case_id=case_id,
                field=f"{field}.{bad}",
                code="SLINT008",
                message="legacy lowercase group key is forbidden; use MUST/MAY/MUST_NOT",
            )
        if len(present) + len(legacy_present) > 1:
            _append_issue(
                issues,
                path=path,
                case_id=case_id,
                field=field,
                code="SLINT009",
                message="assert group must include exactly one group key",
            )
        for key in present + legacy_present:
            children = node.get(key)
            if not isinstance(children, list) or not children:
                _append_issue(
                    issues,
                    path=path,
                    case_id=case_id,
                    field=f"{field}.{key}",
                    code="SLINT010",
                    message="group value must be a non-empty list",
                )
                continue
            for idx, child in enumerate(children):
                _lint_assert_node(
                    child,
                    issues=issues,
                    path=path,
                    case_id=case_id,
                    field=f"{field}.{key}[{idx}]",
                )
        return

    _lint_expression_mapping(expr=node, issues=issues, path=path, case_id=case_id, field=field)


def _lint_when(case: dict[str, Any], *, issues: list[SpecLangLintIssue], path: Path, case_id: str) -> None:
    raw_when = case.get("when")
    if raw_when is None:
        return
    if not isinstance(raw_when, dict):
        _append_issue(
            issues,
            path=path,
            case_id=case_id,
            field="when",
            code="SLINT011",
            message="when must be a mapping",
        )
        return
    for raw_key, expr_list in raw_when.items():
        key = str(raw_key)
        if key not in _WHEN_KEYS:
            _append_issue(
                issues,
                path=path,
                case_id=case_id,
                field=f"when.{key}",
                code="SLINT012",
                message="unknown when hook key",
            )
            continue
        if not isinstance(expr_list, list) or not expr_list:
            _append_issue(
                issues,
                path=path,
                case_id=case_id,
                field=f"when.{key}",
                code="SLINT013",
                message="when hook value must be a non-empty list",
            )
            continue
        for idx, expr in enumerate(expr_list):
            _lint_expression_mapping(
                expr,
                issues=issues,
                path=path,
                case_id=case_id,
                field=f"when.{key}[{idx}]",
            )


def _lint_defines(case: dict[str, Any], *, issues: list[SpecLangLintIssue], path: Path, case_id: str) -> None:
    defines = case.get("defines")
    if defines is None:
        return
    if not isinstance(defines, dict):
        _append_issue(
            issues,
            path=path,
            case_id=case_id,
            field="defines",
            code="SLINT014",
            message="defines must be a mapping",
        )
        return
    for scope_name in ("public", "private"):
        scope = defines.get(scope_name)
        if scope is None:
            continue
        if not isinstance(scope, dict):
            _append_issue(
                issues,
                path=path,
                case_id=case_id,
                field=f"defines.{scope_name}",
                code="SLINT015",
                message="defines scope must be a mapping",
            )
            continue
        for raw_symbol, expr in scope.items():
            symbol = str(raw_symbol).strip()
            if not symbol:
                _append_issue(
                    issues,
                    path=path,
                    case_id=case_id,
                    field=f"defines.{scope_name}",
                    code="SLINT016",
                    message="defines symbol name must be non-empty",
                )
                continue
            _lint_expression_mapping(
                expr,
                issues=issues,
                path=path,
                case_id=case_id,
                field=f"defines.{scope_name}.{symbol}",
            )


def lint_cases(
    cases_path: Path,
    *,
    case_file_pattern: str,
    case_formats: set[str],
) -> list[SpecLangLintIssue]:
    issues: list[SpecLangLintIssue] = []
    for path, case in load_external_cases(
        cases_path,
        formats=case_formats,
        md_pattern=case_file_pattern,
    ):
        case_id = str(case.get("id", "<unknown>")).strip() or "<unknown>"
        contract = case.get("contract", [])
        _lint_assert_node(
            contract,
            issues=issues,
            path=path,
            case_id=case_id,
            field="contract",
        )
        _lint_when(case, issues=issues, path=path, case_id=case_id)
        _lint_defines(case, issues=issues, path=path, case_id=case_id)
    return issues


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="Lint spec-lang assertion expressions and hooks in executable contract-spec cases.",
    )
    ap.add_argument(
        "--cases",
        default="docs/spec",
        help="Path to case docs directory or case file",
    )
    ap.add_argument(
        "--case-file-pattern",
        default=SETTINGS.case.default_file_pattern,
        help="Glob pattern for markdown case files when --cases points to a directory",
    )
    ap.add_argument(
        "--case-formats",
        default="md",
        help="Comma-separated case formats to load (md,yaml,json). Default: md",
    )
    ns = ap.parse_args(argv)

    case_pattern = str(ns.case_file_pattern).strip()
    if not case_pattern:
        print("ERROR: --case-file-pattern requires a non-empty value")
        return 2

    case_formats = {x.strip() for x in str(ns.case_formats).split(",") if x.strip()}
    if not case_formats:
        print("ERROR: --case-formats requires at least one format")
        return 2

    cases_path = Path(str(ns.cases))
    if not cases_path.exists():
        print(f"ERROR: cases path does not exist: {cases_path}")
        return 2

    issues = lint_cases(
        cases_path,
        case_file_pattern=case_pattern,
        case_formats=case_formats,
    )
    if issues:
        for issue in issues:
            print(issue.render())
        print(f"FAIL: spec-lang lint found {len(issues)} issue(s)")
        return 1

    print("OK: spec-lang lint passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
