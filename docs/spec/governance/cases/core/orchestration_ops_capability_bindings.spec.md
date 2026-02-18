# Governance Cases

## SRGOV-OPS-004

```yaml contract-spec
id: SRGOV-OPS-004
title: orchestration ops capability bindings are enforced
purpose: Ensures orchestration tools and case capability bindings remain synchronized.
type: governance.check
check: orchestration.ops_capability_bindings
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
contract:
- id: assert_1
  class: MUST
  asserts:
  - MUST:
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
