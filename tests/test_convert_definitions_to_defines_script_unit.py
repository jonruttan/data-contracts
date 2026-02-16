# SPEC-OPT-OUT: Verifies codemod check/write behavior and idempotence for library key migration.
from __future__ import annotations

from pathlib import Path
import subprocess
import sys


def test_convert_definitions_to_defines_write_and_check(tmp_path: Path) -> None:
    p = tmp_path / "library.spec.md"
    p.write_text(
        """# Sample

```yaml spec-test
id: LIB-1
type: spec_lang.library
definitions:
  public:
    keep:
      fn:
      - [x]
      - {var: x}
```
""",
        encoding="utf-8",
    )

    cp = subprocess.run(
        [sys.executable, "scripts/convert_definitions_to_defines.py", "--write", str(tmp_path)],
        cwd=Path(__file__).resolve().parents[1],
        capture_output=True,
        text=True,
        check=False,
    )
    assert cp.returncode == 0, cp.stdout + cp.stderr
    text = p.read_text(encoding="utf-8")
    assert "defines:" in text
    assert "definitions:" not in text

    cp2 = subprocess.run(
        [sys.executable, "scripts/convert_definitions_to_defines.py", "--check", str(tmp_path)],
        cwd=Path(__file__).resolve().parents[1],
        capture_output=True,
        text=True,
        check=False,
    )
    assert cp2.returncode == 0, cp2.stdout + cp2.stderr


def test_convert_definitions_to_defines_check_fails_on_legacy(tmp_path: Path) -> None:
    p = tmp_path / "library.spec.md"
    p.write_text(
        """```yaml spec-test
id: LIB-2
type: spec_lang.library
definitions:
  private:
    helper:
      fn:
      - [x]
      - {var: x}
```
""",
        encoding="utf-8",
    )

    cp = subprocess.run(
        [sys.executable, "scripts/convert_definitions_to_defines.py", "--check", str(tmp_path)],
        cwd=Path(__file__).resolve().parents[1],
        capture_output=True,
        text=True,
        check=False,
    )
    assert cp.returncode == 1
    assert "definitions->defines drift" in (cp.stdout + cp.stderr)
