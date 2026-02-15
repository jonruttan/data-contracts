# Governance Cases

## SRGOV-CONF-PURPOSE-001

```yaml spec-test
id: SRGOV-CONF-PURPOSE-001
title: purpose warning code doc stays in sync with implementation codes
purpose: Ensures docs for purpose warning codes include all implementation codes and no stale entries.
type: governance.check
check: conformance.purpose_warning_codes_sync
harness:
  root: .
  policy_evaluate:
    - ["is_empty", ["get", ["subject"], "violations"]]
assert:
  - target: text
    must:
      - contain: ["PASS: conformance.purpose_warning_codes_sync"]
```
