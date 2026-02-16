# Governance Cases

## SRGOV-CONF-PURPOSE-002

```yaml spec-test
id: SRGOV-CONF-PURPOSE-002
title: conformance purpose quality remains warning free
purpose: Ensures conformance purpose lint policy and case purpose text stay clean with no
  accumulated warning debt.
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
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
      exports:
        policy.pass_when_no_violations:
          from: library.symbol
          path: /policy.pass_when_no_violations
          required: true
    imports:
    - from_step: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
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
      - conformance.purpose_quality_gate
```
