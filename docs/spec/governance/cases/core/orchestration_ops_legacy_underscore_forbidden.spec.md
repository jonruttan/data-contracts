# Governance Cases

## SRGOV-OPS-002

```yaml spec-test
id: SRGOV-OPS-002
title: orchestration ops legacy underscore forms are forbidden
purpose: Ensures underscore shorthand ops symbols are rejected.
type: governance.check
check: orchestration.ops_legacy_underscore_forbidden
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
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - orchestration.ops_legacy_underscore_forbidden
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
```
