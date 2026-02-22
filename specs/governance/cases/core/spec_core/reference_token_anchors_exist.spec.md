```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'token_anchors': {'files': [{'path': '/specs/contract/03b_spec_lang_v1.md', 'tokens': ['operator-keyed mapping AST']}]}, 'check': {'profile': 'governance.scan', 'config': {'check': 'reference.token_anchors_exist'}}, 'use': [{'ref': '/specs/libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id', 'policy.assert.scan_pass']}]}"
contracts:
  clauses:
  - id: DCGOV-REF-TOKENS-001
    title: configured token anchors exist
    purpose: Ensures configured token anchors resolve to existing files and token matches.
    asserts:
      imports:
      - from: artifact
        names:
        - summary_json
      checks:
      - id: assert_1
        assert:
          call:
          - var: policy.assert.summary_check_id
          - std.object.assoc:
            - summary_json
            - var: summary_json
            - lit: {}
          - reference.token_anchors_exist
adapters:
- type: legacy.root_token_anchors_files_path_specs_contract_03b_spec_lang_v1_md_tokens_operator_keyed_mapping_ast_check_profile_governance_scan_config_check_reference_token_anchors_exist_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
  actions:
  - id: svc.root_token_anchors_files_path_specs_contract_03b_spec_lang_v1_md_tokens_operator_keyed_mapping_ast_check_profile_governance_scan_config_check_reference_token_anchors_exist_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    direction: bidirectional
    profile: default
services:
- id: svc.root_token_anchors_files_path_specs_contract_03b_spec_lang_v1_md_tokens_operator_keyed_mapping_ast_check_profile_governance_scan_config_check_reference_token_anchors_exist_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
  consumes:
  - svc.root_token_anchors_files_path_specs_contract_03b_spec_lang_v1_md_tokens_operator_keyed_mapping_ast_check_profile_governance_scan_config_check_reference_token_anchors_exist_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
```
