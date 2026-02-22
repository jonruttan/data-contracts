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
    - "{'root': '.', 'conformance_evaluate_first_non_regression': {'baseline_path': '/specs/governance/metrics/spec_lang_adoption_baseline.json', 'segment_fields': {'conformance': {'mean_logic_self_contained_ratio': 'non_decrease'}}, 'epsilon': 1e-12, 'spec_lang_adoption': {'roots': ['/specs/conformance/cases'], 'segment_rules': [{'prefix': 'specs/conformance/cases', 'segment': 'conformance'}], 'recursive': True}}, 'check': {'profile': 'governance.scan', 'config': {'check': 'conformance.evaluate_first_ratio_non_regression'}}, 'use': [{'ref': '/specs/libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id', 'policy.assert.scan_pass']}]}"
services:
  actions:
  - id: svc.root_conformance_evaluate_first_non_regression_baseline_path_specs_governance_metrics_spec_lang_adoption_baseline_json_segment_fields_conformance_mean_logic_self_contained_ratio_non_decrease_epsilon_1e_12_spec_lang_adoption_roots_specs_conformance_cases_segment_rules_prefix_specs_conformance_cases_segment_conformance_recursive_true_check_profile_governance_scan_config_check_conformance_evaluate_first_ratio_non_regression_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    type: legacy.root_conformance_evaluate_first_non_regression_baseline_path_specs_governance_metrics_spec_lang_adoption_baseline_json_segment_fields_conformance_mean_logic_self_contained_ratio_non_decrease_epsilon_1e_12_spec_lang_adoption_roots_specs_conformance_cases_segment_rules_prefix_specs_conformance_cases_segment_conformance_recursive_true_check_profile_governance_scan_config_check_conformance_evaluate_first_ratio_non_regression_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
    io: io
    profile: default
contracts:
- id: DCGOV-CONF-SPECLANG-002
  title: conformance evaluate-first ratio is non-regressing
  purpose: Enforces ratchet-style non-regression for conformance evaluate coverage against the checked-in spec-lang adoption baseline.
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
        - conformance.evaluate_first_ratio_non_regression
      imports:
      - from: artifact
        names:
        - summary_json
```
