# Governance Cases

## SRGOV-CONF-PORT-001

```yaml spec-test
id: SRGOV-CONF-PORT-001
title: conformance cases keep runner logic under harness
purpose: Ensures portable conformance fixtures do not place runner/setup keys at top level.
type: governance.check
check: conformance.no_runner_logic_outside_harness
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
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
- id: assert_2
  class: must
  checks:
  - must:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - conformance.no_runner_logic_outside_harness
  target: summary_json
```
