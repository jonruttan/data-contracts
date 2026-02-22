```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'objective_scorecard_non_regression': {'baseline_path': '/specs/governance/metrics/objective_scorecard_baseline.json', 'summary_fields': {'overall_min_score': 'non_decrease', 'overall_mean_score': 'non_decrease', 'tripwire_hit_count': 'non_increase'}, 'epsilon': 1e-12, 'objective_scorecard': {'manifest_path': '/specs/governance/metrics/objective_manifest.yaml'}, 'baseline_notes': {'path': '/specs/governance/metrics/baseline_update_notes.yaml', 'baseline_paths': ['/specs/governance/metrics/spec_portability_baseline.json', '/specs/governance/metrics/spec_lang_adoption_baseline.json', '/specs/governance/metrics/runner_independence_baseline.json', '/specs/governance/metrics/docs_operability_baseline.json', '/specs/governance/metrics/contract_assertions_baseline.json', '/specs/governance/metrics/objective_scorecard_baseline.json']}}, 'check': {'profile': 'governance.scan', 'config': {'check': 'objective.scorecard_non_regression'}}, 'use': [{'ref': '/specs/libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id', 'policy.assert.scan_pass']}]}"
contracts:
  clauses:
  - id: DCGOV-OBJECTIVE-002
    title: objective scorecard is non-regressing
    purpose: Enforces ratchet non-regression for objective scorecard summary metrics and baseline-note integrity.
    asserts:
      imports:
      - from: artifact
        names:
        - violation_count
      checks:
      - id: assert_1
        assert:
          call:
          - var: policy.assert.no_violations
          - std.object.assoc:
            - violation_count
            - var: violation_count
            - lit: {}
      - id: assert_2
        assert:
        - call:
          - var: policy.assert.summary_passed
          - std.object.assoc:
            - summary_json
            - var: summary_json
            - lit: {}
        - call:
          - var: policy.assert.summary_check_id
          - std.object.assoc:
            - summary_json
            - var: summary_json
            - lit: {}
          - objective.scorecard_non_regression
        imports:
        - from: artifact
          names:
          - summary_json
adapters:
- type: legacy.root_objective_scorecard_non_regression_baseline_path_specs_governance_metrics_objective_scorecard_baseline_json_summary_fields_overall_min_score_non_decrease_overall_mean_score_non_decrease_tripwire_hit_count_non_increase_epsilon_1e_12_objective_scorecard_manifest_path_specs_governance_metrics_objective_manifest_yaml_baseline_notes_path_specs_governance_metrics_baseline_update_notes_yaml_baseline_paths_specs_governance_metrics_spec_portability_baseline_json_specs_governance_metrics_spec_lang_adoption_baseline_json_specs_governance_metrics_runner_independence_baseline_json_specs_governance_metrics_docs_operability_baseline_json_specs_governance_metrics_contract_assertions_baseline_json_specs_governance_metrics_objective_scorecard_baseline_json_check_profile_governance_scan_config_check_objective_scorecard_non_regression_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
  actions:
  - id: svc.root_objective_scorecard_non_regression_baseline_path_specs_governance_metrics_objective_scorecard_baseline_json_summary_fields_overall_min_score_non_decrease_overall_mean_score_non_decrease_tripwire_hit_count_non_increase_epsilon_1e_12_objective_scorecard_manifest_path_specs_governance_metrics_objective_manifest_yaml_baseline_notes_path_specs_governance_metrics_baseline_update_notes_yaml_baseline_paths_specs_governance_metrics_spec_portability_baseline_json_specs_governance_metrics_spec_lang_adoption_baseline_json_specs_governance_metrics_runner_independence_baseline_json_specs_governance_metrics_docs_operability_baseline_json_specs_governance_metrics_contract_assertions_baseline_json_specs_governance_metrics_objective_scorecard_baseline_json_check_profile_governance_scan_config_check_objective_scorecard_non_regression_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    direction: bidirectional
    profile: default
services:
- id: svc.root_objective_scorecard_non_regression_baseline_path_specs_governance_metrics_objective_scorecard_baseline_json_summary_fields_overall_min_score_non_decrease_overall_mean_score_non_decrease_tripwire_hit_count_non_increase_epsilon_1e_12_objective_scorecard_manifest_path_specs_governance_metrics_objective_manifest_yaml_baseline_notes_path_specs_governance_metrics_baseline_update_notes_yaml_baseline_paths_specs_governance_metrics_spec_portability_baseline_json_specs_governance_metrics_spec_lang_adoption_baseline_json_specs_governance_metrics_runner_independence_baseline_json_specs_governance_metrics_docs_operability_baseline_json_specs_governance_metrics_contract_assertions_baseline_json_specs_governance_metrics_objective_scorecard_baseline_json_check_profile_governance_scan_config_check_objective_scorecard_non_regression_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
  consumes:
  - svc.root_objective_scorecard_non_regression_baseline_path_specs_governance_metrics_objective_scorecard_baseline_json_summary_fields_overall_min_score_non_decrease_overall_mean_score_non_decrease_tripwire_hit_count_non_increase_epsilon_1e_12_objective_scorecard_manifest_path_specs_governance_metrics_objective_manifest_yaml_baseline_notes_path_specs_governance_metrics_baseline_update_notes_yaml_baseline_paths_specs_governance_metrics_spec_portability_baseline_json_specs_governance_metrics_spec_lang_adoption_baseline_json_specs_governance_metrics_runner_independence_baseline_json_specs_governance_metrics_docs_operability_baseline_json_specs_governance_metrics_contract_assertions_baseline_json_specs_governance_metrics_objective_scorecard_baseline_json_check_profile_governance_scan_config_check_objective_scorecard_non_regression_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
```
