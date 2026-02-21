# Governance Cases

## DCGOV-ARCH-COMPONENTS-005

```yaml contract-spec
id: DCGOV-ARCH-COMPONENTS-005
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: harnesses declare target subject maps
purpose: Enforces explicit target-to-subject mapping declarations so assertion targets remain
  deterministic and reviewable.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: runtime.harness_subject_target_map_declared
  use:
  - ref: /specs/libraries/policy/policy_assertions.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.assert.no_violations
    - policy.assert.summary_passed
    - policy.assert.summary_check_id
    - policy.assert.scan_pass
contract:
  defaults: {}
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

