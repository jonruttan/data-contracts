from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

from spec_runner.conformance import report_to_jsonable, run_conformance_cases
from spec_runner.conformance_parity import ParityConfig, build_parity_artifact, run_parity_check
from spec_runner.conformance import validate_conformance_report_payload
from spec_runner.contract_governance import contract_coverage_jsonable
from spec_runner.docs_quality import (
    DocsIssue,
    check_command_examples_verified,
    check_example_id_uniqueness,
    check_instructions_complete,
    check_token_dependency_resolved,
    check_token_ownership_unique,
    load_docs_meta_for_paths,
    load_reference_manifest,
    manifest_chapter_paths,
)
from spec_runner.schema_registry import compile_registry, write_compiled_registry_artifact
from spec_runner.spec_lang_stdlib_profile import spec_lang_stdlib_report_jsonable
from spec_runner.virtual_paths import VirtualPathError, resolve_contract_path
from spec_runner.dispatcher import SpecRunContext
from spec_runner.runtime_context import MiniCapsys, MiniMonkeyPatch
from spec_runner.settings import SETTINGS


def _write_json(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def conformance_runner_main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="Run conformance cases with Python runner and emit normalized report JSON."
    )
    ap.add_argument("--cases", required=True, help="Path to conformance case docs directory or case file")
    ap.add_argument("--out", required=True, help="Path to write JSON report")
    ap.add_argument(
        "--case-file-pattern",
        default=SETTINGS.case.default_file_pattern,
        help="Glob pattern for case files when --cases points to a directory",
    )
    ap.add_argument(
        "--case-formats",
        default="md",
        help="Comma-separated case formats to load (md,yaml,json). Default: md",
    )
    ns = ap.parse_args(argv)

    case_pattern = str(ns.case_file_pattern).strip()
    if not case_pattern:
        print("ERROR: --case-file-pattern requires a non-empty value", file=sys.stderr)
        return 2
    case_formats = {x.strip() for x in str(ns.case_formats).split(",") if x.strip()}
    if not case_formats:
        print("ERROR: --case-formats requires at least one format", file=sys.stderr)
        return 2

    cases_path = Path(str(ns.cases))
    if not cases_path.exists():
        print(f"ERROR: cases path does not exist: {cases_path}", file=sys.stderr)
        return 2

    with TemporaryDirectory(prefix="spec-runner-python-") as td:
        tmp_path = Path(td)
        patcher = MiniMonkeyPatch()
        capture = MiniCapsys()
        ctx = SpecRunContext(tmp_path=tmp_path, patcher=patcher, capture=capture)
        with capture.capture():
            try:
                results = run_conformance_cases(
                    cases_path,
                    ctx=ctx,
                    implementation="python",
                    case_file_pattern=case_pattern,
                    case_formats=case_formats,
                )
            except BaseException as e:  # noqa: BLE001
                print(f"ERROR: {e}", file=sys.stderr)
                return 1

    payload = report_to_jsonable(results)
    _write_json(Path(str(ns.out)), payload)
    return 0 if all(r.status in {"pass", "skip"} for r in results) else 1


def compare_parity_main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="Run Python/PHP conformance and report normalized parity diffs by case id."
    )
    ap.add_argument(
        "--cases",
        default="docs/spec/conformance/cases",
        help="Path to conformance case docs directory",
    )
    ap.add_argument(
        "--php-runner",
        default="scripts/php/conformance_runner.php",
        help="Path to PHP conformance runner script",
    )
    ap.add_argument(
        "--python-runner",
        default="scripts/python/conformance_runner.py",
        help="Path to Python conformance runner script",
    )
    ap.add_argument(
        "--out",
        default="",
        help="Optional path to write JSON parity artifact",
    )
    ap.add_argument(
        "--case-formats",
        default="md",
        help="Comma-separated case formats to load (md,yaml,json). Default: md",
    )
    ap.add_argument(
        "--php-timeout-seconds",
        type=int,
        default=30,
        help="Timeout in seconds for the PHP parity runner subprocess (default: 30)",
    )
    ap.add_argument(
        "--python-timeout-seconds",
        type=int,
        default=30,
        help="Timeout in seconds for the Python parity runner subprocess (default: 30)",
    )
    ns = ap.parse_args(argv)
    out_path = Path(str(ns.out)).resolve() if str(ns.out).strip() else None

    if shutil.which("php") is None:
        msg = "php executable not found in PATH"
        if out_path is not None:
            _write_json(out_path, build_parity_artifact([msg]))
        print(f"ERROR: {msg}", file=sys.stderr)
        return 2

    case_formats = {x.strip() for x in str(ns.case_formats).split(",") if x.strip()}
    if not case_formats:
        msg = "--case-formats requires at least one format"
        if out_path is not None:
            _write_json(out_path, build_parity_artifact([msg]))
        print(f"ERROR: {msg}", file=sys.stderr)
        return 2

    cfg = ParityConfig(
        cases_dir=Path(ns.cases),
        php_runner=Path(ns.php_runner),
        python_runner=Path(ns.python_runner),
        case_formats=case_formats,
        python_timeout_seconds=int(ns.python_timeout_seconds),
        php_timeout_seconds=int(ns.php_timeout_seconds),
    )
    try:
        errs = run_parity_check(cfg)
    except RuntimeError as err:
        if out_path is not None:
            _write_json(out_path, build_parity_artifact([str(err)]))
        print(f"ERROR: {err}", file=sys.stderr)
        return 1
    if out_path is not None:
        _write_json(out_path, build_parity_artifact(errs))
    if errs:
        print("ERROR: conformance parity check failed", file=sys.stderr)
        for msg in errs:
            print(f"- {msg}", file=sys.stderr)
        return 1

    print(f"OK: conformance parity matched for {cfg.cases_dir}")
    return 0


def validate_report_main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Validate a conformance JSON report payload.")
    ap.add_argument("report", help="Path to report JSON file")
    ns = ap.parse_args(argv)

    p = Path(ns.report)
    payload = json.loads(p.read_text(encoding="utf-8"))
    errs = validate_conformance_report_payload(payload)
    if errs:
        for e in errs:
            print(f"ERROR: {e}", file=sys.stderr)
        return 1
    print(f"OK: valid conformance report ({p})")
    return 0


def _spec_lang_stdlib_to_markdown(payload: dict[str, object]) -> str:
    summary = payload.get("summary") if isinstance(payload, dict) else {}
    if not isinstance(summary, dict):
        summary = {}
    lines = [
        "# Spec-Lang Stdlib Profile Report",
        "",
        f"- profile symbols: {int(summary.get('profile_symbol_count', 0))}",
        f"- python symbols: {int(summary.get('python_symbol_count', 0))}",
        f"- php symbols: {int(summary.get('php_symbol_count', 0))}",
        f"- missing in python: {int(summary.get('missing_in_python_count', 0))}",
        f"- missing in php: {int(summary.get('missing_in_php_count', 0))}",
        f"- arity mismatch: {int(summary.get('arity_mismatch_count', 0))}",
        f"- docs sync missing: {int(summary.get('docs_sync_missing_count', 0))}",
        "",
    ]
    for key in ("missing_in_python", "missing_in_php", "arity_mismatch", "docs_sync_missing", "errors"):
        vals = payload.get(key) if isinstance(payload, dict) else []
        if not isinstance(vals, list) or not vals:
            continue
        lines.append(f"## {key.replace('_', ' ').title()}")
        lines.append("")
        for item in vals:
            lines.append(f"- {item}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def spec_lang_stdlib_report_main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="Emit spec-lang stdlib profile completeness/parity report."
    )
    ap.add_argument("--out", help="Optional output path.")
    ap.add_argument("--format", choices=("json", "md"), default="json")
    ns = ap.parse_args(argv)

    repo_root = Path(__file__).resolve().parents[1]
    payload = spec_lang_stdlib_report_jsonable(repo_root)
    raw = (
        _spec_lang_stdlib_to_markdown(payload)
        if ns.format == "md"
        else json.dumps(payload, indent=2, sort_keys=True) + "\n"
    )

    if ns.out:
        out = Path(ns.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(raw, encoding="utf-8")
        print(f"wrote {out}")
    else:
        print(raw, end="")
    return 0


def contract_coverage_report_main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=(
            "Emit optional spec_runner contract coverage report as JSON "
            "(artifact/reporting helper; not a primary gate)."
        )
    )
    ap.add_argument("--out", help="Optional output path for JSON report.")
    ns = ap.parse_args(argv)

    repo_root = Path(__file__).resolve().parents[1]
    payload = contract_coverage_jsonable(repo_root)
    raw = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if ns.out:
        out = Path(ns.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(raw, encoding="utf-8")
        print(f"wrote {out}")
    else:
        print(raw, end="")
    return 0


def _schema_registry_render_md(payload: dict[str, object]) -> str:
    summary = payload.get("summary") if isinstance(payload, dict) else {}
    if not isinstance(summary, dict):
        summary = {}
    lines = [
        "# Schema Registry Report",
        "",
        f"- profile_count: {int(summary.get('profile_count', 0))}",
        f"- top_level_field_count: {int(summary.get('top_level_field_count', 0))}",
        f"- type_profile_count: {int(summary.get('type_profile_count', 0))}",
        f"- errors: {int(summary.get('error_count', 0))}",
        "",
    ]
    errors = payload.get("errors") if isinstance(payload, dict) else []
    if isinstance(errors, list) and errors:
        lines.extend(["## Errors", ""])
        for err in errors:
            lines.append(f"- {err}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def schema_registry_report_main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Emit schema registry compiled report.")
    ap.add_argument("--out", default=".artifacts/schema_registry_report.md")
    ap.add_argument("--format", choices=("json", "md"), default="md")
    ap.add_argument("--check", action="store_true")
    ns = ap.parse_args(argv)

    repo_root = Path(__file__).resolve().parents[1]
    compiled, errs = compile_registry(repo_root)
    payload: dict[str, object] = {
        "version": 1,
        "summary": {
            "profile_count": int(compiled.get("profile_count", 0)) if compiled else 0,
            "top_level_field_count": len((compiled or {}).get("top_level_fields") or {}),
            "type_profile_count": len((compiled or {}).get("type_profiles") or {}),
            "error_count": len(errs),
        },
        "errors": errs,
    }
    if compiled:
        payload["compiled"] = compiled

    if compiled:
        write_compiled_registry_artifact(repo_root, compiled)
    raw = (
        _schema_registry_render_md(payload)
        if ns.format == "md"
        else json.dumps(payload, indent=2, sort_keys=True) + "\n"
    )
    out = Path(str(ns.out))
    out.parent.mkdir(parents=True, exist_ok=True)
    if ns.check:
        if not out.exists():
            print(f"{out}: missing report artifact")
            return 1
        if out.read_text(encoding="utf-8") != raw:
            print(f"{out}: stale report artifact")
            return 1
        print("OK: schema registry report is up to date")
        return 0
    out.write_text(raw, encoding="utf-8")
    print(f"wrote {out}")
    return 0 if not errs else 1


def _render_docs_issues(issues: list[DocsIssue]) -> None:
    for issue in issues:
        print(issue.render())


def docs_lint_main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Lint docs quality contract rules.")
    ap.add_argument("--manifest", default="docs/book/reference_manifest.yaml")
    ns = ap.parse_args(argv)

    root = Path.cwd()
    manifest, manifest_issues = load_reference_manifest(root, str(ns.manifest))
    issues: list[DocsIssue] = []
    issues.extend(manifest_issues)
    if manifest_issues:
        _render_docs_issues(issues)
        return 1

    docs = manifest_chapter_paths(manifest)
    metas, meta_issues, _meta_lines = load_docs_meta_for_paths(root, docs)
    issues.extend(meta_issues)

    for rel in docs:
        if rel in metas:
            try:
                doc_path = resolve_contract_path(root, str(rel), field="reference_manifest.chapters.path")
            except VirtualPathError as exc:
                issues.append(
                    DocsIssue(path=str(rel), line=1, message=str(exc))
                )
                continue
            metas[rel]["__text__"] = doc_path.read_text(encoding="utf-8")

    issues.extend(check_token_ownership_unique(metas))
    issues.extend(check_token_dependency_resolved(metas))
    issues.extend(check_instructions_complete(root, metas))
    issues.extend(check_command_examples_verified(root, docs))
    issues.extend(check_example_id_uniqueness(metas))

    if issues:
        _render_docs_issues(issues)
        return 1
    print("OK: docs lint passed")
    return 0
