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
  spec_lang:
    includes:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
assert:
- target: summary_json
  must:
  - evaluate:
    - eq:
      - get:
        - {var: subject}
        - check_id
      - reference.check_ids_exist
```
