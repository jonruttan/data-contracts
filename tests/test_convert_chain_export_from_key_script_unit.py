# SPEC-OPT-OUT: Verifies codemod check/write behavior for chain export key rewrite.
from __future__ import annotations

import subprocess
from pathlib import Path


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def test_convert_chain_export_from_key_check_and_write(tmp_path: Path) -> None:
    f = tmp_path / "x.spec.md"
    _write(
        f,
        """# X
```yaml spec-test
id: C1
type: text.file
harness:
  chain:
    steps:
    - id: s1
      class: must
      ref: /a.spec.md#A
      exports:
        x:
          from_target: text
assert: []
```
""",
    )
    cp = subprocess.run(
        ["./.venv/bin/python", "scripts/convert_chain_export_from_key.py", "--check", str(f)],
        text=True,
        capture_output=True,
        check=False,
    )
    assert cp.returncode == 1
    cp = subprocess.run(
        ["./.venv/bin/python", "scripts/convert_chain_export_from_key.py", "--write", str(f)],
        text=True,
        capture_output=True,
        check=False,
    )
    assert cp.returncode == 0
    assert "from_target" not in f.read_text(encoding="utf-8")
    assert "from:" in f.read_text(encoding="utf-8")

