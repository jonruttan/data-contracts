#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path
import yaml


_FENCE_RE = re.compile(r"```yaml contract-spec\n(.*?)\n```", re.DOTALL)


def _iter_files(path: Path):
    if path.is_file():
        if path.suffix == ".md":
            yield path
        return
    if path.is_dir():
        for p in sorted(path.rglob("*.md")):
            if p.is_file():
                yield p


def _rewrite(text: str) -> tuple[str, bool]:
    out: list[str] = []
    last = 0
    changed = False
    for m in _FENCE_RE.finditer(text):
        out.append(text[last : m.start(1)])
        block = m.group(1)
        try:
            case = yaml.safe_load(block)
        except Exception:
            out.append(block)
            last = m.end(1)
            continue
        if not isinstance(case, dict) or str(case.get("type", "")).strip() != "spec_lang.export":
            out.append(block)
            last = m.end(1)
            continue
        defines = case.get("defines")
        public = defines.get("public") if isinstance(defines, dict) else None
        if not isinstance(public, dict) or not public:
            out.append(block)
            last = m.end(1)
            continue
        harness = case.get("harness")
        if not isinstance(harness, dict):
            harness = {}
            case["harness"] = harness
        chain = harness.get("chain")
        if not isinstance(chain, dict):
            chain = {}
            harness["chain"] = chain
        exports = chain.get("exports")
        if not isinstance(exports, list):
            exports = []
            chain["exports"] = exports
        seen = {str(x.get("as", "")).strip() for x in exports if isinstance(x, dict)}
        local_changed = False
        for symbol in public.keys():
            name = str(symbol).strip()
            if not name or name in seen:
                continue
            exports.append(
                {
                    "as": name,
                    "from": "assert.function",
                    "path": f"/{name}",
                    "required": True,
                }
            )
            seen.add(name)
            local_changed = True
        if local_changed:
            changed = True
            out.append(yaml.safe_dump(case, sort_keys=False).rstrip("\n"))
        else:
            out.append(block)
        last = m.end(1)
    out.append(text[last:])
    return "".join(out), changed


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Ensure spec_lang.export cases declare harness.chain.exports for public symbols.")
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    ap.add_argument("paths", nargs="+")
    ns = ap.parse_args(argv)

    changed: list[Path] = []
    for raw in ns.paths:
        for f in _iter_files(Path(raw)):
            original = f.read_text(encoding="utf-8")
            updated, touched = _rewrite(original)
            if touched:
                changed.append(f)
                if ns.write:
                    f.write_text(updated, encoding="utf-8")

    if ns.check:
        if changed:
            for f in changed:
                print(f"{f.as_posix()}: library chain export drift")
            return 1
        print("OK: library chain exports are canonical")
        return 0
    print(f"OK: rewrote {len(changed)} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
