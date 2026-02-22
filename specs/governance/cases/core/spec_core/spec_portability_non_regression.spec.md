```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-SPEC-PORT-002
  title: spec-lang self-containment metric is non-regressing
  purpose: Enforces a monotonic ratchet so configured spec-lang self-containment
    metrics cannot decrease from baseline.
  clauses:
    imports:
    - from: artifact
      names:
      - violation_count
    predicates:
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
        - spec.portability_non_regression
      imports:
      - from: artifact
        names:
        - summary_json
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'portability_non_regression': {'baseline_path': '/specs/governance/metrics/spec_portability_baseline.json',
      'summary_fields': ['overall_logic_self_contained_ratio'], 'segment_fields':
      {'conformance': ['mean_logic_self_contained_ratio'], 'governance': ['mean_logic_self_contained_ratio'],
      'impl': ['mean_logic_self_contained_ratio']}, 'epsilon': 1e-12, 'portability_metric':
      {'roots': ['/specs/conformance/cases', '/specs/governance/cases', 'runner-owned
      implementation specs'], 'core_types': ['text.file', 'cli.run'], 'segment_rules':
      [{'prefix': 'specs/conformance/cases', 'segment': 'conformance'}, {'prefix':
      'specs/governance/cases', 'segment': 'governance'}, {'prefix': 'runner-owned
      implementation specs', 'segment': 'impl'}], 'runtime_capability_tokens': ['api.http',
      'governance.check'], 'runtime_capability_prefixes': ['runtime.', 'php.', 'python.'],
      'weights': {'non_evaluate_leaf_share': 0.45, 'expect_impl_overlay': 0.25, 'runtime_specific_capability':
      0.15, 'non_core_type': 0.15}, 'report': {'top_n': 10}, 'enforce': False}}, 'check':
      {'profile': 'governance.scan', 'config': {'check': 'spec.portability_non_regression'}},
      'use': [{'ref': '/specs/libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec',
      'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id',
      'policy.assert.scan_pass']}]}"
services:
  entries:
  - id: 
      svc.root_portability_non_regression_baseline_path_specs_governance_metrics_spec_portability_baseline_json_summary_fields_overall_logic_self_contained_ratio_segment_fields_conformance_mean_logic_self_contained_ratio_governance_mean_logic_self_contained_ratio_impl_mean_logic_self_contained_ratio_epsilon_1e_12_portability_metric_roots_specs_conformance_cases_specs_governance_cases_runner_owned_implementation_specs_core_types_text_file_cli_run_segment_rules_prefix_specs_conformance_cases_segment_conformance_prefix_specs_governance_cases_segment_governance_prefix_runner_owned_implementation_specs_segment_impl_runtime_capability_tokens_api_http_governance_check_runtime_capability_prefixes_runtime_php_python_weights_non_evaluate_leaf_share_0_45_expect_impl_overlay_0_25_runtime_specific_capability_0_15_non_core_type_0_15_report_top_n_10_enforce_false_check_profile_governance_scan_config_check_spec_portability_non_regression_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    type: 
      legacy.root_portability_non_regression_baseline_path_specs_governance_metrics_spec_portability_baseline_json_summary_fields_overall_logic_self_contained_ratio_segment_fields_conformance_mean_logic_self_contained_ratio_governance_mean_logic_self_contained_ratio_impl_mean_logic_self_contained_ratio_epsilon_1e_12_portability_metric_roots_specs_conformance_cases_specs_governance_cases_runner_owned_implementation_specs_core_types_text_file_cli_run_segment_rules_prefix_specs_conformance_cases_segment_conformance_prefix_specs_governance_cases_segment_governance_prefix_runner_owned_implementation_specs_segment_impl_runtime_capability_tokens_api_http_governance_check_runtime_capability_prefixes_runtime_php_python_weights_non_evaluate_leaf_share_0_45_expect_impl_overlay_0_25_runtime_specific_capability_0_15_non_core_type_0_15_report_top_n_10_enforce_false_check_profile_governance_scan_config_check_spec_portability_non_regression_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
    io: io
    profile: default
    config: {}
```
