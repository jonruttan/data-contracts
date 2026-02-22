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
    - "{'root': '.', 'filename_policy': {'paths': ['docs'], 'include_extensions': ['.md', '.yaml', '.yml', '.json'], 'allow_exact': ['README.md'], 'allowed_name_regex': '^[a-z0-9]+(?:_[a-z0-9]+)*(?:-[a-z0-9]+(?:_[a-z0-9]+)*)*(?:\\\\.spec)?\\\\.(?:md|yaml|yml|json)$'}, 'check': {'profile': 'governance.scan', 'config': {'check': 'naming.filename_policy'}}, 'use': [{'ref': '/specs/libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id', 'policy.assert.scan_pass']}]}"
services:
  entries:
  - id: svc.root_filename_policy_paths_docs_include_extensions_md_yaml_yml_json_allow_exact_readme_md_allowed_name_regex_a_z0_9_a_z0_9_a_z0_9_a_z0_9_spec_md_yaml_yml_json_check_profile_governance_scan_config_check_naming_filename_policy_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    type: legacy.root_filename_policy_paths_docs_include_extensions_md_yaml_yml_json_allow_exact_readme_md_allowed_name_regex_a_z0_9_a_z0_9_a_z0_9_a_z0_9_spec_md_yaml_yml_json_check_profile_governance_scan_config_check_naming_filename_policy_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
    io: io
    profile: default
    config: {}
contracts:
- id: DCGOV-DOCS-NAME-001
  title: docs filenames follow lowercase separator policy
  purpose: Enforces deterministic docs filename shape using underscores for words and hyphens for section separators.
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
        - naming.filename_policy
      imports:
      - from: artifact
        names:
        - summary_json
```
