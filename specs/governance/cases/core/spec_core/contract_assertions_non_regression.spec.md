```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'contract_assertions_non_regression': {'baseline_path': '/specs/governance/metrics/contract_assertions_baseline.json', 'summary_fields': {'overall_contract_assertions_ratio': 'non_decrease', 'overall_required_token_coverage_ratio': 'non_decrease', 'contract_must_coverage_ratio': 'non_decrease', 'token_sync_ratio': 'non_decrease'}, 'epsilon': 1e-12, 'contract_assertions': {'paths': ['specs/contract/03_assertions.md', 'specs/schema/schema_v1.md', 'docs/book/30_assertion_model.md', 'specs/contract/03b_spec_lang_v1.md']}}, 'check': {'profile': 'governance.scan', 'config': {'check': 'spec.contract_assertions_non_regression'}}, 'use': [{'ref': '/specs/libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id', 'policy.assert.scan_pass']}]}"
services:
- type: legacy.root_contract_assertions_non_regression_baseline_path_specs_governance_metrics_contract_assertions_baseline_json_summary_fields_overall_contract_assertions_ratio_non_decrease_overall_required_token_coverage_ratio_non_decrease_contract_must_coverage_ratio_non_decrease_token_sync_ratio_non_decrease_epsilon_1e_12_contract_assertions_paths_specs_contract_03_assertions_md_specs_schema_schema_v1_md_docs_book_30_assertion_model_md_specs_contract_03b_spec_lang_v1_md_check_profile_governance_scan_config_check_spec_contract_assertions_non_regression_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
  operations:
  - id: svc.root_contract_assertions_non_regression_baseline_path_specs_governance_metrics_contract_assertions_baseline_json_summary_fields_overall_contract_assertions_ratio_non_decrease_overall_required_token_coverage_ratio_non_decrease_contract_must_coverage_ratio_non_decrease_token_sync_ratio_non_decrease_epsilon_1e_12_contract_assertions_paths_specs_contract_03_assertions_md_specs_schema_schema_v1_md_docs_book_30_assertion_model_md_specs_contract_03b_spec_lang_v1_md_check_profile_governance_scan_config_check_spec_contract_assertions_non_regression_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    mode: default
    direction: bidirectional
contracts:
  clauses:
  - id: DCGOV-CONTRACT-ASSERT-002
    title: contract assertions metric is non-regressing
    purpose: Enforces monotonic non-regression for contract assertions metrics against checked-in baseline.
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
          - spec.contract_assertions_non_regression
        imports:
        - from: artifact
          names:
          - summary_json
```
