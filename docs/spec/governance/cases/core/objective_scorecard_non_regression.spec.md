# Governance Cases

## SRGOV-OBJECTIVE-002

```yaml spec-test
id: SRGOV-OBJECTIVE-002
title: objective scorecard is non-regressing
purpose: Enforces ratchet non-regression for objective scorecard summary metrics and baseline-note
  integrity.
type: governance.check
check: objective.scorecard_non_regression
harness:
  root: .
  objective_scorecard_non_regression:
    baseline_path: /docs/spec/metrics/objective_scorecard_baseline.json
    summary_fields:
      overall_min_score: non_decrease
      overall_mean_score: non_decrease
      tripwire_hit_count: non_increase
    epsilon: 1.0e-12
    objective_scorecard:
      manifest_path: /docs/spec/metrics/objective_manifest.yaml
    baseline_notes:
      path: /docs/spec/metrics/baseline_update_notes.yaml
      baseline_paths:
      - /docs/spec/metrics/spec_portability_baseline.json
      - /docs/spec/metrics/spec_lang_adoption_baseline.json
      - /docs/spec/metrics/runner_independence_baseline.json
      - /docs/spec/metrics/docs_operability_baseline.json
      - /docs/spec/metrics/contract_assertions_baseline.json
      - /docs/spec/metrics/objective_scorecard_baseline.json
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
      exports:
        policy.pass_when_no_violations:
          from: library.symbol
          path: /policy.pass_when_no_violations
          required: true
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
      - objective.scorecard_non_regression
  target: summary_json
```
