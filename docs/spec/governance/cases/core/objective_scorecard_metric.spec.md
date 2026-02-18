# Governance Cases

## SRGOV-OBJECTIVE-001

```yaml contract-spec
id: SRGOV-OBJECTIVE-001
title: objective scorecard metric report generation is valid
purpose: Ensures objective scorecard generation is deterministic and includes required summary/objective/tripwire
  fields.
type: governance.check
check: objective.scorecard_metric
harness:
  root: .
  objective_scorecard:
    manifest_path: /docs/spec/metrics/objective_manifest.yaml
    policy_evaluate:
    - std.logic.and:
      - std.object.has_key:
        - {var: subject}
        - summary
      - std.object.has_key:
        - {var: subject}
        - objectives
      - std.object.has_key:
        - {var: subject}
        - tripwire_hits
      - std.object.has_key:
        - std.object.get:
          - {var: subject}
          - summary
        - overall_min_score
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
contract:
- id: assert_1
  class: must
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
- id: assert_2
  class: must
  asserts:
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
      - objective.scorecard_metric
  target: summary_json
```
