from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Mapping

from spec_runner.codecs import load_external_cases
from spec_runner.compiler import compile_external_case
from spec_runner.internal_model import InternalSpecCase
from spec_runner.virtual_paths import contract_root_for, parse_external_ref, resolve_contract_path

_DOTTED_PATH_PART = re.compile(r"^[A-Za-z0-9_.-]+$")
_CASE_ID_PART = re.compile(r"^[A-Za-z0-9._:-]+$")


@dataclass(frozen=True)
class ChainRef:
    raw: str
    path: str | None
    case_id: str | None


@dataclass(frozen=True)
class ChainExport:
    from_target: str
    path: str | None
    required: bool


@dataclass(frozen=True)
class ChainStep:
    id: str
    ref: ChainRef
    exports: dict[str, ChainExport]
    allow_continue: bool


def parse_spec_ref(raw_ref: str) -> ChainRef:
    raw = str(raw_ref).strip()
    if not raw:
        raise ValueError("harness.chain.steps[*].ref must be a non-empty string")
    if "#" in raw:
        path_part, case_part = raw.split("#", 1)
        path = path_part.strip() or None
        case_id = case_part.strip()
        if not case_id:
            raise ValueError("harness.chain.steps[*].ref fragment case_id must be non-empty when '#' is present")
        if not _CASE_ID_PART.match(case_id):
            raise ValueError(
                "harness.chain.steps[*].ref fragment case_id must match [A-Za-z0-9._:-]+"
            )
        if path is not None and parse_external_ref(path) is not None:
            raise ValueError("harness.chain.steps[*].ref path must not be external://")
        return ChainRef(raw=raw, path=path, case_id=case_id)
    if parse_external_ref(raw) is not None:
        raise ValueError("harness.chain.steps[*].ref path must not be external://")
    return ChainRef(raw=raw, path=raw, case_id=None)


def _resolve_dotted_path(value: Any, dotted: str) -> tuple[bool, Any]:
    current = value
    if not dotted:
        return True, current
    if not _DOTTED_PATH_PART.match(dotted):
        return False, None
    for part in dotted.split("."):
        if isinstance(current, dict):
            if part not in current:
                return False, None
            current = current[part]
            continue
        if isinstance(current, list):
            try:
                idx = int(part)
            except ValueError:
                return False, None
            if idx < 0 or idx >= len(current):
                return False, None
            current = current[idx]
            continue
        return False, None
    return True, current


def compile_chain_plan(case: InternalSpecCase) -> list[ChainStep]:
    harness = case.harness or {}
    raw_chain = harness.get("chain")
    if raw_chain is None:
        return []
    if not isinstance(raw_chain, dict):
        raise TypeError("harness.chain must be a mapping")
    raw_steps = raw_chain.get("steps")
    if not isinstance(raw_steps, list) or not raw_steps:
        raise ValueError("harness.chain.steps must be a non-empty list")
    seen_ids: set[str] = set()
    steps: list[ChainStep] = []
    for idx, raw in enumerate(raw_steps):
        if not isinstance(raw, dict):
            raise TypeError(f"harness.chain.steps[{idx}] must be a mapping")
        step_id = str(raw.get("id", "")).strip()
        if not step_id:
            raise ValueError(f"harness.chain.steps[{idx}].id must be a non-empty string")
        if step_id in seen_ids:
            raise ValueError(f"harness.chain.steps has duplicate id: {step_id}")
        seen_ids.add(step_id)
        raw_ref = raw.get("ref")
        if isinstance(raw_ref, dict):
            raise TypeError(
                f"harness.chain.steps[{idx}].ref legacy mapping format is not supported; use string [path][#case_id]"
            )
        if not isinstance(raw_ref, str):
            raise TypeError(f"harness.chain.steps[{idx}].ref must be a string")
        parsed_ref = parse_spec_ref(raw_ref)
        raw_exports = raw.get("exports") or {}
        if not isinstance(raw_exports, dict):
            raise TypeError(f"harness.chain.steps[{idx}].exports must be a mapping when provided")
        if raw_exports and not parsed_ref.case_id:
            raise ValueError(f"harness.chain.steps[{idx}] exports require ref with #case_id fragment")
        exports: dict[str, ChainExport] = {}
        for export_name, export_raw in raw_exports.items():
            name = str(export_name).strip()
            if not name:
                raise ValueError(f"harness.chain.steps[{idx}].exports contains empty export key")
            if not isinstance(export_raw, dict):
                raise TypeError(f"harness.chain.steps[{idx}].exports.{name} must be a mapping")
            from_target = str(export_raw.get("from_target", "")).strip()
            if not from_target:
                raise ValueError(f"harness.chain.steps[{idx}].exports.{name}.from_target is required")
            export_path = export_raw.get("path")
            if export_path is not None and not isinstance(export_path, str):
                raise TypeError(f"harness.chain.steps[{idx}].exports.{name}.path must be a string when provided")
            raw_required = export_raw.get("required", True)
            if not isinstance(raw_required, bool):
                raise TypeError(f"harness.chain.steps[{idx}].exports.{name}.required must be a bool when provided")
            exports[name] = ChainExport(
                from_target=from_target,
                path=None if export_path is None else str(export_path),
                required=raw_required,
            )
        raw_allow_continue = raw.get("allow_continue", False)
        if not isinstance(raw_allow_continue, bool):
            raise TypeError(f"harness.chain.steps[{idx}].allow_continue must be a bool when provided")
        steps.append(
            ChainStep(
                id=step_id,
                ref=parsed_ref,
                exports=exports,
                allow_continue=raw_allow_continue,
            )
        )
    return steps


def _resolve_ref_path(*, ref_path: str, current_case: InternalSpecCase) -> Path:
    root = contract_root_for(current_case.doc_path)
    if ref_path.startswith("/"):
        return resolve_contract_path(root, ref_path, field="harness.chain.steps.ref")
    doc_parent = current_case.doc_path.resolve().parent
    resolved = (doc_parent / ref_path).resolve()
    try:
        resolved.relative_to(root)
    except ValueError as exc:
        raise ValueError("harness.chain.steps.ref escapes contract root") from exc
    return resolved


def resolve_chain_reference(step: ChainStep, *, current_case: InternalSpecCase) -> list[InternalSpecCase]:
    if step.ref.path:
        resolved = _resolve_ref_path(ref_path=step.ref.path, current_case=current_case)
        if not resolved.exists() or not resolved.is_file():
            raise ValueError(f"chain ref path does not exist as file: {step.ref.path}")
        docs = list(load_external_cases(resolved, formats={"md"}))
        if step.ref.case_id:
            filtered = [x for x in docs if str(x[1].get("id", "")).strip() == step.ref.case_id]
            if not filtered:
                raise ValueError(
                    f"chain step {step.id} could not resolve case_id {step.ref.case_id} in {step.ref.path}"
                )
            if len(filtered) > 1:
                raise ValueError(
                    f"chain step {step.id} resolved duplicate case_id {step.ref.case_id} in {step.ref.path}"
                )
            return [compile_external_case(filtered[0][1], doc_path=filtered[0][0])]
        return [compile_external_case(test, doc_path=doc_path) for doc_path, test in docs]

    assert step.ref.case_id is not None
    docs = list(load_external_cases(current_case.doc_path, formats={"md"}))
    filtered = [x for x in docs if str(x[1].get("id", "")).strip() == step.ref.case_id]
    if not filtered:
        raise ValueError(f"chain step {step.id} could not resolve local case_id {step.ref.case_id}")
    if len(filtered) > 1:
        raise ValueError(f"chain step {step.id} resolved duplicate local case_id {step.ref.case_id}")
    return [compile_external_case(filtered[0][1], doc_path=filtered[0][0])]


def extract_exports(*, step: ChainStep, executed_case: InternalSpecCase, target_values: Mapping[str, Any]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for export_name, export in step.exports.items():
        if export.from_target not in target_values:
            if export.required:
                raise ValueError(
                    f"chain step {step.id} export {export_name} missing from_target {export.from_target} on case {executed_case.id}"
                )
            continue
        raw = target_values[export.from_target]
        if export.path:
            ok, value = _resolve_dotted_path(raw, export.path)
            if not ok:
                if export.required:
                    raise ValueError(
                        f"chain step {step.id} export {export_name} could not resolve path {export.path} from target {export.from_target}"
                    )
                continue
            out[export_name] = value
            continue
        out[export_name] = raw
    return out


def execute_chain_plan(
    case: InternalSpecCase,
    *,
    ctx,
    run_case_fn: Callable[[InternalSpecCase], None],
) -> None:
    steps = compile_chain_plan(case)
    if not steps:
        return
    raw_fail_fast = ((case.harness or {}).get("chain") or {}).get("fail_fast", True)
    if not isinstance(raw_fail_fast, bool):
        raise TypeError("harness.chain.fail_fast must be a bool when provided")
    fail_fast = raw_fail_fast
    for step in steps:
        refs = resolve_chain_reference(step, current_case=case)
        step_exports: dict[str, Any] = {}
        for ref_case in refs:
            ref_key = f"{ref_case.doc_path.resolve().as_posix()}::{ref_case.id}"
            cur_key = f"{case.doc_path.resolve().as_posix()}::{case.id}"
            if ref_key == cur_key:
                raise RuntimeError(f"chain step {step.id} references current case recursively")
            try:
                run_case_fn(ref_case)
                targets = ctx.get_case_targets(case_key=ref_key)
                if targets is None:
                    targets = {}
                if step.exports:
                    step_exports.update(extract_exports(step=step, executed_case=ref_case, target_values=targets))
                ctx.chain_trace.append(
                    {
                        "step_id": step.id,
                        "ref_case_id": ref_case.id,
                        "ref_doc_path": "/" + ref_case.doc_path.resolve().as_posix().lstrip("/"),
                        "status": "pass",
                    }
                )
            except Exception:
                ctx.chain_trace.append(
                    {
                        "step_id": step.id,
                        "ref_case_id": ref_case.id,
                        "ref_doc_path": "/" + ref_case.doc_path.resolve().as_posix().lstrip("/"),
                        "status": "fail",
                    }
                )
                if fail_fast and not step.allow_continue:
                    raise
        ctx.chain_state[step.id] = dict(step_exports)


def execute_case_chain(
    case: InternalSpecCase,
    *,
    ctx,
    run_case_fn: Callable[[InternalSpecCase], None],
) -> None:
    execute_chain_plan(case, ctx=ctx, run_case_fn=run_case_fn)
