# Governance Cases

## SRGOV-POLICY-REQ-001

```yaml spec-test
id: SRGOV-POLICY-REQ-001
title: governance checks require policy_evaluate contract
purpose: Ensures governance decision contracts include explicit policy_evaluate expressions
  in harness config.
type: governance.check
check: governance.policy_evaluate_required
harness:
  root: .
  policy_requirements:
    cases_path: /docs/spec/governance/cases
    case_file_pattern: '*.spec.md'
    ignore_checks:
    - governance.policy_evaluate_required
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
      - governance.policy_evaluate_required
  target: summary_json
```
