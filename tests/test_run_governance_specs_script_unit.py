# SPEC-OPT-OUT: Exercises script wiring and governance harness behavior not yet representable as stable .spec.md coverage.
import importlib.util
from pathlib import Path


def _load_script_module():
    repo_root = Path(__file__).resolve().parents[1]
    script_path = repo_root / "scripts/run_governance_specs.py"
    spec = importlib.util.spec_from_file_location("run_governance_specs_script", script_path)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _governance_case(root: Path) -> str:
    return f"""# Governance

## SRGOV-TEST-001

```yaml spec-test
id: SRGOV-TEST-001
type: governance.check
check: pending.no_resolved_markers
harness:
  root: {root}
assert:
  - target: text
    must:
      - contain: ["PASS: pending.no_resolved_markers"]
```
"""


def test_script_returns_zero_when_governance_case_passes(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(cases_dir / "governance.spec.md", _governance_case(tmp_path))
    (tmp_path / "docs/spec/pending").mkdir(parents=True, exist_ok=True)

    code = mod.main(["--cases", str(cases_dir)])
    assert code == 0


def test_script_returns_one_when_pending_has_resolved_marker(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(cases_dir / "governance.spec.md", _governance_case(tmp_path))
    _write_text(
        tmp_path / "docs/spec/pending/sample.md",
        "# sample\n\n- resolved: 2026-02-13\n",
    )

    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1


def test_script_rejects_empty_case_pattern(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    cases_dir.mkdir(parents=True, exist_ok=True)

    code = mod.main(["--cases", str(cases_dir), "--case-file-pattern", ""])
    assert code == 2
