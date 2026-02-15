# Governance Cases

## SRGOV-POLICY-REQ-002

```yaml spec-test
id: SRGOV-POLICY-REQ-002
title: governance checks require structured assertion targets
purpose: Ensures governance cases validate deterministic structured result targets instead of relying on PASS text markers as primary contract truth.
type: governance.check
check: governance.structured_assertions_required
harness:
  root: .
  structured_assertions:
    cases_path: docs/spec/governance/cases
    case_file_pattern: '*.spec.md'
    ignore_checks:
    - governance.structured_assertions_required
  policy_evaluate:
  - is_empty:
    - get:
      - subject: []
      - violations
assert:
- target: violation_count
  must:
  - evaluate:
    - eq:
      - subject: []
      - 0
- target: summary_json
  must:
  - evaluate:
    - eq:
      - get:
        - subject: []
        - passed
      - true
    - eq:
      - get:
        - subject: []
        - check_id
      - governance.structured_assertions_required
```
