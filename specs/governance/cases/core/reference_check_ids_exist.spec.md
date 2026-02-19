# Governance Cases

## SRGOV-REF-CHECKS-001

```yaml contract-spec
id: SRGOV-REF-CHECKS-001
title: governance check ids exist
purpose: Ensures governance cases only reference registered check ids.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: reference.check_ids_exist
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
    target: summary_json
    assert:
      std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - reference.check_ids_exist
```
