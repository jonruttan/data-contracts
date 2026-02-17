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
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
      exports:
      - as: policy.pass_when_no_violations
        from: library.symbol
        required: true
        path: /policy.pass_when_no_violations
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
      - orchestration.ops_capability_bindings
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
  target: summary_json
```
