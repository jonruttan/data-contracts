#!/usr/bin/env python3
from __future__ import annotations

from spec_runner.spec_lang_commands import schema_registry_report_main


def main(argv: list[str] | None = None) -> int:
    # Keep script compatibility while using the canonical CLI implementation.
    return schema_registry_report_main(argv)


if __name__ == "__main__":
    raise SystemExit(main())
