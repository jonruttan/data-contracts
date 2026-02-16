# Governance Cases

## SRGOV-OBJECTIVE-001

```yaml spec-test
id: SRGOV-OBJECTIVE-001
title: objective scorecard metric report generation is valid
purpose: Ensures objective scorecard generation is deterministic and includes required summary/objective/tripwire
  fields.
type: governance.check
check: objective.scorecard_metric
harness:
  root: .
  spec_lang:
    includes:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  objective_scorecard:
    manifest_path: /docs/spec/metrics/objective_manifest.yaml
    policy_evaluate:
    - and:
      - has_key:
        - {var: subject}
        - summary
      - has_key:
        - {var: subject}
        - objectives
      - has_key:
        - {var: subject}
        - tripwire_hits
      - has_key:
        - get:
          - {var: subject}
          - summary
        - overall_min_score
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
      - objective.scorecard_metric
```
