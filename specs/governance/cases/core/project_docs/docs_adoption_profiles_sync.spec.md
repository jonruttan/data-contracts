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
    - "{'root': '.', 'adoption_profiles': {'files': ['README.md', 'docs/development.md'],
      'required_tokens': ['Core profile', 'Full profile', 'make core-check', 'make
      check']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'docs.adoption_profiles_sync'}},
      'use': [{'ref': '/specs/libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec',
      'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id',
      'policy.assert.scan_pass']}]}"
services:
- id: svc.root_adoption_profiles_files_readme_md_docs_development_md_required_tokens_core_profile_full_profile_make_core_check_make_check_check_profile_governance_scan_config_check_docs_adoption_profiles_sync_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
  type: legacy.root_adoption_profiles_files_readme_md_docs_development_md_required_tokens_core_profile_full_profile_make_core_check_make_check_check_profile_governance_scan_config_check_docs_adoption_profiles_sync_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
  mode: default
  direction: bidirectional
contracts:
- id: DCGOV-DOCS-REF-009
  title: core and full adoption profile docs stay synchronized
  purpose: Keeps contributor-facing docs aligned on core-check and full-check adoption
    profile wording.
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
        - docs.adoption_profiles_sync
      imports:
      - from: artifact
        names:
        - summary_json
```
