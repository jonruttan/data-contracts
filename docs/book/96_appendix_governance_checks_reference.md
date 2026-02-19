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
- run: ./runners/public/runner_adapter.sh docs-generate-check
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

- check_count: 244
- checks_with_cases: 0
- checks_without_cases: 244

| check_id | case_count | has_case |
|---|---|---|
| `architecture.harness_local_workflow_duplication_forbidden` | 0 | false |
| `architecture.harness_workflow_components_required` | 0 | false |
| `assert.adapter_projection_contract_sync` | 0 | false |
| `assert.compiler_schema_matrix_sync` | 0 | false |
| `assert.domain_library_usage_required` | 0 | false |
| `assert.domain_profiles_docs_sync` | 0 | false |
| `assert.spec_lang_builtin_surface_sync` | 0 | false |
| `assert.subject_profiles_declared` | 0 | false |
| `assert.subject_profiles_json_only` | 0 | false |
| `assert.sugar_compile_only_sync` | 0 | false |
| `assert.type_contract_subject_semantics_sync` | 0 | false |
| `assert.universal_core_sync` | 0 | false |
| `conformance.api_http_portable_shape` | 0 | false |
| `conformance.case_doc_style_guard` | 0 | false |
| `conformance.case_index_sync` | 0 | false |
| `conformance.evaluate_first_ratio_non_regression` | 0 | false |
| `conformance.extension_requires_capabilities` | 0 | false |
| `conformance.library_contract_cases_present` | 0 | false |
| `conformance.library_policy_usage_required` | 0 | false |
| `conformance.no_runner_logic_outside_harness` | 0 | false |
| `conformance.purpose_quality_gate` | 0 | false |
| `conformance.purpose_warning_codes_sync` | 0 | false |
| `conformance.spec_lang_fixture_library_usage` | 0 | false |
| `conformance.type_contract_docs` | 0 | false |
| `conformance.type_contract_field_sync` | 0 | false |
| `contract.coverage_threshold` | 0 | false |
| `contract.governance_check` | 0 | false |
| `docs.adoption_profiles_sync` | 0 | false |
| `docs.api_http_tutorial_sync` | 0 | false |
| `docs.book_chapter_order_canonical` | 0 | false |
| `docs.canonical_freshness_strict` | 0 | false |
| `docs.cli_flags_documented` | 0 | false |
| `docs.command_examples_verified` | 0 | false |
| `docs.contract_schema_book_sync` | 0 | false |
| `docs.current_spec_only_contract` | 0 | false |
| `docs.current_spec_policy_key_names` | 0 | false |
| `docs.docgen_quality_score_threshold` | 0 | false |
| `docs.example_id_uniqueness` | 0 | false |
| `docs.examples_prefer_domain_fs_helpers` | 0 | false |
| `docs.examples_runnable` | 0 | false |
| `docs.filename_policy` | 0 | false |
| `docs.generate_check_passes` | 0 | false |
| `docs.generated_files_clean` | 0 | false |
| `docs.generated_sections_read_only` | 0 | false |
| `docs.generation_registry_surface_case_sync` | 0 | false |
| `docs.generation_spec_cases_present` | 0 | false |
| `docs.generator_outputs_sync` | 0 | false |
| `docs.generator_registry_valid` | 0 | false |
| `docs.governance_check_catalog_sync` | 0 | false |
| `docs.governance_check_family_map_complete` | 0 | false |
| `docs.harness_reference_semantics_complete` | 0 | false |
| `docs.harness_type_catalog_sync` | 0 | false |
| `docs.reviews_namespace_active` | 0 | false |
| `docs.index_filename_policy` | 0 | false |
| `docs.instructions_complete` | 0 | false |
| `docs.layout_canonical_trees` | 0 | false |
| `docs.make_commands_sync` | 0 | false |
| `docs.markdown_structured_assertions_required` | 0 | false |
| `docs.meta_schema_valid` | 0 | false |
| `docs.metrics_field_catalog_sync` | 0 | false |
| `docs.no_os_artifact_files` | 0 | false |
| `docs.operability_non_regression` | 0 | false |
| `docs.output_mode_contract_valid` | 0 | false |
| `docs.policy_rule_catalog_sync` | 0 | false |
| `docs.reference_index_sync` | 0 | false |
| `docs.reference_manifest_sync` | 0 | false |
| `docs.reference_namespace_chapters_sync` | 0 | false |
| `docs.reference_surface_complete` | 0 | false |
| `docs.regex_doc_sync` | 0 | false |
| `docs.release_contract_automation_policy` | 0 | false |
| `docs.required_sections` | 0 | false |
| `docs.runner_api_catalog_sync` | 0 | false |
| `docs.runner_reference_semantics_complete` | 0 | false |
| `docs.security_warning_contract` | 0 | false |
| `docs.spec_index_reachability` | 0 | false |
| `docs.spec_lang_builtin_catalog_sync` | 0 | false |
| `docs.spec_schema_field_catalog_sync` | 0 | false |
| `docs.stdlib_examples_complete` | 0 | false |
| `docs.stdlib_symbol_docs_complete` | 0 | false |
| `docs.template_data_sources_declared` | 0 | false |
| `docs.template_paths_valid` | 0 | false |
| `docs.token_dependency_resolved` | 0 | false |
| `docs.token_ownership_unique` | 0 | false |
| `docs.traceability_catalog_sync` | 0 | false |
| `docs.v1_scope_contract` | 0 | false |
| `governance.extractor_only_no_verdict_branching` | 0 | false |
| `governance.policy_library_usage_non_regression` | 0 | false |
| `governance.policy_library_usage_required` | 0 | false |
| `governance.structured_assertions_required` | 0 | false |
| `impl.evaluate_ratio_non_regression` | 0 | false |
| `impl.library_usage_non_regression` | 0 | false |
| `library.colocated_symbol_tests_required` | 0 | false |
| `library.domain_index_sync` | 0 | false |
| `library.domain_ownership` | 0 | false |
| `library.public_surface_model` | 0 | false |
| `library.single_public_symbol_per_case_required` | 0 | false |
| `library.verb_first_schema_keys_required` | 0 | false |
| `naming.filename_policy` | 0 | false |
| `normalization.docs_token_sync` | 0 | false |
| `normalization.library_mapping_ast_only` | 0 | false |
| `normalization.mapping_ast_only` | 0 | false |
| `normalization.profile_sync` | 0 | false |
| `normalization.spec_style_sync` | 0 | false |
| `normalization.virtual_root_paths_only` | 0 | false |
| `objective.scorecard_non_regression` | 0 | false |
| `objective.tripwires_clean` | 0 | false |
| `orchestration.ops_capability_bindings` | 0 | false |
| `orchestration.ops_registry_sync` | 0 | false |
| `orchestration.ops_symbol_grammar` | 0 | false |
| `pending.no_resolved_markers` | 0 | false |
| `reference.check_ids_exist` | 0 | false |
| `reference.contract_paths_exist` | 0 | false |
| `reference.external_refs_policy` | 0 | false |
| `reference.library_exports_used` | 0 | false |
| `reference.policy_symbols_resolve` | 0 | false |
| `reference.private_symbols_forbidden` | 0 | false |
| `reference.symbols_exist` | 0 | false |
| `reference.token_anchors_exist` | 0 | false |
| `runtime.api_http_cors_support` | 0 | false |
| `runtime.api_http_live_mode_explicit` | 0 | false |
| `runtime.api_http_oauth_docs_sync` | 0 | false |
| `runtime.api_http_oauth_env_only` | 0 | false |
| `runtime.api_http_oauth_no_secret_literals` | 0 | false |
| `runtime.api_http_parity_contract_sync` | 0 | false |
| `runtime.api_http_scenario_roundtrip` | 0 | false |
| `runtime.api_http_verb_suite` | 0 | false |
| `runtime.assert_block_decision_authority_required` | 0 | false |
| `runtime.assertions_via_spec_lang` | 0 | false |
| `runtime.case_contract_block_required` | 0 | false |
| `runtime.chain_contract_single_location` | 0 | false |
| `runtime.chain_cycle_forbidden` | 0 | false |
| `runtime.chain_exports_explicit_only` | 0 | false |
| `runtime.chain_exports_from_key_required` | 0 | false |
| `runtime.chain_exports_list_only_required` | 0 | false |
| `runtime.chain_exports_target_derived_only` | 0 | false |
| `runtime.chain_fail_fast_default` | 0 | false |
| `runtime.chain_import_alias_collision_forbidden` | 0 | false |
| `runtime.chain_imports_consumer_surface_unchanged` | 0 | false |
| `runtime.chain_library_symbol_exports_valid` | 0 | false |
| `runtime.chain_ref_scalar_required` | 0 | false |
| `runtime.chain_reference_resolution` | 0 | false |
| `runtime.chain_shared_context_required` | 0 | false |
| `runtime.chain_state_template_resolution` | 0 | false |
| `runtime.chain_step_class_required` | 0 | false |
| `runtime.ci_artifact_upload_paths_valid` | 0 | false |
| `runtime.ci_gate_default_no_python_governance_required` | 0 | false |
| `runtime.ci_gate_default_report_commands_forbidden` | 0 | false |
| `runtime.ci_gate_ownership_contract_required` | 0 | false |
| `runtime.ci_workflow_critical_gate_required` | 0 | false |
| `runtime.cigate_uses_governance_triage_required` | 0 | false |
| `runtime.config_literals` | 0 | false |
| `runtime.contract_job_dispatch_in_contract_required` | 0 | false |
| `runtime.contract_job_hooks_refactor_applied` | 0 | false |
| `runtime.contract_spec_fence_required` | 0 | false |
| `runtime.contract_step_asserts_required` | 0 | false |
| `runtime.domain_library_preferred_for_fs_ops` | 0 | false |
| `runtime.domain_library_preferred_for_http_helpers` | 0 | false |
| `runtime.executable_spec_lang_includes_forbidden` | 0 | false |
| `runtime.fast_path_consistency_required` | 0 | false |
| `runtime.gate_fail_fast_behavior_required` | 0 | false |
| `runtime.gate_skipped_steps_contract_required` | 0 | false |
| `runtime.git_hook_prepush_enforced` | 0 | false |
| `runtime.governance_prefix_selection_from_changed_paths` | 0 | false |
| `runtime.governance_triage_artifact_contains_selection_metadata` | 0 | false |
| `runtime.governance_triage_entrypoint_required` | 0 | false |
| `runtime.governance_triage_targeted_first_required` | 0 | false |
| `runtime.harness_exports_location_required` | 0 | false |
| `runtime.harness_exports_schema_valid` | 0 | false |
| `runtime.harness_jobs_metadata_map_required` | 0 | false |
| `runtime.harness_subject_target_map_declared` | 0 | false |
| `runtime.liveness_hard_cap_token_emitted` | 0 | false |
| `runtime.liveness_stall_token_emitted` | 0 | false |
| `runtime.liveness_watchdog_contract_valid` | 0 | false |
| `runtime.local_ci_parity_entrypoint_documented` | 0 | false |
| `runtime.local_ci_parity_python_lane_forbidden` | 0 | false |
| `runtime.local_prepush_broad_governance_forbidden` | 0 | false |
| `runtime.make_python_parity_targets_forbidden` | 0 | false |
| `runtime.meta_json_target_required` | 0 | false |
| `runtime.no_public_direct_rust_adapter_docs` | 0 | false |
| `runtime.non_python_lane_no_python_exec` | 0 | false |
| `runtime.ops_job_capability_required` | 0 | false |
| `runtime.ops_job_nested_dispatch_forbidden` | 0 | false |
| `runtime.ops_os_capability_required` | 0 | false |
| `runtime.ops_os_stdlib_surface_sync` | 0 | false |
| `runtime.orchestration_policy_via_spec_lang` | 0 | false |
| `runtime.prepush_parity_default_required` | 0 | false |
| `runtime.prepush_python_parity_not_optional_by_default` | 0 | false |
| `runtime.prepush_uses_governance_triage_required` | 0 | false |
| `runtime.profile_artifacts_on_fail_required` | 0 | false |
| `runtime.profiling_contract_artifacts` | 0 | false |
| `runtime.profiling_redaction_policy` | 0 | false |
| `runtime.profiling_span_taxonomy` | 0 | false |
| `runtime.public_runner_default_rust` | 0 | false |
| `runtime.public_runner_entrypoint_single` | 0 | false |
| `runtime.python_bin_resolver_sync` | 0 | false |
| `runtime.python_dependency_metric` | 0 | false |
| `runtime.python_dependency_non_regression` | 0 | false |
| `runtime.python_lane_explicit_opt_in` | 0 | false |
| `runtime.runner_adapter_python_impl_forbidden` | 0 | false |
| `runtime.runner_independence_metric` | 0 | false |
| `runtime.runner_independence_non_regression` | 0 | false |
| `runtime.runner_interface_ci_lane` | 0 | false |
| `runtime.runner_interface_gate_sync` | 0 | false |
| `runtime.runner_interface_subcommands` | 0 | false |
| `runtime.rust_adapter_exec_smoke` | 0 | false |
| `runtime.rust_adapter_no_delegate` | 0 | false |
| `runtime.rust_adapter_no_python_exec` | 0 | false |
| `runtime.rust_adapter_subcommand_parity` | 0 | false |
| `runtime.rust_adapter_transitive_no_python` | 0 | false |
| `runtime.rust_only_prepush_required` | 0 | false |
| `runtime.scope_sync` | 0 | false |
| `runtime.settings_import_policy` | 0 | false |
| `runtime.spec_lang_export_type_forbidden` | 0 | false |
| `runtime.spec_lang_pure_no_effect_builtins` | 0 | false |
| `runtime.triage_artifacts_emitted_required` | 0 | false |
| `runtime.triage_bypass_logged_required` | 0 | false |
| `runtime.triage_failure_id_parsing_required` | 0 | false |
| `runtime.universal_chain_support_required` | 0 | false |
| `runtime.when_complete_hook_required_behavior` | 0 | false |
| `runtime.when_fail_hook_required_behavior` | 0 | false |
| `runtime.when_hooks_schema_valid` | 0 | false |
| `runtime.when_ordering_contract_required` | 0 | false |
| `schema.harness_contract_overlay_sync` | 0 | false |
| `schema.harness_type_overlay_complete` | 0 | false |
| `schema.no_prose_only_rules` | 0 | false |
| `schema.registry_compiled_sync` | 0 | false |
| `schema.registry_docs_sync` | 0 | false |
| `schema.registry_valid` | 0 | false |
| `schema.type_profiles_complete` | 0 | false |
| `schema.verb_first_contract_sync` | 0 | false |
| `spec.contract_assertions_non_regression` | 0 | false |
| `spec.domain_index_sync` | 0 | false |
| `spec.executable_surface_markdown_only` | 0 | false |
| `spec.generated_data_artifacts_not_embedded_in_spec_blocks` | 0 | false |
| `spec.layout_domain_trees` | 0 | false |
| `spec.library_cases_markdown_only` | 0 | false |
| `spec.no_executable_yaml_json_in_case_trees` | 0 | false |
| `spec.portability_non_regression` | 0 | false |
| `spec.spec_lang_adoption_non_regression` | 0 | false |
| `spec_lang.stdlib_conformance_coverage` | 0 | false |
| `spec_lang.stdlib_docs_sync` | 0 | false |
| `spec_lang.stdlib_profile_complete` | 0 | false |
| `spec_lang.stdlib_py_php_parity` | 0 | false |
| `tests.unit_opt_out_non_regression` | 0 | false |
<!-- GENERATED:END governance_check_catalog -->
