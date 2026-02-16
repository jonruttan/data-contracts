from __future__ import annotations

from spec_runner.components.contracts import HarnessExecutionContext
from spec_runner.spec_lang import compile_import_bindings, limits_from_harness
from spec_runner.spec_lang_libraries import load_spec_lang_symbols_for_case


def build_execution_context(*, case_id: str, harness: dict, doc_path) -> HarnessExecutionContext:
    limits = limits_from_harness(harness)
    imports = compile_import_bindings((harness or {}).get("spec_lang"))
    symbols = load_spec_lang_symbols_for_case(
        doc_path=doc_path,
        harness=harness,
        limits=limits,
    )
    chain_bindings = dict((harness or {}).get("_chain_imports") or {})
    if chain_bindings:
        for key in chain_bindings:
            s = str(key).strip()
            if not s:
                raise ValueError("harness.chain.imports local binding names must be non-empty strings")
            if s in symbols:
                raise ValueError(f"harness.chain.imports local binding collides with existing symbol: {s}")
        symbols = {**symbols, **{str(k): v for k, v in chain_bindings.items()}}
    return HarnessExecutionContext(
        case_id=case_id,
        limits=limits,
        imports=imports,
        symbols=symbols,
    )
