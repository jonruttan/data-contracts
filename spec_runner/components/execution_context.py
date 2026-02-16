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
    return HarnessExecutionContext(
        case_id=case_id,
        limits=limits,
        imports=imports,
        symbols=symbols,
    )

