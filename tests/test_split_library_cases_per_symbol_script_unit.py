# SPEC-OPT-OUT: Verifies codemod split behavior for library case public-symbol granularity.
from __future__ import annotations

import subprocess
from pathlib import Path

from spec_runner.codecs import load_external_cases


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def test_split_library_cases_per_symbol(tmp_path: Path) -> None:
    f = tmp_path / "lib.spec.md"
    _write(
        f,
        """# Lib
```yaml spec-test
id: LIB-1
type: spec_lang.library
defines:
  public:
    a:
      fn:
      - [x]
      - {var: x}
    b:
      fn:
      - [x]
      - {var: x}
  private:
    helper:
      fn:
      - [x]
      - {var: x}
```
""",
    )
    cp = subprocess.run(
        ["./.venv/bin/python", "scripts/split_library_cases_per_symbol.py", "--write", str(f)],
        text=True,
        capture_output=True,
        check=False,
    )
    assert cp.returncode == 0
    loaded = list(load_external_cases(f, formats={"md"}))
    libs = [case for _, case in loaded if str(case.get("type", "")).strip() == "spec_lang.library"]
    assert len(libs) == 2
    for case in libs:
        public = ((case.get("defines") or {}).get("public") or {})
        assert isinstance(public, dict)
        assert len(public) == 1

