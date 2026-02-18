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
  - must:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - orchestration.ops_legacy_underscore_forbidden
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
  target: summary_json
```
