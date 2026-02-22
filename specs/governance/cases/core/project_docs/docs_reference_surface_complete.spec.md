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
    - "{'root': '.', 'docs_reference_surface': {'required_files': ['docs/book/reference_index.md', 'specs/schema/schema_v1.md', 'specs/contract/10_docs_quality.md', 'docs/book/05_what_is_data_contracts.md', 'docs/book/10_getting_started.md', 'docs/book/15_spec_lifecycle.md', 'docs/book/20_case_model.md', 'docs/book/25_system_topology.md', 'docs/book/30_assertion_model.md', 'docs/book/35_usage_guides_index.md', 'docs/book/guides/index.md', 'docs/book/guides/guide_01_onboarding.md', 'docs/book/guides/guide_02_first_spec_authoring.md', 'docs/book/guides/guide_03_running_checks_and_gates.md', 'docs/book/guides/guide_04_debugging_failures.md', 'docs/book/guides/guide_05_release_and_change_control.md', 'docs/book/guides/guide_06_governance_tuning.md', 'docs/book/guides/guide_07_schema_extension_workflow.md', 'docs/book/guides/guide_08_ci_integration.md', 'docs/book/guides/guide_09_status_exchange_operations.md', 'docs/book/guides/guide_10_reference_navigation_patterns.md', 'docs/book/40_spec_lang_authoring.md', 'docs/book/50_library_authoring.md', 'docs/book/60_runner_and_gates.md', 'docs/book/65_runner_status_and_compatibility.md', 'docs/book/70_governance_and_quality.md', 'docs/book/80_troubleshooting.md', 'docs/book/90_reference_guide.md', 'docs/book/99_generated_reference_index.md', 'docs/book/93_appendix_spec_lang_builtin_catalog.md', 'docs/book/93a_std_core.md', 'docs/book/93b_std_logic.md', 'docs/book/93c_std_math.md', 'docs/book/93d_std_string.md', 'docs/book/93e_std_collection.md', 'docs/book/93f_std_object.md', 'docs/book/93g_std_type.md', 'docs/book/93h_std_set.md', 'docs/book/93i_std_json_schema_fn_null.md', 'docs/book/93n_spec_case_templates_reference.md'], 'required_globs': ['specs/contract/*.md']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'docs.reference_surface_complete'}}, 'use': [{'ref': '/specs/libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id', 'policy.assert.scan_pass']}]}"
services:
  actions:
  - id: svc.root_docs_reference_surface_required_files_docs_book_reference_index_md_specs_schema_schema_v1_md_specs_contract_10_docs_quality_md_docs_book_05_what_is_data_contracts_md_docs_book_10_getting_started_md_docs_book_15_spec_lifecycle_md_docs_book_20_case_model_md_docs_book_25_system_topology_md_docs_book_30_assertion_model_md_docs_book_35_usage_guides_index_md_docs_book_guides_index_md_docs_book_guides_guide_01_onboarding_md_docs_book_guides_guide_02_first_spec_authoring_md_docs_book_guides_guide_03_running_checks_and_gates_md_docs_book_guides_guide_04_debugging_failures_md_docs_book_guides_guide_05_release_and_change_control_md_docs_book_guides_guide_06_governance_tuning_md_docs_book_guides_guide_07_schema_extension_workflow_md_docs_book_guides_guide_08_ci_integration_md_docs_book_guides_guide_09_status_exchange_operations_md_docs_book_guides_guide_10_reference_navigation_patterns_md_docs_book_40_spec_lang_authoring_md_docs_book_50_library_authoring_md_docs_book_60_runner_and_gates_md_docs_book_65_runner_status_and_compatibility_md_docs_book_70_governance_and_quality_md_docs_book_80_troubleshooting_md_docs_book_90_reference_guide_md_docs_book_99_generated_reference_index_md_docs_book_93_appendix_spec_lang_builtin_catalog_md_docs_book_93a_std_core_md_docs_book_93b_std_logic_md_docs_book_93c_std_math_md_docs_book_93d_std_string_md_docs_book_93e_std_collection_md_docs_book_93f_std_object_md_docs_book_93g_std_type_md_docs_book_93h_std_set_md_docs_book_93i_std_json_schema_fn_null_md_docs_book_93n_spec_case_templates_reference_md_required_globs_specs_contract_md_check_profile_governance_scan_config_check_docs_reference_surface_complete_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    type: legacy.root_docs_reference_surface_required_files_docs_book_reference_index_md_specs_schema_schema_v1_md_specs_contract_10_docs_quality_md_docs_book_05_what_is_data_contracts_md_docs_book_10_getting_started_md_docs_book_15_spec_lifecycle_md_docs_book_20_case_model_md_docs_book_25_system_topology_md_docs_book_30_assertion_model_md_docs_book_35_usage_guides_index_md_docs_book_guides_index_md_docs_book_guides_guide_01_onboarding_md_docs_book_guides_guide_02_first_spec_authoring_md_docs_book_guides_guide_03_running_checks_and_gates_md_docs_book_guides_guide_04_debugging_failures_md_docs_book_guides_guide_05_release_and_change_control_md_docs_book_guides_guide_06_governance_tuning_md_docs_book_guides_guide_07_schema_extension_workflow_md_docs_book_guides_guide_08_ci_integration_md_docs_book_guides_guide_09_status_exchange_operations_md_docs_book_guides_guide_10_reference_navigation_patterns_md_docs_book_40_spec_lang_authoring_md_docs_book_50_library_authoring_md_docs_book_60_runner_and_gates_md_docs_book_65_runner_status_and_compatibility_md_docs_book_70_governance_and_quality_md_docs_book_80_troubleshooting_md_docs_book_90_reference_guide_md_docs_book_99_generated_reference_index_md_docs_book_93_appendix_spec_lang_builtin_catalog_md_docs_book_93a_std_core_md_docs_book_93b_std_logic_md_docs_book_93c_std_math_md_docs_book_93d_std_string_md_docs_book_93e_std_collection_md_docs_book_93f_std_object_md_docs_book_93g_std_type_md_docs_book_93h_std_set_md_docs_book_93i_std_json_schema_fn_null_md_docs_book_93n_spec_case_templates_reference_md_required_globs_specs_contract_md_check_profile_governance_scan_config_check_docs_reference_surface_complete_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
    io: io
    profile: default
contracts:
- id: DCGOV-DOCS-REF-001
  title: docs reference surface files exist
  purpose: Enforces that the canonical docs reference surface remains complete and cannot silently lose required files.
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
        - docs.reference_surface_complete
      imports:
      - from: artifact
        names:
        - summary_json
```
