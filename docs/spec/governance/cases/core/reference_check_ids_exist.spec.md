# Governance Cases

## SRGOV-REF-CHECKS-001

```yaml contract-spec
id: SRGOV-REF-CHECKS-001
title: governance check ids exist
purpose: Ensures governance cases only reference registered check ids.
type: contract.check
harness:
  root: .
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
  check:
    profile: governance.scan
    config:
      check: reference.check_ids_exist
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
      lit:
        lit:
          std.logic.eq:
          - std.object.get:
            - {var: subject}
            - check_id
          - reference.check_ids_exist
  target: summary_json
```
