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
    - "{'root': '.', 'conformance_library_contract_cases_present': {'path': '/specs/conformance/cases/core/spec_lang_library_contract.spec.md', 'required_case_ids': ['DCCONF-LIB-CONTRACT-001', 'DCCONF-LIB-CONTRACT-002', 'DCCONF-LIB-CONTRACT-003']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'conformance.library_contract_cases_present'}}, 'use': [{'ref': '/specs/libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id', 'policy.assert.scan_pass']}]}"
services:
  actions:
  - id: svc.root_conformance_library_contract_cases_present_path_specs_conformance_cases_core_spec_lang_library_contract_spec_md_required_case_ids_dcconf_lib_contract_001_dcconf_lib_contract_002_dcconf_lib_contract_003_check_profile_governance_scan_config_check_conformance_library_contract_cases_present_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    type: legacy.root_conformance_library_contract_cases_present_path_specs_conformance_cases_core_spec_lang_library_contract_spec_md_required_case_ids_dcconf_lib_contract_001_dcconf_lib_contract_002_dcconf_lib_contract_003_check_profile_governance_scan_config_check_conformance_library_contract_cases_present_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
    io: io
    profile: default
contracts:
- id: DCGOV-CONF-LIB-CONTRACT-001
  title: conformance library contract coverage cases are present
  purpose: Ensures conformance includes executable evaluate-based coverage for flat spec_lang.export defines contract behavior.
  clauses:
    imports:
    - from: artifact
      names:
      - summary_json
    predicates:
    - id: assert_1
      assert:
        call:
        - var: policy.assert.summary_check_id
        - std.object.assoc:
          - summary_json
          - var: summary_json
          - lit: {}
        - conformance.library_contract_cases_present
```
