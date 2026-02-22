```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'spec_lang_fixture_library_usage': {'path': '/specs/conformance/cases/core/spec_lang.spec.md',
      'required_library_path': '/specs/libraries/conformance/assertion_core.spec.md',
      'required_call_prefix': 'conf.', 'min_call_count': 4, 'required_case_ids': ['DCCONF-EXPR-001',
      'DCCONF-EXPR-002', 'DCCONF-EXPR-008']}, 'check': {'profile': 'governance.scan',
      'config': {'check': 'conformance.spec_lang_fixture_library_usage'}}, 'use':
      [{'ref': '/specs/libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec',
      'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id',
      'policy.assert.scan_pass']}]}"
services:
- type: legacy.root_spec_lang_fixture_library_usage_path_specs_conformance_cases_core_spec_lang_spec_md_required_library_path_specs_libraries_conformance_assertion_core_spec_md_required_call_prefix_conf_min_call_count_4_required_case_ids_dcconf_expr_001_dcconf_expr_002_dcconf_expr_008_check_profile_governance_scan_config_check_conformance_spec_lang_fixture_library_usage_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
  operations:
  - id: svc.root_spec_lang_fixture_library_usage_path_specs_conformance_cases_core_spec_lang_spec_md_required_library_path_specs_libraries_conformance_assertion_core_spec_md_required_call_prefix_conf_min_call_count_4_required_case_ids_dcconf_expr_001_dcconf_expr_002_dcconf_expr_008_check_profile_governance_scan_config_check_conformance_spec_lang_fixture_library_usage_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    mode: default
    direction: bidirectional
contracts:
  defaults:
    type: contract.check
  clauses:
  - id: DCGOV-CONF-LIB-EXPR-001
    title: spec_lang conformance fixture uses shared helper library calls
    purpose: Ensures spec_lang conformance fixtures reuse shared conformance helper
      library functions for repeated expression patterns.
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
          - conformance.spec_lang_fixture_library_usage
        imports:
        - from: artifact
          names:
          - summary_json
```
