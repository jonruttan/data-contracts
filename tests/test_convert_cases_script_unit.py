# SPEC-OPT-OUT: Script wiring/IO behavior for format conversion utility.
from __future__ import annotations

import importlib.util
import json
from pathlib import Path


def _load_module():
    path = Path(__file__).resolve().parents[1] / "scripts/convert_cases.py"
    spec = importlib.util.spec_from_file_location("convert_cases_script", path)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_convert_md_to_json(tmp_path: Path) -> None:
    mod = _load_module()
    src = tmp_path / "a.spec.md"
    src.write_text(
        """```yaml contract-spec
id: C1
type: text.file
assert:
  - target: text
    must:
      - contain: [\"ok\"]
```
""",
        encoding="utf-8",
    )
    out = tmp_path / "out.spec.json"
    code = mod.main(["--in", str(src), "--out", str(out), "--out-format", "json", "--formats", "md"])
    assert code == 0
    payload = json.loads(out.read_text(encoding="utf-8"))
    assert payload["id"] == "C1"


def test_convert_yaml_to_md(tmp_path: Path) -> None:
    mod = _load_module()
    src = tmp_path / "b.spec.yaml"
    src.write_text("id: C2\ntype: text.file\n", encoding="utf-8")
    out = tmp_path / "out.spec.md"
    code = mod.main(["--in", str(src), "--out", str(out), "--out-format", "md", "--formats", "yaml"])
    assert code == 0
    text = out.read_text(encoding="utf-8")
    assert "```yaml contract-spec" in text
    assert "id: C2" in text
