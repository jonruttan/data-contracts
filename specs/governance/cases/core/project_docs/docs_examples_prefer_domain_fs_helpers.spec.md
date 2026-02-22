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
    - "{'root': '.', 'examples_prefer_domain_fs_helpers': {'files': ['docs/book/60_runner_and_gates.md', 'docs/book/90_reference_guide.md', 'specs/contract/04_harness.md']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'docs.examples_prefer_domain_fs_helpers'}}, 'use': [{'ref': '/specs/libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id', 'policy.assert.scan_pass']}]}"
services:
  actions:
  - id: svc.root_examples_prefer_domain_fs_helpers_files_docs_book_60_runner_and_gates_md_docs_book_90_reference_guide_md_specs_contract_04_harness_md_check_profile_governance_scan_config_check_docs_examples_prefer_domain_fs_helpers_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    type: legacy.root_examples_prefer_domain_fs_helpers_files_docs_book_60_runner_and_gates_md_docs_book_90_reference_guide_md_specs_contract_04_harness_md_check_profile_governance_scan_config_check_docs_examples_prefer_domain_fs_helpers_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
    io: io
    profile: default
contracts:
- id: DCGOV-DOCS-FS-EXAMPLES-001
  title: docs yaml examples prefer domain fs/path helpers over raw ops fs
  purpose: Keeps contributor-facing docs examples aligned with the domain-library-first authoring model for filesystem/json/glob/path flows.
  clauses:
    imports:
    - from: artifact
      names:
      - summary_json
    predicates:
    - id: assert_1
      assert:
        call:
        - var: policy.assert.summary_passed
        - std.object.assoc:
          - summary_json
          - var: summary_json
          - lit: {}
```
