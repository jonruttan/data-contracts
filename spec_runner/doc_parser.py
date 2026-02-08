import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterator

import yaml


@dataclass(frozen=True)
class SpecDocTest:
    doc_path: Path
    test: dict[str, Any]


_FENCE_RE = re.compile(r"```yaml\s+spec-test\s*\n(.*?)\n```", re.DOTALL)


def iter_spec_doc_tests(spec_dir: Path) -> Iterator[SpecDocTest]:
    for p in sorted(spec_dir.glob("*.md")):
        raw = p.read_text(encoding="utf-8")
        for m in _FENCE_RE.finditer(raw):
            block = m.group(1)
            payload = yaml.safe_load(block) or {}
            if isinstance(payload, dict):
                tests = [payload]
            elif isinstance(payload, list):
                tests = payload
            else:
                raise TypeError(f"spec-test block in {p} must be a mapping or a list of mappings")

            for t in tests:
                if not isinstance(t, dict):
                    raise TypeError(f"spec-test block in {p} contains a non-mapping test")
                if "id" not in t or "kind" not in t:
                    raise ValueError(f"spec-test in {p} must include 'id' and 'kind'")
                yield SpecDocTest(doc_path=p, test=t)
