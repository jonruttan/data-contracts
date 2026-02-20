# Governance Cases

## DCGOV-ASSERT-PROFILE-005

```yaml contract-spec
id: DCGOV-ASSERT-PROFILE-005
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
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
  - ref: /specs/libraries/policy/policy_assertions.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.assert.no_violations
    - policy.assert.summary_passed
    - policy.assert.summary_check_id
    - policy.assert.scan_pass
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - violation_count
  steps:
  - id: assert_1
    assert:
      call:
      - {var: policy.assert.no_violations}
      - std.object.assoc:
        - violation_count
        - {var: violation_count}
        - lit: {}
```
