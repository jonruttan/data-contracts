# Governance Cases

## SRGOV-ASSERT-PROFILE-005

```yaml spec-test
id: SRGOV-ASSERT-PROFILE-005
title: harness adapters expose context profile projections
type: governance.check
check: assert.adapter_projection_contract_sync
purpose: Ensures core harness adapters expose context_json subject profile targets with profile
  metadata fields.
harness:
  root: .
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
      exports:
        policy.pass_when_no_violations:
          from: library.symbol
          path: /policy.pass_when_no_violations
          required: true
    imports:
    - from_step: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- target: violation_count
  must:
  - evaluate:
    - std.logic.eq:
      - {var: subject}
      - 0
```
