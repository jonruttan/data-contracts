# Governance Cases

## SRGOV-TEST-UNIT-OPT-OUT-001

```yaml contract-spec
id: SRGOV-TEST-UNIT-OPT-OUT-001
title: unit test opt-out usage is measured and non-regressing
purpose: Tracks unit-test opt-out usage and enforces a non-regression baseline so opt-out
  coverage is reduced over time.
type: governance.check
check: tests.unit_opt_out_non_regression
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
  class: must
  asserts:
  - std.logic.eq:
    - std.object.get:
      - var: subject
      - check_id
    - tests.unit_opt_out_non_regression
  target: summary_json
```
