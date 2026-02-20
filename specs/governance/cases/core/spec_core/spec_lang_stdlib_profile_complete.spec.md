# Governance Cases

## DCGOV-STDLIB-001

```yaml contract-spec
id: DCGOV-STDLIB-001
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: spec-lang stdlib profile is complete
purpose: Ensures the declared stdlib profile symbols are implemented in Python and PHP.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: spec_lang.stdlib_profile_complete
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
