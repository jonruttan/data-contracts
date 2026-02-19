# Governance Cases

## SRGOV-RUNTIME-ORCH-001

```yaml contract-spec
id: SRGOV-RUNTIME-ORCH-001
title: gate orchestration verdict is policy-driven via spec-lang
purpose: Ensures CI gate summary determines final verdict from assert-derived step statuses
  without evaluate expressions.
type: contract.check
harness:
  root: .
  orchestration_policy:
    files:
    - path: /runners/python/spec_runner/script_runtime_commands.py
      required_tokens:
      - _evaluate_gate_policy(
      - all(str(row.get("status", "")) == "pass"
      - policy_verdict
    - path: /specs/governance/cases/core/runtime_orchestration_policy_via_spec_lang.spec.md
      required_tokens:
      - runtime.orchestration_policy_via_spec_lang
      - _evaluate_gate_policy(
    forbidden_tokens: []
  check:
    profile: governance.scan
    config:
      check: runtime.orchestration_policy_via_spec_lang
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    target: violation_count
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
  - id: assert_2
    target: summary_json
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
      - runtime.orchestration_policy_via_spec_lang
```
