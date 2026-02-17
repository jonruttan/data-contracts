#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def _load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _top_slow_spans(payload: dict, limit: int) -> list[dict]:
    spans = payload.get("spans")
    if not isinstance(spans, list):
        return []
    rows = [x for x in spans if isinstance(x, dict)]
    rows.sort(key=lambda row: float(row.get("duration_ms") or 0.0), reverse=True)
    return rows[: max(limit, 1)]


def _repeat_fail_steps(payload: dict) -> dict[str, int]:
    steps = payload.get("steps")
    counts: dict[str, int] = {}
    if not isinstance(steps, list):
        return counts
    for step in steps:
        if not isinstance(step, dict):
            continue
        if str(step.get("status", "")).strip() != "fail":
            continue
        name = str(step.get("name", "")).strip() or "<unknown>"
        counts[name] = counts.get(name, 0) + 1
    return dict(sorted(counts.items(), key=lambda kv: kv[1], reverse=True))


def _last_progress_event(payload: dict) -> dict | None:
    events = payload.get("events")
    if not isinstance(events, list):
        return None
    out: dict | None = None
    best = -1
    for event in events:
        if not isinstance(event, dict):
            continue
        ts = int(event.get("ts_ns") or 0)
        if ts >= best:
            best = ts
            out = event
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Summarize profiling hotspots from run-trace artifacts")
    ap.add_argument("--trace", default=".artifacts/run-trace.json", help="Path to run trace JSON")
    ap.add_argument("--out", default=".artifacts/profile-hotspots-summary.md", help="Output markdown path")
    ap.add_argument("--top", type=int, default=10, help="Number of slow spans to include")
    ns = ap.parse_args(argv)

    trace_path = Path(str(ns.trace))
    if not trace_path.exists():
        print(f"ERROR: trace file not found: {trace_path}")
        return 1

    payload = _load_json(trace_path)
    slow_spans = _top_slow_spans(payload, int(ns.top))
    failed_steps = _repeat_fail_steps(payload)
    last_event = _last_progress_event(payload)

    lines = [
        "# Profile Hotspots Summary",
        "",
        f"- trace: `{trace_path}`",
        f"- status: `{payload.get('status', 'unknown')}`",
        f"- run_id: `{payload.get('run_id', '')}`",
        "",
        "## Slowest Spans",
        "",
        "| span | phase | status | duration_ms |",
        "|---|---|---|---|",
    ]
    for row in slow_spans:
        lines.append(
            "| `{}` | `{}` | `{}` | `{}` |".format(
                row.get("name", ""),
                row.get("phase", ""),
                row.get("status", ""),
                row.get("duration_ms", ""),
            )
        )

    lines.extend(["", "## Repeated Failing Steps", ""])
    if failed_steps:
        lines.append("| step | count |")
        lines.append("|---|---|")
        for name, count in failed_steps.items():
            lines.append(f"| `{name}` | `{count}` |")
    else:
        lines.append("- none")

    lines.extend(["", "## Last Progress Event", ""])
    if isinstance(last_event, dict):
        lines.append(f"- kind: `{last_event.get('kind', '')}`")
        lines.append(f"- ts_ns: `{last_event.get('ts_ns', '')}`")
        lines.append(f"- attrs: `{json.dumps(last_event.get('attrs', {}), sort_keys=True)}`")
    else:
        lines.append("- none")

    lines.extend(
        [
            "",
            "## Suggested Next Command",
            "",
            "- `./scripts/runner_adapter.sh --impl rust --profile-level detailed --profile-heartbeat-ms 250 --profile-stall-threshold-ms 2000 ci-gate-summary`",
            "",
        ]
    )

    out_path = Path(str(ns.out))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
