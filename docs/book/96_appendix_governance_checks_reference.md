# Governance Checks Reference

```yaml doc-meta
doc_id: DOC-REF-096
title: Appendix Governance Checks Reference
status: active
audience: reviewer
owns_tokens:
- appendix_governance_checks_reference
requires_tokens:
- governance_workflow_quickpath
commands:
- run: ./scripts/runner_adapter.sh docs-generate-check
  purpose: Verify generated governance check catalog remains synchronized.
examples:
- id: EX-APP-GOVCHECK-001
  runnable: false
  opt_out_reason: Generated reference page intentionally contains no runnable fenced examples.
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

This page is machine-generated from governance check registrations and case mappings.

## Purpose

Provide generated inventory of governance check IDs and case coverage.

## Inputs

- governance check registry and governance case files

## Outputs

- deterministic check-id coverage table

## Failure Modes

- stale generated block after check/case changes
- missing generated markers
- check-to-case mapping drift

<!-- GENERATED:START governance_check_catalog -->

## Generated Governance Check Catalog

- check_count: 266
- checks_with_cases: 257
- checks_without_cases: 9

| check_id | case_count | has_case |
|---|---|---|
| `architecture.harness_local_workflow_duplication_forbidden` | 1 | true |
| `architecture.harness_workflow_components_required` | 1 | true |
| `assert.adapter_projection_contract_sync` | 1 | true |
| `assert.compiler_schema_matrix_sync` | 1 | true |
| `assert.domain_library_usage_required` | 1 | true |
| `assert.domain_profiles_docs_sync` | 1 | true |
| `assert.spec_lang_builtin_surface_sync` | 1 | true |
| `assert.subject_profiles_declared` | 1 | true |
| `assert.subject_profiles_json_only` | 1 | true |
| `assert.sugar_compile_only_sync` | 1 | true |
| `assert.type_contract_subject_semantics_sync` | 1 | true |
| `assert.universal_core_sync` | 1 | true |
| `conformance.api_http_portable_shape` | 1 | true |
| `conformance.case_doc_style_guard` | 1 | true |
| `conformance.case_index_sync` | 1 | true |
| `conformance.evaluate_first_ratio_non_regression` | 1 | true |
| `conformance.extension_requires_capabilities` | 1 | true |
| `conformance.library_contract_cases_present` | 1 | true |
| `conformance.library_policy_usage_required` | 1 | true |
| `conformance.no_ambient_assumptions` | 1 | true |
| `conformance.no_runner_logic_outside_harness` | 1 | true |
| `conformance.portable_determinism_guard` | 1 | true |
| `conformance.purpose_quality_gate` | 1 | true |
| `conformance.purpose_warning_codes_sync` | 1 | true |
| `conformance.spec_lang_fixture_library_usage` | 1 | true |
| `conformance.spec_lang_preferred` | 1 | true |
| `conformance.type_contract_docs` | 1 | true |
| `conformance.type_contract_field_sync` | 1 | true |
| `contract.coverage_threshold` | 1 | true |
| `contract.governance_check` | 1 | true |
| `docs.adoption_profiles_sync` | 1 | true |
| `docs.api_http_tutorial_sync` | 1 | true |
| `docs.book_chapter_order_canonical` | 1 | true |
| `docs.cli_flags_documented` | 1 | true |
| `docs.command_examples_verified` | 1 | true |
| `docs.contract_schema_book_sync` | 1 | true |
| `docs.current_spec_only_contract` | 1 | true |
| `docs.current_spec_policy_key_names` | 1 | true |
| `docs.docgen_quality_score_threshold` | 1 | true |
| `docs.example_id_uniqueness` | 1 | true |
| `docs.examples_prefer_domain_fs_helpers` | 1 | true |
| `docs.examples_runnable` | 1 | true |
| `docs.filename_policy` | 1 | true |
| `docs.generate_check_passes` | 0 | false |
| `docs.generated_files_clean` | 1 | true |
| `docs.generated_sections_read_only` | 1 | true |
| `docs.generation_registry_surface_case_sync` | 0 | false |
| `docs.generation_spec_cases_present` | 0 | false |
| `docs.generator_outputs_sync` | 1 | true |
| `docs.generator_registry_valid` | 1 | true |
| `docs.governance_check_catalog_sync` | 1 | true |
| `docs.harness_reference_semantics_complete` | 1 | true |
| `docs.harness_type_catalog_sync` | 1 | true |
| `docs.history_reviews_namespace` | 1 | true |
| `docs.index_filename_policy` | 1 | true |
| `docs.instructions_complete` | 1 | true |
| `docs.layout_canonical_trees` | 1 | true |
| `docs.make_commands_sync` | 1 | true |
| `docs.markdown_namespace_legacy_alias_forbidden` | 1 | true |
| `docs.markdown_structured_assertions_required` | 1 | true |
| `docs.meta_schema_valid` | 1 | true |
| `docs.metrics_field_catalog_sync` | 1 | true |
| `docs.no_os_artifact_files` | 1 | true |
| `docs.operability_metric` | 1 | true |
| `docs.operability_non_regression` | 1 | true |
| `docs.output_mode_contract_valid` | 0 | false |
| `docs.policy_rule_catalog_sync` | 1 | true |
| `docs.reference_index_sync` | 1 | true |
| `docs.reference_manifest_sync` | 1 | true |
| `docs.reference_namespace_chapters_sync` | 1 | true |
| `docs.reference_surface_complete` | 1 | true |
| `docs.regex_doc_sync` | 1 | true |
| `docs.release_contract_automation_policy` | 1 | true |
| `docs.required_sections` | 1 | true |
| `docs.runner_api_catalog_sync` | 1 | true |
| `docs.runner_reference_semantics_complete` | 1 | true |
| `docs.security_warning_contract` | 1 | true |
| `docs.spec_lang_builtin_catalog_sync` | 1 | true |
| `docs.spec_schema_field_catalog_sync` | 1 | true |
| `docs.stdlib_examples_complete` | 1 | true |
| `docs.stdlib_symbol_docs_complete` | 1 | true |
| `docs.template_data_sources_declared` | 0 | false |
| `docs.template_paths_valid` | 0 | false |
| `docs.token_dependency_resolved` | 1 | true |
| `docs.token_ownership_unique` | 1 | true |
| `docs.traceability_catalog_sync` | 1 | true |
| `docs.v1_scope_contract` | 1 | true |
| `governance.extractor_only_no_verdict_branching` | 1 | true |
| `governance.policy_evaluate_required` | 1 | true |
| `governance.policy_library_usage_non_regression` | 1 | true |
| `governance.policy_library_usage_required` | 1 | true |
| `governance.structured_assertions_required` | 1 | true |
| `impl.evaluate_first_required` | 1 | true |
| `impl.evaluate_ratio_non_regression` | 1 | true |
| `impl.library_usage_non_regression` | 1 | true |
| `library.colocated_symbol_tests_required` | 1 | true |
| `library.domain_index_sync` | 1 | true |
| `library.domain_ownership` | 1 | true |
| `library.legacy_definitions_key_forbidden` | 1 | true |
| `library.public_surface_model` | 1 | true |
| `library.single_public_symbol_per_case_required` | 1 | true |
| `library.verb_first_schema_keys_required` | 1 | true |
| `naming.filename_policy` | 1 | true |
| `normalization.docs_token_sync` | 1 | true |
| `normalization.library_mapping_ast_only` | 1 | true |
| `normalization.mapping_ast_only` | 1 | true |
| `normalization.profile_sync` | 1 | true |
| `normalization.spec_style_sync` | 1 | true |
| `normalization.virtual_root_paths_only` | 1 | true |
| `objective.scorecard_metric` | 1 | true |
| `objective.scorecard_non_regression` | 1 | true |
| `objective.tripwires_clean` | 1 | true |
| `orchestration.ops_capability_bindings` | 1 | true |
| `orchestration.ops_legacy_underscore_forbidden` | 1 | true |
| `orchestration.ops_registry_sync` | 1 | true |
| `orchestration.ops_symbol_grammar` | 1 | true |
| `pending.no_resolved_markers` | 1 | true |
| `reference.check_ids_exist` | 1 | true |
| `reference.contract_paths_exist` | 1 | true |
| `reference.external_refs_policy` | 1 | true |
| `reference.library_exports_used` | 1 | true |
| `reference.policy_symbols_resolve` | 1 | true |
| `reference.private_symbols_forbidden` | 1 | true |
| `reference.symbols_exist` | 1 | true |
| `reference.token_anchors_exist` | 1 | true |
| `runtime.api_http_cors_support` | 1 | true |
| `runtime.api_http_live_mode_explicit` | 1 | true |
| `runtime.api_http_oauth_docs_sync` | 1 | true |
| `runtime.api_http_oauth_env_only` | 1 | true |
| `runtime.api_http_oauth_no_secret_literals` | 1 | true |
| `runtime.api_http_parity_contract_sync` | 1 | true |
| `runtime.api_http_scenario_roundtrip` | 1 | true |
| `runtime.api_http_verb_suite` | 1 | true |
| `runtime.assert_block_decision_authority_required` | 1 | true |
| `runtime.assertions_via_spec_lang` | 1 | true |
| `runtime.case_contract_block_required` | 1 | true |
| `runtime.chain_contract_single_location` | 1 | true |
| `runtime.chain_cycle_forbidden` | 1 | true |
| `runtime.chain_exports_explicit_only` | 1 | true |
| `runtime.chain_exports_from_key_required` | 1 | true |
| `runtime.chain_exports_legacy_forbidden` | 1 | true |
| `runtime.chain_exports_list_only_required` | 1 | true |
| `runtime.chain_exports_target_derived_only` | 1 | true |
| `runtime.chain_fail_fast_default` | 1 | true |
| `runtime.chain_import_alias_collision_forbidden` | 1 | true |
| `runtime.chain_imports_consumer_surface_unchanged` | 1 | true |
| `runtime.chain_legacy_from_forbidden` | 1 | true |
| `runtime.chain_library_symbol_exports_valid` | 1 | true |
| `runtime.chain_ref_scalar_required` | 1 | true |
| `runtime.chain_reference_resolution` | 1 | true |
| `runtime.chain_shared_context_required` | 1 | true |
| `runtime.chain_state_template_resolution` | 1 | true |
| `runtime.chain_step_class_required` | 1 | true |
| `runtime.ci_artifact_upload_paths_valid` | 1 | true |
| `runtime.ci_gate_default_no_python_governance_required` | 1 | true |
| `runtime.ci_gate_default_report_commands_forbidden` | 1 | true |
| `runtime.ci_gate_ownership_contract_required` | 1 | true |
| `runtime.ci_python_lane_non_blocking_required` | 1 | true |
| `runtime.ci_workflow_critical_gate_required` | 1 | true |
| `runtime.cigate_uses_governance_triage_required` | 1 | true |
| `runtime.config_literals` | 1 | true |
| `runtime.contract_job_dispatch_in_contract_required` | 1 | true |
| `runtime.contract_job_hooks_refactor_applied` | 1 | true |
| `runtime.contract_spec_fence_required` | 1 | true |
| `runtime.contract_step_asserts_required` | 1 | true |
| `runtime.domain_library_preferred_for_fs_ops` | 1 | true |
| `runtime.domain_library_preferred_for_http_helpers` | 1 | true |
| `runtime.executable_spec_lang_includes_forbidden` | 1 | true |
| `runtime.fast_path_consistency_required` | 1 | true |
| `runtime.gate_fail_fast_behavior_required` | 1 | true |
| `runtime.gate_policy_evaluates_with_skipped_rows` | 1 | true |
| `runtime.gate_skipped_steps_contract_required` | 1 | true |
| `runtime.git_hook_prepush_enforced` | 1 | true |
| `runtime.governance_prefix_selection_from_changed_paths` | 1 | true |
| `runtime.governance_triage_artifact_contains_selection_metadata` | 1 | true |
| `runtime.governance_triage_entrypoint_required` | 1 | true |
| `runtime.governance_triage_targeted_first_required` | 1 | true |
| `runtime.harness_exports_location_required` | 1 | true |
| `runtime.harness_exports_schema_valid` | 1 | true |
| `runtime.harness_job_legacy_forbidden` | 1 | true |
| `runtime.harness_jobs_metadata_map_required` | 1 | true |
| `runtime.harness_on_complete_hook_required_behavior` | 1 | true |
| `runtime.harness_on_fail_hook_required_behavior` | 1 | true |
| `runtime.harness_on_hooks_schema_valid` | 2 | true |
| `runtime.harness_on_ordering_contract_required` | 1 | true |
| `runtime.harness_subject_target_map_declared` | 1 | true |
| `runtime.legacy_assert_block_forbidden` | 1 | true |
| `runtime.legacy_checks_key_forbidden` | 1 | true |
| `runtime.legacy_spec_test_fence_forbidden` | 1 | true |
| `runtime.legacy_timeout_envs_deprecated` | 1 | true |
| `runtime.liveness_hard_cap_token_emitted` | 1 | true |
| `runtime.liveness_stall_token_emitted` | 1 | true |
| `runtime.liveness_watchdog_contract_valid` | 1 | true |
| `runtime.local_ci_parity_entrypoint_documented` | 1 | true |
| `runtime.local_ci_parity_python_lane_forbidden` | 1 | true |
| `runtime.local_prepush_broad_governance_forbidden` | 1 | true |
| `runtime.make_python_parity_targets_forbidden` | 1 | true |
| `runtime.meta_json_target_required` | 1 | true |
| `runtime.no_public_direct_rust_adapter_docs` | 1 | true |
| `runtime.non_python_lane_no_python_exec` | 1 | true |
| `runtime.ops_job_capability_required` | 1 | true |
| `runtime.ops_job_nested_dispatch_forbidden` | 1 | true |
| `runtime.ops_os_capability_required` | 1 | true |
| `runtime.ops_os_stdlib_surface_sync` | 1 | true |
| `runtime.orchestration_policy_via_spec_lang` | 1 | true |
| `runtime.policy_evaluate_forbidden` | 1 | true |
| `runtime.prepush_parity_default_required` | 0 | false |
| `runtime.prepush_python_parity_not_optional_by_default` | 0 | false |
| `runtime.prepush_uses_governance_triage_required` | 1 | true |
| `runtime.profile_artifacts_on_fail_required` | 1 | true |
| `runtime.profiling_contract_artifacts` | 1 | true |
| `runtime.profiling_redaction_policy` | 1 | true |
| `runtime.profiling_span_taxonomy` | 1 | true |
| `runtime.public_runner_default_rust` | 1 | true |
| `runtime.public_runner_entrypoint_single` | 1 | true |
| `runtime.python_bin_resolver_sync` | 1 | true |
| `runtime.python_dependency_metric` | 1 | true |
| `runtime.python_dependency_non_regression` | 1 | true |
| `runtime.python_lane_explicit_opt_in` | 0 | false |
| `runtime.runner_adapter_python_impl_forbidden` | 1 | true |
| `runtime.runner_independence_metric` | 1 | true |
| `runtime.runner_independence_non_regression` | 1 | true |
| `runtime.runner_interface_ci_lane` | 1 | true |
| `runtime.runner_interface_gate_sync` | 3 | true |
| `runtime.runner_interface_subcommands` | 2 | true |
| `runtime.rust_adapter_exec_smoke` | 2 | true |
| `runtime.rust_adapter_no_delegate` | 1 | true |
| `runtime.rust_adapter_no_python_exec` | 1 | true |
| `runtime.rust_adapter_subcommand_parity` | 1 | true |
| `runtime.rust_adapter_target_fallback_defined` | 1 | true |
| `runtime.rust_adapter_transitive_no_python` | 1 | true |
| `runtime.rust_only_prepush_required` | 1 | true |
| `runtime.scope_sync` | 1 | true |
| `runtime.settings_import_policy` | 1 | true |
| `runtime.spec_lang_export_type_forbidden` | 1 | true |
| `runtime.spec_lang_pure_no_effect_builtins` | 1 | true |
| `runtime.triage_artifacts_emitted_required` | 1 | true |
| `runtime.triage_bypass_logged_required` | 1 | true |
| `runtime.triage_failure_id_parsing_required` | 1 | true |
| `runtime.triage_stall_fallback_required` | 1 | true |
| `runtime.universal_chain_support_required` | 1 | true |
| `schema.harness_contract_overlay_sync` | 1 | true |
| `schema.harness_type_overlay_complete` | 1 | true |
| `schema.no_prose_only_rules` | 1 | true |
| `schema.registry_compiled_sync` | 1 | true |
| `schema.registry_docs_sync` | 1 | true |
| `schema.registry_valid` | 1 | true |
| `schema.type_profiles_complete` | 1 | true |
| `schema.verb_first_contract_sync` | 1 | true |
| `spec.contract_assertions_metric` | 1 | true |
| `spec.contract_assertions_non_regression` | 1 | true |
| `spec.domain_index_sync` | 1 | true |
| `spec.executable_surface_markdown_only` | 1 | true |
| `spec.generated_data_artifacts_not_embedded_in_spec_blocks` | 1 | true |
| `spec.layout_domain_trees` | 1 | true |
| `spec.library_cases_markdown_only` | 1 | true |
| `spec.no_executable_yaml_json_in_case_trees` | 1 | true |
| `spec.portability_metric` | 1 | true |
| `spec.portability_non_regression` | 1 | true |
| `spec.spec_lang_adoption_metric` | 1 | true |
| `spec.spec_lang_adoption_non_regression` | 1 | true |
| `spec_lang.stdlib_conformance_coverage` | 1 | true |
| `spec_lang.stdlib_docs_sync` | 1 | true |
| `spec_lang.stdlib_profile_complete` | 1 | true |
| `spec_lang.stdlib_py_php_parity` | 1 | true |
| `tests.unit_opt_out_non_regression` | 1 | true |
<!-- GENERATED:END governance_check_catalog -->
