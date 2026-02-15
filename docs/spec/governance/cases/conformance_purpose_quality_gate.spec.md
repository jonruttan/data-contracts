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
  spec_lang:
    library_paths:
    - ../../libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  purpose_quality:
    cases: docs/spec/conformance/cases
    max_total_warnings: 0
    fail_on_policy_errors: true
    fail_on_severity: warn
  policy_evaluate:
  - {call: [{var: [policy.pass_when_no_violations]}, {subject: []}]}
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
      - conformance.purpose_quality_gate
```
