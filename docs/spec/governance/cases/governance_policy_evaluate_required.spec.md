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
  spec_lang:
    library_paths:
    - ../../libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  policy_requirements:
    cases_path: docs/spec/governance/cases
    case_file_pattern: '*.spec.md'
    ignore_checks:
    - governance.policy_evaluate_required
  policy_evaluate:
  - {eq: [true, true]}
assert:
- target: violation_count
  must:
  - evaluate:
    - {eq: [{subject: []}, 0]}
- target: summary_json
  must:
  - evaluate:
    - eq:
      - {get: [{subject: []}, passed]}
      - true
    - eq:
      - {get: [{subject: []}, check_id]}
      - governance.policy_evaluate_required
```
