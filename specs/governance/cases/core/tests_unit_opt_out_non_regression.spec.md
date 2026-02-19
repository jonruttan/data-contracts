# Governance Cases

## SRGOV-TEST-UNIT-OPT-OUT-001

```yaml contract-spec
id: SRGOV-TEST-UNIT-OPT-OUT-001
title: unit test opt-out usage is measured and non-regressing
purpose: Tracks unit-test opt-out usage and enforces a non-regression baseline so opt-out
  coverage is reduced over time.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: tests.unit_opt_out_non_regression
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  imports:
    subject:
      from: artifact
      key: summary_json
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - tests.unit_opt_out_non_regression
```
