```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'policy_library_usage_non_regression': {'baseline_path': '/specs/governance/metrics/spec_lang_adoption_baseline.json',
      'summary_fields': {'governance_library_backed_policy_ratio': 'non_decrease'},
      'segment_fields': {'governance': {'library_backed_policy_ratio': 'non_decrease'}},
      'epsilon': 1e-12, 'spec_lang_adoption': {'roots': ['/specs/conformance/cases',
      '/specs/governance/cases', 'runner-owned implementation specs'], 'segment_rules':
      [{'prefix': 'specs/conformance/cases', 'segment': 'conformance'}, {'prefix':
      'specs/governance/cases', 'segment': 'governance'}, {'prefix': 'runner-owned
      implementation specs', 'segment': 'impl'}], 'recursive': True}}, 'check': {'profile':
      'governance.scan', 'config': {'check': 'governance.policy_library_usage_non_regression'}},
      'use': [{'ref': '/specs/libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec',
      'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id',
      'policy.assert.scan_pass']}]}"
services:
- id: svc.root_policy_library_usage_non_regression_baseline_path_specs_governance_metrics_spec_lang_adoption_baseline_json_summary_fields_governance_library_backed_policy_ratio_non_decrease_segment_fields_governance_library_backed_policy_ratio_non_decrease_epsilon_1e_12_spec_lang_adoption_roots_specs_conformance_cases_specs_governance_cases_runner_owned_implementation_specs_segment_rules_prefix_specs_conformance_cases_segment_conformance_prefix_specs_governance_cases_segment_governance_prefix_runner_owned_implementation_specs_segment_impl_recursive_true_check_profile_governance_scan_config_check_governance_policy_library_usage_non_regression_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
  type: legacy.root_policy_library_usage_non_regression_baseline_path_specs_governance_metrics_spec_lang_adoption_baseline_json_summary_fields_governance_library_backed_policy_ratio_non_decrease_segment_fields_governance_library_backed_policy_ratio_non_decrease_epsilon_1e_12_spec_lang_adoption_roots_specs_conformance_cases_specs_governance_cases_runner_owned_implementation_specs_segment_rules_prefix_specs_conformance_cases_segment_conformance_prefix_specs_governance_cases_segment_governance_prefix_runner_owned_implementation_specs_segment_impl_recursive_true_check_profile_governance_scan_config_check_governance_policy_library_usage_non_regression_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
  mode: default
  direction: bidirectional
contracts:
- id: DCGOV-POLICY-LIB-001
  title: governance library-backed policy usage is non-regressing
  purpose: Enforces monotonic non-regression for governance policy expressions that
    use shared spec-lang libraries.
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
        - governance.policy_library_usage_non_regression
      imports:
      - from: artifact
        names:
        - summary_json
```
