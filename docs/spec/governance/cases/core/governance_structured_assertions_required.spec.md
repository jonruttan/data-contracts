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
  spec_lang:
    includes:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  structured_assertions:
    cases_path: /docs/spec/governance/cases
    case_file_pattern: '*.spec.md'
    ignore_checks:
    - governance.structured_assertions_required
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
      - governance.structured_assertions_required
```
