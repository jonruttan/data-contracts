# SPEC-OPT-OUT: Script IO/report-shape verification for migration inventory reporting.
from __future__ import annotations

import importlib.util
import json
from pathlib import Path


def _load_module():
    repo_root = Path(__file__).resolve().parents[1]
    script_path = repo_root / "scripts/report_impl_evaluate_migration.py"
    spec = importlib.util.spec_from_file_location("impl_evaluate_migration_report_script", script_path)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def test_report_impl_evaluate_migration_outputs_expected_summary(tmp_path: Path) -> None:
    mod = _load_module()
    cases_dir = tmp_path / "docs/spec/impl"
    _write(
        cases_dir / "a.spec.md",
        """# Impl

## CASE-1

```yaml contract-spec
id: CASE-1
type: text.file
assert:
- target: text
  must:
  - contain:
    - token
```
""",
    )
    _write(
        cases_dir / "b.spec.md",
        """# Impl

## CASE-2

```yaml contract-spec
id: CASE-2
type: text.file
assert:
- target: text
  must:
  - contains:
      - {var: subject}
      - token
```
""",
    )
    out_json = tmp_path / "impl-migration.json"
    out_md = tmp_path / "impl-migration.md"
    code = mod.main(
        [
            "--cases",
            str(cases_dir),
            "--out-json",
            str(out_json),
            "--out-md",
            str(out_md),
        ]
    )
    assert code == 0
    payload = json.loads(out_json.read_text(encoding="utf-8"))
    assert payload["summary"]["total_cases"] == 2
    assert payload["summary"]["classification_counts"]["already_evaluate_primary"] == 2
    assert "convertible_now_simple" not in payload["summary"]["classification_counts"]
    assert "Impl Evaluate Migration" in out_md.read_text(encoding="utf-8")
