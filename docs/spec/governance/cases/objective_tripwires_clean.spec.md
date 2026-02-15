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
  spec_lang:
    library_paths:
    - ../../libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  objective_tripwires:
    manifest_path: docs/spec/metrics/objective_manifest.yaml
    cases_path: docs/spec/governance/cases
    case_file_pattern: '*.spec.md'
  policy_evaluate:
  - {call: [{var: [policy.pass_when_no_violations]}, {ref: subject}]}
assert:
- target: violation_count
  must:
  - evaluate:
    - {eq: [{ref: subject}, 0]}
- target: summary_json
  must:
  - evaluate:
    - eq:
      - {get: [{ref: subject}, passed]}
      - true
    - eq:
      - {get: [{ref: subject}, check_id]}
      - objective.tripwires_clean
```
