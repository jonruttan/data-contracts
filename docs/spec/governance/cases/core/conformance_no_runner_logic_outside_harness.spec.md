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
- target: violation_count
  must:
  - evaluate:
    - std.logic.eq:
      - {var: subject}
      - 0
- target: summary_json
  must:
  - evaluate:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - conformance.no_runner_logic_outside_harness
```
