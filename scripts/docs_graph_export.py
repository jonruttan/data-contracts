#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from spec_runner.docs_quality import build_docs_graph, load_docs_meta_for_paths, load_reference_manifest, manifest_chapter_paths
from spec_runner.virtual_paths import VirtualPathError, resolve_contract_path


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Export docs relationship graph JSON.")
    ap.add_argument("--manifest", default="docs/book/reference_manifest.yaml")
    ap.add_argument("--out", default="docs/book/docs_graph.json")
    ns = ap.parse_args(argv)

    root = Path.cwd()
    manifest, issues = load_reference_manifest(root, str(ns.manifest))
    if issues:
        for issue in issues:
            print(issue.render())
        return 1

    docs = manifest_chapter_paths(manifest)
    metas, meta_issues, _meta_lines = load_docs_meta_for_paths(root, docs)
    if meta_issues:
        for issue in meta_issues:
            print(issue.render())
        return 1
    graph = build_docs_graph(root, metas)
    try:
        out_path = resolve_contract_path(root, str(ns.out), field="docs_graph_out")
    except VirtualPathError:
        out_path = root / str(ns.out).lstrip("/")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(graph, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {ns.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
