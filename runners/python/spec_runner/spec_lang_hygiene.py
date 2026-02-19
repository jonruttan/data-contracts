from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from spec_runner.codecs import load_external_cases
from spec_runner.spec_lang_yaml_ast import SpecLangYamlAstError, compile_yaml_expr_to_sexpr

_GROUP_KEYS = {"MUST", "MAY", "MUST_NOT"}
_LEGACY_GROUP_KEYS = {"must", "can", "cannot"}
_WHEN_KEYS = {"must", "may", "must_not", "fail", "complete"}


@dataclass(frozen=True)
class SpecLangIssue:
    path: Path
    case_id: str
    field: str
    code: str
    message: str
    severity: str = "error"
    fixable: bool = False

    def render(self) -> str:
        return (
            f"{self.path.as_posix()}: case {self.case_id}: {self.code}: "
            f"{self.field}: {self.message}"
        )


class _FlowSeq(list):
    pass


class _FlowMap(dict):
    pass


class _CompactDumper(yaml.SafeDumper):
    pass


def _flow_seq_representer(dumper: yaml.Dumper, data: _FlowSeq) -> yaml.nodes.SequenceNode:
    return dumper.represent_sequence("tag:yaml.org,2002:seq", list(data), flow_style=True)


def _flow_map_representer(dumper: yaml.Dumper, data: _FlowMap) -> yaml.nodes.MappingNode:
    return dumper.represent_mapping("tag:yaml.org,2002:map", dict(data), flow_style=True)


_CompactDumper.add_representer(_FlowSeq, _flow_seq_representer)
_CompactDumper.add_representer(_FlowMap, _flow_map_representer)


def iter_case_files(paths: list[Path], *, pattern: str) -> list[Path]:
    out: list[Path] = []
    for p in paths:
        if p.is_file():
            if p.match(pattern):
                out.append(p)
            continue
        if not p.exists():
            continue
        out.extend(sorted(x for x in p.rglob(pattern) if x.is_file()))
    seen: set[Path] = set()
    uniq: list[Path] = []
    for p in out:
        rp = p.resolve()
        if rp in seen:
            continue
        seen.add(rp)
        uniq.append(p)
    return uniq


def _is_yaml_opening_fence(line: str) -> tuple[str, int] | None:
    stripped = line.lstrip(" \t")
    if not stripped:
        return None
    if stripped[0] not in ("`", "~"):
        return None
    ch = stripped[0]
    i = 0
    while i < len(stripped) and stripped[i] == ch:
        i += 1
    if i < 3:
        return None
    info = stripped[i:].strip().lower().split()
    if "yaml" not in info and "yml" not in info:
        return None
    if "contract-spec" not in info:
        return None
    return ch, i


def _is_closing_fence(line: str, *, ch: str, min_len: int) -> bool:
    stripped = line.lstrip(" \t").rstrip()
    if not stripped or stripped[0] != ch:
        return False
    i = 0
    while i < len(stripped) and stripped[i] == ch:
        i += 1
    return i >= min_len and i == len(stripped)


def _is_scalar(node: Any) -> bool:
    return isinstance(node, (str, int, float, bool)) or node is None


def _normalize_literal(value: Any) -> Any:
    if isinstance(value, dict):
        return {str(k): _normalize_literal(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_normalize_literal(v) for v in value]
    return value


def _is_operatorish_key(key: str) -> bool:
    s = str(key).strip()
    if not s:
        return False
    if s in {"var", "fn", "lit"}:
        return True
    return (
        "." in s
        or s.startswith("std.")
        or s.startswith("ops.")
        or s.startswith("core.")
        or s.startswith("json.")
    )


def _normalize_expr_node(node: Any) -> tuple[Any, bool]:
    changed = False
    if _is_scalar(node):
        return node, changed

    if isinstance(node, list):
        list_out: list[Any] = []
        for item in node:
            norm, ch = _normalize_expr_node(item)
            changed = changed or ch
            list_out.append(norm)
        return list_out, changed

    if not isinstance(node, dict):
        return node, changed

    if set(node.keys()) == {"evaluate"}:
        raw = node.get("evaluate")
        if isinstance(raw, dict):
            lifted, ch = _normalize_expr_node(raw)
            return lifted, True or ch
        if isinstance(raw, list) and len(raw) == 1 and isinstance(raw[0], dict):
            lifted, ch = _normalize_expr_node(raw[0])
            return lifted, True or ch

    if set(node.keys()) == {"lit"}:
        lit_value = node.get("lit")
        while isinstance(lit_value, dict) and set(lit_value.keys()) == {"lit"}:
            lit_value = lit_value.get("lit")
            changed = True
        lit_value = _normalize_literal(lit_value)
        if isinstance(lit_value, dict) and len(lit_value) == 1:
            raw_key = next(iter(lit_value.keys()))
            if _is_operatorish_key(str(raw_key)):
                lifted, ch = _normalize_expr_node(lit_value)
                return lifted, True or changed or ch
        if _is_scalar(lit_value):
            return _FlowMap({"lit": lit_value}), True or changed
        return {"lit": lit_value}, changed

    if len(node) == 1:
        op = str(next(iter(node.keys())))
        raw_args = node[op]
        if op == "var" and isinstance(raw_args, str):
            return _FlowMap({"var": raw_args.strip() or raw_args}), True
        if op == "fn" and isinstance(raw_args, list) and len(raw_args) == 2:
            params = raw_args[0]
            body = raw_args[1]
            if isinstance(params, dict) and set(params.keys()) == {"lit"} and isinstance(params.get("lit"), list):
                params = params.get("lit")
                changed = True
            norm_body, body_changed = _normalize_expr_node(body)
            changed = changed or body_changed
            if isinstance(params, list) and all(isinstance(x, str) and x.strip() for x in params):
                return {"fn": [_FlowSeq([str(x).strip() for x in params]), norm_body]}, True or changed
            norm_params, params_changed = _normalize_expr_node(params)
            changed = changed or params_changed
            return {"fn": [norm_params, norm_body]}, changed
        if isinstance(raw_args, list):
            args_out: list[Any] = []
            for arg in raw_args:
                norm_arg, ch = _normalize_expr_node(arg)
                changed = changed or ch
                args_out.append(norm_arg)
            return {op: args_out}, changed

    map_out: dict[str, Any] = {}
    for k, v in node.items():
        norm, ch = _normalize_expr_node(v)
        changed = changed or ch
        map_out[str(k)] = norm
    return map_out, changed


def _normalize_assert_node(node: Any) -> tuple[Any, bool]:
    changed = False
    if isinstance(node, list):
        list_out: list[Any] = []
        for child in node:
            norm, ch = _normalize_assert_node(child)
            changed = changed or ch
            list_out.append(norm)
        return list_out, changed
    if not isinstance(node, dict):
        return node, changed

    step_class = str(node.get("class", "")).strip() if "class" in node else ""
    if step_class in _GROUP_KEYS and "asserts" in node:
        step_out = dict(node)
        asserts = node.get("asserts")
        if isinstance(asserts, list):
            norm_asserts: list[Any] = []
            for child in asserts:
                norm, ch = _normalize_assert_node(child)
                changed = changed or ch
                if (
                    isinstance(norm, dict)
                    and set(norm.keys()) == {step_class}
                    and isinstance(norm.get(step_class), list)
                ):
                    changed = True
                    norm_asserts.extend(list(norm.get(step_class) or []))
                else:
                    norm_asserts.append(norm)
            step_out["asserts"] = norm_asserts
        return step_out, changed

    present = [k for k in _GROUP_KEYS if k in node]
    if present:
        group_out = dict(node)
        for key in present:
            raw_group_children = node.get(key)
            if not isinstance(raw_group_children, list):
                continue
            norm_children: list[Any] = []
            for child in raw_group_children:
                norm, ch = _normalize_assert_node(child)
                changed = changed or ch
                norm_children.append(norm)
            group_out[key] = norm_children
        return group_out, changed

    norm_expr, expr_changed = _normalize_expr_node(node)
    changed = changed or expr_changed
    if isinstance(norm_expr, dict) and set(norm_expr.keys()) == {"lit"}:
        inner = norm_expr.get("lit")
        if isinstance(inner, dict):
            mapped_key: str | None = None
            raw_lit_group_children: Any = None
            if "MUST" in inner:
                mapped_key = "MUST"
                raw_lit_group_children = inner.get("MUST")
            elif "MAY" in inner:
                mapped_key = "MAY"
                raw_lit_group_children = inner.get("MAY")
            elif "MUST_NOT" in inner:
                mapped_key = "MUST_NOT"
                raw_lit_group_children = inner.get("MUST_NOT")
            elif "must" in inner:
                mapped_key = "MUST"
                raw_lit_group_children = inner.get("must")
            elif "can" in inner:
                mapped_key = "MAY"
                raw_lit_group_children = inner.get("can")
            elif "cannot" in inner:
                mapped_key = "MUST_NOT"
                raw_lit_group_children = inner.get("cannot")
            if mapped_key and isinstance(raw_lit_group_children, list):
                normalized_children: list[Any] = []
                for child in raw_lit_group_children:
                    cnode, ch = _normalize_assert_node(child)
                    changed = changed or ch
                    normalized_children.append(cnode)
                return {mapped_key: normalized_children}, True
    return norm_expr, changed


def _normalize_contract(node: Any) -> tuple[Any, bool]:
    changed = False
    if isinstance(node, dict):
        defaults_raw = node.get("defaults")
        defaults: dict[str, Any] = dict(defaults_raw) if isinstance(defaults_raw, dict) else {}
        raw_steps = node.get("steps")
        if raw_steps is None:
            raw_steps = []
        if not isinstance(raw_steps, list):
            return node, changed
        normalized_steps: list[dict[str, Any]] = []
        for idx, raw_step in enumerate(raw_steps):
            if not isinstance(raw_step, dict):
                normalized_steps.append({"id": f"step_{idx+1:03d}", "assert": raw_step})
                changed = True
                continue
            step = dict(raw_step)
            if "asserts" in step and "assert" not in step:
                step["assert"] = step.pop("asserts")
                changed = True
            if "target" in step and "on" not in step:
                step["on"] = step.pop("target")
                changed = True
            raw_assert = step.get("assert")
            if isinstance(raw_assert, list):
                norm_asserts: list[Any] = []
                for child in raw_assert:
                    norm, ch = _normalize_assert_node(child)
                    changed = changed or ch
                    norm_asserts.append(norm)
                if len(norm_asserts) == 1:
                    step["assert"] = norm_asserts[0]
                    changed = True
                else:
                    step["assert"] = norm_asserts
            elif raw_assert is not None:
                norm, ch = _normalize_assert_node(raw_assert)
                changed = changed or ch
                step["assert"] = norm
            if "id" not in step or not str(step.get("id", "")).strip():
                step["id"] = f"step_{idx+1:03d}"
                changed = True
            step_class = str(step.get("class", "MUST")).strip() or "MUST"
            if step_class == "MUST" and "class" in step:
                step.pop("class", None)
                changed = True
            normalized_steps.append(step)

        if "class" not in defaults:
            defaults["class"] = "MUST"
        out: dict[str, Any] = {"defaults": defaults, "steps": normalized_steps}
        return out, True or changed

    if isinstance(node, list):
        # Legacy step-list migration shape.
        steps: list[dict[str, Any]] = []
        for idx, raw_step in enumerate(node):
            if not isinstance(raw_step, dict):
                steps.append({"id": f"step_{idx+1:03d}", "assert": raw_step})
                changed = True
                continue
            step = dict(raw_step)
            if "asserts" in step and "assert" not in step:
                step["assert"] = step.pop("asserts")
                changed = True
            if "target" in step and "on" not in step:
                step["on"] = step.pop("target")
                changed = True
            step_id = str(step.get("id", "")).strip() or f"step_{idx+1:03d}"
            step_class = str(step.get("class", "MUST")).strip() or "MUST"
            out_step: dict[str, Any] = {"id": step_id}
            if step_class != "MUST":
                out_step["class"] = step_class
            if "on" in step:
                out_step["on"] = step.get("on")
            raw_assert = step.get("assert")
            if isinstance(raw_assert, list):
                norm_asserts_v1: list[Any] = []
                for child in raw_assert:
                    norm, ch = _normalize_assert_node(child)
                    changed = changed or ch
                    norm_asserts_v1.append(norm)
                out_step["assert"] = (
                    norm_asserts_v1[0] if len(norm_asserts_v1) == 1 else norm_asserts_v1
                )
            else:
                norm, ch = _normalize_assert_node(raw_assert)
                changed = changed or ch
                out_step["assert"] = norm
            steps.append(out_step)
        return {"defaults": {"class": "MUST"}, "steps": steps}, True or changed
    return node, changed


def _normalize_case(case: dict[str, Any]) -> tuple[dict[str, Any], bool]:
    out = dict(case)
    changed = False

    if "contract" in out:
        norm_contract, ch = _normalize_contract(out.get("contract"))
        out["contract"] = norm_contract
        changed = changed or ch

    when = out.get("when")
    if isinstance(when, dict):
        when_out: dict[str, Any] = {}
        for raw_key, raw_list in when.items():
            key = str(raw_key)
            if isinstance(raw_list, list):
                exprs: list[Any] = []
                for expr in raw_list:
                    norm, ch = _normalize_expr_node(expr)
                    changed = changed or ch
                    exprs.append(norm)
                when_out[key] = exprs
            else:
                when_out[key] = raw_list
        out["when"] = when_out

    defines = out.get("defines")
    if isinstance(defines, dict):
        def_out: dict[str, Any] = {}
        for scope, raw_map in defines.items():
            skey = str(scope)
            if isinstance(raw_map, dict):
                scope_out: dict[str, Any] = {}
                for raw_symbol, expr in raw_map.items():
                    sym = str(raw_symbol)
                    norm, ch = _normalize_expr_node(expr)
                    changed = changed or ch
                    scope_out[sym] = norm
                def_out[skey] = scope_out
            else:
                def_out[skey] = raw_map
        out["defines"] = def_out

    return out, changed


def normalize_case_payload(payload: Any) -> tuple[Any, bool]:
    if isinstance(payload, dict):
        return _normalize_case(payload)
    if isinstance(payload, list):
        changed = False
        out: list[Any] = []
        for item in payload:
            if isinstance(item, dict):
                norm, ch = _normalize_case(item)
                changed = changed or ch
                out.append(norm)
            else:
                out.append(item)
        return out, changed
    return payload, False


def _yaml_dump(payload: Any) -> str:
    return yaml.dump(payload, sort_keys=False, allow_unicode=False, width=88, Dumper=_CompactDumper)


def format_spec_markdown(text: str) -> str:
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    i = 0
    while i < len(lines):
        opening = _is_yaml_opening_fence(lines[i])
        if not opening:
            out.append(lines[i])
            i += 1
            continue
        ch, fence_len = opening
        out.append(lines[i])
        i += 1
        block_lines: list[str] = []
        while i < len(lines) and not _is_closing_fence(lines[i], ch=ch, min_len=fence_len):
            block_lines.append(lines[i])
            i += 1

        if i >= len(lines):
            out.extend(block_lines)
            break

        block = "".join(block_lines)
        try:
            payload = yaml.safe_load(block)
            if payload is None:
                formatted = block.strip() + "\n"
            else:
                norm, _changed = normalize_case_payload(payload)
                formatted = _yaml_dump(norm)
        except yaml.YAMLError:
            formatted = block

        out.append(formatted)
        out.append(lines[i])
        i += 1

    return "".join(out)


def format_file(path: Path) -> tuple[str, bool]:
    original = path.read_text(encoding="utf-8")
    updated = format_spec_markdown(original)
    return updated, updated != original


def _append_issue(
    issues: list[SpecLangIssue],
    *,
    path: Path,
    case_id: str,
    field: str,
    code: str,
    message: str,
    fixable: bool = False,
) -> None:
    issues.append(
        SpecLangIssue(
            path=path,
            case_id=case_id,
            field=field,
            code=code,
            message=message,
            severity="error",
            fixable=fixable,
        )
    )


def _lint_direct_nested_lit(
    expr: Any,
    *,
    issues: list[SpecLangIssue],
    path: Path,
    case_id: str,
    field: str,
) -> None:
    if not isinstance(expr, dict):
        return

    depth = 0
    cur: Any = expr
    while isinstance(cur, dict) and set(cur.keys()) == {"lit"}:
        lit_value = cur.get("lit")
        depth += 1
        if depth >= 2:
            _append_issue(
                issues,
                path=path,
                case_id=case_id,
                field=field,
                code="SLINT002",
                message="nested lit wrapper is forbidden",
                fixable=True,
            )
            break
        if isinstance(lit_value, dict) and len(lit_value) == 1:
            raw_key = next(iter(lit_value.keys()))
            if _is_operatorish_key(str(raw_key)):
                _append_issue(
                    issues,
                    path=path,
                    case_id=case_id,
                    field=field,
                    code="SLINT017",
                    message="operator-shaped lit wrapper is forbidden; use direct operator mapping",
                    fixable=True,
                )
        cur = lit_value


def _lint_expression_mapping(
    expr: Any,
    *,
    issues: list[SpecLangIssue],
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
            message="evaluate wrapper is forbidden; place operator mapping directly in assert",
            fixable=True,
        )
    for key in expr.keys():
        skey = str(key)
        if skey in _GROUP_KEYS or skey in _LEGACY_GROUP_KEYS:
            _append_issue(
                issues,
                path=path,
                case_id=case_id,
                field=f"{field}.{skey}",
                code="SLINT003",
                message="assertion group key is not a valid spec-lang operator in expression context",
            )

    _lint_direct_nested_lit(
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
    issues: list[SpecLangIssue],
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
            if isinstance(child, dict):
                nested_groups = [k for k in _GROUP_KEYS if k in child]
                if nested_groups:
                    only_same_class = (
                        set(child.keys()) == {step_class}
                        and isinstance(child.get(step_class), list)
                    )
                    if only_same_class:
                        _append_issue(
                            issues,
                            path=path,
                            case_id=case_id,
                            field=f"{field}.asserts[{idx}]",
                            code="SLINT018",
                            message="redundant nested group matches step class; flatten into asserts entries",
                            fixable=True,
                        )
                    else:
                        _append_issue(
                            issues,
                            path=path,
                            case_id=case_id,
                            field=f"{field}.asserts[{idx}]",
                            code="SLINT019",
                            message="nested assert groups are forbidden inside step asserts; use step class semantics",
                        )
            if (
                isinstance(child, dict)
                and set(child.keys()) == {step_class}
                and isinstance(child.get(step_class), list)
            ):
                _append_issue(
                    issues,
                    path=path,
                    case_id=case_id,
                    field=f"{field}.asserts[{idx}]",
                    code="SLINT018",
                    message="redundant nested group matches step class; flatten into asserts entries",
                    fixable=True,
                )
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


def _lint_when(case: dict[str, Any], *, issues: list[SpecLangIssue], path: Path, case_id: str) -> None:
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


def _lint_defines(case: dict[str, Any], *, issues: list[SpecLangIssue], path: Path, case_id: str) -> None:
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


def _lint_contract(case: dict[str, Any], *, issues: list[SpecLangIssue], path: Path, case_id: str) -> None:
    contract = case.get("contract")
    if contract is None:
        _append_issue(
            issues,
            path=path,
            case_id=case_id,
            field="contract",
            code="SLINT020",
            message="contract is required and must use mapping form",
        )
        return
    if isinstance(contract, list):
        _append_issue(
            issues,
            path=path,
            case_id=case_id,
            field="contract",
            code="SLINT021",
            message="v1 list contract is forbidden; use contract.defaults + contract.steps",
            fixable=True,
        )
        return
    if not isinstance(contract, dict):
        _append_issue(
            issues,
            path=path,
            case_id=case_id,
            field="contract",
            code="SLINT022",
            message="contract must be a mapping with defaults and steps",
        )
        return
    defaults = contract.get("defaults")
    if defaults is not None and not isinstance(defaults, dict):
        _append_issue(
            issues,
            path=path,
            case_id=case_id,
            field="contract.defaults",
            code="SLINT023",
            message="contract.defaults must be a mapping when provided",
        )
    steps = contract.get("steps")
    if not isinstance(steps, list):
        _append_issue(
            issues,
            path=path,
            case_id=case_id,
            field="contract.steps",
            code="SLINT024",
            message="contract.steps must be a list",
        )
        return
    for idx, step in enumerate(steps):
        if not isinstance(step, dict):
            _append_issue(
                issues,
                path=path,
                case_id=case_id,
                field=f"contract.steps[{idx}]",
                code="SLINT025",
                message="contract step must be a mapping",
            )
            continue
        if "asserts" in step:
            _append_issue(
                issues,
                path=path,
                case_id=case_id,
                field=f"contract.steps[{idx}].asserts",
                code="SLINT026",
                message="v1 step key asserts is forbidden; use assert",
                fixable=True,
            )
        if "target" in step:
            _append_issue(
                issues,
                path=path,
                case_id=case_id,
                field=f"contract.steps[{idx}].target",
                code="SLINT027",
                message="v1 step key target is forbidden; use on",
                fixable=True,
            )
        class_name = str(step.get("class", "MUST")).strip() or "MUST"
        if class_name not in _GROUP_KEYS:
            _append_issue(
                issues,
                path=path,
                case_id=case_id,
                field=f"contract.steps[{idx}].class",
                code="SLINT028",
                message="contract step class must be MUST, MAY, or MUST_NOT",
            )
        raw_assert = step.get("assert")
        if raw_assert is None:
            _append_issue(
                issues,
                path=path,
                case_id=case_id,
                field=f"contract.steps[{idx}].assert",
                code="SLINT029",
                message="contract step assert is required",
            )
            continue
        if isinstance(raw_assert, list):
            if not raw_assert:
                _append_issue(
                    issues,
                    path=path,
                    case_id=case_id,
                    field=f"contract.steps[{idx}].assert",
                    code="SLINT030",
                    message="contract step assert list must be non-empty",
                )
                continue
            for aidx, expr in enumerate(raw_assert):
                _lint_assert_node(
                    expr,
                    issues=issues,
                    path=path,
                    case_id=case_id,
                    field=f"contract.steps[{idx}].assert[{aidx}]",
                )
        else:
            _lint_assert_node(
                raw_assert,
                issues=issues,
                path=path,
                case_id=case_id,
                field=f"contract.steps[{idx}].assert",
            )


def lint_cases(
    cases_path: Path,
    *,
    case_file_pattern: str,
    case_formats: set[str],
) -> list[SpecLangIssue]:
    issues: list[SpecLangIssue] = []
    for path, case in load_external_cases(
        cases_path,
        formats=case_formats,
        md_pattern=case_file_pattern,
    ):
        case_id = str(case.get("id", "<unknown>")).strip() or "<unknown>"
        _lint_contract(case, issues=issues, path=path, case_id=case_id)
        harness = case.get("harness")
        if isinstance(harness, dict):
            if "chain" in harness:
                _append_issue(
                    issues,
                    path=path,
                    case_id=case_id,
                    field="harness.chain",
                    code="SLINT031",
                    message="harness.chain is forbidden; use harness.use",
                    fixable=True,
                )
            raw_use = harness.get("use")
            if raw_use is not None and (not isinstance(raw_use, list) or not raw_use):
                _append_issue(
                    issues,
                    path=path,
                    case_id=case_id,
                    field="harness.use",
                    code="SLINT032",
                    message="harness.use must be a non-empty list when provided",
                )
        _lint_when(case, issues=issues, path=path, case_id=case_id)
        _lint_defines(case, issues=issues, path=path, case_id=case_id)

    return sorted(issues, key=lambda i: (i.path.as_posix(), i.case_id, i.field, i.code))
