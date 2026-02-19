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
  check:
    profile: governance.scan
    config:
      check: assert.adapter_projection_contract_sync
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
```
