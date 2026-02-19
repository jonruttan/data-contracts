# Governance Cases

## SRGOV-OBJECTIVE-002

```yaml contract-spec
id: SRGOV-OBJECTIVE-002
title: objective scorecard is non-regressing
purpose: Enforces ratchet non-regression for objective scorecard summary metrics and baseline-note
  integrity.
type: contract.check
harness:
  root: .
  objective_scorecard_non_regression:
    baseline_path: /specs/metrics/objective_scorecard_baseline.json
    summary_fields:
      overall_min_score: non_decrease
      overall_mean_score: non_decrease
      tripwire_hit_count: non_increase
    epsilon: 1.0e-12
    objective_scorecard:
      manifest_path: /specs/metrics/objective_manifest.yaml
    baseline_notes:
      path: /specs/metrics/baseline_update_notes.yaml
      baseline_paths:
      - /specs/metrics/spec_portability_baseline.json
      - /specs/metrics/spec_lang_adoption_baseline.json
      - /specs/metrics/runner_independence_baseline.json
      - /specs/metrics/docs_operability_baseline.json
      - /specs/metrics/contract_assertions_baseline.json
      - /specs/metrics/objective_scorecard_baseline.json
  check:
    profile: governance.scan
    config:
      check: objective.scorecard_non_regression
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    target: violation_count
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
  - id: assert_2
    target: summary_json
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
      - objective.scorecard_non_regression
```
