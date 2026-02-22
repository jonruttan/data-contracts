```yaml contract-spec
spec_version: 2
schema_ref: "/specs/01_schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'compatibility_matrix': {'path': '/specs/02_contracts/25_compatibility_matrix.md', 'required_tokens': ['- `required`:', '- `compatibility_non_blocking`:', '- `rust`', '- `python`', '- `php`', '- `node`', '- `c`']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.compatibility_matrix_registration_required'}}, 'use': [{'ref': '/specs/05_libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id', 'policy.assert.scan_pass']}]}"
contracts:
  clauses:
  - id: DCGOV-RUNTIME-CONFIG-008
    title: compatibility matrix registration is explicit
    purpose: Ensures runtime lanes are registered in the compatibility matrix contract before use.
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
adapters:
- type: legacy.root_compatibility_matrix_path_specs_contract_25_compatibility_matrix_md_required_tokens_required_compatibility_non_blocking_rust_python_php_node_c_check_profile_governance_scan_config_check_runtime_compatibility_matrix_registration_required_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
  actions:
  - id: svc.root_compatibility_matrix_path_specs_contract_25_compatibility_matrix_md_required_tokens_required_compatibility_non_blocking_rust_python_php_node_c_check_profile_governance_scan_config_check_runtime_compatibility_matrix_registration_required_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    direction: bidirectional
    profile: default
services:
- id: svc.root_compatibility_matrix_path_specs_contract_25_compatibility_matrix_md_required_tokens_required_compatibility_non_blocking_rust_python_php_node_c_check_profile_governance_scan_config_check_runtime_compatibility_matrix_registration_required_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
  consumes:
  - svc.root_compatibility_matrix_path_specs_contract_25_compatibility_matrix_md_required_tokens_required_compatibility_non_blocking_rust_python_php_node_c_check_profile_governance_scan_config_check_runtime_compatibility_matrix_registration_required_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
```
