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


def _case_for_check(case_id: str, check: str, root: Path) -> str:
    return f"""# Governance

## {case_id}

```yaml spec-test
id: {case_id}
type: governance.check
check: {check}
harness:
  root: {root}
assert:
  - target: text
    must:
      - contain: ["PASS: {check}"]
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


def test_script_enforces_security_warning_doc_tokens(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "security.spec.md",
        _case_for_check("SRGOV-TEST-SEC-001", "docs.security_warning_contract", tmp_path),
    )
    _write_text(tmp_path / "README.md", "trusted inputs\nnot a sandbox\nuntrusted spec\n")
    _write_text(tmp_path / "docs/book/00_first_10_minutes.md", "trusted inputs\nnot a sandbox\nuntrusted spec\n")
    _write_text(tmp_path / "docs/spec/schema/schema_v1.md", "trusted inputs\nnot a sandbox\nuntrusted spec\n")

    code = mod.main(["--cases", str(cases_dir)])
    assert code == 0

    _write_text(tmp_path / "docs/spec/schema/schema_v1.md", "trusted inputs only\n")
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1


def test_script_enforces_v1_scope_doc_tokens(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "v1scope.spec.md",
        _case_for_check("SRGOV-TEST-V1-001", "docs.v1_scope_contract", tmp_path),
    )
    _write_text(
        tmp_path / "docs/spec/contract/08_v1_scope.md",
        "# V1 In Scope\n\n## V1 In Scope\n\n## V1 Non-Goals\n\n## Compatibility Commitments (v1)\n\n- Current-spec-only rule\n",
    )

    code = mod.main(["--cases", str(cases_dir)])
    assert code == 0

    _write_text(tmp_path / "docs/spec/contract/08_v1_scope.md", "# scope\n")
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1


def test_script_enforces_current_spec_only_contract(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "current_spec_only.spec.md",
        _case_for_check("SRGOV-TEST-CURRENT-001", "docs.current_spec_only_contract", tmp_path),
    )
    _write_text(
        tmp_path / "docs/spec/schema/schema_v1.md",
        "# Schema v1\n\n- type is required.\n",
    )
    _write_text(
        tmp_path / "spec_runner/doc_parser.py",
        "def parse_case(payload):\n    return payload.get('type')\n",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 0

    _write_text(
        tmp_path / "docs/spec/schema/schema_v1.md",
        "# Schema v1\n\n- legacy note\n",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1


def test_script_enforces_runtime_config_literal_policy(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "runtime_literals.spec.md",
        _case_for_check("SRGOV-TEST-RUNTIME-CONFIG-001", "runtime.config_literals", tmp_path),
    )
    (tmp_path / "spec_runner").mkdir(parents=True, exist_ok=True)
    _write_text(
        tmp_path / "spec_runner/settings.py",
        """DEFAULT_CASE_FILE_PATTERN = "*.spec.md"
ENV_ASSERT_HEALTH = "SPEC_RUNNER_ASSERT_HEALTH"
ENV_ENTRYPOINT = "SPEC_RUNNER_ENTRYPOINT"
ENV_SAFE_MODE = "SPEC_RUNNER_SAFE_MODE"
ENV_ENV_ALLOWLIST = "SPEC_RUNNER_ENV_ALLOWLIST"

def governed_config_literals():
    return {
        DEFAULT_CASE_FILE_PATTERN: "SETTINGS.case.default_file_pattern",
        ENV_ASSERT_HEALTH: "SETTINGS.env.assert_health",
        ENV_ENTRYPOINT: "SETTINGS.env.entrypoint",
        ENV_SAFE_MODE: "SETTINGS.env.safe_mode",
        ENV_ENV_ALLOWLIST: "SETTINGS.env.env_allowlist",
    }
""",
    )
    _write_text(
        tmp_path / "spec_runner/good.py",
        "from spec_runner.settings import SETTINGS\n"
        "CASE_PATTERN = SETTINGS.case.default_file_pattern\n",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 0

    _write_text(tmp_path / "spec_runner/bad.py", 'PATTERN = "*.spec.md"\n')
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1


def test_script_enforces_runtime_settings_import_policy(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "runtime_imports.spec.md",
        _case_for_check("SRGOV-TEST-RUNTIME-IMPORT-001", "runtime.settings_import_policy", tmp_path),
    )
    (tmp_path / "spec_runner").mkdir(parents=True, exist_ok=True)
    _write_text(tmp_path / "spec_runner/good.py", "from spec_runner.settings import SETTINGS\n")
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 0

    _write_text(
        tmp_path / "spec_runner/bad_import.py",
        "from spec_runner.settings import DEFAULT_CASE_FILE_PATTERN\n",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1


def test_script_enforces_conformance_case_index_sync(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "index_sync.spec.md",
        _case_for_check("SRGOV-TEST-CONF-INDEX-001", "conformance.case_index_sync", tmp_path),
    )
    _write_text(
        tmp_path / "docs/spec/conformance/cases/sample.spec.md",
        """# Sample

## SRCONF-IDX-001

```yaml spec-test
id: SRCONF-IDX-001
type: text.file
assert:
  - target: text
    must:
      - contain: ["SRCONF-IDX-001"]
```
""",
    )
    _write_text(tmp_path / "docs/spec/conformance/cases/README.md", "# Cases\n\n- SRCONF-IDX-001\n")
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 0

    _write_text(tmp_path / "docs/spec/conformance/cases/README.md", "# Cases\n\n- SRCONF-STALE-999\n")
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1


def test_script_enforces_conformance_type_contract_docs(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "type_contracts.spec.md",
        _case_for_check("SRGOV-TEST-CONF-TYPE-001", "conformance.type_contract_docs", tmp_path),
    )
    _write_text(
        tmp_path / "docs/spec/conformance/cases/sample.spec.md",
        """# Sample

## SRCONF-TYPE-001

```yaml spec-test
id: SRCONF-TYPE-001
type: text.file
assert:
  - target: text
    must:
      - contain: ["SRCONF-TYPE-001"]
```
""",
    )
    _write_text(
        tmp_path / "docs/spec/contract/types/text_file.md",
        "# Type Contract: text.file\n",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 0

    _write_text(
        tmp_path / "docs/spec/contract/types/text_file.md",
        "# Wrong Heading\n",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1


def test_script_enforces_conformance_api_http_portable_shape(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "api_shape.spec.md",
        _case_for_check("SRGOV-TEST-CONF-API-001", "conformance.api_http_portable_shape", tmp_path),
    )
    _write_text(
        tmp_path / "docs/spec/conformance/cases/api_ok.spec.md",
        """# API

## SRCONF-API-001

```yaml spec-test
id: SRCONF-API-001
type: api.http
request:
  method: GET
  url: https://example.test/v1/ping
assert:
  - target: status
    must:
      - contain: ["200"]
```
""",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 0

    _write_text(
        tmp_path / "docs/spec/conformance/cases/api_bad.spec.md",
        """# API Bad

## SRCONF-API-002

```yaml spec-test
id: SRCONF-API-002
type: api.http
method: GET
request:
  method: GET
  url: https://example.test/v1/ping
assert:
  - target: stdout
    must:
      - contain: ["200"]
```
""",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1


def test_script_enforces_conformance_purpose_warning_code_sync(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "purpose_sync.spec.md",
        _case_for_check(
            "SRGOV-TEST-CONF-PURPOSE-001",
            "conformance.purpose_warning_codes_sync",
            tmp_path,
        ),
    )
    _write_text(
        tmp_path / "docs/spec/conformance/purpose_warning_codes.md",
        "# Purpose Warning Codes\n\n- PUR001\n- PUR002\n- PUR003\n- PUR004\n",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 0

    _write_text(
        tmp_path / "docs/spec/conformance/purpose_warning_codes.md",
        "# Purpose Warning Codes\n\n- PUR001\n- PUR002\n- PUR003\n",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1


def test_script_enforces_conformance_case_doc_style_guard(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "style_guard.spec.md",
        _case_for_check("SRGOV-TEST-CONF-STYLE-001", "conformance.case_doc_style_guard", tmp_path),
    )
    _write_text(
        tmp_path / "docs/spec/conformance/cases/good.spec.md",
        """# Good

## SRCONF-STYLE-001

```yaml spec-test
id: SRCONF-STYLE-001
title: good style case
purpose: Purpose text with enough words to satisfy quality checks here.
type: text.file
expect:
  portable:
    status: pass
    category: null
```
""",
    )
    _write_text(tmp_path / "docs/spec/conformance/cases/README.md", "# Cases\n\n- SRCONF-STYLE-001\n")
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 0

    _write_text(
        tmp_path / "docs/spec/conformance/cases/bad.spec.md",
        """# Bad

## SRCONF-STYLE-002

```yaml spec-test
- id: SRCONF-STYLE-002
  type: text.file
  expect:
    portable: {status: pass, category: null}
```
""",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1


def test_script_enforces_regex_doc_sync(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "regex_sync.spec.md",
        _case_for_check("SRGOV-TEST-DOC-REGEX-001", "docs.regex_doc_sync", tmp_path),
    )
    _write_text(
        tmp_path / "docs/spec/contract/03_assertions.md",
        "contain regex docs/spec/contract/03a_regex_portability_v1.md\n",
    )
    _write_text(
        tmp_path / "docs/spec/schema/schema_v1.md",
        "contain regex docs/spec/contract/03a_regex_portability_v1.md\n",
    )
    _write_text(
        tmp_path / "docs/spec/contract/policy_v1.yaml",
        "rules: []\n# docs/spec/contract/03a_regex_portability_v1.md\n",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 0

    _write_text(tmp_path / "docs/spec/contract/03_assertions.md", "contain regex\n")
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1
