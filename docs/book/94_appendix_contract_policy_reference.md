# Contract Policy Reference

```yaml doc-meta
doc_id: DOC-REF-094
title: Appendix Contract Policy Reference
status: active
audience: reviewer
owns_tokens:
- appendix_contract_policy_reference
requires_tokens:
- quickstart_minimal_case
commands:
- run: ./scripts/runner_adapter.sh docs-generate-check
  purpose: Verify generated policy catalog remains synchronized.
examples:
- id: EX-APP-POLICY-001
  runnable: false
  opt_out_reason: Generated reference page intentionally contains no runnable fenced examples.
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

This page is machine-generated from policy rule definitions.

## Purpose

Provide generated policy-rule inventory for governance and traceability review.

## Inputs

- policy rule source file (`policy_v1.yaml`)

## Outputs

- deterministic policy rule catalog tables

## Failure Modes

- stale generated block after policy edits
- missing generated markers
- policy/source drift

<!-- GENERATED:START policy_rule_catalog -->

## Generated Contract Policy Rule Catalog

- rule_count: 203
- must_count: 189
- should_count: 12
- must_not_count: 2
- active_count: 203
- deprecated_count: 0
- removed_count: 0

| id | norm | scope | applies_to | references | lifecycle |
|---|---|---|---|---|---|
| `API_HTTP_CORS_PRELIGHT_AND_ACTUAL_SUPPORTED` | `MUST` | `implementation` | `api.http.request.cors` | 3 | `active` |
| `API_HTTP_DETERMINISTIC_DEFAULT_REQUIRED` | `MUST` | `implementation` | `api.http.harness.mode` | 2 | `active` |
| `API_HTTP_LIVE_MODE_EXPLICIT_OPT_IN_REQUIRED` | `MUST` | `governance` | `api.http.network_execution` | 2 | `active` |
| `API_HTTP_OAUTH_ENV_REF_ONLY_REQUIRED` | `MUST` | `governance` | `api.http.harness.auth.oauth.credentials` | 3 | `active` |
| `API_HTTP_OAUTH_HARNESS_PROFILE_SUPPORTED` | `MUST` | `implementation` | `api.http.harness.auth.oauth` | 3 | `active` |
| `API_HTTP_OAUTH_SECRET_REDACTION_REQUIRED` | `MUST` | `implementation` | `api.http.context_and_diagnostics` | 2 | `active` |
| `API_HTTP_PY_PHP_BEHAVIOR_PARITY_REQUIRED` | `MUST` | `conformance` | `api.http.shared_capability_fixtures` | 3 | `active` |
| `API_HTTP_SCENARIO_DETERMINISTIC_LIFECYCLE_REQUIRED` | `MUST` | `implementation` | `api.http.harness.scenario.lifecycle` | 2 | `active` |
| `API_HTTP_SCENARIO_ROUNDTRIP_SUPPORTED` | `MUST` | `implementation` | `api.http.requests.scenario` | 3 | `active` |
| `API_HTTP_TUTORIAL_COVERAGE_REQUIRED` | `MUST` | `docs` | `docs.book.rest_and_cors_tutorials` | 3 | `active` |
| `API_HTTP_VERB_SUITE_REQUIRED` | `MUST` | `implementation` | `api.http.request.method` | 3 | `active` |
| `ASSERT_ADAPTER_PROJECTION_SYNC_REQUIRED` | `MUST` | `governance` | `docs.contract.adapter_projection_sync` | 8 | `active` |
| `ASSERT_COMPILER_SCHEMA_MATRIX_SYNC` | `MUST` | `governance` | `assert.tree.compiler_contract_sync` | 4 | `active` |
| `ASSERT_CONTEXT_PROJECTION_CONTRACT_REQUIRED` | `MUST` | `governance` | `harness.subject_projection.context_profiles` | 6 | `active` |
| `ASSERT_DOMAIN_ASSERTIONS_LIBRARY_BACKED` | `MUST` | `governance` | `conformance.domain_assertions.library_usage` | 3 | `active` |
| `ASSERT_HEALTH_GLOBAL_AND_PER_CASE_POLICY` | `SHOULD` | `implementation` | `assertion_health.policy_resolution` | 2 | `active` |
| `ASSERT_HEALTH_MODE_VALID_VALUES` | `MUST` | `case` | `assert_health.mode` | 2 | `active` |
| `ASSERT_HEALTH_NON_PORTABLE_REGEX_DIAGNOSTIC` | `SHOULD` | `case` | `assert.tree.regex` | 3 | `active` |
| `ASSERT_HEALTH_REDUNDANT_BRANCH_DIAGNOSTIC` | `SHOULD` | `case` | `assert.tree.group_children` | 4 | `active` |
| `ASSERT_NO_NON_JSON_EVALUATOR_TYPES` | `MUST` | `governance` | `assert.evaluator.value_model` | 3 | `active` |
| `ASSERT_SUBJECT_PROFILE_JSON_CORE_ONLY` | `MUST` | `governance` | `assert.subject_profiles.json_core` | 4 | `active` |
| `ASSERT_SUGAR_OPERATORS_COMPILE_ONLY` | `MUST` | `implementation` | `assert.tree.operator_surface` | 4 | `active` |
| `ASSERT_TARGET_CONTRACT_SUBJECT_DRIVEN` | `MUST` | `contract` | `assert.tree.target_applicability` | 4 | `active` |
| `ASSERT_UNIVERSAL_CORE_EVALUATE_ONLY` | `MUST` | `contract` | `assert.tree.operator_model` | 3 | `active` |
| `CHAIN_CYCLE_FORBIDDEN` | `MUST` | `runtime` | `harness.chain.graph` | 3 | `active` |
| `CHAIN_EXPORTS_EXPLICIT_REQUIRED` | `MUST` | `implementation` | `harness.chain.steps.exports` | 2 | `active` |
| `CHAIN_FAIL_FAST_DEFAULT_REQUIRED` | `MUST` | `implementation` | `harness.chain.fail_fast` | 2 | `active` |
| `CHAIN_REFERENCE_CONTRACT_REQUIRED` | `MUST` | `implementation` | `harness.chain.steps.ref` | 3 | `active` |
| `CHAIN_SHARED_CONTEXT_REQUIRED` | `MUST` | `runtime` | `harness.chain.state` | 3 | `active` |
| `CLI_RUN_CONFORMANCE_EXPLICIT_ENTRYPOINT` | `MUST` | `conformance` | `fixtures.cli.run` | 2 | `active` |
| `CLI_RUN_CONFORMANCE_NO_ENV_DEPENDENCY` | `MUST_NOT` | `conformance` | `fixtures.cli.run` | 2 | `active` |
| `CLI_RUN_ENTRYPOINT_REQUIRED` | `MUST` | `case` | `cli.run.harness.entrypoint` | 2 | `active` |
| `CLI_RUN_ENV_ALLOWLIST_CONTROL` | `SHOULD` | `implementation` | `cli.run.process_environment` | 3 | `active` |
| `CLI_RUN_SAFE_MODE_RESTRICTS_HOOKS` | `SHOULD` | `implementation` | `cli.run.safe_mode` | 3 | `active` |
| `CONFORMANCE_CASE_STYLE_GUARD` | `MUST` | `governance` | `fixtures.conformance.cases_style` | 2 | `active` |
| `CONFORMANCE_EVALUATE_FIRST_REQUIRED` | `MUST` | `governance` | `conformance.assertion_authoring.metric_ratchet` | 3 | `active` |
| `CONFORMANCE_EXPECT_OVERLAY_RESOLUTION` | `MUST` | `conformance` | `fixtures.expect` | 2 | `active` |
| `CONFORMANCE_LIBRARY_POLICY_USAGE_REQUIRED` | `MUST` | `governance` | `conformance.governance.policy_authoring` | 4 | `active` |
| `CONFORMANCE_NO_AMBIENT_ASSUMPTIONS_GUARD` | `MUST` | `governance` | `fixtures.portable.ambient_assumptions` | 3 | `active` |
| `CONFORMANCE_PURPOSE_QUALITY_GATE` | `MUST` | `governance` | `fixtures.conformance.purpose_quality` | 2 | `active` |
| `CONFORMANCE_REQUIRES_CAPABILITIES_POLICY` | `MUST` | `conformance` | `fixtures.requires.capabilities` | 3 | `active` |
| `CONFORMANCE_SPEC_LANG_FIXTURE_LIBRARY_USAGE_REQUIRED` | `MUST` | `governance` | `conformance.spec_lang_fixtures.reusable_helpers` | 3 | `active` |
| `CONTRACT_ASSERTIONS_METRIC_REPORTED` | `MUST` | `governance` | `specs.contract_assertions.metric_report` | 2 | `active` |
| `CONTRACT_ASSERTIONS_NON_REGRESSION_REQUIRED` | `MUST` | `governance` | `specs.contract_assertions.metric_non_regression` | 3 | `active` |
| `CONTRACT_MUST_RULE_COVERAGE_COMPLETE` | `MUST` | `governance` | `docs.spec.contract.coverage` | 2 | `active` |
| `CURRENT_SPEC_POLICY_KEY_NAMES` | `MUST` | `governance` | `docs.spec.case_key_names` | 3 | `active` |
| `DATA_ARTIFACT_SURFACES_MUST_REMAIN_MACHINE_FILES` | `MUST` | `governance` | `docs.spec.data_artifacts` | 2 | `active` |
| `DOCS_ADOPTION_PROFILES_SYNC` | `MUST` | `governance` | `docs.adoption.profiles` | 3 | `active` |
| `DOCS_API_CATALOGS_GENERATED_AND_SYNCED` | `MUST` | `governance` | `docs.generator.api_catalogs` | 6 | `active` |
| `DOCS_BOOK_APPENDIX_CATALOG_NAMESPACE_REQUIRED` | `MUST` | `governance` | `docs.book.appendix_catalog_naming` | 3 | `active` |
| `DOCS_BOOK_CHAPTER_ORDER_CANONICAL` | `MUST` | `governance` | `docs.book.chapter_order` | 2 | `active` |
| `DOCS_CLI_FLAGS_DOCUMENTED` | `MUST` | `governance` | `docs.cli.flags` | 4 | `active` |
| `DOCS_COMMAND_EXAMPLES_VERIFIED` | `MUST` | `governance` | `docs.reference.examples_v2` | 2 | `active` |
| `DOCS_CONTRACT_SCHEMA_BOOK_TOKEN_SYNC` | `MUST` | `governance` | `docs.contract.schema.book.tokens` | 4 | `active` |
| `DOCS_DOCGEN_OUTPUT_MIN_QUALITY_SCORE_REQUIRED` | `MUST` | `governance` | `docs.generator.outputs.quality` | 2 | `active` |
| `DOCS_EXAMPLES_RUNNABLE_OR_EXPLICITLY_OPTED_OUT` | `MUST` | `governance` | `docs.reference.examples` | 2 | `active` |
| `DOCS_EXAMPLE_IDS_UNIQUE` | `MUST` | `governance` | `docs.reference.example_ids` | 2 | `active` |
| `DOCS_FILENAME_POLICY_REQUIRED` | `MUST` | `governance` | `docs.layout.filename_policy` | 2 | `active` |
| `DOCS_GENERATED_ARTIFACTS_FRESH` | `MUST` | `governance` | `docs.reference.generated_artifacts` | 3 | `active` |
| `DOCS_GENERATED_SECTIONS_READ_ONLY` | `MUST` | `governance` | `docs.generator.read_only_sections` | 4 | `active` |
| `DOCS_GENERATED_SURFACES_SYNC_REQUIRED` | `MUST` | `governance` | `docs.generator.outputs` | 2 | `active` |
| `DOCS_GENERATOR_ORCHESTRATOR_REQUIRED` | `MUST` | `runtime` | `docs.generator.execution` | 3 | `active` |
| `DOCS_GENERATOR_REGISTRY_DEFINED` | `MUST` | `governance` | `docs.generator.registry` | 2 | `active` |
| `DOCS_GENERATOR_REPORT_REQUIRED` | `MUST` | `governance` | `docs.generator.reporting` | 3 | `active` |
| `DOCS_GOVERNANCE_CHECK_CATALOG_SYNC_REQUIRED` | `MUST` | `governance` | `docs.generator.catalog.governance_checks` | 3 | `active` |
| `DOCS_HARNESS_FIELD_SEMANTICS_DOC_REQUIRED` | `MUST` | `governance` | `docs.harness_type.profiles` | 2 | `active` |
| `DOCS_HISTORY_REVIEWS_NAMESPACE_REQUIRED` | `MUST` | `governance` | `docs.history.reviews` | 2 | `active` |
| `DOCS_INDEX_FILENAME_INDEX_MD_REQUIRED` | `MUST` | `governance` | `docs.layout.index_filenames` | 2 | `active` |
| `DOCS_INSTRUCTIONS_REQUIRED_SECTIONS` | `MUST` | `governance` | `docs.reference.instructions` | 2 | `active` |
| `DOCS_LAYOUT_CANONICAL_TREES_REQUIRED` | `MUST` | `governance` | `docs.layout.roots` | 3 | `active` |
| `DOCS_MAKE_COMMANDS_SYNC` | `MUST` | `governance` | `docs.command.entrypoints` | 2 | `active` |
| `DOCS_META_SCHEMA_VALID` | `MUST` | `governance` | `docs.reference.doc_meta` | 3 | `active` |
| `DOCS_METRICS_FIELD_CATALOG_SYNC_REQUIRED` | `MUST` | `governance` | `docs.generator.catalog.metrics_fields` | 3 | `active` |
| `DOCS_NO_OS_ARTIFACT_FILES_TRACKED` | `MUST` | `governance` | `docs.layout.artifact_files` | 2 | `active` |
| `DOCS_OPERABILITY_METRIC_REPORTED` | `MUST` | `governance` | `docs.operability.metric_report` | 2 | `active` |
| `DOCS_OPERABILITY_NON_REGRESSION_REQUIRED` | `MUST` | `governance` | `docs.operability.metric_non_regression` | 3 | `active` |
| `DOCS_POLICY_RULE_CATALOG_SYNC_REQUIRED` | `MUST` | `governance` | `docs.generator.catalog.policy_rules` | 3 | `active` |
| `DOCS_REFERENCE_INDEX_SYNC` | `MUST` | `governance` | `docs.reference.index` | 2 | `active` |
| `DOCS_REFERENCE_MANIFEST_SYNC` | `MUST` | `governance` | `docs.reference.manifest` | 3 | `active` |
| `DOCS_REFERENCE_NAMESPACE_CHAPTERS_SYNC_REQUIRED` | `MUST` | `governance` | `docs.book.spec_lang_namespace_chapters` | 2 | `active` |
| `DOCS_REF_SURFACE_COMPLETE` | `MUST` | `governance` | `docs.reference.surface` | 3 | `active` |
| `DOCS_RELEASE_CONTRACT_AUTOMATION_ONLY` | `MUST` | `governance` | `docs.release.contract` | 3 | `active` |
| `DOCS_REQUIRED_SECTIONS_PRESENT` | `MUST` | `governance` | `docs.reference.sections` | 4 | `active` |
| `DOCS_RUNNER_COMMAND_SEMANTICS_DOC_REQUIRED` | `MUST` | `governance` | `docs.runner_api.commands` | 2 | `active` |
| `DOCS_SPEC_LANG_GUIDE_BEFORE_REFERENCE_REQUIRED` | `MUST` | `governance` | `docs.book.spec_lang_chapter_order` | 3 | `active` |
| `DOCS_SPEC_SCHEMA_FIELD_CATALOG_SYNC_REQUIRED` | `MUST` | `governance` | `docs.generator.catalog.spec_schema_fields` | 4 | `active` |
| `DOCS_STDLIB_EXAMPLES_REQUIRED` | `MUST` | `governance` | `docs.spec_lang.symbols.examples` | 2 | `active` |
| `DOCS_STDLIB_SYMBOL_DESCRIPTION_REQUIRED` | `MUST` | `governance` | `docs.spec_lang.symbols.semantic_docs` | 2 | `active` |
| `DOCS_TOKEN_DEPENDENCY_RESOLVED` | `MUST` | `governance` | `docs.reference.token_dependencies` | 2 | `active` |
| `DOCS_TOKEN_OWNERSHIP_UNIQUE` | `MUST` | `governance` | `docs.reference.tokens` | 2 | `active` |
| `DOCS_TRACEABILITY_CATALOG_SYNC_REQUIRED` | `MUST` | `governance` | `docs.generator.catalog.traceability` | 3 | `active` |
| `DOC_ASSERTION_OPERATOR_DOC_SYNC` | `MUST` | `governance` | `docs.spec.assertion_operators` | 2 | `active` |
| `DOC_NORMATIVE_PAGE_TRACEABILITY` | `MUST` | `governance` | `docs.spec.contract.normative_pages` | 2 | `active` |
| `DOC_REGEX_PROFILE_LINKAGE` | `MUST` | `governance` | `docs.spec.regex_portability_profile` | 4 | `active` |
| `EXECUTABLE_DISCOVERY_MARKDOWN_ONLY` | `MUST` | `runtime` | `discovery.canonical_executable_trees` | 2 | `active` |
| `EXECUTABLE_SURFACES_MUST_BE_SPEC_MD` | `MUST` | `governance` | `docs.spec.executable_surfaces` | 2 | `active` |
| `GOVERNANCE_DECISIONS_VIA_SPEC_LANG_ONLY` | `MUST` | `governance` | `governance.check_decisions` | 2 | `active` |
| `GOVERNANCE_EXTRACTOR_ONLY_NO_VERDICT_BRANCHING` | `MUST` | `governance` | `scripts.run_governance_specs` | 3 | `active` |
| `GOVERNANCE_POLICY_EVALUATE_REQUIRED` | `MUST` | `governance` | `governance.check.harness.policy_evaluate` | 3 | `active` |
| `GOVERNANCE_POLICY_LIBRARY_USAGE_NON_REGRESSION` | `MUST` | `governance` | `governance.policy_libraries.metric_non_regression` | 3 | `active` |
| `GOVERNANCE_POLICY_LIBRARY_USAGE_REQUIRED` | `MUST` | `governance` | `governance.check.policy_authoring` | 4 | `active` |
| `GOVERNANCE_STRUCTURED_ASSERTIONS_REQUIRED` | `SHOULD` | `governance` | `governance.check.assertions` | 3 | `active` |
| `GOVERNANCE_SUBJECT_MODEL_SPEC_LANG_DECISIONS` | `SHOULD` | `governance` | `governance.check.subject_decision_split` | 2 | `active` |
| `GOVERNANCE_SYMBOL_RESOLUTION_RATIO_NON_REGRESSION` | `MUST` | `governance` | `specs.spec_lang_adoption.metric_non_regression` | 3 | `active` |
| `HARNESS_CONTRACT_OVERLAY_SYNC_REQUIRED` | `MUST` | `governance` | `harness.contract.schema_sync` | 3 | `active` |
| `HARNESS_LOCAL_WORKFLOW_DUPLICATION_FORBIDDEN` | `MUST_NOT` | `implementation` | `harness.execution.workflow` | 2 | `active` |
| `HARNESS_SUBJECT_TARGET_MAP_DECLARED` | `MUST` | `implementation` | `harness.assertion.targets` | 2 | `active` |
| `HARNESS_TYPE_OVERLAY_COMPLETE_REQUIRED` | `MUST` | `schema` | `schema.registry.v1.types` | 3 | `active` |
| `HARNESS_WORKFLOW_COMPONENTS_REQUIRED` | `MUST` | `implementation` | `harness.execution.workflow` | 4 | `active` |
| `IMPL_EVALUATE_FIRST_REQUIRED` | `MUST` | `governance` | `impl.assertion_authoring.surface` | 3 | `active` |
| `IMPL_EVALUATE_RATIO_NON_REGRESSION_REQUIRED` | `MUST` | `governance` | `impl.assertion_authoring.metric_ratchet` | 3 | `active` |
| `IMPL_LIBRARY_BACKED_ASSERTIONS_NON_REGRESSION_REQUIRED` | `MUST` | `governance` | `impl.assertion_authoring.library_usage` | 3 | `active` |
| `LIBRARY_DOMAIN_INDEX_SYNC` | `MUST` | `governance` | `docs/spec/libraries/*/index.md` | 3 | `active` |
| `LIBRARY_DOMAIN_OWNERSHIP` | `MUST` | `governance` | `governance_and_conformance_library_paths` | 2 | `active` |
| `LIBRARY_PUBLIC_SURFACE_MODEL` | `MUST` | `governance` | `type_spec_lang_library_shape` | 3 | `active` |
| `LIBRARY_PUBLIC_SURFACE_RATIO_NON_REGRESSION` | `MUST` | `governance` | `specs.spec_lang_adoption.metric_non_regression` | 3 | `active` |
| `NAMING_FILENAME_STRICT_SEPARATORS` | `MUST` | `governance` | `docs_and_spec_filenames` | 2 | `active` |
| `NORMALIZATION_CHECK_GATE_REQUIRED` | `MUST` | `governance` | `scripts.runner_adapter` | 3 | `active` |
| `NORMALIZATION_CONTRACT_SCHEMA_BOOK_SYNC` | `MUST` | `governance` | `docs.spec.contract_schema_book_wording` | 2 | `active` |
| `NORMALIZATION_FIX_COMMAND_AVAILABLE` | `MUST` | `tooling` | `local_authoring_workflow` | 4 | `active` |
| `NORMALIZATION_MAPPING_AST_ONLY` | `MUST` | `schema` | `evaluate_and_policy_evaluate_yaml_authoring` | 4 | `active` |
| `NORMALIZATION_PROFILE_DEFINED` | `MUST` | `governance` | `docs.spec.schema.normalization_profile` | 2 | `active` |
| `NORMALIZATION_VIRTUAL_ROOT_PATHS_ONLY` | `MUST` | `governance` | `path_authoring.virtual_root` | 3 | `active` |
| `NO_EXECUTABLE_YAML_JSON_CASES_IN_CANONICAL_TREES` | `MUST` | `governance` | `docs.spec.canonical_executable_case_trees` | 3 | `active` |
| `OBJECTIVE_COURSE_CORRECTION_POLICY_DEFINED` | `MUST` | `governance` | `docs.spec.metrics.objective_baseline_updates` | 3 | `active` |
| `OBJECTIVE_METRIC_MANIFEST_VALID` | `MUST` | `governance` | `docs.spec.metrics.objective_manifest` | 4 | `active` |
| `OBJECTIVE_SCORECARD_NON_REGRESSION_REQUIRED` | `MUST` | `governance` | `docs.spec.metrics.objective_scorecard` | 2 | `active` |
| `OBJECTIVE_SCORECARD_REPORTED` | `MUST` | `governance` | `docs.spec.metrics.objective_scorecard` | 3 | `active` |
| `OBJECTIVE_TRIPWIRES_ENFORCED` | `MUST` | `governance` | `docs.spec.metrics.objective_tripwires` | 2 | `active` |
| `ORCHESTRATION_OPS_CAPABILITY_BINDING_REQUIRED` | `MUST` | `governance` | `orchestration.case.capabilities` | 2 | `active` |
| `ORCHESTRATION_OPS_DEEP_DOT_REQUIRED` | `MUST` | `governance` | `orchestration.ops.symbol_grammar` | 3 | `active` |
| `ORCHESTRATION_OPS_REGISTRY_DECLARED_REQUIRED` | `MUST` | `governance` | `orchestration.tools.registry` | 4 | `active` |
| `ORCHESTRATION_OPS_UNDERSCORE_LEGACY_FORBIDDEN` | `MUST` | `governance` | `orchestration.ops.legacy_symbols` | 2 | `active` |
| `ORCHESTRATION_POLICY_VIA_SPEC_LANG_ONLY` | `MUST` | `governance` | `runtime.gate_orchestration_policy` | 2 | `active` |
| `PORTABLE_SPEC_CANONICAL_SINGLE_SET` | `MUST` | `conformance` | `fixtures.portable.canonical_set` | 3 | `active` |
| `PORTABLE_SPEC_DETERMINISM_BY_CONSTRUCTION` | `SHOULD` | `conformance` | `fixtures.portable.determinism` | 3 | `active` |
| `PORTABLE_SPEC_EXPECT_PORTABLE_IMPL_OVERLAY` | `MUST` | `conformance` | `fixtures.expect_shape` | 3 | `active` |
| `REFERENCE_CHECK_IDS_EXIST` | `MUST` | `governance` | `governance.check_ids` | 2 | `active` |
| `REFERENCE_CONTRACT_PATHS_EXIST` | `MUST` | `governance` | `referenced_contract_paths` | 2 | `active` |
| `REFERENCE_EXTERNAL_REFS_POLICY` | `MUST` | `governance` | `external_references.policy` | 2 | `active` |
| `REFERENCE_LIBRARY_EXPORTS_USED` | `MUST` | `governance` | `docs/spec/libraries/* exports` | 2 | `active` |
| `REFERENCE_POLICY_SYMBOLS_RESOLVE` | `MUST` | `governance` | `governance.check.harness.policy_evaluate.var_symbols` | 2 | `active` |
| `REFERENCE_PRIVATE_SYMBOLS_FORBIDDEN` | `MUST` | `governance` | `cross_case_library_symbol_references` | 2 | `active` |
| `REFERENCE_SYMBOLS_EXIST` | `MUST` | `governance` | `harness.spec_lang.symbol_references` | 2 | `active` |
| `REFERENCE_TOKEN_ANCHORS_EXIST` | `MUST` | `governance` | `token_anchor_references` | 2 | `active` |
| `RUNNER_INDEPENDENCE_METRIC_REPORTED` | `MUST` | `governance` | `runtime.runner_independence.metric_report` | 2 | `active` |
| `RUNNER_INDEPENDENCE_NON_REGRESSION_REQUIRED` | `MUST` | `governance` | `runtime.runner_independence.metric_non_regression` | 3 | `active` |
| `RUNTIME_ASSERTIONS_VIA_SPEC_LANG` | `MUST` | `implementation` | `runtime.assertion_execution` | 2 | `active` |
| `RUNTIME_DECISIONS_VIA_SPEC_LANG_ONLY` | `MUST` | `implementation` | `runtime.assertion_decisions` | 2 | `active` |
| `RUNTIME_DEFAULT_GATE_RUST_ADAPTER_REQUIRED` | `MUST` | `governance` | `runtime.default_gate.adapter` | 3 | `active` |
| `RUNTIME_NON_PYTHON_LANES_FORBID_PYTHON_EXEC` | `MUST` | `governance` | `runtime.non_python_lanes.exec_tokens` | 2 | `active` |
| `RUNTIME_PUBLIC_DOCS_NO_DIRECT_RUST_ADAPTER_INVOCATION` | `MUST` | `governance` | `docs.runner_interface.public_usage` | 2 | `active` |
| `RUNTIME_PUBLIC_ENTRYPOINT_RUST_DEFAULT_REQUIRED` | `MUST` | `governance` | `runtime.runner_interface.default_mode` | 2 | `active` |
| `RUNTIME_PYTHON_DEPENDENCY_EVIDENCE_REPORTED` | `MUST` | `governance` | `runtime.python_dependency.metric_report` | 2 | `active` |
| `RUNTIME_PYTHON_DEPENDENCY_NON_REGRESSION_REQUIRED` | `MUST` | `governance` | `runtime.python_dependency.metric_non_regression` | 3 | `active` |
| `RUNTIME_PYTHON_LANE_EXPLICIT_OPT_IN_ONLY` | `MUST` | `governance` | `runtime.runner_interface.python_lane` | 2 | `active` |
| `RUNTIME_PYTHON_USAGE_SCOPED_TO_PYTHON_RUNNER` | `MUST` | `governance` | `runtime.python_usage.scope` | 3 | `active` |
| `RUNTIME_RUNNER_INTERFACE_CI_LANE_REQUIRED` | `MUST` | `governance` | `runtime.runner_interface.ci_lane` | 2 | `active` |
| `RUNTIME_RUNNER_INTERFACE_GATE_SYNC` | `MUST` | `governance` | `runtime.gate_orchestration` | 5 | `active` |
| `RUNTIME_RUNNER_INTERFACE_SUBCOMMANDS_DECLARED` | `MUST` | `governance` | `runtime.runner_interface.subcommands` | 2 | `active` |
| `RUNTIME_RUST_ADAPTER_NO_DELEGATION` | `MUST` | `governance` | `runtime.runner_interface.rust_adapter` | 2 | `active` |
| `RUNTIME_RUST_ADAPTER_NO_PYTHON_EXEC` | `MUST` | `runtime` | `scripts.rust.spec_runner_cli` | 3 | `active` |
| `RUNTIME_RUST_ADAPTER_TRANSITIVE_NO_PYTHON` | `MUST` | `governance` | `runtime.rust_adapter.transitive_path` | 2 | `active` |
| `RUNTIME_SCOPE_BOUNDED_FOR_V1` | `SHOULD` | `governance` | `runtime.support.matrix` | 3 | `active` |
| `RUNTIME_SINGLE_PUBLIC_RUNNER_ENTRYPOINT_REQUIRED` | `MUST` | `governance` | `runtime.runner_interface.public_entrypoint` | 2 | `active` |
| `RUST_PRIMARY_ADAPTER_EXEC_SMOKE_REQUIRED` | `MUST` | `governance` | `runtime.rust_primary.adapter_exec` | 2 | `active` |
| `RUST_PRIMARY_DOCS_ADOPTION_SYNC` | `SHOULD` | `docs` | `docs.rust_primary.adoption` | 2 | `active` |
| `RUST_PRIMARY_GATE_PATH_REQUIRED` | `MUST` | `governance` | `runtime.rust_primary.ci_lane` | 2 | `active` |
| `RUST_PRIMARY_INTERFACE_STABILITY_REQUIRED` | `MUST` | `governance` | `runtime.rust_primary.interface_stability` | 2 | `active` |
| `RUST_PRIMARY_NO_PYTHON_GATE_DEPENDENCY` | `MUST` | `governance` | `runtime.rust_primary.gate_dependency` | 2 | `active` |
| `RUST_PRIMARY_SHARED_CAPABILITY_PARITY_REQUIRED` | `MUST` | `governance` | `runtime.rust_primary.parity` | 2 | `active` |
| `RUST_PRIMARY_SUBCOMMAND_PARITY_REQUIRED` | `MUST` | `governance` | `runtime.rust_primary.interface_parity` | 2 | `active` |
| `SCHEMA_DOCS_GENERATED_FROM_REGISTRY_REQUIRED` | `MUST` | `governance` | `docs.spec.schema_v1` | 2 | `active` |
| `SCHEMA_PROSE_ONLY_RULES_FORBIDDEN` | `MUST` | `governance` | `schema.contract.wording` | 2 | `active` |
| `SCHEMA_REGISTRY_SOURCE_OF_TRUTH_REQUIRED` | `MUST` | `governance` | `schema.registry.source_of_truth` | 3 | `active` |
| `SCHEMA_REGISTRY_VALIDATION_REQUIRED` | `MUST` | `runtime` | `case.validation.pre_dispatch` | 3 | `active` |
| `SCHEMA_TYPE_PROFILE_COVERAGE_REQUIRED` | `MUST` | `governance` | `schema.registry.type_profiles` | 5 | `active` |
| `SCHEMA_UNKNOWN_KEYS_HARD_FAIL` | `MUST` | `runtime` | `case.top_level_keys` | 2 | `active` |
| `SPEC_DOMAIN_INDEX_SYNC` | `MUST` | `governance` | `domain index files` | 2 | `active` |
| `SPEC_LANG_ADOPTION_METRIC_REPORTED` | `MUST` | `governance` | `specs.spec_lang_adoption.metric_report` | 2 | `active` |
| `SPEC_LANG_ADOPTION_NON_REGRESSION_REQUIRED` | `MUST` | `governance` | `specs.spec_lang_adoption.metric_non_regression` | 3 | `active` |
| `SPEC_LANG_COLLECTION_FORMS_CONTRACTED` | `MUST` | `implementation` | `assert.tree.evaluate.collection_forms` | 3 | `active` |
| `SPEC_LANG_CURRY_ALL_BUILTINS` | `MUST` | `implementation` | `assert.tree.evaluate.currying` | 2 | `active` |
| `SPEC_LANG_DEEP_EQUALITY_DETERMINISTIC` | `MUST` | `implementation` | `assert.tree.evaluate.deep_equality` | 2 | `active` |
| `SPEC_LANG_ERROR_CLASSIFICATION` | `MUST` | `implementation` | `assert.tree.evaluate.errors` | 3 | `active` |
| `SPEC_LANG_EVALUATE_LIST_SHAPE` | `MUST` | `case` | `assert.tree.evaluate` | 3 | `active` |
| `SPEC_LANG_EVAL_BUDGETS_REQUIRED` | `MUST` | `implementation` | `assert.tree.evaluate.budgets` | 2 | `active` |
| `SPEC_LANG_LIBRARY_INCLUDE_FORMAT_SCOPE` | `MUST` | `schema` | `harness.spec_lang.includes` | 2 | `active` |
| `SPEC_LANG_LIBRARY_REUSE_MODEL` | `SHOULD` | `implementation` | `assert.tree.evaluate.library_symbols` | 2 | `active` |
| `SPEC_LANG_PREFERRED_AUTHORING` | `MUST` | `conformance` | `conformance_governance.assert.tree` | 3 | `active` |
| `SPEC_LANG_PROPER_TCO_REQUIRED` | `MUST` | `implementation` | `assert.tree.evaluate.recursion` | 2 | `active` |
| `SPEC_LANG_PURE_EVALUATOR` | `MUST` | `implementation` | `assert.tree.evaluate.evaluator` | 2 | `active` |
| `SPEC_LANG_PURE_NO_EFFECT_BUILTINS` | `MUST` | `implementation` | `assert.tree.evaluate.builtins` | 2 | `active` |
| `SPEC_LANG_SET_ALGEBRA_PARITY` | `MUST` | `implementation` | `assert.tree.evaluate.set_algebra` | 2 | `active` |
| `SPEC_LANG_STDLIB_CONFORMANCE_COVERAGE_REQUIRED` | `MUST` | `governance` | `spec_lang.stdlib.conformance` | 3 | `active` |
| `SPEC_LANG_STDLIB_DOCS_SYNC_REQUIRED` | `MUST` | `governance` | `spec_lang.stdlib.docs` | 2 | `active` |
| `SPEC_LANG_STDLIB_PROFILE_COMPLETE` | `MUST` | `governance` | `spec_lang.stdlib.implementations` | 2 | `active` |
| `SPEC_LANG_STDLIB_PROFILE_DEFINED` | `MUST` | `contract` | `spec_lang.stdlib.profile` | 2 | `active` |
| `SPEC_LANG_STDLIB_PY_PHP_PARITY_REQUIRED` | `MUST` | `governance` | `spec_lang.stdlib.parity` | 2 | `active` |
| `SPEC_LAYOUT_DOMAIN_TREES` | `MUST` | `governance` | `docs/spec tree layout` | 2 | `active` |
| `SPEC_PORTABILITY_METRIC_REPORTED` | `MUST` | `governance` | `specs.portability.metric_report` | 4 | `active` |
| `SPEC_PORTABILITY_NON_REGRESSION_REQUIRED` | `MUST` | `governance` | `specs.portability.metric_non_regression` | 3 | `active` |
| `SPEC_PORTABILITY_THRESHOLD_ENFORCED` | `SHOULD` | `governance` | `specs.portability.metric_thresholds` | 3 | `active` |
<!-- GENERATED:END policy_rule_catalog -->
