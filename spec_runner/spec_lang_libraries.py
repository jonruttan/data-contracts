from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from spec_runner.codecs import load_external_cases
from spec_runner.external_refs import resolve_external_ref
from spec_runner.spec_lang import SpecLangLimits, compile_symbol_bindings
from spec_runner.spec_lang_yaml_ast import SpecLangYamlAstError, compile_yaml_expr_to_sexpr
from spec_runner.virtual_paths import VirtualPathError, contract_root_for, parse_external_ref, resolve_contract_path


@dataclass(frozen=True)
class _LibraryDoc:
    path: Path
    imports: tuple[str, ...]
    bindings: dict[str, Any]
    exports: tuple[str, ...]


def _resolve_library_path(
    base_doc: Path,
    rel_path: str,
    *,
    harness: dict[str, Any] | None,
    requires: dict[str, Any] | None,
) -> Path:
    raw = str(rel_path).strip()
    if parse_external_ref(raw) is not None:
        try:
            p = resolve_external_ref(raw, harness=harness, requires=requires)
        except VirtualPathError as exc:
            raise ValueError(str(exc)) from exc
    else:
        root = contract_root_for(base_doc)
        try:
            p = resolve_contract_path(root, raw, field="harness.spec_lang.library_paths")
        except VirtualPathError as exc:
            raise ValueError(str(exc)) from exc
    if not p.exists() or not p.is_file():
        raise ValueError(f"library path does not exist: {rel_path}")
    return p


def _as_non_empty_str_list(value: object, *, field: str) -> tuple[str, ...]:
    if value is None:
        return ()
    if not isinstance(value, list):
        raise TypeError(f"{field} must be a list of non-empty strings")
    out: list[str] = []
    for i, item in enumerate(value):
        s = str(item).strip() if isinstance(item, str) else ""
        if not s:
            raise TypeError(f"{field}[{i}] must be a non-empty string")
        out.append(s)
    return tuple(out)


def _load_library_doc(path: Path) -> _LibraryDoc:
    loaded = load_external_cases(path, formats={"md", "yaml", "json"})
    imports: list[str] = []
    bindings: dict[str, Any] = {}
    exports: list[str] = []

    for _, case in loaded:
        case_type = str(case.get("type", "")).strip()
        if case_type != "spec_lang.library":
            continue

        case_imports = _as_non_empty_str_list(case.get("imports"), field="imports")
        imports.extend(case_imports)

        raw_bindings = case.get("functions")
        if not isinstance(raw_bindings, dict) or not raw_bindings:
            raise TypeError("spec_lang.library requires non-empty functions mapping")
        for raw_name, expr in raw_bindings.items():
            name = str(raw_name).strip()
            if not name:
                raise ValueError("spec_lang.library function name must be non-empty")
            if name in bindings:
                raise ValueError(f"duplicate library function in file {path}: {name}")
            try:
                bindings[name] = compile_yaml_expr_to_sexpr(
                    expr,
                    field_path=f"{path.as_posix()} functions.{name}",
                )
            except SpecLangYamlAstError as exc:
                raise ValueError(str(exc)) from exc

        case_exports = _as_non_empty_str_list(case.get("exports"), field="exports")
        exports.extend(case_exports)

    if not bindings:
        raise ValueError(f"library file has no spec_lang.library functions: {path}")

    return _LibraryDoc(
        path=path,
        imports=tuple(dict.fromkeys(imports)),
        bindings=bindings,
        exports=tuple(dict.fromkeys(exports)),
    )


def _resolve_library_graph(
    entry_docs: list[Path], *, harness: dict[str, Any] | None, requires: dict[str, Any] | None
) -> list[_LibraryDoc]:
    docs: dict[Path, _LibraryDoc] = {}
    visiting: set[Path] = set()
    visited: set[Path] = set()
    ordered: list[Path] = []

    def _dfs(path: Path) -> None:
        if path in visited:
            return
        if path in visiting:
            raise ValueError(f"library import cycle detected at: {path}")
        visiting.add(path)
        doc = docs.get(path)
        if doc is None:
            doc = _load_library_doc(path)
            docs[path] = doc
        for rel in doc.imports:
            dep = _resolve_library_path(path, rel, harness=harness, requires=requires)
            _dfs(dep)
        visiting.remove(path)
        visited.add(path)
        ordered.append(path)

    for p in entry_docs:
        _dfs(p)

    return [docs[p] for p in ordered]


def load_spec_lang_symbols_for_case(
    *,
    doc_path: Path,
    harness: dict[str, Any] | None,
    limits: SpecLangLimits,
) -> dict[str, Any]:
    cfg = dict((harness or {}).get("spec_lang") or {})
    lib_paths = _as_non_empty_str_list(cfg.get("library_paths"), field="harness.spec_lang.library_paths")
    if not lib_paths:
        return {}
    requires = dict((harness or {}).get("requires") or {})

    entry_docs = [
        _resolve_library_path(doc_path, rel, harness=harness, requires=requires) for rel in lib_paths
    ]
    graph = _resolve_library_graph(entry_docs, harness=harness, requires=requires)

    merged_bindings: dict[str, Any] = {}
    export_allow: set[str] = set()
    for doc in graph:
        for name, expr in doc.bindings.items():
            if name in merged_bindings:
                raise ValueError(f"duplicate exported library symbol across imports: {name}")
            merged_bindings[name] = expr
        if doc.exports:
            export_allow.update(doc.exports)

    consumer_exports = _as_non_empty_str_list(cfg.get("exports"), field="harness.spec_lang.exports")
    if consumer_exports:
        export_allow = set(consumer_exports)

    if export_allow:
        filtered = {k: v for k, v in merged_bindings.items() if k in export_allow}
        unknown = sorted(x for x in export_allow if x not in merged_bindings)
        if unknown:
            raise ValueError(
                "harness.spec_lang.exports contains unknown symbols: " + ", ".join(unknown)
            )
        merged_bindings = filtered

    return compile_symbol_bindings(merged_bindings, limits=limits)
