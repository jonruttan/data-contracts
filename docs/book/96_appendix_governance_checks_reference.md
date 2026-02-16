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

- check_count: 152
- checks_with_cases: 152
- checks_without_cases: 0

| check_id | case_count | has_case |
|---|---|---|
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
| `docs.book_chapter_order_canonical` | 1 | true |
| `docs.cli_flags_documented` | 1 | true |
| `docs.command_examples_verified` | 1 | true |
| `docs.contract_schema_book_sync` | 1 | true |
| `docs.current_spec_only_contract` | 1 | true |
| `docs.current_spec_policy_key_names` | 1 | true |
| `docs.example_id_uniqueness` | 1 | true |
| `docs.examples_runnable` | 1 | true |
| `docs.filename_policy` | 1 | true |
| `docs.generated_files_clean` | 1 | true |
| `docs.generated_sections_read_only` | 1 | true |
| `docs.generator_outputs_sync` | 1 | true |
| `docs.generator_registry_valid` | 1 | true |
| `docs.governance_check_catalog_sync` | 1 | true |
| `docs.harness_type_catalog_sync` | 1 | true |
| `docs.history_reviews_namespace` | 1 | true |
| `docs.index_filename_policy` | 1 | true |
| `docs.instructions_complete` | 1 | true |
| `docs.layout_canonical_trees` | 1 | true |
| `docs.make_commands_sync` | 1 | true |
| `docs.meta_schema_valid` | 1 | true |
| `docs.metrics_field_catalog_sync` | 1 | true |
| `docs.no_os_artifact_files` | 1 | true |
| `docs.operability_metric` | 1 | true |
| `docs.operability_non_regression` | 1 | true |
| `docs.policy_rule_catalog_sync` | 1 | true |
| `docs.reference_index_sync` | 1 | true |
| `docs.reference_manifest_sync` | 1 | true |
| `docs.reference_surface_complete` | 1 | true |
| `docs.regex_doc_sync` | 1 | true |
| `docs.release_contract_automation_policy` | 1 | true |
| `docs.required_sections` | 1 | true |
| `docs.runner_api_catalog_sync` | 1 | true |
| `docs.security_warning_contract` | 1 | true |
| `docs.spec_lang_builtin_catalog_sync` | 1 | true |
| `docs.spec_schema_field_catalog_sync` | 1 | true |
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
| `library.domain_index_sync` | 1 | true |
| `library.domain_ownership` | 1 | true |
| `library.public_surface_model` | 1 | true |
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
| `runtime.api_http_live_mode_explicit` | 1 | true |
| `runtime.api_http_oauth_docs_sync` | 1 | true |
| `runtime.api_http_oauth_env_only` | 1 | true |
| `runtime.api_http_oauth_no_secret_literals` | 1 | true |
| `runtime.assertions_via_spec_lang` | 1 | true |
| `runtime.config_literals` | 1 | true |
| `runtime.no_public_direct_rust_adapter_docs` | 1 | true |
| `runtime.non_python_lane_no_python_exec` | 1 | true |
| `runtime.orchestration_policy_via_spec_lang` | 1 | true |
| `runtime.public_runner_default_rust` | 1 | true |
| `runtime.public_runner_entrypoint_single` | 1 | true |
| `runtime.python_bin_resolver_sync` | 1 | true |
| `runtime.python_dependency_metric` | 1 | true |
| `runtime.python_dependency_non_regression` | 1 | true |
| `runtime.python_lane_explicit_opt_in` | 1 | true |
| `runtime.runner_independence_metric` | 1 | true |
| `runtime.runner_independence_non_regression` | 1 | true |
| `runtime.runner_interface_ci_lane` | 2 | true |
| `runtime.runner_interface_gate_sync` | 3 | true |
| `runtime.runner_interface_subcommands` | 2 | true |
| `runtime.rust_adapter_exec_smoke` | 2 | true |
| `runtime.rust_adapter_no_delegate` | 1 | true |
| `runtime.rust_adapter_no_python_exec` | 1 | true |
| `runtime.rust_adapter_subcommand_parity` | 1 | true |
| `runtime.rust_adapter_transitive_no_python` | 1 | true |
| `runtime.scope_sync` | 1 | true |
| `runtime.settings_import_policy` | 1 | true |
| `runtime.spec_lang_pure_no_effect_builtins` | 1 | true |
| `schema.no_prose_only_rules` | 1 | true |
| `schema.registry_compiled_sync` | 1 | true |
| `schema.registry_docs_sync` | 1 | true |
| `schema.registry_valid` | 1 | true |
| `schema.type_profiles_complete` | 1 | true |
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
<!-- GENERATED:END governance_check_catalog -->
