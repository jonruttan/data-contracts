#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
import subprocess


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Generate and verify docs surfaces via spec-driven docs.generate cases.")
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--build", action="store_true")
    mode.add_argument("--check", action="store_true")
    ap.add_argument("--surface", default="", help="Optional docs surface_id filter")
    ap.add_argument("--jobs", type=int, default=0, help="Parallel jobs for docs generation (0=auto)")
    ap.add_argument("--report-out", default=".artifacts/docs-generator-report.json")
    ap.add_argument("--summary-out", default=".artifacts/docs-generator-summary.md")
    ap.add_argument("--timing-out", default=".artifacts/docs-generate-timing.json")
    ap.add_argument("--profile", action="store_true", help="Emit per-case harness timing profile JSON")
    ap.add_argument("--profile-out", default=".artifacts/docs-generate-profile.json")
    ns = ap.parse_args(argv)

    repo_root = Path(__file__).resolve().parents[1]
    py = repo_root / ".venv/bin/python"
    cmd = [
        str(py if py.exists() else "python3"),
        "scripts/docs_generate_specs.py",
        "--check" if ns.check else "--build",
        "--report-out",
        str(ns.report_out),
        "--summary-out",
        str(ns.summary_out),
        "--timing-out",
        str(ns.timing_out),
    ]
    if bool(ns.profile):
        cmd.append("--profile")
        cmd += ["--profile-out", str(ns.profile_out)]
    if int(ns.jobs) != 0:
        cmd += ["--jobs", str(int(ns.jobs))]
    if str(ns.surface).strip():
        cmd += ["--surface", str(ns.surface).strip()]
    cp = subprocess.run(cmd, cwd=repo_root, check=False)
    return int(cp.returncode)


if __name__ == "__main__":
    raise SystemExit(main())
