```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'docs_examples': {'files': ['docs/book/10_getting_started.md', 'docs/book/20_case_model.md', 'docs/book/30_assertion_model.md', 'docs/book/40_spec_lang_authoring.md', 'docs/book/60_runner_and_gates.md', 'docs/book/80_troubleshooting.md', 'docs/book/90_reference_guide.md', 'docs/development.md']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'docs.examples_runnable'}}, 'use': [{'ref': '/specs/libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id', 'policy.assert.scan_pass']}]}"
contracts:
  clauses:
  - id: DCGOV-DOCS-REF-004
    title: reference examples parse or are explicitly opted out
    purpose: Ensures reference examples are trustworthy by requiring parseable or statically valid fenced examples unless explicitly opted out.
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
          - docs.examples_runnable
        imports:
        - from: artifact
          names:
          - summary_json
adapters:
- type: legacy.root_docs_examples_files_docs_book_10_getting_started_md_docs_book_20_case_model_md_docs_book_30_assertion_model_md_docs_book_40_spec_lang_authoring_md_docs_book_60_runner_and_gates_md_docs_book_80_troubleshooting_md_docs_book_90_reference_guide_md_docs_development_md_check_profile_governance_scan_config_check_docs_examples_runnable_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
  actions:
  - id: svc.root_docs_examples_files_docs_book_10_getting_started_md_docs_book_20_case_model_md_docs_book_30_assertion_model_md_docs_book_40_spec_lang_authoring_md_docs_book_60_runner_and_gates_md_docs_book_80_troubleshooting_md_docs_book_90_reference_guide_md_docs_development_md_check_profile_governance_scan_config_check_docs_examples_runnable_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    direction: bidirectional
    profile: default
services:
- id: svc.root_docs_examples_files_docs_book_10_getting_started_md_docs_book_20_case_model_md_docs_book_30_assertion_model_md_docs_book_40_spec_lang_authoring_md_docs_book_60_runner_and_gates_md_docs_book_80_troubleshooting_md_docs_book_90_reference_guide_md_docs_development_md_check_profile_governance_scan_config_check_docs_examples_runnable_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
  consumes:
  - svc.root_docs_examples_files_docs_book_10_getting_started_md_docs_book_20_case_model_md_docs_book_30_assertion_model_md_docs_book_40_spec_lang_authoring_md_docs_book_60_runner_and_gates_md_docs_book_80_troubleshooting_md_docs_book_90_reference_guide_md_docs_development_md_check_profile_governance_scan_config_check_docs_examples_runnable_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
```
