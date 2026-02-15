# Governance Cases

## SRGOV-CONF-PURPOSE-002

```yaml spec-test
id: SRGOV-CONF-PURPOSE-002
title: conformance purpose quality remains warning free
purpose: Ensures conformance purpose lint policy and case purpose text stay clean with no accumulated warning debt.
type: governance.check
check: conformance.purpose_quality_gate
harness:
  root: .
  purpose_quality:
    cases: docs/spec/conformance/cases
    max_total_warnings: 0
    fail_on_policy_errors: true
    fail_on_severity: warn
  policy_evaluate:
  - is_empty:
    - get:
      - subject: []
      - violations
assert:
- target: text
  must:
  - contain:
    - 'PASS: conformance.purpose_quality_gate'
```
