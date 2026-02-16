from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import subprocess
from typing import Any

import yaml

from spec_runner.assertions import evaluate_internal_assert_tree
from spec_runner.compiler import compile_external_case
from spec_runner.ops_namespace import validate_registry_entry
from spec_runner.spec_lang import limits_from_harness
from spec_runner.spec_lang_libraries import load_spec_lang_symbols_for_case
from spec_runner.virtual_paths import contract_root_for


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _load_tools_registry(root: Path, impl: str) -> list[dict[str, Any]]:
    path = root / "docs/spec/tools" / impl / "tools_v1.yaml"
    if not path.exists():
        raise ValueError(f"missing tools registry for impl '{impl}': {path}")
    payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise TypeError(f"tools registry must be a mapping: {path}")
    tools = payload.get("tools")
    if not isinstance(tools, list):
        raise TypeError(f"tools registry tools must be a list: {path}")
    out: list[dict[str, Any]] = []
    for i, raw in enumerate(tools):
        if not isinstance(raw, dict):
            raise TypeError(f"tools[{i}] must be a mapping: {path}")
        diags = validate_registry_entry(raw, where=f"{path}:{i}")
        if diags:
            raise ValueError("; ".join(d.message for d in diags))
        out.append({str(k): v for k, v in raw.items()})
    return out


def _resolve_tool(tools: list[dict[str, Any]], tool_id: str) -> dict[str, Any]:
    for tool in tools:
        if str(tool.get("tool_id", "")).strip() == tool_id:
            return tool
    raise ValueError(f"unknown orchestration tool_id: {tool_id}")


def run(case, *, ctx) -> None:
    if hasattr(case, "test") and hasattr(case, "doc_path"):
        case = compile_external_case(case.test, doc_path=case.doc_path)

    case_id = case.id
    harness = case.harness
    orch = dict(harness.get("orchestration") or {})
    if not orch:
        raise ValueError("orchestration.run requires harness.orchestration mapping")

    tool_id = str(orch.get("tool_id", "")).strip()
    if not tool_id:
        raise ValueError("harness.orchestration.tool_id must be a non-empty string")

    impl = str(orch.get("impl", "")).strip() or "python"
    if impl not in {"python", "rust"}:
        raise ValueError("harness.orchestration.impl must be rust|python when provided")

    args_raw = orch.get("args")
    forwarded: list[str] = []
    if args_raw is None:
        forwarded = []
    elif isinstance(args_raw, list):
        forwarded = [str(x) for x in args_raw]
    else:
        raise TypeError("harness.orchestration.args must be a list when provided")

    capabilities_raw = orch.get("capabilities") or []
    if not isinstance(capabilities_raw, list):
        raise TypeError("harness.orchestration.capabilities must be a list when provided")
    declared_caps = {str(x).strip() for x in capabilities_raw if str(x).strip()}

    root = contract_root_for(case.doc_path)
    tools = _load_tools_registry(root, impl)
    tool = _resolve_tool(tools, tool_id)
    capability_id = str(tool.get("capability_id", "")).strip()
    if capability_id and capability_id not in declared_caps:
        raise ValueError(
            f"harness.orchestration.capabilities missing required capability for tool {tool_id}: {capability_id}"
        )

    subcommand = str(tool.get("adapter_subcommand", "")).strip()
    if not subcommand:
        raise ValueError(f"tool {tool_id} missing adapter_subcommand")

    adapter = root / "scripts/runner_adapter.sh"
    started_at = _now_iso()
    cp = subprocess.run(
        [str(adapter), "--impl", impl, subcommand, *forwarded],
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
    )
    ended_at = _now_iso()

    result_envelope: dict[str, Any] = {
        "status": "pass" if cp.returncode == 0 else "fail",
        "tool_id": tool_id,
        "impl": impl,
        "started_at_utc": started_at,
        "ended_at_utc": ended_at,
        "duration_ms": 0,
        "data": {
            "exit_code": int(cp.returncode),
            "stdout": cp.stdout,
            "stderr": cp.stderr,
        },
        "diagnostics": [],
        "artifacts": [],
    }

    context_profile = {
        "profile_id": "orchestration.run/v1",
        "profile_version": 1,
        "value": result_envelope,
        "meta": {
            "target": "orchestration.run",
            "case_id": case_id,
            "tool_id": tool_id,
            "effect_symbol": str(tool.get("effect_symbol", "")),
        },
        "context": {
            "impl": impl,
            "subcommand": subcommand,
        },
    }

    spec_lang_limits = limits_from_harness(harness)
    spec_lang_symbols = load_spec_lang_symbols_for_case(
        doc_path=case.doc_path,
        harness=harness,
        limits=spec_lang_limits,
    )

    def _subject_for_key(subject_key: str):
        if subject_key == "result_json":
            return result_envelope
        if subject_key == "stdout":
            return str(result_envelope["data"]["stdout"])
        if subject_key == "stderr":
            return str(result_envelope["data"]["stderr"])
        if subject_key == "exit_code":
            return int(result_envelope["data"]["exit_code"])
        if subject_key == "context_json":
            return context_profile
        raise ValueError(f"unknown assert target for orchestration.run: {subject_key}")

    evaluate_internal_assert_tree(
        case.assert_tree,
        case_id=case_id,
        subject_for_key=_subject_for_key,
        limits=spec_lang_limits,
        symbols=spec_lang_symbols,
    )
