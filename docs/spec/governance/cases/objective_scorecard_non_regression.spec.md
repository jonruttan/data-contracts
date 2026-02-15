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
  objective_scorecard_non_regression:
    baseline_path: docs/spec/metrics/objective_scorecard_baseline.json
    summary_fields:
      overall_min_score: non_decrease
      overall_mean_score: non_decrease
      tripwire_hit_count: non_increase
    epsilon: 0.000000000001
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
    - ["is_empty", ["get", ["subject"], "violations"]]
assert:
  - target: text
    must:
      - contain: ["PASS: objective.scorecard_non_regression"]
```
