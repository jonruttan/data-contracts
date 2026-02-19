# Governance Cases

## SRGOV-OBJECTIVE-003

```yaml contract-spec
id: SRGOV-OBJECTIVE-003
title: objective tripwires are clean
purpose: Ensures objective manifest tripwire checks map to valid governance checks and currently
  pass.
type: contract.check
harness:
  root: .
  objective_tripwires:
    manifest_path: /specs/metrics/objective_manifest.yaml
    cases_path: /specs/governance/cases
    case_file_pattern: '*.spec.md'
  check:
    profile: governance.scan
    config:
      check: objective.tripwires_clean
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  imports:
    subject:
      from: artifact
      key: violation_count
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
  - id: assert_2
    assert:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - objective.tripwires_clean
    imports:
      subject:
        from: artifact
        key: summary_json
```
