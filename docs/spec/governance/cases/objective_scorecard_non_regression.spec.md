# Governance Cases

## SRGOV-OBJECTIVE-002

```yaml spec-test
id: SRGOV-OBJECTIVE-002
title: objective scorecard is non-regressing
purpose: Enforces ratchet non-regression for objective scorecard summary metrics and baseline-note integrity.
type: governance.check
check: objective.scorecard_non_regression
harness:
  root: .
  spec_lang:
    library_paths:
    - ../../libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  objective_scorecard_non_regression:
    baseline_path: docs/spec/metrics/objective_scorecard_baseline.json
    summary_fields:
      overall_min_score: non_decrease
      overall_mean_score: non_decrease
      tripwire_hit_count: non_increase
    epsilon: 1.0e-12
    objective_scorecard:
      manifest_path: docs/spec/metrics/objective_manifest.yaml
    baseline_notes:
      path: docs/spec/metrics/baseline_update_notes.yaml
      baseline_paths:
      - docs/spec/metrics/spec_portability_baseline.json
      - docs/spec/metrics/spec_lang_adoption_baseline.json
      - docs/spec/metrics/runner_independence_baseline.json
      - docs/spec/metrics/docs_operability_baseline.json
      - docs/spec/metrics/contract_assertions_baseline.json
      - docs/spec/metrics/objective_scorecard_baseline.json
  policy_evaluate:
  - {call: [{var: [policy.pass_when_no_violations]}, {subject: []}]}
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
      - objective.scorecard_non_regression
```
