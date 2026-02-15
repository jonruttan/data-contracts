# Governance Cases

## SRGOV-OBJECTIVE-003

```yaml spec-test
id: SRGOV-OBJECTIVE-003
title: objective tripwires are clean
purpose: Ensures objective manifest tripwire checks map to valid governance checks and currently pass.
type: governance.check
check: objective.tripwires_clean
harness:
  root: .
  objective_tripwires:
    manifest_path: docs/spec/metrics/objective_manifest.yaml
    cases_path: docs/spec/governance/cases
    case_file_pattern: '*.spec.md'
  policy_evaluate:
  - is_empty:
    - get:
      - subject: []
      - violations
assert:
- target: text
  must:
  - contain:
    - 'PASS: objective.tripwires_clean'
```
