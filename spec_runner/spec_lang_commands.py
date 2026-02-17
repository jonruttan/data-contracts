from __future__ import annotations

import argparse
import json
import sys
from functools import lru_cache
from pathlib import Path

from spec_runner.codecs import load_external_cases
from spec_runner.spec_lang import SpecLangLimits, eval_expr
from spec_runner.spec_lang_yaml_ast import SpecLangYamlAstError, compile_yaml_expr_to_sexpr


def validate_report_main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Validate a conformance JSON report payload.")
    ap.add_argument("report", help="Path to report JSON file")
    ns = ap.parse_args(argv)

    p = Path(ns.report)
    payload = json.loads(p.read_text(encoding="utf-8"))
    errs = _validate_report_payload_spec_lang(payload)
    if errs:
        for e in errs:
            print(f"ERROR: {e}", file=sys.stderr)
        return 1
    print(f"OK: valid conformance report ({p})")
    return 0


@lru_cache(maxsize=1)
def _load_validate_report_errors_fn_expr() -> list[object]:
    repo_root = Path(__file__).resolve().parents[1]
    lib_path = repo_root / "docs/spec/libraries/domain/conformance_core.spec.md"
    target_symbol = "domain.conformance.validate_report_errors"
    if not lib_path.exists():
        raise RuntimeError(f"missing spec library file: {lib_path}")
    for _doc_path, raw_case in load_external_cases(lib_path, formats={"md"}):
        if str(raw_case.get("type", "")).strip() != "spec.export":
            continue
        chain = dict((dict(raw_case.get("harness") or {})).get("chain") or {})
        exports = chain.get("exports") or []
        if not isinstance(exports, list):
            continue
        for exp in exports:
            if not isinstance(exp, dict):
                continue
            if str(exp.get("as", "")).strip() != target_symbol:
                continue
            if str(exp.get("from", "")).strip() != "assert.function":
                raise RuntimeError(f"{target_symbol} must use from: assert.function")
            step_id = str(exp.get("path", "")).strip().lstrip("/")
            params = exp.get("params")
            if not isinstance(params, list) or not params or not all(isinstance(x, str) and x.strip() for x in params):
                raise RuntimeError(f"{target_symbol} must declare non-empty string params list")
            assert_steps = raw_case.get("assert")
            if not isinstance(assert_steps, list):
                raise RuntimeError(f"{target_symbol} producer case must include assert list")
            for step in assert_steps:
                if not isinstance(step, dict):
                    continue
                if str(step.get("id", "")).strip() != step_id:
                    continue
                checks = step.get("checks")
                if not isinstance(checks, list) or len(checks) != 1 or not isinstance(checks[0], dict):
                    raise RuntimeError(f"{target_symbol} export step must have exactly one expression check")
                try:
                    body_expr = compile_yaml_expr_to_sexpr(
                        checks[0],
                        field_path=f"{lib_path.as_posix()}#{step_id}.checks[0]",
                    )
                except SpecLangYamlAstError as exc:
                    raise RuntimeError(str(exc)) from exc
                return ["fn", [str(x).strip() for x in params], body_expr]
            raise RuntimeError(f"{target_symbol} export step id not found: {step_id}")
    raise RuntimeError(f"symbol not found in spec export library: {target_symbol}")


def _validate_report_payload_spec_lang(payload: object) -> list[str]:
    fn_expr = _load_validate_report_errors_fn_expr()
    result = eval_expr(
        ["call", fn_expr, ["var", "subject"]],
        subject=payload,
        limits=SpecLangLimits(),
        symbols={},
        imports={},
    )
    if not isinstance(result, list):
        raise RuntimeError("spec-lang validate_report function must return list[str]")
    out: list[str] = []
    for item in result:
        if isinstance(item, str) and item.strip():
            out.append(item.strip())
    return out
