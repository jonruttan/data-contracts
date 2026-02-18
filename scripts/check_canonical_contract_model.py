#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path


FORBIDDEN_TOKENS = (
    "type: text.file",
    "type: cli.run",
    "type: api.http",
    "type: governance.check",
    "type: orchestration.run",
    "type: docs.generate",
    "type: spec.export",
    "\n  contain:",
    "\n  regex:",
    "\n  json_type:",
    "\n  exists:",
)


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    docs = root / "docs"
    violations: list[str] = []
    for p in sorted(docs.rglob("*.md")):
        text = p.read_text(encoding="utf-8")
        for token in FORBIDDEN_TOKENS:
            if token in text:
                violations.append(f"{p.relative_to(root)}: forbidden token {token!r}")
    if violations:
        for v in violations:
            print(v)
        return 1
    print("OK: canonical contract model checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
