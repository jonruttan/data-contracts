#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path
from typing import Any

_REQUIRED_KEYS = {"id", "where", "priority", "statement", "rationale", "verification"}


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _extract_yaml_blocks(md: str) -> list[str]:
    blocks: list[str] = []
    in_yaml = False
    cur: list[str] = []
    for line in md.splitlines():
        if not in_yaml and line.strip().startswith("```yaml"):
            in_yaml = True
            cur = []
            continue
        if in_yaml and line.strip() == "```":
            blocks.append("\n".join(cur).strip())
            in_yaml = False
            cur = []
            continue
        if in_yaml:
            cur.append(line)
    return [b for b in blocks if b]


def _parse_candidates(md: str) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for block in _extract_yaml_blocks(md):
        raw = _parse_simple_yaml_candidate(block)
        if raw is None:
            continue
        if not _REQUIRED_KEYS.issubset(raw.keys()):
            continue
        out.append({k: raw[k] for k in _REQUIRED_KEYS})
    return out


def _parse_simple_yaml_candidate(block: str) -> dict[str, str] | None:
    """
    Parse the limited candidate schema without external YAML dependencies.

    Supports scalar `key: value` and folded style:
      key: >
        line 1
        line 2
    """
    out: dict[str, str] = {}
    lines = block.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^([a-z_]+):\s*(.*)$", line.strip())
        if not m:
            i += 1
            continue
        key = m.group(1)
        val = m.group(2).strip()
        if val in {">", "|"}:
            i += 1
            buf: list[str] = []
            while i < len(lines):
                nxt = lines[i]
                if re.match(r"^[a-z_]+:\s*", nxt.strip()):
                    break
                if nxt.startswith("  ") or nxt.startswith("\t") or nxt.strip() == "":
                    buf.append(nxt.strip())
                    i += 1
                    continue
                break
            out[key] = " ".join(x for x in buf if x).strip()
            continue
        if val.startswith("'") and val.endswith("'") and len(val) >= 2:
            val = val[1:-1]
        if val.startswith('"') and val.endswith('"') and len(val) >= 2:
            val = val[1:-1]
        out[key] = val
        i += 1
    if not out:
        return None
    return out


def _extract_classifications(md: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for line in md.splitlines():
        m = re.match(r"\s*-\s*`([^`]+)`:\s*(behavior|docs|tooling)\s*$", line.strip(), flags=re.I)
        if not m:
            continue
        out[m.group(1)] = m.group(2).lower()
    return out


def _infer_implicit(md: str, *, limit: int = 10) -> list[dict[str, str]]:
    bullets: list[str] = []
    capture = False
    for line in md.splitlines():
        s = line.strip()
        if s.startswith("## "):
            head = s[3:].lower()
            capture = any(
                key in head
                for key in (
                    "must-do",
                    "blocker",
                    "biggest risk",
                    "definition of done",
                    "north-star",
                )
            )
            continue
        if capture and s.startswith("- "):
            txt = s[2:].strip()
            if len(txt) >= 20 and "|" not in txt and "`" not in txt:
                bullets.append(txt)
    seen = set()
    uniq: list[str] = []
    for b in bullets:
        k = b.lower()
        if k in seen:
            continue
        seen.add(k)
        uniq.append(b)
    uniq = uniq[:limit]

    out: list[dict[str, str]] = []
    for i, b in enumerate(uniq, start=1):
        area = "CORE"
        lower = b.lower()
        if "security" in lower or "trust" in lower or "safe" in lower:
            area = "SEC"
        elif "cli" in lower or "command" in lower:
            area = "CLI"
        elif "config" in lower or "discover" in lower:
            area = "CONF"
        elif "doc" in lower or "onboarding" in lower:
            area = "DOC"
        elif "ci" in lower or "reliab" in lower or "timeout" in lower:
            area = "OPS"
        out.append(
            {
                "id": f"CK-{area}-IMP-{i:03d}",
                "where": "specs/backlog.md",
                "priority": "P1",
                "statement": f"SHOULD {b[0].lower() + b[1:]}" if b and b[0].isupper() else f"SHOULD {b}",
                "rationale": "Inferred from repeated narrative concerns in the review output; requires human triage.",
                "verification": "Define as yaml contract-spec where possible; otherwise add a governance check with deterministic output.",
            }
        )
    return out


def _write_pending(
    out_path: Path,
    *,
    title: str,
    source: Path,
    explicit: list[dict[str, Any]],
    classifications: dict[str, str],
    implicit: list[dict[str, str]],
) -> None:
    today = dt.date.today().isoformat()
    lines: list[str] = []
    lines.append("---")
    lines.append(f"id: CK-REVIEW-{today.replace('-', '')}")
    lines.append(f"title: {title}")
    lines.append("priority: P1")
    lines.append("---")
    lines.append("")
    lines.append(f"# {title}")
    lines.append("")
    lines.append(f"Source snapshot: `{source.as_posix()}`")
    lines.append("")

    if explicit:
        lines.append("## Explicit Spec Candidates")
        lines.append("")
        for c in explicit:
            cid = str(c["id"])
            cls = classifications.get(cid, "unclassified")
            lines.append(f"### {cid}")
            lines.append("")
            lines.append(f"- where: `{c['where']}`")
            lines.append(f"- priority: `{c['priority']}`")
            lines.append(f"- classification: `{cls}`")
            lines.append(f"- statement: {c['statement']}")
            lines.append(f"- rationale: {c['rationale']}")
            lines.append(f"- verification: {c['verification']}")
            lines.append("")

    if implicit:
        lines.append("## Implicit Suggestions (Inferred, Needs Review)")
        lines.append("")
        for c in implicit:
            lines.append(f"### {c['id']}")
            lines.append("")
            lines.append(f"- where: `{c['where']}`")
            lines.append(f"- priority: `{c['priority']}`")
            lines.append(f"- statement: {c['statement']}")
            lines.append(f"- rationale: {c['rationale']}")
            lines.append(f"- verification: {c['verification']}")
            lines.append("")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="Extract explicit YAML spec candidates from a review snapshot and infer implicit suggestions into specs/pending.",
    )
    ap.add_argument("snapshot", help="Path to review snapshot markdown")
    ap.add_argument(
        "--out",
        default="",
        help="Output pending markdown path (default: specs/governance/pending/<snapshot-stem>-pending.md)",
    )
    ap.add_argument(
        "--implicit-limit",
        type=int,
        default=10,
        help="Maximum inferred implicit suggestions",
    )
    ns = ap.parse_args(argv)

    src = Path(ns.snapshot)
    md = _read(src)
    explicit = _parse_candidates(md)
    cls = _extract_classifications(md)
    implicit = _infer_implicit(md, limit=max(0, int(ns.implicit_limit)))

    out_path = Path(ns.out) if ns.out else Path("specs/pending") / f"{src.stem}-pending.md"
    _write_pending(
        out_path,
        title="Review-Derived Spec Candidates",
        source=src,
        explicit=explicit,
        classifications=cls,
        implicit=implicit,
    )

    print(f"wrote {out_path.as_posix()} (explicit={len(explicit)} implicit={len(implicit)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
