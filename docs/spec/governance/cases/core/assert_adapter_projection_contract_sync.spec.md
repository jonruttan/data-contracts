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
      - as: policy.pass_when_no_violations
        from: library.symbol
        required: true
        path: /policy.pass_when_no_violations
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- id: assert_1
  class: must
  checks:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
```
