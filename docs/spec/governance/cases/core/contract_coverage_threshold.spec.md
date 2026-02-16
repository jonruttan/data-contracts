# Governance Cases

## SRGOV-CONTRACT-002

```yaml spec-test
id: SRGOV-CONTRACT-002
title: contract must-rule coverage stays complete
purpose: Ensures all MUST policy rules remain covered by traceability evidence and keeps overall
  contract coverage above a minimum baseline.
type: governance.check
check: contract.coverage_threshold
harness:
  root: .
  spec_lang:
    includes:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  contract_coverage:
    require_all_must_covered: true
    min_coverage_ratio: 0.5
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
      - contract.coverage_threshold
```
