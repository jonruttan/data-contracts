#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

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
from spec_runner.virtual_paths import VirtualPathError, resolve_contract_path


def _render_issues(issues: list[DocsIssue]) -> None:
    for issue in issues:
        print(issue.render())


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Lint docs quality contract rules.")
    ap.add_argument("--manifest", default="docs/book/reference_manifest.yaml")
    ns = ap.parse_args(argv)

    root = Path.cwd()
    manifest, manifest_issues = load_reference_manifest(root, str(ns.manifest))
    issues: list[DocsIssue] = []
    issues.extend(manifest_issues)
    if manifest_issues:
        _render_issues(issues)
        return 1

    docs = manifest_chapter_paths(manifest)
    metas, meta_issues, _meta_lines = load_docs_meta_for_paths(root, docs)
    issues.extend(meta_issues)

    for rel in docs:
        if rel in metas:
            try:
                doc_path = resolve_contract_path(root, str(rel), field="reference_manifest.chapters.path")
            except VirtualPathError as exc:
                issues.append(DocsIssue(rule_id="DOCS_REFERENCE_MANIFEST_SYNC", path=str(rel), message=str(exc)))
                continue
            metas[rel]["__text__"] = doc_path.read_text(encoding="utf-8")

    issues.extend(check_token_ownership_unique(metas))
    issues.extend(check_token_dependency_resolved(metas))
    issues.extend(check_instructions_complete(root, metas))
    issues.extend(check_command_examples_verified(root, docs))
    issues.extend(check_example_id_uniqueness(metas))

    if issues:
        _render_issues(issues)
        return 1
    print("OK: docs lint passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
