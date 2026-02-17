#!/usr/bin/env python3
from __future__ import annotations

from spec_runner.cli import docs_lint_main


def main(argv: list[str] | None = None) -> int:
    # Keep script compatibility while using the canonical CLI implementation.
    return docs_lint_main(argv)


if __name__ == "__main__":
    raise SystemExit(main())
