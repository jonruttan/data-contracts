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
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /specs/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
  check:
    profile: governance.scan
    config:
      check: objective.scorecard_non_regression
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - {var: subject}
    - 0
  target: violation_count
- id: assert_2
  class: MUST
  asserts:
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
  target: summary_json
```
