# Governance Cases

## SRGOV-REF-CHECKS-001

```yaml spec-test
id: SRGOV-REF-CHECKS-001
title: governance check ids exist
purpose: Ensures governance cases only reference registered check ids.
type: governance.check
check: reference.check_ids_exist
harness:
  root: .
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- id: assert_1
  class: must
  checks:
  - std.logic.eq:
    - std.object.get:
      - var: subject
      - check_id
    - reference.check_ids_exist
  target: summary_json
```
