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
  spec_lang:
    library_paths:
    - ../../libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  objective_scorecard:
    manifest_path: docs/spec/metrics/objective_manifest.yaml
    policy_evaluate:
    - and:
      - {has_key: [{ref: subject}, summary]}
      - {has_key: [{ref: subject}, objectives]}
      - {has_key: [{ref: subject}, tripwire_hits]}
      - has_key:
        - {get: [{ref: subject}, summary]}
        - overall_min_score
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
      - objective.scorecard_metric
```
