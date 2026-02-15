# Governance Cases

## SRGOV-POLICY-REQ-001

```yaml spec-test
id: SRGOV-POLICY-REQ-001
title: governance checks require policy_evaluate contract
purpose: Ensures governance decision contracts include explicit policy_evaluate expressions in harness config.
type: governance.check
check: governance.policy_evaluate_required
harness:
  root: .
  policy_requirements:
    cases_path: docs/spec/governance/cases
    case_file_pattern: '*.spec.md'
    ignore_checks:
    - governance.policy_evaluate_required
  policy_evaluate:
  - eq:
    - true
    - true
assert:
- target: text
  must:
  - contain:
    - 'PASS: governance.policy_evaluate_required'
```
