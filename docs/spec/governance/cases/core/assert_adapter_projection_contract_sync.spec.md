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
  spec_lang:
    library_paths:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
assert:
- target: violation_count
  must:
  - evaluate:
    - eq:
      - {var: subject}
      - 0
```
