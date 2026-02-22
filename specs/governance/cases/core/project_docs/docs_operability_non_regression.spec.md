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
    - "{'root': '.', 'docs_operability_non_regression': {'baseline_path': '/specs/governance/metrics/docs_operability_baseline.json',
      'summary_fields': {'overall_docs_operability_ratio': 'non_decrease'}, 'segment_fields':
      {'book': {'mean_runnable_example_coverage_ratio': 'non_decrease'}, 'contract':
      {'mean_token_sync_compliance_ratio': 'non_decrease'}}, 'epsilon': 1e-12, 'docs_operability':
      {'reference_manifest': '/docs/book/reference_manifest.yaml'}}, 'check': {'profile':
      'governance.scan', 'config': {'check': 'docs.operability_non_regression'}},
      'use': [{'ref': '/specs/libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec',
      'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id',
      'policy.assert.scan_pass']}]}"
services:
  actions:
  - id: svc.root_docs_operability_non_regression_baseline_path_specs_governance_metrics_docs_operability_baseline_json_summary_fields_overall_docs_operability_ratio_non_decrease_segment_fields_book_mean_runnable_example_coverage_ratio_non_decrease_contract_mean_token_sync_compliance_ratio_non_decrease_epsilon_1e_12_docs_operability_reference_manifest_docs_book_reference_manifest_yaml_check_profile_governance_scan_config_check_docs_operability_non_regression_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    type: legacy.root_docs_operability_non_regression_baseline_path_specs_governance_metrics_docs_operability_baseline_json_summary_fields_overall_docs_operability_ratio_non_decrease_segment_fields_book_mean_runnable_example_coverage_ratio_non_decrease_contract_mean_token_sync_compliance_ratio_non_decrease_epsilon_1e_12_docs_operability_reference_manifest_docs_book_reference_manifest_yaml_check_profile_governance_scan_config_check_docs_operability_non_regression_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
    io: io
    profile: default
contracts:
- id: DCGOV-DOCS-OPER-002
  title: docs operability metric is non-regressing
  purpose: Enforces monotonic non-regression for docs operability metrics against
    checked-in baseline.
  clauses:
    imports:
    - artifact:
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
        - docs.operability_non_regression
      imports:
      - artifact:
        - summary_json
```
