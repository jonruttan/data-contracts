#!/usr/bin/env python3
from __future__ import annotations

from spec_runner.cli import validate_report_main


def main(argv: list[str] | None = None) -> int:
    # Keep legacy script entrypoint while using the canonical CLI implementation.
    return validate_report_main(argv)


if __name__ == "__main__":
    raise SystemExit(main())
