# Governance Cases

## SRGOV-ASSERT-PROFILE-005

```yaml contract-spec
id: SRGOV-ASSERT-PROFILE-005
title: harness adapters expose context profile projections
type: contract.check
purpose: Ensures core harness adapters expose context_json subject profile targets with profile
  metadata fields.
harness:
  root: .
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /specs/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
  check:
    profile: governance.scan
    config:
      check: assert.adapter_projection_contract_sync
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - {var: subject}
    - 0
  target: violation_count
```
