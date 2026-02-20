# Governance Cases

## DCGOV-ARCH-COMPONENTS-003

```yaml contract-spec
id: DCGOV-ARCH-COMPONENTS-003
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: harness type overlays are complete
purpose: Ensures behavior-heavy harness types publish non-empty schema overlays for machine
  validation and drift prevention.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: schema.harness_type_overlay_complete
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

