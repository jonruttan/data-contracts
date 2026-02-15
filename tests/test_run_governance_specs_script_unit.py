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


def test_script_enforces_runtime_python_bin_resolver_sync(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "runtime_python_bin.spec.md",
        f"""# Governance

## SRGOV-TEST-RUNTIME-CONFIG-002

```yaml spec-test
id: SRGOV-TEST-RUNTIME-CONFIG-002
type: governance.check
check: runtime.python_bin_resolver_sync
harness:
  root: {tmp_path}
  python_bin_resolver:
    helper: scripts/lib/python_bin.sh
    files:
      - scripts/ci_gate.sh
    required_tokens:
      - source "${{ROOT_DIR}}/scripts/lib/python_bin.sh"
      - resolve_python_bin "${{ROOT_DIR}}"
    forbidden_tokens:
      - ROOT_DIR}}/.venv/bin/python
assert:
  - target: text
    must:
      - contain: ["PASS: runtime.python_bin_resolver_sync"]
```
""",
    )
    _write_text(
        tmp_path / "scripts/lib/python_bin.sh",
        "resolve_python_bin() {\n  printf '%s\\n' \"python3\"\n}\n",
    )
    _write_text(
        tmp_path / "scripts/ci_gate.sh",
        "source \"${ROOT_DIR}/scripts/lib/python_bin.sh\"\n"
        "PYTHON_BIN=\"$(resolve_python_bin \"${ROOT_DIR}\")\"\n",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 0

    _write_text(
        tmp_path / "scripts/ci_gate.sh",
        "PYTHON_BIN=\"${ROOT_DIR}/.venv/bin/python\"\n",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1


def test_script_enforces_runtime_runner_interface_gate_sync(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "runtime_runner_interface.spec.md",
        f"""# Governance

## SRGOV-TEST-RUNTIME-CONFIG-003

```yaml spec-test
id: SRGOV-TEST-RUNTIME-CONFIG-003
type: governance.check
check: runtime.runner_interface_gate_sync
harness:
  root: {tmp_path}
  runner_interface:
    required_paths:
      - scripts/runner_adapter.sh
    files:
      - scripts/ci_gate.sh
    required_tokens:
      - SPEC_RUNNER_BIN
      - scripts/runner_adapter.sh
    forbidden_tokens:
      - scripts/run_governance_specs.py
assert:
  - target: text
    must:
      - contain: ["PASS: runtime.runner_interface_gate_sync"]
```
""",
    )
    _write_text(tmp_path / "scripts/runner_adapter.sh", "#!/usr/bin/env bash\n")
    _write_text(
        tmp_path / "scripts/ci_gate.sh",
        "SPEC_RUNNER_BIN=\"${ROOT_DIR}/scripts/runner_adapter.sh\"\n"
        "\"${SPEC_RUNNER_BIN}\" governance\n",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 0

    _write_text(
        tmp_path / "scripts/ci_gate.sh",
        "python scripts/run_governance_specs.py\n",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1


def test_script_enforces_runtime_scope_sync(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "runtime_scope.spec.md",
        f"""# Governance

## SRGOV-TEST-RUNTIME-SCOPE-001

```yaml spec-test
id: SRGOV-TEST-RUNTIME-SCOPE-001
type: governance.check
check: runtime.scope_sync
harness:
  root: {tmp_path}
  runtime_scope:
    files:
      - docs/spec/contract/08_v1_scope.md
      - docs/spec/contract/13_runtime_scope.md
    required_tokens:
      - Python runner
      - PHP runner
      - required support targets
      - contract/governance expansion
    forbidden_tokens:
      - Node.js runner
assert:
  - target: text
    must:
      - contain: ["PASS: runtime.scope_sync"]
```
""",
    )
    _write_text(
        tmp_path / "docs/spec/contract/08_v1_scope.md",
        "Python runner\nPHP runner\nrequired support targets\ncontract/governance expansion\n",
    )
    _write_text(
        tmp_path / "docs/spec/contract/13_runtime_scope.md",
        "Python runner\nPHP runner\nrequired support targets\ncontract/governance expansion\n",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 0

    _write_text(
        tmp_path / "docs/spec/contract/13_runtime_scope.md",
        "Python runner\nrequired support targets\ncontract/governance expansion\n",
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
        f"""# Governance

## SRGOV-TEST-CONF-API-001

```yaml spec-test
id: SRGOV-TEST-CONF-API-001
type: governance.check
check: conformance.api_http_portable_shape
harness:
  root: {tmp_path}
  api_http:
    allowed_top_level_keys: ["id", "type", "title", "purpose", "request", "assert", "expect", "requires", "assert_health", "harness"]
    allowed_assert_targets: ["status", "headers", "body_text", "body_json"]
    required_request_fields: ["method", "url"]
assert:
  - target: text
    must:
      - contain: ["PASS: conformance.api_http_portable_shape"]
```
""",
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


def test_script_requires_api_http_shape_policy_in_governance_spec(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "api_shape_missing_policy.spec.md",
        _case_for_check("SRGOV-TEST-CONF-API-001-MISS", "conformance.api_http_portable_shape", tmp_path),
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1


def test_script_enforces_conformance_no_runner_logic_outside_harness(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "no_runner_logic.spec.md",
        _case_for_check("SRGOV-TEST-CONF-PORT-001", "conformance.no_runner_logic_outside_harness", tmp_path),
    )
    _write_text(
        tmp_path / "docs/spec/conformance/cases/good.spec.md",
        """# Good

## SRCONF-PORT-001

```yaml spec-test
id: SRCONF-PORT-001
type: cli.run
argv: ["--help"]
exit_code: 0
harness:
  entrypoint: /bin/echo
assert:
  - target: stdout
    must:
      - contain: ["--help"]
```
""",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 0

    _write_text(
        tmp_path / "docs/spec/conformance/cases/bad.spec.md",
        """# Bad

## SRCONF-PORT-002

```yaml spec-test
id: SRCONF-PORT-002
type: cli.run
argv: ["--help"]
exit_code: 0
entrypoint: /bin/echo
assert:
  - target: stdout
    must:
      - contain: ["--help"]
```
""",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1


def test_script_enforces_conformance_portable_determinism_guard(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "determinism.spec.md",
        f"""# Governance

## SRGOV-TEST-CONF-PORT-002

```yaml spec-test
id: SRGOV-TEST-CONF-PORT-002
type: governance.check
check: conformance.portable_determinism_guard
harness:
  root: {tmp_path}
  determinism:
    exclude_case_keys: ["id", "title", "purpose", "expect", "requires", "assert_health"]
    patterns:
      - "\\\\bdatetime\\\\.now\\\\s*\\\\("
      - "\\\\bdatetime\\\\.utcnow\\\\s*\\\\("
      - "\\\\btime\\\\.time\\\\s*\\\\("
      - "\\\\bdate\\\\.today\\\\s*\\\\("
      - "\\\\bDate\\\\.now\\\\s*\\\\("
      - "\\\\bnew\\\\s+Date\\\\s*\\\\("
      - "\\\\brandom\\\\."
      - "\\\\brand(?:int|range)?\\\\s*\\\\("
      - "\\\\bMath\\\\.random\\\\s*\\\\("
    policy_evaluate:
      - ["eq",
         ["count",
          ["filter",
           ["fn", ["row"],
            ["gt",
             ["count",
              ["filter",
               ["fn", ["s"],
                ["any",
                 ["map",
                  ["fn", ["p"], ["matches", ["var", "s"], ["var", "p"]]],
                  ["var", "patterns"]]]],
               ["get", ["var", "row"], "strings"]]],
             0]],
           ["subject"]]],
         0]
assert:
  - target: text
    must:
      - contain: ["PASS: conformance.portable_determinism_guard"]
```
""",
    )
    _write_text(
        tmp_path / "docs/spec/conformance/cases/good.spec.md",
        """# Good

## SRCONF-PORT-003

```yaml spec-test
id: SRCONF-PORT-003
type: text.file
assert:
  - target: text
    must:
      - contain: ["fixed-value"]
```
""",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 0

    _write_text(
        tmp_path / "docs/spec/conformance/cases/bad.spec.md",
        """# Bad

## SRCONF-PORT-004

```yaml spec-test
id: SRCONF-PORT-004
type: text.file
assert:
  - target: text
    must:
      - contain: ["datetime.now()"]
```
""",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1


def test_script_requires_determinism_patterns_in_governance_spec(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "determinism_missing_patterns.spec.md",
        f"""# Governance

## SRGOV-TEST-CONF-PORT-002-MISS

```yaml spec-test
id: SRGOV-TEST-CONF-PORT-002-MISS
type: governance.check
check: conformance.portable_determinism_guard
harness:
  root: {tmp_path}
assert:
  - target: text
    must:
      - contain: ["PASS: conformance.portable_determinism_guard"]
```
""",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1


def test_script_enforces_conformance_no_ambient_assumptions(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "ambient_assumptions.spec.md",
        f"""# Governance

## SRGOV-TEST-CONF-PORT-003

```yaml spec-test
id: SRGOV-TEST-CONF-PORT-003
type: governance.check
check: conformance.no_ambient_assumptions
harness:
  root: {tmp_path}
  ambient_assumptions:
    exclude_case_keys: ["id", "title", "purpose", "expect", "requires", "assert_health"]
    patterns:
      - "\\\\bos\\\\.getenv\\\\s*\\\\("
      - "\\\\bdatetime\\\\.now\\\\s*\\\\("
    policy_evaluate:
      - ["eq",
         ["count",
          ["filter",
           ["fn", ["row"],
            ["gt",
             ["count",
              ["filter",
               ["fn", ["s"],
                ["any",
                 ["map",
                  ["fn", ["p"], ["matches", ["var", "s"], ["var", "p"]]],
                  ["var", "patterns"]]]],
               ["get", ["var", "row"], "strings"]]],
             0]],
           ["subject"]]],
         0]
assert:
  - target: text
    must:
      - contain: ["PASS: conformance.no_ambient_assumptions"]
```
""",
    )
    _write_text(
        tmp_path / "docs/spec/conformance/cases/good.spec.md",
        """# Good

## SRCONF-PORT-005

```yaml spec-test
id: SRCONF-PORT-005
type: text.file
assert:
  - target: text
    must:
      - contain: ["fixed-value"]
```
""",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 0

    _write_text(
        tmp_path / "docs/spec/conformance/cases/bad.spec.md",
        """# Bad

## SRCONF-PORT-006

```yaml spec-test
id: SRCONF-PORT-006
type: text.file
assert:
  - target: text
    must:
      - contain: ["os.getenv('HOME')"]
```
""",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1


def test_script_requires_ambient_assumption_patterns_in_governance_spec(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "ambient_missing_patterns.spec.md",
        f"""# Governance

## SRGOV-TEST-CONF-PORT-003-MISS

```yaml spec-test
id: SRGOV-TEST-CONF-PORT-003-MISS
type: governance.check
check: conformance.no_ambient_assumptions
harness:
  root: {tmp_path}
assert:
  - target: text
    must:
      - contain: ["PASS: conformance.no_ambient_assumptions"]
```
""",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1


def test_script_enforces_conformance_extension_requires_capabilities(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "extension_caps.spec.md",
        _case_for_check("SRGOV-TEST-CONF-PORT-003", "conformance.extension_requires_capabilities", tmp_path),
    )
    _write_text(
        tmp_path / "docs/spec/conformance/cases/good.spec.md",
        """# Good

## SRCONF-PORT-005

```yaml spec-test
id: SRCONF-PORT-005
type: api.http
request:
  method: GET
  url: https://example.test/ping
requires:
  capabilities: ["api.http"]
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
        tmp_path / "docs/spec/conformance/cases/bad.spec.md",
        """# Bad

## SRCONF-PORT-006

```yaml spec-test
id: SRCONF-PORT-006
type: api.http
request:
  method: GET
  url: https://example.test/ping
assert:
  - target: status
    must:
      - contain: ["200"]
```
""",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1


def test_script_enforces_conformance_type_contract_field_sync(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "type_field_sync.spec.md",
        _case_for_check("SRGOV-TEST-CONF-PORT-004", "conformance.type_contract_field_sync", tmp_path),
    )
    _write_text(
        tmp_path / "docs/spec/contract/types/text_file.md",
        """# Type Contract: text.file

## Required Fields

- `id`
- `type`
- `assert`

## Optional Fields

- `path`
""",
    )
    _write_text(
        tmp_path / "docs/spec/conformance/cases/good.spec.md",
        """# Good

## SRCONF-PORT-007

```yaml spec-test
id: SRCONF-PORT-007
type: text.file
path: fixtures/a.txt
assert:
  - target: text
    must:
      - contain: ["a"]
```
""",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 0

    _write_text(
        tmp_path / "docs/spec/conformance/cases/bad.spec.md",
        """# Bad

## SRCONF-PORT-008

```yaml spec-test
id: SRCONF-PORT-008
type: text.file
path: fixtures/a.txt
foobar: 1
assert:
  - target: text
    must:
      - contain: ["a"]
```
""",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1


def test_script_enforces_conformance_spec_lang_preferred(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "spec_lang_preferred.spec.md",
        f"""# Governance

## SRGOV-TEST-CONF-SPECLANG-001

```yaml spec-test
id: SRGOV-TEST-CONF-SPECLANG-001
type: governance.check
check: conformance.spec_lang_preferred
harness:
  root: {tmp_path}
  spec_lang_preferred:
    roots:
      - docs/spec/conformance/cases
    allow_non_evaluate_files: []
    policy_evaluate:
      - ["eq",
         ["count",
          ["filter",
           ["fn", ["row"], ["gt", ["count", ["get", ["var", "row"], "non_eval_ops"]], 0]],
           ["subject"]]],
         0]
assert:
  - target: text
    must:
      - contain: ["PASS: conformance.spec_lang_preferred"]
```
""",
    )
    _write_text(
        tmp_path / "docs/spec/conformance/cases/good.spec.md",
        """# Good

## SRCONF-SPECLANG-001

```yaml spec-test
id: SRCONF-SPECLANG-001
type: text.file
path: fixtures/a.txt
assert:
  - target: text
    must:
      - evaluate:
          - ["contains", ["subject"], "a"]
```
""",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 0

    _write_text(
        tmp_path / "docs/spec/conformance/cases/bad.spec.md",
        """# Bad

## SRCONF-SPECLANG-002

```yaml spec-test
id: SRCONF-SPECLANG-002
type: text.file
path: fixtures/a.txt
assert:
  - target: text
    must:
      - contain: ["a"]
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


def test_script_enforces_docs_reference_surface_complete(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "docs_surface.spec.md",
        f"""# Governance

## SRGOV-TEST-DOCS-REF-001

```yaml spec-test
id: SRGOV-TEST-DOCS-REF-001
type: governance.check
check: docs.reference_surface_complete
harness:
  root: {tmp_path}
  docs_reference_surface:
    required_files:
      - docs/book/reference_index.md
      - docs/spec/schema/schema_v1.md
    required_globs:
      - docs/spec/contract/*.md
assert:
  - target: text
    must:
      - contain: ["PASS: docs.reference_surface_complete"]
```
""",
    )
    _write_text(tmp_path / "docs/book/reference_index.md", "# index\n")
    _write_text(tmp_path / "docs/spec/schema/schema_v1.md", "# schema\n")
    _write_text(tmp_path / "docs/spec/contract/03_assertions.md", "# assertions\n")
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 0

    (tmp_path / "docs/spec/schema/schema_v1.md").unlink()
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1


def test_script_enforces_docs_reference_index_sync(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "docs_index.spec.md",
        f"""# Governance

## SRGOV-TEST-DOCS-REF-002

```yaml spec-test
id: SRGOV-TEST-DOCS-REF-002
type: governance.check
check: docs.reference_index_sync
harness:
  root: {tmp_path}
  reference_index:
    path: docs/book/reference_index.md
    include_glob: docs/book/*.md
    exclude_files: ["docs/book/reference_index.md"]
assert:
  - target: text
    must:
      - contain: ["PASS: docs.reference_index_sync"]
```
""",
    )
    _write_text(tmp_path / "docs/book/00_first_10_minutes.md", "# 00\n")
    _write_text(tmp_path / "docs/book/01_quickstart.md", "# 01\n")
    _write_text(
        tmp_path / "docs/book/reference_index.md",
        "1. `docs/book/00_first_10_minutes.md`\n2. `docs/book/01_quickstart.md`\n",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 0

    _write_text(tmp_path / "docs/book/reference_index.md", "1. `docs/book/00_first_10_minutes.md`\n")
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1


def test_script_enforces_docs_examples_runnable(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "docs_examples.spec.md",
        f"""# Governance

## SRGOV-TEST-DOCS-REF-004

```yaml spec-test
id: SRGOV-TEST-DOCS-REF-004
type: governance.check
check: docs.examples_runnable
harness:
  root: {tmp_path}
  docs_examples:
    files: ["docs/book/03_assertions.md"]
assert:
  - target: text
    must:
      - contain: ["PASS: docs.examples_runnable"]
```
""",
    )
    _write_text(
        tmp_path / "docs/book/03_assertions.md",
        """# Assertions

```yaml spec-test
id: T-1
type: text.file
assert:
  - target: text
    must:
      - contain: ["x"]
```

```python
print("ok")
```

```sh
python -m pytest -q
```
""",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 0

    _write_text(
        tmp_path / "docs/book/03_assertions.md",
        """# Assertions

```python
if True print("bad")
```
""",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1

    _write_text(
        tmp_path / "docs/book/03_assertions.md",
        """# Assertions

DOCS-EXAMPLE-OPT-OUT: temporary invalid snippet under rewrite

```python
if True print("bad")
```
""",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 0


def test_script_enforces_docs_required_sections(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "docs_sections.spec.md",
        f"""# Governance

## SRGOV-TEST-DOCS-REF-003

```yaml spec-test
id: SRGOV-TEST-DOCS-REF-003
type: governance.check
check: docs.required_sections
harness:
  root: {tmp_path}
  required_sections:
    docs/book/02_core_model.md: ["## Required Keys", "## Discovery Model"]
assert:
  - target: text
    must:
      - contain: ["PASS: docs.required_sections"]
```
""",
    )
    _write_text(tmp_path / "docs/book/02_core_model.md", "## Required Keys\n## Discovery Model\n")
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 0

    _write_text(tmp_path / "docs/book/02_core_model.md", "## Required Keys\n")
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1


def test_script_enforces_docs_cli_flags_documented(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "docs_cli_flags.spec.md",
        f"""# Governance

## SRGOV-TEST-DOCS-REF-005

```yaml spec-test
id: SRGOV-TEST-DOCS-REF-005
type: governance.check
check: docs.cli_flags_documented
harness:
  root: {tmp_path}
  cli_docs:
    python_scripts: ["scripts/python/conformance_runner.py"]
    php_scripts: ["scripts/php/spec_runner.php"]
    python_docs: ["docs/development.md", "docs/spec/impl/python.md"]
    php_docs: ["docs/development.md", "docs/spec/impl/php.md"]
assert:
  - target: text
    must:
      - contain: ["PASS: docs.cli_flags_documented"]
```
""",
    )
    _write_text(
        tmp_path / "scripts/python/conformance_runner.py",
        "ap.add_argument('--cases')\nap.add_argument('--out')\n",
    )
    _write_text(
        tmp_path / "scripts/php/spec_runner.php",
        "if ($arg === '--cases') {}\nif ($arg === '--out') {}\n",
    )
    _write_text(tmp_path / "docs/development.md", "--cases --out\n")
    _write_text(tmp_path / "docs/spec/impl/python.md", "--cases --out\n")
    _write_text(tmp_path / "docs/spec/impl/php.md", "--cases --out\n")
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 0

    _write_text(tmp_path / "docs/spec/impl/php.md", "--cases\n")
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1


def test_script_enforces_docs_contract_schema_book_sync(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "docs_sync.spec.md",
        f"""# Governance

## SRGOV-TEST-DOCS-REF-006

```yaml spec-test
id: SRGOV-TEST-DOCS-REF-006
type: governance.check
check: docs.contract_schema_book_sync
harness:
  root: {tmp_path}
  doc_sync:
    files:
      - docs/book/03_assertions.md
      - docs/spec/contract/03_assertions.md
      - docs/spec/schema/schema_v1.md
    tokens: ["must", "can", "cannot", "contain", "regex", "evaluate"]
assert:
  - target: text
    must:
      - contain: ["PASS: docs.contract_schema_book_sync"]
```
""",
    )
    _write_text(tmp_path / "docs/book/03_assertions.md", "must can cannot contain regex evaluate\n")
    _write_text(tmp_path / "docs/spec/contract/03_assertions.md", "must can cannot contain regex evaluate\n")
    _write_text(tmp_path / "docs/spec/schema/schema_v1.md", "must can cannot contain regex evaluate\n")
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 0

    _write_text(tmp_path / "docs/spec/schema/schema_v1.md", "must can cannot contain regex\n")
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1


def test_script_docs_examples_opt_out_requires_non_empty_reason(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "docs_examples_optout.spec.md",
        f"""# Governance

## SRGOV-TEST-DOCS-REF-007

```yaml spec-test
id: SRGOV-TEST-DOCS-REF-007
type: governance.check
check: docs.examples_runnable
harness:
  root: {tmp_path}
  docs_examples:
    files: ["docs/book/03_assertions.md"]
assert:
  - target: text
    must:
      - contain: ["PASS: docs.examples_runnable"]
```
""",
    )
    _write_text(
        tmp_path / "docs/book/03_assertions.md",
        """# Assertions

DOCS-EXAMPLE-OPT-OUT:

```python
if True print("bad")
```
""",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1


def test_script_docs_examples_shell_prompt_marker_fails_without_opt_out(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "docs_examples_shell.spec.md",
        f"""# Governance

## SRGOV-TEST-DOCS-REF-008

```yaml spec-test
id: SRGOV-TEST-DOCS-REF-008
type: governance.check
check: docs.examples_runnable
harness:
  root: {tmp_path}
  docs_examples:
    files: ["docs/book/01_quickstart.md"]
assert:
  - target: text
    must:
      - contain: ["PASS: docs.examples_runnable"]
```
""",
    )
    _write_text(
        tmp_path / "docs/book/01_quickstart.md",
        """# Quickstart

```sh
$ python -m pytest -q
```
""",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1


def test_script_docs_reference_index_detects_duplicate_entries(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "docs_index_duplicates.spec.md",
        f"""# Governance

## SRGOV-TEST-DOCS-REF-009

```yaml spec-test
id: SRGOV-TEST-DOCS-REF-009
type: governance.check
check: docs.reference_index_sync
harness:
  root: {tmp_path}
  reference_index:
    path: docs/book/reference_index.md
    include_glob: docs/book/*.md
    exclude_files: ["docs/book/reference_index.md"]
assert:
  - target: text
    must:
      - contain: ["PASS: docs.reference_index_sync"]
```
""",
    )
    _write_text(tmp_path / "docs/book/00_first_10_minutes.md", "# 00\n")
    _write_text(tmp_path / "docs/book/01_quickstart.md", "# 01\n")
    _write_text(
        tmp_path / "docs/book/reference_index.md",
        "1. `docs/book/00_first_10_minutes.md`\n2. `docs/book/00_first_10_minutes.md`\n",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1


def test_script_enforces_runtime_assertions_via_spec_lang(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "runtime_assert_engine.spec.md",
        f"""# Governance

## SRGOV-TEST-RUNTIME-ASSERT-001

```yaml spec-test
id: SRGOV-TEST-RUNTIME-ASSERT-001
type: governance.check
check: runtime.assertions_via_spec_lang
harness:
  root: {tmp_path}
  assert_engine:
    files:
      - path: scripts/php/conformance_runner.php
        required_tokens: ["compileLeafExpr(", "assertLeafPredicate(", "specLangEvalPredicate("]
        forbidden_tokens:
          - "strpos($subject, $v)"
          - "preg_match('/' . str_replace('/', '\\\\/', $v) . '/u', $subject)"
      - path: scripts/php/spec_runner.php
        required_tokens: ["compileLeafExpr(", "assertLeafPredicate(", "specLangEvalPredicate("]
        forbidden_tokens:
          - "strpos($subject, $v)"
          - "preg_match('/' . str_replace('/', '\\\\/', $v) . '/u', $subject)"
      - path: spec_runner/assertions.py
        required_tokens: ["evaluate_internal_assert_tree(", "eval_predicate("]
        forbidden_tokens: ["def assert_text_op("]
      - path: spec_runner/harnesses/text_file.py
        required_tokens: ["evaluate_internal_assert_tree("]
        forbidden_tokens: ["contain assertion failed"]
assert:
  - target: text
    must:
      - contain: ["PASS: runtime.assertions_via_spec_lang"]
```
""",
    )
    _write_text(
        tmp_path / "scripts/php/conformance_runner.php",
        "function evalTextLeaf() { compileLeafExpr('contain','x','text'); assertLeafPredicate('id','assert','text','contain',['contains',['subject'],'x'],'x',[]); specLangEvalPredicate(['contains',['subject'],'x'],'x',[]); }\n",
    )
    _write_text(
        tmp_path / "scripts/php/spec_runner.php",
        "function evalTextLeaf() { compileLeafExpr('contain','x','text'); assertLeafPredicate('id','assert','text','contain',['contains',['subject'],'x'],'x',[]); specLangEvalPredicate(['contains',['subject'],'x'],'x',[]); }\n",
    )
    _write_text(
        tmp_path / "spec_runner/assertions.py",
        "def evaluate_internal_assert_tree():\n    eval_predicate(['contains',['subject'],'x'], subject='x')\n",
    )
    _write_text(
        tmp_path / "spec_runner/harnesses/text_file.py",
        "def run(case, ctx):\n    evaluate_internal_assert_tree(case.assert_tree, case_id=case.id, subject_for_target=lambda t: '', limits=None)\n",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 0

    _write_text(
        tmp_path / "spec_runner/assertions.py",
        "def assert_text_op(subject, op, value):\n    return value in subject\n",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1


def test_script_can_run_contract_governance_check(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "contract.spec.md",
        f"""# Governance

## SRGOV-TEST-CONTRACT-001

```yaml spec-test
id: SRGOV-TEST-CONTRACT-001
type: governance.check
check: contract.governance_check
harness:
  root: {tmp_path}
assert:
  - target: text
    must:
      - contain: ["PASS: contract.governance_check"]
```
""",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1


def test_script_enforces_conformance_purpose_quality_gate(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "purpose_quality.spec.md",
        f"""# Governance

## SRGOV-TEST-CONF-PURPOSE-002

```yaml spec-test
id: SRGOV-TEST-CONF-PURPOSE-002
type: governance.check
check: conformance.purpose_quality_gate
harness:
  root: {tmp_path}
  purpose_quality:
    cases: docs/spec/conformance/cases
    max_total_warnings: 0
    fail_on_policy_errors: true
    fail_on_severity: warn
assert:
  - target: text
    must:
      - contain: ["PASS: conformance.purpose_quality_gate"]
```
""",
    )
    _write_text(
        tmp_path / "docs/spec/conformance/cases/sample.spec.md",
        """# Sample

## SRCONF-PURPOSE-001

```yaml spec-test
id: SRCONF-PURPOSE-001
title: stable purpose sentence for quality checks
purpose: This purpose sentence provides concrete deterministic intent for this case.
type: text.file
assert:
  - target: text
    must:
      - contain: ["ok"]
```
""",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 0

    _write_text(
        tmp_path / "docs/spec/conformance/cases/sample.spec.md",
        """# Sample

## SRCONF-PURPOSE-001

```yaml spec-test
id: SRCONF-PURPOSE-001
title: stable purpose sentence for quality checks
purpose: short words only
type: text.file
assert:
  - target: text
    must:
      - contain: ["ok"]
```
""",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1


def test_script_enforces_conformance_purpose_quality_gate_severity_threshold(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "purpose_quality_severity.spec.md",
        f"""# Governance

## SRGOV-TEST-CONF-PURPOSE-003

```yaml spec-test
id: SRGOV-TEST-CONF-PURPOSE-003
type: governance.check
check: conformance.purpose_quality_gate
harness:
  root: {tmp_path}
  purpose_quality:
    cases: docs/spec/conformance/cases
    max_total_warnings: 10
    fail_on_policy_errors: true
    fail_on_severity: warn
assert:
  - target: text
    must:
      - contain: ["PASS: conformance.purpose_quality_gate"]
```
""",
    )
    _write_text(
        tmp_path / "docs/spec/conformance/cases/sample.spec.md",
        """# Sample

## SRCONF-PURPOSE-002

```yaml spec-test
id: SRCONF-PURPOSE-002
title: short purpose title
purpose: too short
type: text.file
assert:
  - target: text
    must:
      - contain: ["ok"]
```
""",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1


def test_script_enforces_contract_coverage_threshold(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "coverage_threshold.spec.md",
        f"""# Governance

## SRGOV-TEST-CONTRACT-002

```yaml spec-test
id: SRGOV-TEST-CONTRACT-002
type: governance.check
check: contract.coverage_threshold
harness:
  root: {tmp_path}
  contract_coverage:
    require_all_must_covered: true
    min_coverage_ratio: 0.50
assert:
  - target: text
    must:
      - contain: ["PASS: contract.coverage_threshold"]
```
""",
    )

    (tmp_path / "docs/spec/contract").mkdir(parents=True, exist_ok=True)
    (tmp_path / "docs/spec/schema").mkdir(parents=True, exist_ok=True)
    (tmp_path / "docs/spec/conformance/cases").mkdir(parents=True, exist_ok=True)
    _write_text(tmp_path / "docs/spec/schema/schema_v1.md", "# schema\n")
    _write_text(
        tmp_path / "docs/spec/contract/policy_v1.yaml",
        """version: 1
rules:
  - id: R-MUST-001
    introduced_in: v1
    scope: governance
    applies_to: docs
    norm: MUST
    requirement: x
    rationale: x
    risk_if_violated: x
    references:
      - docs/spec/schema/schema_v1.md
""",
    )
    _write_text(
        tmp_path / "docs/spec/contract/traceability_v1.yaml",
        """version: 1
links:
  - rule_id: R-MUST-001
    policy_ref: docs/spec/contract/policy_v1.yaml#R-MUST-001
    contract_refs: []
    schema_refs:
      - docs/spec/schema/schema_v1.md
    conformance_case_ids: []
    unit_test_refs:
      - tests/test_run_governance_specs_script_unit.py
    implementation_refs: []
""",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 0

    _write_text(
        tmp_path / "docs/spec/contract/traceability_v1.yaml",
        """version: 1
links:
  - rule_id: R-MUST-001
    policy_ref: docs/spec/contract/policy_v1.yaml#R-MUST-001
    contract_refs: []
    schema_refs:
      - docs/spec/schema/schema_v1.md
    conformance_case_ids: []
    unit_test_refs: []
    implementation_refs: []
""",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1


def test_script_enforces_docs_make_commands_sync(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "docs_make_commands.spec.md",
        f"""# Governance

## SRGOV-TEST-DOCS-REF-007

```yaml spec-test
id: SRGOV-TEST-DOCS-REF-007
type: governance.check
check: docs.make_commands_sync
harness:
  root: {tmp_path}
  make_commands:
    files:
      - README.md
      - docs/development.md
    required_tokens:
      - make verify-docs
      - make core-check
      - make check
assert:
  - target: text
    must:
      - contain: ["PASS: docs.make_commands_sync"]
```
""",
    )
    _write_text(tmp_path / "README.md", "make verify-docs\nmake core-check\nmake check\n")
    _write_text(tmp_path / "docs/development.md", "make verify-docs\nmake core-check\nmake check\n")
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 0

    _write_text(tmp_path / "docs/development.md", "make verify-docs\nmake check\n")
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1


def test_script_enforces_docs_adoption_profiles_sync(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "docs_adoption_profiles.spec.md",
        f"""# Governance

## SRGOV-TEST-DOCS-REF-009

```yaml spec-test
id: SRGOV-TEST-DOCS-REF-009
type: governance.check
check: docs.adoption_profiles_sync
harness:
  root: {tmp_path}
  adoption_profiles:
    files:
      - README.md
      - docs/development.md
    required_tokens:
      - Core profile
      - Full profile
      - make core-check
      - make check
assert:
  - target: text
    must:
      - contain: ["PASS: docs.adoption_profiles_sync"]
```
""",
    )
    _write_text(
        tmp_path / "README.md",
        "Core profile\nFull profile\nmake core-check\nmake check\n",
    )
    _write_text(
        tmp_path / "docs/development.md",
        "Core profile\nFull profile\nmake core-check\nmake check\n",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 0

    _write_text(tmp_path / "docs/development.md", "Core profile\nmake core-check\nmake check\n")
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1


def test_script_enforces_naming_filename_policy(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "naming_filename_policy.spec.md",
        f"""# Governance

## SRGOV-TEST-DOCS-NAME-001

```yaml spec-test
id: SRGOV-TEST-DOCS-NAME-001
type: governance.check
check: naming.filename_policy
harness:
  root: {tmp_path}
  filename_policy:
    paths:
      - docs
    include_extensions:
      - .md
    allow_exact:
      - README.md
    allowed_name_regex: "^[a-z0-9]+(?:[._-][a-z0-9]+)*$"
assert:
  - target: text
    must:
      - contain: ["PASS: naming.filename_policy"]
```
""",
    )
    _write_text(tmp_path / "docs/good_name.md", "# ok\n")
    _write_text(tmp_path / "docs/README.md", "# allowed\n")
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 0

    _write_text(tmp_path / "docs/Bad Name.md", "# bad\n")
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1


def test_script_enforces_spec_portability_metric(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "spec_portability_metric.spec.md",
        f"""# Governance

## SRGOV-TEST-SPEC-PORT-001

```yaml spec-test
id: SRGOV-TEST-SPEC-PORT-001
type: governance.check
check: spec.portability_metric
harness:
  root: {tmp_path}
  portability_metric:
    roots: ["docs/spec/conformance/cases"]
    core_types: ["text.file", "cli.run"]
    segment_rules:
      - prefix: docs/spec/conformance/cases
        segment: conformance
    runtime_capability_tokens: ["api.http"]
    runtime_capability_prefixes: ["runtime."]
    weights:
      non_evaluate_leaf_share: 0.45
      expect_impl_overlay: 0.25
      runtime_specific_capability: 0.15
      non_core_type: 0.15
    report:
      top_n: 5
assert:
  - target: text
    must:
      - contain: ["PASS: spec.portability_metric"]
```
""",
    )
    _write_text(
        tmp_path / "docs/spec/conformance/cases/a.spec.md",
        """# A

## C1

```yaml spec-test
id: C1
type: text.file
assert:
  - target: text
    must:
      - evaluate:
          - ["contains", ["subject"], "x"]
```
""",
    )

    code = mod.main(["--cases", str(cases_dir)])
    assert code == 0



def test_script_rejects_invalid_spec_portability_metric_config(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "spec_portability_metric_bad.spec.md",
        f"""# Governance

## SRGOV-TEST-SPEC-PORT-002

```yaml spec-test
id: SRGOV-TEST-SPEC-PORT-002
type: governance.check
check: spec.portability_metric
harness:
  root: {tmp_path}
  portability_metric:
    roots: ["docs/spec/conformance/cases"]
    core_types: ["text.file", "cli.run"]
    segment_rules:
      - prefix: docs/spec/conformance/cases
        segment: conformance
    runtime_capability_tokens: ["api.http"]
    runtime_capability_prefixes: ["runtime."]
    weights:
      non_evaluate_leaf_share: 0.45
      expect_impl_overlay: 0.25
      runtime_specific_capability: 0.15
      non_core_type: 0.15
    report:
      top_n: 0
assert:
  - target: text
    must:
      - contain: ["PASS: spec.portability_metric"]
```
""",
    )
    _write_text(
        tmp_path / "docs/spec/conformance/cases/a.spec.md",
        """# A

## C1

```yaml spec-test
id: C1
type: text.file
assert: []
```
""",
    )

    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1


def _docs_quality_chapter(doc_id: str, own: str, req: str, ex_id: str) -> str:
    return f"""# Chapter

```yaml doc-meta
doc_id: {doc_id}
title: {doc_id}
status: active
audience: author
owns_tokens: ["{own}"]
requires_tokens: ["{req}"]
commands:
  - run: "./scripts/ci_gate.sh"
    purpose: run gate
examples:
  - id: {ex_id}
    runnable: true
sections_required:
  - "## Purpose"
  - "## Inputs"
  - "## Outputs"
  - "## Failure Modes"
```

## Purpose
x
## Inputs
x
## Outputs
x
## Failure Modes
x
"""


def _seed_docs_quality(tmp_path: Path) -> None:
    _write_text(
        tmp_path / "docs/book/reference_manifest.yaml",
        """version: 1
chapters:
  - path: docs/book/a.md
    summary: A.
  - path: docs/book/b.md
    summary: B.
""",
    )
    _write_text(tmp_path / "docs/book/a.md", _docs_quality_chapter("DOC-REF-001", "tok.a", "tok.b", "EX-A-001"))
    _write_text(tmp_path / "docs/book/b.md", _docs_quality_chapter("DOC-REF-002", "tok.b", "tok.a", "EX-B-001"))


def test_script_enforces_docs_meta_schema_valid(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "docs_meta_schema.spec.md",
        f"""# Governance

## SRGOV-TEST-DOCS-QUAL-001

```yaml spec-test
id: SRGOV-TEST-DOCS-QUAL-001
type: governance.check
check: docs.meta_schema_valid
harness:
  root: {tmp_path}
  docs_quality:
    manifest: docs/book/reference_manifest.yaml
assert:
  - target: text
    must:
      - contain: ["PASS: docs.meta_schema_valid"]
```
""",
    )
    _seed_docs_quality(tmp_path)
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 0

    _write_text(tmp_path / "docs/book/b.md", "# missing meta\n")
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1


def test_script_enforces_docs_generated_files_clean(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "docs_generated.spec.md",
        f"""# Governance

## SRGOV-TEST-DOCS-QUAL-002

```yaml spec-test
id: SRGOV-TEST-DOCS-QUAL-002
type: governance.check
check: docs.generated_files_clean
harness:
  root: {tmp_path}
  docs_quality:
    manifest: docs/book/reference_manifest.yaml
    index_out: docs/book/reference_index.md
    coverage_out: docs/book/reference_coverage.md
    graph_out: docs/book/docs_graph.json
assert:
  - target: text
    must:
      - contain: ["PASS: docs.generated_files_clean"]
```
""",
    )
    _seed_docs_quality(tmp_path)
    from spec_runner.docs_quality import build_docs_graph, load_docs_meta_for_paths, load_reference_manifest, manifest_chapter_paths, render_reference_coverage, render_reference_index
    import json as _json

    manifest, _errs = load_reference_manifest(tmp_path, "docs/book/reference_manifest.yaml")
    docs = manifest_chapter_paths(manifest)
    metas, _meta_errs, _ = load_docs_meta_for_paths(tmp_path, docs)
    for rel in docs:
        if rel in metas:
            metas[rel]["__text__"] = (tmp_path / rel).read_text(encoding="utf-8")
    _write_text(tmp_path / "docs/book/reference_index.md", render_reference_index(manifest))
    _write_text(tmp_path / "docs/book/reference_coverage.md", render_reference_coverage(tmp_path, metas))
    _write_text(
        tmp_path / "docs/book/docs_graph.json",
        _json.dumps(build_docs_graph(tmp_path, metas), indent=2, sort_keys=True) + "\n",
    )

    code = mod.main(["--cases", str(cases_dir)])
    assert code == 0

    _write_text(tmp_path / "docs/book/reference_index.md", "# stale\n")
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1


def test_docs_generated_files_clean_reports_first_mismatch_context(tmp_path):
    mod = _load_script_module()
    _seed_docs_quality(tmp_path)
    from spec_runner.docs_quality import (
        build_docs_graph,
        load_docs_meta_for_paths,
        load_reference_manifest,
        manifest_chapter_paths,
        render_reference_coverage,
        render_reference_index,
    )
    import json as _json

    manifest, _errs = load_reference_manifest(tmp_path, "docs/book/reference_manifest.yaml")
    docs = manifest_chapter_paths(manifest)
    metas, _meta_errs, _ = load_docs_meta_for_paths(tmp_path, docs)
    for rel in docs:
        if rel in metas:
            metas[rel]["__text__"] = (tmp_path / rel).read_text(encoding="utf-8")

    _write_text(tmp_path / "docs/book/reference_index.md", render_reference_index(manifest))
    _write_text(tmp_path / "docs/book/reference_coverage.md", render_reference_coverage(tmp_path, metas))
    _write_text(
        tmp_path / "docs/book/docs_graph.json",
        _json.dumps(build_docs_graph(tmp_path, metas), indent=2, sort_keys=True) + "\n",
    )
    _write_text(tmp_path / "docs/book/reference_index.md", "# stale\n")

    violations = mod._scan_docs_generated_files_clean(  # noqa: SLF001
        tmp_path,
        harness={
            "docs_quality": {
                "manifest": "docs/book/reference_manifest.yaml",
                "index_out": "docs/book/reference_index.md",
                "coverage_out": "docs/book/reference_coverage.md",
                "graph_out": "docs/book/docs_graph.json",
            }
        },
    )
    assert violations
    first = "\n".join(violations)
    assert "docs/book/reference_index.md:1:" in first
    assert "expected=" in first and "actual=" in first


def test_script_enforces_docs_release_contract_automation_policy(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "docs_release_contract.spec.md",
        f"""# Governance

## SRGOV-TEST-DOCS-QUAL-009

```yaml spec-test
id: SRGOV-TEST-DOCS-QUAL-009
type: governance.check
check: docs.release_contract_automation_policy
harness:
  root: {tmp_path}
  release_contract:
    files:
      - docs/release_checklist.md
    required_tokens:
      - Release readiness is defined by executable gates, not manual checklists.
      - make ci-smoke
      - ./scripts/ci_gate.sh
      - convert it into an executable
    forbidden_patterns:
      - "(?m)^##\\\\s+[0-9]+\\\\)"
      - "(?m)^\\\\s*[0-9]+\\\\.\\\\s+(Run|Then|Check|Inspect)\\\\b"
assert:
  - target: text
    must:
      - contain: ["PASS: docs.release_contract_automation_policy"]
```
""",
    )
    _write_text(
        tmp_path / "docs/release_checklist.md",
        """# Release Contract

Release readiness is defined by executable gates, not manual checklists.
make ci-smoke
./scripts/ci_gate.sh
convert it into an executable check
""",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 0

    _write_text(
        tmp_path / "docs/release_checklist.md",
        """# Release Contract

Release readiness is defined by executable gates, not manual checklists.
1. Run ci gate
""",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1


def test_script_enforces_runtime_spec_lang_pure_no_effect_builtins(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "runtime_spec_lang_pure.spec.md",
        f"""# Governance

## SRGOV-TEST-RUNTIME-PURE-001

```yaml spec-test
id: SRGOV-TEST-RUNTIME-PURE-001
type: governance.check
check: runtime.spec_lang_pure_no_effect_builtins
harness:
  root: {tmp_path}
  spec_lang_purity:
    files:
      - spec_runner/spec_lang.py
    forbidden_tokens:
      - \"path_exists\"
assert:
  - target: text
    must:
      - contain: [\"PASS: runtime.spec_lang_pure_no_effect_builtins\"]
```
""",
    )
    _write_text(tmp_path / "spec_runner/spec_lang.py", "def eval():\n    return True\n")
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 0

    _write_text(tmp_path / "spec_runner/spec_lang.py", "def eval():\n    return 'path_exists'\n")
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1


def test_script_enforces_runtime_orchestration_policy_via_spec_lang(tmp_path):
    mod = _load_script_module()
    cases_dir = tmp_path / "cases"
    _write_text(
        cases_dir / "runtime_orchestration.spec.md",
        f"""# Governance

## SRGOV-TEST-RUNTIME-ORCH-001

```yaml spec-test
id: SRGOV-TEST-RUNTIME-ORCH-001
type: governance.check
check: runtime.orchestration_policy_via_spec_lang
harness:
  root: {tmp_path}
  orchestration_policy:
    files:
      - path: scripts/ci_gate_summary.py
        required_tokens:
          - \"_load_gate_policy_expr(\"
          - \"eval_predicate(\"
          - \"gate_policy\"
          - \"policy_evaluate\"
      - path: docs/spec/governance/cases/runtime_orchestration_policy_via_spec_lang.spec.md
        required_tokens:
          - \"gate_policy\"
          - \"policy_evaluate\"
    forbidden_tokens: []
assert:
  - target: text
    must:
      - contain: [\"PASS: runtime.orchestration_policy_via_spec_lang\"]
```
""",
    )
    _write_text(
        tmp_path / "scripts/ci_gate_summary.py",
        "def x():\n    _load_gate_policy_expr()\n    eval_predicate(['eq', 1, 1], subject=[])\n    gate_policy='ok'\n    policy_evaluate=['eq',1,1]\n",
    )
    _write_text(
        tmp_path / "docs/spec/governance/cases/runtime_orchestration_policy_via_spec_lang.spec.md",
        "gate_policy\npolicy_evaluate\n",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 0

    _write_text(
        tmp_path / "scripts/ci_gate_summary.py",
        "payload = {'status': 'pass' if exit_code == 0 else 'fail'}\n",
    )
    code = mod.main(["--cases", str(cases_dir)])
    assert code == 1
