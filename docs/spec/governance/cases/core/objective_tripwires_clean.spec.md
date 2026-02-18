# Governance Cases

## SRGOV-OBJECTIVE-003

```yaml spec-test
id: SRGOV-OBJECTIVE-003
title: objective tripwires are clean
purpose: Ensures objective manifest tripwire checks map to valid governance checks and currently
  pass.
type: governance.check
check: objective.tripwires_clean
harness:
  root: .
  objective_tripwires:
    manifest_path: /docs/spec/metrics/objective_manifest.yaml
    cases_path: /docs/spec/governance/cases
    case_file_pattern: '*.spec.md'
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- id: assert_1
  class: must
  checks:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
- id: assert_2
  class: must
  checks:
  - must:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - objective.tripwires_clean
  target: summary_json
```
