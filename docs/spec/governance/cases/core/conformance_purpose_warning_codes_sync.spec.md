# Governance Cases

## SRGOV-CONF-PURPOSE-001

```yaml spec-test
id: SRGOV-CONF-PURPOSE-001
title: purpose warning code doc stays in sync with implementation codes
purpose: Ensures docs for purpose warning codes include all implementation codes and no stale
  entries.
type: governance.check
check: conformance.purpose_warning_codes_sync
harness:
  root: .
  spec_lang:
    includes:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
assert:
- target: violation_count
  must:
  - evaluate:
    - eq:
      - {var: subject}
      - 0
- target: summary_json
  must:
  - evaluate:
    - eq:
      - get:
        - {var: subject}
        - passed
      - true
    - eq:
      - get:
        - {var: subject}
        - check_id
      - conformance.purpose_warning_codes_sync
```
