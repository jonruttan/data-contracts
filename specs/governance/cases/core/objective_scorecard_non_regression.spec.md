```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-OBJECTIVE-002
    title: objective scorecard is non-regressing
    purpose: Enforces ratchet non-regression for objective scorecard summary metrics and baseline-note
      integrity.
    harness:
      root: .
      objective_scorecard_non_regression:
        baseline_path: /specs/governance/metrics/objective_scorecard_baseline.json
        summary_fields:
          overall_min_score: non_decrease
          overall_mean_score: non_decrease
          tripwire_hit_count: non_increase
        epsilon: 1.0e-12
        objective_scorecard:
          manifest_path: /specs/governance/metrics/objective_manifest.yaml
        baseline_notes:
          path: /specs/governance/metrics/baseline_update_notes.yaml
          baseline_paths:
          - /specs/governance/metrics/spec_portability_baseline.json
          - /specs/governance/metrics/spec_lang_adoption_baseline.json
          - /specs/governance/metrics/runner_independence_baseline.json
          - /specs/governance/metrics/docs_operability_baseline.json
          - /specs/governance/metrics/contract_assertions_baseline.json
          - /specs/governance/metrics/objective_scorecard_baseline.json
      check:
        profile: governance.scan
        config:
          check: objective.scorecard_non_regression
      use:
      - ref: /specs/libraries/policy/policy_assertions.spec.md
        as: lib_policy_core_spec
        symbols:
        - policy.assert.no_violations
        - policy.assert.summary_passed
        - policy.assert.summary_check_id
        - policy.assert.scan_pass
    clauses:
      defaults: {}
      imports:
      - from: artifact
        names:
        - violation_count
      predicates:
      - id: assert_1
        assert:
          call:
          - {var: policy.assert.no_violations}
          - std.object.assoc:
            - violation_count
            - {var: violation_count}
            - lit: {}
      - id: assert_2
        assert:
        - call:
          - {var: policy.assert.summary_passed}
          - std.object.assoc:
            - summary_json
            - {var: summary_json}
            - lit: {}
        - call:
          - {var: policy.assert.summary_check_id}
          - std.object.assoc:
            - summary_json
            - {var: summary_json}
            - lit: {}
          - objective.scorecard_non_regression
        imports:
        - from: artifact
          names:
          - summary_json
```
