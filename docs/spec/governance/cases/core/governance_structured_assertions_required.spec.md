# Governance Cases

## SRGOV-POLICY-REQ-002

```yaml spec-test
id: SRGOV-POLICY-REQ-002
title: governance checks require structured assertion targets
purpose: Ensures governance cases validate deterministic structured result targets instead
  of relying on PASS text markers as primary contract truth.
type: governance.check
check: governance.structured_assertions_required
harness:
  root: .
  structured_assertions:
    cases_path: /docs/spec/governance/cases
    case_file_pattern: '*.spec.md'
    ignore_checks:
    - governance.structured_assertions_required
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
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
      - governance.structured_assertions_required
  target: summary_json
```
