# Governance Cases

## SRGOV-OBJECTIVE-001

```yaml spec-test
id: SRGOV-OBJECTIVE-001
title: objective scorecard metric report generation is valid
purpose: Ensures objective scorecard generation is deterministic and includes required summary/objective/tripwire fields.
type: governance.check
check: objective.scorecard_metric
harness:
  root: .
  objective_scorecard:
    manifest_path: docs/spec/metrics/objective_manifest.yaml
    policy_evaluate:
    - and:
      - {has_key: [{subject: []}, summary]}
      - {has_key: [{subject: []}, objectives]}
      - {has_key: [{subject: []}, tripwire_hits]}
      - has_key:
        - {get: [{subject: []}, summary]}
        - overall_min_score
  policy_evaluate:
  - is_empty:
    - {get: [{subject: []}, violations]}
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
      - objective.scorecard_metric
```
