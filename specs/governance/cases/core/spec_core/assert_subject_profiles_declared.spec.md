# Governance Cases

## DCGOV-ASSERT-PROFILE-001

```yaml contract-spec
id: DCGOV-ASSERT-PROFILE-001
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: subject profile contract artifacts are declared
purpose: Ensures subject profile contract/schema/type docs and domain libraries are present
  as required artifacts.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: assert.subject_profiles_declared
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
