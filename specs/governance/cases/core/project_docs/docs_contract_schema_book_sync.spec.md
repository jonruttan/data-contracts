```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'doc_sync': {'files': ['docs/book/30_assertion_model.md', 'specs/contract/03_assertions.md',
      'specs/schema/schema_v1.md'], 'tokens': ['MUST', 'MAY', 'MUST_NOT', 'contract.imports']},
      'check': {'profile': 'governance.scan', 'config': {'check': 'docs.contract_schema_book_sync'}},
      'use': [{'ref': '/specs/libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec',
      'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id',
      'policy.assert.scan_pass']}]}"
services:
- type: legacy.root_doc_sync_files_docs_book_30_assertion_model_md_specs_contract_03_assertions_md_specs_schema_schema_v1_md_tokens_must_may_must_not_contract_imports_check_profile_governance_scan_config_check_docs_contract_schema_book_sync_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
  operations:
  - id: svc.root_doc_sync_files_docs_book_30_assertion_model_md_specs_contract_03_assertions_md_specs_schema_schema_v1_md_tokens_must_may_must_not_contract_imports_check_profile_governance_scan_config_check_docs_contract_schema_book_sync_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    mode: default
    direction: bidirectional
contracts:
  defaults:
    type: contract.check
  clauses:
  - id: DCGOV-DOCS-REF-006
    title: assertion tokens stay aligned across book contract and schema docs
    purpose: Ensures core assertion terminology remains synchronized across author-facing
      and normative specification documents.
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
          - docs.contract_schema_book_sync
        imports:
        - from: artifact
          names:
          - summary_json
```
