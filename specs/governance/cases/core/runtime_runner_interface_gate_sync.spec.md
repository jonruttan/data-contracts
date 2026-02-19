# Governance Cases

## SRGOV-RUNTIME-CONFIG-003

```yaml contract-spec
id: SRGOV-RUNTIME-CONFIG-003
title: gate scripts call runner interface boundary
purpose: Ensures gate scripts call a runner command boundary instead of hardcoding Python
  implementation entrypoints.
type: contract.check
harness:
  root: .
  runner_interface:
    required_paths:
    - /runners/public/runner_adapter.sh
    - /runners/python/runner_adapter.sh
    - /runners/rust/runner_adapter.sh
    files:
    - scripts/ci_gate.sh
    - scripts/docs_doctor.sh
    - scripts/core_gate.sh
    required_tokens:
    - SPEC_RUNNER_BIN
    - runners/public/runner_adapter.sh
    forbidden_tokens:
    - spec_lang_commands run-governance-specs
    - runners/python/spec_runner/script_runtime_commands.py
    - spec_lang_commands spec-lang-format --check specs
    - scripts/conformance_purpose_report.py
    - spec_lang_commands compare-conformance-parity
  check:
    profile: governance.scan
    config:
      check: runtime.runner_interface_gate_sync
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - violation_count
    as:
      violation_count: subject
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
  - id: assert_2
    assert:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - runtime.runner_interface_gate_sync
    imports:
    - from: artifact
      names:
      - summary_json
      as:
        summary_json: subject
```
