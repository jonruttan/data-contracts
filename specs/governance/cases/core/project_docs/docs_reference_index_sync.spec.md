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
    - "{'root': '.', 'reference_index': {'path': '/docs/book/reference_index.md', 'include_glob': 'docs/book/*.md', 'exclude_files': ['docs/book/index.md', 'docs/book/reference_index.md', 'docs/book/reference_coverage.md']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'docs.reference_index_sync'}}, 'use': [{'ref': '/specs/libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id', 'policy.assert.scan_pass']}]}"
services:
  entries:
  - id: svc.root_reference_index_path_docs_book_reference_index_md_include_glob_docs_book_md_exclude_files_docs_book_index_md_docs_book_reference_index_md_docs_book_reference_coverage_md_check_profile_governance_scan_config_check_docs_reference_index_sync_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    type: legacy.root_reference_index_path_docs_book_reference_index_md_include_glob_docs_book_md_exclude_files_docs_book_index_md_docs_book_reference_index_md_docs_book_reference_coverage_md_check_profile_governance_scan_config_check_docs_reference_index_sync_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
    io: io
    profile: default
    config: {}
contracts:
- id: DCGOV-DOCS-REF-002
  title: reference index stays synced with chapter files
  purpose: Ensures the machine-checked reference index entries stay aligned with the actual chapter set and order.
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
        - docs.reference_index_sync
      imports:
      - from: artifact
        names:
        - summary_json
```
