# SPEC-OPT-OUT: Verifies codemod behavior for executable includes-to-chain migration.
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from spec_runner.codecs import load_external_cases


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def test_migrate_includes_to_chain_symbols(tmp_path: Path) -> None:
    _write(
        tmp_path / "docs/spec/libraries/domain/lib.spec.md",
        """# Lib
```yaml spec-test
id: LIB-1
type: spec_lang.library
defines:
  public:
    dom.fn:
      fn:
      - [x]
      - {var: x}
```
""",
    )
    f = tmp_path / "docs/spec/conformance/cases/core/case.spec.md"
    _write(
        f,
        """# Case
```yaml spec-test
id: C1
type: text.file
harness:
  spec_lang:
    includes:
      - /docs/spec/libraries/domain/lib.spec.md
assert:
  - target: text
    must:
      - call:
          - {var: dom.fn}
          - {var: subject}
```
""",
    )
    cp = subprocess.run(
        [sys.executable, "scripts/migrate_includes_to_chain_symbols.py", "--write", str(tmp_path / "docs/spec")],
        text=True,
        capture_output=True,
        check=False,
        cwd=Path(__file__).resolve().parents[1],
    )
    assert cp.returncode == 0
    loaded = list(load_external_cases(f, formats={"md"}))
    case = loaded[0][1]
    harness = case.get("harness") or {}
    assert "spec_lang" not in harness or "includes" not in (harness.get("spec_lang") or {})
    chain = harness.get("chain")
    assert isinstance(chain, dict)
    assert isinstance(chain.get("steps"), list) and chain.get("steps")
    assert isinstance(chain.get("imports"), list) and chain.get("imports")
