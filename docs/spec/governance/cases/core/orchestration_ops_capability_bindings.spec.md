# Governance Cases

## SRGOV-OPS-004

```yaml spec-test
id: SRGOV-OPS-004
title: orchestration ops capability bindings are enforced
purpose: Ensures orchestration tools and case capability bindings remain synchronized.
type: governance.check
check: orchestration.ops_capability_bindings
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
      - orchestration.ops_capability_bindings
    - eq:
      - get:
        - {var: subject}
        - passed
      - true
```
