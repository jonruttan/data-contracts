```yaml contract-spec
spec_version: 2
schema_ref: "/specs/01_schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'python_dependency_non_regression': {'baseline_path': '/specs/04_governance/metrics/python_dependency_baseline.json', 'summary_fields': {'non_python_lane_python_exec_count': 'non_increase', 'transitive_adapter_python_exec_count': 'non_increase', 'python_usage_scope_violation_count': 'non_increase', 'default_lane_python_free_ratio': 'non_decrease'}, 'segment_fields': {}, 'epsilon': 1e-12, 'python_dependency': {}}, 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.compatibility_python_lane_dependency_non_regression'}}, 'use': [{'ref': '/specs/05_libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id', 'policy.assert.scan_pass']}]}"
contracts:
  clauses:
  - id: DCGOV-RUNTIME-PYDEP-002
    title: python dependency metric is non-regressing
    purpose: Enforces monotonic non-regression for python dependency metrics against checked-in baseline.
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
          - runtime.compatibility_python_lane_dependency_non_regression
        imports:
        - from: artifact
          names:
          - summary_json
adapters:
- type: legacy.root_python_dependency_non_regression_baseline_path_specs_governance_metrics_python_dependency_baseline_json_summary_fields_non_python_lane_python_exec_count_non_increase_transitive_adapter_python_exec_count_non_increase_python_usage_scope_violation_count_non_increase_default_lane_python_free_ratio_non_decrease_segment_fields_epsilon_1e_12_python_dependency_check_profile_governance_scan_config_check_runtime_compatibility_python_lane_dependency_non_regression_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
  actions:
  - id: svc.root_python_dependency_non_regression_baseline_path_specs_governance_metrics_python_dependency_baseline_json_summary_fields_non_python_lane_python_exec_count_non_increase_transitive_adapter_python_exec_count_non_increase_python_usage_scope_violation_count_non_increase_default_lane_python_free_ratio_non_decrease_segment_fields_epsilon_1e_12_python_dependency_check_profile_governance_scan_config_check_runtime_compatibility_python_lane_dependency_non_regression_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    direction: bidirectional
    profile: default
services:
- id: svc.root_python_dependency_non_regression_baseline_path_specs_governance_metrics_python_dependency_baseline_json_summary_fields_non_python_lane_python_exec_count_non_increase_transitive_adapter_python_exec_count_non_increase_python_usage_scope_violation_count_non_increase_default_lane_python_free_ratio_non_decrease_segment_fields_epsilon_1e_12_python_dependency_check_profile_governance_scan_config_check_runtime_compatibility_python_lane_dependency_non_regression_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
  consumes:
  - svc.root_python_dependency_non_regression_baseline_path_specs_governance_metrics_python_dependency_baseline_json_summary_fields_non_python_lane_python_exec_count_non_increase_transitive_adapter_python_exec_count_non_increase_python_usage_scope_violation_count_non_increase_default_lane_python_free_ratio_non_decrease_segment_fields_epsilon_1e_12_python_dependency_check_profile_governance_scan_config_check_runtime_compatibility_python_lane_dependency_non_regression_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
```
