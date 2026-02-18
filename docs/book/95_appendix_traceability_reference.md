# Traceability Reference

```yaml doc-meta
doc_id: DOC-REF-095
title: Appendix Traceability Reference
status: active
audience: reviewer
owns_tokens:
- appendix_traceability_reference
requires_tokens:
- quickstart_minimal_case
commands:
- run: ./scripts/runner_adapter.sh docs-generate-check
  purpose: Verify generated traceability catalog remains synchronized.
examples:
- id: EX-APP-TRACE-001
  runnable: false
  opt_out_reason: Generated reference page intentionally contains no runnable fenced examples.
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

This page is machine-generated from traceability link mappings.

## Purpose

Provide generated policy-to-contract/schema/test implementation traceability links.

## Inputs

- traceability registry YAML

## Outputs

- deterministic traceability catalog tables

## Failure Modes

- stale generated block after traceability edits
- missing generated markers
- unresolved rule references

<!-- GENERATED:START traceability_catalog -->

## Generated Traceability Catalog

- link_count: 246
- rules_with_conformance_cases: 50
- rules_with_unit_tests: 246
- rules_with_implementation_refs: 244

| rule_id | policy_ref | contract_refs | schema_refs | conformance_cases | unit_tests | implementation_refs |
|---|---|---|---|---|---|---|
| `API_HTTP_CORS_PRELIGHT_AND_ACTUAL_SUPPORTED` | `docs/spec/contract/policy_v1.yaml#API_HTTP_CORS_PRELIGHT_AND_ACTUAL_SUPPORTED` | 2 | 1 | 1 | 1 | 2 |
| `API_HTTP_DETERMINISTIC_DEFAULT_REQUIRED` | `docs/spec/contract/policy_v1.yaml#API_HTTP_DETERMINISTIC_DEFAULT_REQUIRED` | 1 | 1 | 2 | 1 | 1 |
| `API_HTTP_LIVE_MODE_EXPLICIT_OPT_IN_REQUIRED` | `docs/spec/contract/policy_v1.yaml#API_HTTP_LIVE_MODE_EXPLICIT_OPT_IN_REQUIRED` | 1 | 1 | 1 | 2 | 2 |
| `API_HTTP_OAUTH_ENV_REF_ONLY_REQUIRED` | `docs/spec/contract/policy_v1.yaml#API_HTTP_OAUTH_ENV_REF_ONLY_REQUIRED` | 1 | 1 | 1 | 2 | 2 |
| `API_HTTP_OAUTH_HARNESS_PROFILE_SUPPORTED` | `docs/spec/contract/policy_v1.yaml#API_HTTP_OAUTH_HARNESS_PROFILE_SUPPORTED` | 2 | 1 | 1 | 1 | 1 |
| `API_HTTP_OAUTH_SECRET_REDACTION_REQUIRED` | `docs/spec/contract/policy_v1.yaml#API_HTTP_OAUTH_SECRET_REDACTION_REQUIRED` | 1 | 1 | 1 | 1 | 1 |
| `API_HTTP_PY_PHP_BEHAVIOR_PARITY_REQUIRED` | `docs/spec/contract/policy_v1.yaml#API_HTTP_PY_PHP_BEHAVIOR_PARITY_REQUIRED` | 1 | 1 | 2 | 2 | 2 |
| `API_HTTP_SCENARIO_DETERMINISTIC_LIFECYCLE_REQUIRED` | `docs/spec/contract/policy_v1.yaml#API_HTTP_SCENARIO_DETERMINISTIC_LIFECYCLE_REQUIRED` | 1 | 1 | 1 | 1 | 1 |
| `API_HTTP_SCENARIO_ROUNDTRIP_SUPPORTED` | `docs/spec/contract/policy_v1.yaml#API_HTTP_SCENARIO_ROUNDTRIP_SUPPORTED` | 1 | 1 | 1 | 1 | 2 |
| `API_HTTP_TUTORIAL_COVERAGE_REQUIRED` | `docs/spec/contract/policy_v1.yaml#API_HTTP_TUTORIAL_COVERAGE_REQUIRED` | 2 | 0 | 0 | 1 | 1 |
| `API_HTTP_VERB_SUITE_REQUIRED` | `docs/spec/contract/policy_v1.yaml#API_HTTP_VERB_SUITE_REQUIRED` | 1 | 1 | 7 | 1 | 2 |
| `ASSERT_ADAPTER_PROJECTION_SYNC_REQUIRED` | `docs/spec/contract/policy_v1.yaml#ASSERT_ADAPTER_PROJECTION_SYNC_REQUIRED` | 1 | 1 | 1 | 1 | 7 |
| `ASSERT_COMPILER_SCHEMA_MATRIX_SYNC` | `docs/spec/contract/policy_v1.yaml#ASSERT_COMPILER_SCHEMA_MATRIX_SYNC` | 3 | 1 | 0 | 2 | 3 |
| `ASSERT_CONTEXT_PROJECTION_CONTRACT_REQUIRED` | `docs/spec/contract/policy_v1.yaml#ASSERT_CONTEXT_PROJECTION_CONTRACT_REQUIRED` | 2 | 2 | 1 | 1 | 5 |
| `ASSERT_DOMAIN_ASSERTIONS_LIBRARY_BACKED` | `docs/spec/contract/policy_v1.yaml#ASSERT_DOMAIN_ASSERTIONS_LIBRARY_BACKED` | 2 | 1 | 2 | 1 | 7 |
| `ASSERT_HEALTH_GLOBAL_AND_PER_CASE_POLICY` | `docs/spec/contract/policy_v1.yaml#ASSERT_HEALTH_GLOBAL_AND_PER_CASE_POLICY` | 2 | 1 | 3 | 3 | 3 |
| `ASSERT_HEALTH_MODE_VALID_VALUES` | `docs/spec/contract/policy_v1.yaml#ASSERT_HEALTH_MODE_VALID_VALUES` | 1 | 1 | 1 | 1 | 1 |
| `ASSERT_HEALTH_NON_PORTABLE_REGEX_DIAGNOSTIC` | `docs/spec/contract/policy_v1.yaml#ASSERT_HEALTH_NON_PORTABLE_REGEX_DIAGNOSTIC` | 3 | 1 | 1 | 2 | 3 |
| `ASSERT_HEALTH_REDUNDANT_BRANCH_DIAGNOSTIC` | `docs/spec/contract/policy_v1.yaml#ASSERT_HEALTH_REDUNDANT_BRANCH_DIAGNOSTIC` | 2 | 1 | 1 | 2 | 2 |
| `ASSERT_NO_NON_JSON_EVALUATOR_TYPES` | `docs/spec/contract/policy_v1.yaml#ASSERT_NO_NON_JSON_EVALUATOR_TYPES` | 2 | 1 | 1 | 1 | 3 |
| `ASSERT_SUBJECT_PROFILE_JSON_CORE_ONLY` | `docs/spec/contract/policy_v1.yaml#ASSERT_SUBJECT_PROFILE_JSON_CORE_ONLY` | 2 | 1 | 2 | 1 | 3 |
| `ASSERT_SUGAR_OPERATORS_COMPILE_ONLY` | `docs/spec/contract/policy_v1.yaml#ASSERT_SUGAR_OPERATORS_COMPILE_ONLY` | 3 | 1 | 1 | 3 | 4 |
| `ASSERT_TARGET_CONTRACT_SUBJECT_DRIVEN` | `docs/spec/contract/policy_v1.yaml#ASSERT_TARGET_CONTRACT_SUBJECT_DRIVEN` | 4 | 1 | 0 | 1 | 2 |
| `ASSERT_UNIVERSAL_CORE_EVALUATE_ONLY` | `docs/spec/contract/policy_v1.yaml#ASSERT_UNIVERSAL_CORE_EVALUATE_ONLY` | 3 | 1 | 1 | 2 | 3 |
| `CHAIN_CONTRACT_SINGLE_LOCATION_REQUIRED` | `docs/spec/contract/policy_v1.yaml#CHAIN_CONTRACT_SINGLE_LOCATION_REQUIRED` | 1 | 1 | 0 | 1 | 2 |
| `CHAIN_CYCLE_FORBIDDEN` | `docs/spec/contract/policy_v1.yaml#CHAIN_CYCLE_FORBIDDEN` | 1 | 1 | 0 | 1 | 2 |
| `CHAIN_EXPORTS_EXPLICIT_REQUIRED` | `docs/spec/contract/policy_v1.yaml#CHAIN_EXPORTS_EXPLICIT_REQUIRED` | 1 | 1 | 0 | 1 | 1 |
| `CHAIN_EXPORTS_FROM_KEY_REQUIRED` | `docs/spec/contract/policy_v1.yaml#CHAIN_EXPORTS_FROM_KEY_REQUIRED` | 1 | 1 | 0 | 2 | 3 |
| `CHAIN_EXPORTS_LIST_ONLY_REQUIRED` | `docs/spec/contract/policy_v1.yaml#CHAIN_EXPORTS_LIST_ONLY_REQUIRED` | 1 | 1 | 1 | 2 | 3 |
| `CHAIN_FAIL_FAST_DEFAULT_REQUIRED` | `docs/spec/contract/policy_v1.yaml#CHAIN_FAIL_FAST_DEFAULT_REQUIRED` | 1 | 1 | 0 | 1 | 1 |
| `CHAIN_IMPORT_ALIAS_COLLISION_FORBIDDEN` | `docs/spec/contract/policy_v1.yaml#CHAIN_IMPORT_ALIAS_COLLISION_FORBIDDEN` | 1 | 1 | 0 | 2 | 2 |
| `CHAIN_LEGACY_FROM_TARGET_FORBIDDEN` | `docs/spec/contract/policy_v1.yaml#CHAIN_LEGACY_FROM_TARGET_FORBIDDEN` | 1 | 1 | 1 | 2 | 4 |
| `CHAIN_LIBRARY_SYMBOL_EXPORTS_VALID` | `docs/spec/contract/policy_v1.yaml#CHAIN_LIBRARY_SYMBOL_EXPORTS_VALID` | 2 | 1 | 0 | 3 | 3 |
| `CHAIN_REFERENCE_CONTRACT_REQUIRED` | `docs/spec/contract/policy_v1.yaml#CHAIN_REFERENCE_CONTRACT_REQUIRED` | 1 | 1 | 1 | 2 | 3 |
| `CHAIN_SHARED_CONTEXT_REQUIRED` | `docs/spec/contract/policy_v1.yaml#CHAIN_SHARED_CONTEXT_REQUIRED` | 1 | 1 | 0 | 1 | 2 |
| `CHAIN_STEP_CLASS_REQUIRED` | `docs/spec/contract/policy_v1.yaml#CHAIN_STEP_CLASS_REQUIRED` | 1 | 1 | 0 | 2 | 2 |
| `CLI_RUN_CONFORMANCE_EXPLICIT_ENTRYPOINT` | `docs/spec/contract/policy_v1.yaml#CLI_RUN_CONFORMANCE_EXPLICIT_ENTRYPOINT` | 2 | 1 | 2 | 2 | 0 |
| `CLI_RUN_CONFORMANCE_NO_ENV_DEPENDENCY` | `docs/spec/contract/policy_v1.yaml#CLI_RUN_CONFORMANCE_NO_ENV_DEPENDENCY` | 2 | 1 | 2 | 2 | 0 |
| `CLI_RUN_ENTRYPOINT_REQUIRED` | `docs/spec/contract/policy_v1.yaml#CLI_RUN_ENTRYPOINT_REQUIRED` | 1 | 1 | 1 | 2 | 1 |
| `CLI_RUN_ENV_ALLOWLIST_CONTROL` | `docs/spec/contract/policy_v1.yaml#CLI_RUN_ENV_ALLOWLIST_CONTROL` | 1 | 1 | 0 | 1 | 1 |
| `CLI_RUN_SAFE_MODE_RESTRICTS_HOOKS` | `docs/spec/contract/policy_v1.yaml#CLI_RUN_SAFE_MODE_RESTRICTS_HOOKS` | 1 | 1 | 0 | 1 | 1 |
| `CONFORMANCE_CASE_STYLE_GUARD` | `docs/spec/contract/policy_v1.yaml#CONFORMANCE_CASE_STYLE_GUARD` | 2 | 0 | 0 | 1 | 1 |
| `CONFORMANCE_EVALUATE_FIRST_REQUIRED` | `docs/spec/contract/policy_v1.yaml#CONFORMANCE_EVALUATE_FIRST_REQUIRED` | 3 | 1 | 0 | 2 | 3 |
| `CONFORMANCE_EXPECT_OVERLAY_RESOLUTION` | `docs/spec/contract/policy_v1.yaml#CONFORMANCE_EXPECT_OVERLAY_RESOLUTION` | 1 | 1 | 0 | 2 | 1 |
| `CONFORMANCE_LIBRARY_POLICY_USAGE_REQUIRED` | `docs/spec/contract/policy_v1.yaml#CONFORMANCE_LIBRARY_POLICY_USAGE_REQUIRED` | 3 | 1 | 0 | 1 | 1 |
| `CONFORMANCE_NO_AMBIENT_ASSUMPTIONS_GUARD` | `docs/spec/contract/policy_v1.yaml#CONFORMANCE_NO_AMBIENT_ASSUMPTIONS_GUARD` | 2 | 1 | 0 | 2 | 2 |
| `CONFORMANCE_PURPOSE_QUALITY_GATE` | `docs/spec/contract/policy_v1.yaml#CONFORMANCE_PURPOSE_QUALITY_GATE` | 2 | 1 | 0 | 2 | 2 |
| `CONFORMANCE_REQUIRES_CAPABILITIES_POLICY` | `docs/spec/contract/policy_v1.yaml#CONFORMANCE_REQUIRES_CAPABILITIES_POLICY` | 2 | 1 | 0 | 2 | 1 |
| `CONFORMANCE_SPEC_LANG_FIXTURE_LIBRARY_USAGE_REQUIRED` | `docs/spec/contract/policy_v1.yaml#CONFORMANCE_SPEC_LANG_FIXTURE_LIBRARY_USAGE_REQUIRED` | 2 | 1 | 3 | 1 | 2 |
| `CONTRACT_ASSERTIONS_METRIC_REPORTED` | `docs/spec/contract/policy_v1.yaml#CONTRACT_ASSERTIONS_METRIC_REPORTED` | 2 | 1 | 0 | 3 | 3 |
| `CONTRACT_ASSERTIONS_NON_REGRESSION_REQUIRED` | `docs/spec/contract/policy_v1.yaml#CONTRACT_ASSERTIONS_NON_REGRESSION_REQUIRED` | 2 | 1 | 0 | 2 | 3 |
| `CONTRACT_MUST_RULE_COVERAGE_COMPLETE` | `docs/spec/contract/policy_v1.yaml#CONTRACT_MUST_RULE_COVERAGE_COMPLETE` | 2 | 1 | 0 | 2 | 2 |
| `CURRENT_SPEC_POLICY_KEY_NAMES` | `docs/spec/contract/policy_v1.yaml#CURRENT_SPEC_POLICY_KEY_NAMES` | 2 | 1 | 0 | 1 | 2 |
| `DATA_ARTIFACT_SURFACES_MUST_REMAIN_MACHINE_FILES` | `docs/spec/contract/policy_v1.yaml#DATA_ARTIFACT_SURFACES_MUST_REMAIN_MACHINE_FILES` | 1 | 1 | 0 | 1 | 2 |
| `DOCS_ADOPTION_PROFILES_SYNC` | `docs/spec/contract/policy_v1.yaml#DOCS_ADOPTION_PROFILES_SYNC` | 3 | 0 | 0 | 2 | 3 |
| `DOCS_API_CATALOGS_GENERATED_AND_SYNCED` | `docs/spec/contract/policy_v1.yaml#DOCS_API_CATALOGS_GENERATED_AND_SYNCED` | 2 | 3 | 0 | 3 | 6 |
| `DOCS_BOOK_APPENDIX_CATALOG_NAMESPACE_REQUIRED` | `docs/spec/contract/policy_v1.yaml#DOCS_BOOK_APPENDIX_CATALOG_NAMESPACE_REQUIRED` | 1 | 2 | 0 | 1 | 2 |
| `DOCS_BOOK_CHAPTER_ORDER_CANONICAL` | `docs/spec/contract/policy_v1.yaml#DOCS_BOOK_CHAPTER_ORDER_CANONICAL` | 1 | 1 | 0 | 1 | 2 |
| `DOCS_CLI_FLAGS_DOCUMENTED` | `docs/spec/contract/policy_v1.yaml#DOCS_CLI_FLAGS_DOCUMENTED` | 4 | 0 | 0 | 2 | 2 |
| `DOCS_COMMAND_EXAMPLES_VERIFIED` | `docs/spec/contract/policy_v1.yaml#DOCS_COMMAND_EXAMPLES_VERIFIED` | 1 | 2 | 0 | 3 | 4 |
| `DOCS_CONTRACT_SCHEMA_BOOK_TOKEN_SYNC` | `docs/spec/contract/policy_v1.yaml#DOCS_CONTRACT_SCHEMA_BOOK_TOKEN_SYNC` | 3 | 1 | 0 | 2 | 2 |
| `DOCS_DOCGEN_OUTPUT_MIN_QUALITY_SCORE_REQUIRED` | `docs/spec/contract/policy_v1.yaml#DOCS_DOCGEN_OUTPUT_MIN_QUALITY_SCORE_REQUIRED` | 1 | 1 | 0 | 1 | 1 |
| `DOCS_EXAMPLES_RUNNABLE_OR_EXPLICITLY_OPTED_OUT` | `docs/spec/contract/policy_v1.yaml#DOCS_EXAMPLES_RUNNABLE_OR_EXPLICITLY_OPTED_OUT` | 1 | 1 | 0 | 2 | 2 |
| `DOCS_EXAMPLE_IDS_UNIQUE` | `docs/spec/contract/policy_v1.yaml#DOCS_EXAMPLE_IDS_UNIQUE` | 1 | 1 | 0 | 3 | 4 |
| `DOCS_FILENAME_POLICY_REQUIRED` | `docs/spec/contract/policy_v1.yaml#DOCS_FILENAME_POLICY_REQUIRED` | 2 | 1 | 0 | 1 | 2 |
| `DOCS_GENERATED_ARTIFACTS_FRESH` | `docs/spec/contract/policy_v1.yaml#DOCS_GENERATED_ARTIFACTS_FRESH` | 2 | 1 | 0 | 3 | 4 |
| `DOCS_GENERATED_SECTIONS_READ_ONLY` | `docs/spec/contract/policy_v1.yaml#DOCS_GENERATED_SECTIONS_READ_ONLY` | 1 | 1 | 0 | 1 | 2 |
| `DOCS_GENERATED_SURFACES_SYNC_REQUIRED` | `docs/spec/contract/policy_v1.yaml#DOCS_GENERATED_SURFACES_SYNC_REQUIRED` | 1 | 1 | 0 | 1 | 2 |
| `DOCS_GENERATOR_ORCHESTRATOR_REQUIRED` | `docs/spec/contract/policy_v1.yaml#DOCS_GENERATOR_ORCHESTRATOR_REQUIRED` | 1 | 1 | 0 | 1 | 4 |
| `DOCS_GENERATOR_REGISTRY_DEFINED` | `docs/spec/contract/policy_v1.yaml#DOCS_GENERATOR_REGISTRY_DEFINED` | 2 | 1 | 0 | 1 | 2 |
| `DOCS_GENERATOR_REPORT_REQUIRED` | `docs/spec/contract/policy_v1.yaml#DOCS_GENERATOR_REPORT_REQUIRED` | 1 | 1 | 0 | 1 | 3 |
| `DOCS_GOVERNANCE_CHECK_CATALOG_SYNC_REQUIRED` | `docs/spec/contract/policy_v1.yaml#DOCS_GOVERNANCE_CHECK_CATALOG_SYNC_REQUIRED` | 1 | 1 | 0 | 1 | 2 |
| `DOCS_HARNESS_FIELD_SEMANTICS_DOC_REQUIRED` | `docs/spec/contract/policy_v1.yaml#DOCS_HARNESS_FIELD_SEMANTICS_DOC_REQUIRED` | 1 | 1 | 0 | 1 | 1 |
| `DOCS_HISTORY_REVIEWS_NAMESPACE_REQUIRED` | `docs/spec/contract/policy_v1.yaml#DOCS_HISTORY_REVIEWS_NAMESPACE_REQUIRED` | 1 | 1 | 0 | 1 | 2 |
| `DOCS_INDEX_FILENAME_INDEX_MD_REQUIRED` | `docs/spec/contract/policy_v1.yaml#DOCS_INDEX_FILENAME_INDEX_MD_REQUIRED` | 2 | 1 | 0 | 1 | 2 |
| `DOCS_INSTRUCTIONS_REQUIRED_SECTIONS` | `docs/spec/contract/policy_v1.yaml#DOCS_INSTRUCTIONS_REQUIRED_SECTIONS` | 1 | 1 | 0 | 3 | 4 |
| `DOCS_LAYOUT_CANONICAL_TREES_REQUIRED` | `docs/spec/contract/policy_v1.yaml#DOCS_LAYOUT_CANONICAL_TREES_REQUIRED` | 2 | 1 | 0 | 1 | 2 |
| `DOCS_MAKE_COMMANDS_SYNC` | `docs/spec/contract/policy_v1.yaml#DOCS_MAKE_COMMANDS_SYNC` | 2 | 0 | 0 | 2 | 2 |
| `DOCS_MARKDOWN_NAMESPACE_LEGACY_ALIAS_FORBIDDEN` | `docs/spec/contract/policy_v1.yaml#DOCS_MARKDOWN_NAMESPACE_LEGACY_ALIAS_FORBIDDEN` | 2 | 1 | 1 | 1 | 2 |
| `DOCS_MARKDOWN_STRUCTURED_ASSERTIONS_REQUIRED` | `docs/spec/contract/policy_v1.yaml#DOCS_MARKDOWN_STRUCTURED_ASSERTIONS_REQUIRED` | 1 | 1 | 0 | 1 | 2 |
| `DOCS_META_SCHEMA_VALID` | `docs/spec/contract/policy_v1.yaml#DOCS_META_SCHEMA_VALID` | 1 | 2 | 0 | 3 | 4 |
| `DOCS_METRICS_FIELD_CATALOG_SYNC_REQUIRED` | `docs/spec/contract/policy_v1.yaml#DOCS_METRICS_FIELD_CATALOG_SYNC_REQUIRED` | 1 | 1 | 0 | 1 | 2 |
| `DOCS_NO_OS_ARTIFACT_FILES_TRACKED` | `docs/spec/contract/policy_v1.yaml#DOCS_NO_OS_ARTIFACT_FILES_TRACKED` | 1 | 1 | 0 | 1 | 3 |
| `DOCS_OPERABILITY_METRIC_REPORTED` | `docs/spec/contract/policy_v1.yaml#DOCS_OPERABILITY_METRIC_REPORTED` | 2 | 1 | 0 | 3 | 3 |
| `DOCS_OPERABILITY_NON_REGRESSION_REQUIRED` | `docs/spec/contract/policy_v1.yaml#DOCS_OPERABILITY_NON_REGRESSION_REQUIRED` | 2 | 1 | 0 | 2 | 3 |
| `DOCS_POLICY_RULE_CATALOG_SYNC_REQUIRED` | `docs/spec/contract/policy_v1.yaml#DOCS_POLICY_RULE_CATALOG_SYNC_REQUIRED` | 1 | 1 | 0 | 1 | 2 |
| `DOCS_REFERENCE_INDEX_SYNC` | `docs/spec/contract/policy_v1.yaml#DOCS_REFERENCE_INDEX_SYNC` | 2 | 0 | 0 | 2 | 2 |
| `DOCS_REFERENCE_MANIFEST_SYNC` | `docs/spec/contract/policy_v1.yaml#DOCS_REFERENCE_MANIFEST_SYNC` | 2 | 1 | 0 | 3 | 4 |
| `DOCS_REFERENCE_NAMESPACE_CHAPTERS_SYNC_REQUIRED` | `docs/spec/contract/policy_v1.yaml#DOCS_REFERENCE_NAMESPACE_CHAPTERS_SYNC_REQUIRED` | 1 | 1 | 0 | 1 | 2 |
| `DOCS_REF_SURFACE_COMPLETE` | `docs/spec/contract/policy_v1.yaml#DOCS_REF_SURFACE_COMPLETE` | 2 | 1 | 0 | 2 | 2 |
| `DOCS_RELEASE_CONTRACT_AUTOMATION_ONLY` | `docs/spec/contract/policy_v1.yaml#DOCS_RELEASE_CONTRACT_AUTOMATION_ONLY` | 2 | 0 | 0 | 2 | 3 |
| `DOCS_REQUIRED_SECTIONS_PRESENT` | `docs/spec/contract/policy_v1.yaml#DOCS_REQUIRED_SECTIONS_PRESENT` | 4 | 0 | 0 | 2 | 2 |
| `DOCS_RUNNER_COMMAND_SEMANTICS_DOC_REQUIRED` | `docs/spec/contract/policy_v1.yaml#DOCS_RUNNER_COMMAND_SEMANTICS_DOC_REQUIRED` | 1 | 1 | 0 | 1 | 1 |
| `DOCS_SPEC_LANG_GUIDE_BEFORE_REFERENCE_REQUIRED` | `docs/spec/contract/policy_v1.yaml#DOCS_SPEC_LANG_GUIDE_BEFORE_REFERENCE_REQUIRED` | 1 | 1 | 0 | 1 | 2 |
| `DOCS_SPEC_SCHEMA_FIELD_CATALOG_SYNC_REQUIRED` | `docs/spec/contract/policy_v1.yaml#DOCS_SPEC_SCHEMA_FIELD_CATALOG_SYNC_REQUIRED` | 2 | 2 | 0 | 1 | 2 |
| `DOCS_STDLIB_EXAMPLES_REQUIRED` | `docs/spec/contract/policy_v1.yaml#DOCS_STDLIB_EXAMPLES_REQUIRED` | 1 | 1 | 0 | 1 | 1 |
| `DOCS_STDLIB_SYMBOL_DESCRIPTION_REQUIRED` | `docs/spec/contract/policy_v1.yaml#DOCS_STDLIB_SYMBOL_DESCRIPTION_REQUIRED` | 1 | 1 | 0 | 1 | 3 |
| `DOCS_TOKEN_DEPENDENCY_RESOLVED` | `docs/spec/contract/policy_v1.yaml#DOCS_TOKEN_DEPENDENCY_RESOLVED` | 1 | 1 | 0 | 3 | 4 |
| `DOCS_TOKEN_OWNERSHIP_UNIQUE` | `docs/spec/contract/policy_v1.yaml#DOCS_TOKEN_OWNERSHIP_UNIQUE` | 1 | 1 | 0 | 3 | 4 |
| `DOCS_TRACEABILITY_CATALOG_SYNC_REQUIRED` | `docs/spec/contract/policy_v1.yaml#DOCS_TRACEABILITY_CATALOG_SYNC_REQUIRED` | 1 | 1 | 0 | 1 | 2 |
| `DOC_ASSERTION_OPERATOR_DOC_SYNC` | `docs/spec/contract/policy_v1.yaml#DOC_ASSERTION_OPERATOR_DOC_SYNC` | 1 | 1 | 0 | 1 | 1 |
| `DOC_NORMATIVE_PAGE_TRACEABILITY` | `docs/spec/contract/policy_v1.yaml#DOC_NORMATIVE_PAGE_TRACEABILITY` | 12 | 1 | 0 | 1 | 1 |
| `DOC_REGEX_PROFILE_LINKAGE` | `docs/spec/contract/policy_v1.yaml#DOC_REGEX_PROFILE_LINKAGE` | 2 | 1 | 0 | 1 | 1 |
| `EXECUTABLE_DISCOVERY_MARKDOWN_ONLY` | `docs/spec/contract/policy_v1.yaml#EXECUTABLE_DISCOVERY_MARKDOWN_ONLY` | 2 | 1 | 0 | 2 | 3 |
| `EXECUTABLE_SPEC_LANG_INCLUDES_FORBIDDEN` | `docs/spec/contract/policy_v1.yaml#EXECUTABLE_SPEC_LANG_INCLUDES_FORBIDDEN` | 1 | 1 | 0 | 2 | 4 |
| `EXECUTABLE_SURFACES_MUST_BE_SPEC_MD` | `docs/spec/contract/policy_v1.yaml#EXECUTABLE_SURFACES_MUST_BE_SPEC_MD` | 3 | 1 | 0 | 1 | 2 |
| `GOVERNANCE_DECISIONS_VIA_SPEC_LANG_ONLY` | `docs/spec/contract/policy_v1.yaml#GOVERNANCE_DECISIONS_VIA_SPEC_LANG_ONLY` | 1 | 1 | 0 | 1 | 2 |
| `GOVERNANCE_EXTRACTOR_ONLY_NO_VERDICT_BRANCHING` | `docs/spec/contract/policy_v1.yaml#GOVERNANCE_EXTRACTOR_ONLY_NO_VERDICT_BRANCHING` | 2 | 1 | 0 | 1 | 2 |
| `GOVERNANCE_POLICY_EVALUATE_REQUIRED` | `docs/spec/contract/policy_v1.yaml#GOVERNANCE_POLICY_EVALUATE_REQUIRED` | 2 | 1 | 0 | 1 | 2 |
| `GOVERNANCE_POLICY_LIBRARY_USAGE_NON_REGRESSION` | `docs/spec/contract/policy_v1.yaml#GOVERNANCE_POLICY_LIBRARY_USAGE_NON_REGRESSION` | 2 | 1 | 0 | 2 | 3 |
| `GOVERNANCE_POLICY_LIBRARY_USAGE_REQUIRED` | `docs/spec/contract/policy_v1.yaml#GOVERNANCE_POLICY_LIBRARY_USAGE_REQUIRED` | 3 | 1 | 0 | 1 | 1 |
| `GOVERNANCE_STRUCTURED_ASSERTIONS_REQUIRED` | `docs/spec/contract/policy_v1.yaml#GOVERNANCE_STRUCTURED_ASSERTIONS_REQUIRED` | 2 | 1 | 0 | 1 | 2 |
| `GOVERNANCE_SUBJECT_MODEL_SPEC_LANG_DECISIONS` | `docs/spec/contract/policy_v1.yaml#GOVERNANCE_SUBJECT_MODEL_SPEC_LANG_DECISIONS` | 1 | 1 | 0 | 1 | 1 |
| `GOVERNANCE_SYMBOL_RESOLUTION_RATIO_NON_REGRESSION` | `docs/spec/contract/policy_v1.yaml#GOVERNANCE_SYMBOL_RESOLUTION_RATIO_NON_REGRESSION` | 3 | 1 | 0 | 2 | 3 |
| `HARNESS_CONTRACT_OVERLAY_SYNC_REQUIRED` | `docs/spec/contract/policy_v1.yaml#HARNESS_CONTRACT_OVERLAY_SYNC_REQUIRED` | 2 | 2 | 0 | 1 | 1 |
| `HARNESS_LOCAL_WORKFLOW_DUPLICATION_FORBIDDEN` | `docs/spec/contract/policy_v1.yaml#HARNESS_LOCAL_WORKFLOW_DUPLICATION_FORBIDDEN` | 1 | 1 | 0 | 1 | 1 |
| `HARNESS_SUBJECT_TARGET_MAP_DECLARED` | `docs/spec/contract/policy_v1.yaml#HARNESS_SUBJECT_TARGET_MAP_DECLARED` | 1 | 1 | 0 | 1 | 2 |
| `HARNESS_TYPE_OVERLAY_COMPLETE_REQUIRED` | `docs/spec/contract/policy_v1.yaml#HARNESS_TYPE_OVERLAY_COMPLETE_REQUIRED` | 1 | 2 | 0 | 1 | 1 |
| `HARNESS_WORKFLOW_COMPONENTS_REQUIRED` | `docs/spec/contract/policy_v1.yaml#HARNESS_WORKFLOW_COMPONENTS_REQUIRED` | 1 | 1 | 0 | 1 | 8 |
| `IMPL_EVALUATE_FIRST_REQUIRED` | `docs/spec/contract/policy_v1.yaml#IMPL_EVALUATE_FIRST_REQUIRED` | 2 | 1 | 0 | 1 | 2 |
| `IMPL_EVALUATE_RATIO_NON_REGRESSION_REQUIRED` | `docs/spec/contract/policy_v1.yaml#IMPL_EVALUATE_RATIO_NON_REGRESSION_REQUIRED` | 2 | 1 | 0 | 2 | 3 |
| `IMPL_LIBRARY_BACKED_ASSERTIONS_NON_REGRESSION_REQUIRED` | `docs/spec/contract/policy_v1.yaml#IMPL_LIBRARY_BACKED_ASSERTIONS_NON_REGRESSION_REQUIRED` | 2 | 1 | 0 | 2 | 3 |
| `LIBRARY_COLOCATED_SYMBOL_TESTS_REQUIRED` | `docs/spec/contract/policy_v1.yaml#LIBRARY_COLOCATED_SYMBOL_TESTS_REQUIRED` | 1 | 1 | 0 | 1 | 2 |
| `LIBRARY_DOMAIN_INDEX_SYNC` | `docs/spec/contract/policy_v1.yaml#LIBRARY_DOMAIN_INDEX_SYNC` | 2 | 1 | 0 | 1 | 3 |
| `LIBRARY_DOMAIN_OWNERSHIP` | `docs/spec/contract/policy_v1.yaml#LIBRARY_DOMAIN_OWNERSHIP` | 2 | 1 | 0 | 1 | 2 |
| `LIBRARY_LEGACY_DEFINITIONS_KEY_FORBIDDEN` | `docs/spec/contract/policy_v1.yaml#LIBRARY_LEGACY_DEFINITIONS_KEY_FORBIDDEN` | 1 | 1 | 1 | 2 | 6 |
| `LIBRARY_PUBLIC_SURFACE_MODEL` | `docs/spec/contract/policy_v1.yaml#LIBRARY_PUBLIC_SURFACE_MODEL` | 1 | 1 | 0 | 2 | 3 |
| `LIBRARY_PUBLIC_SURFACE_RATIO_NON_REGRESSION` | `docs/spec/contract/policy_v1.yaml#LIBRARY_PUBLIC_SURFACE_RATIO_NON_REGRESSION` | 2 | 1 | 0 | 2 | 3 |
| `LIBRARY_SINGLE_PUBLIC_SYMBOL_PER_CASE_REQUIRED` | `docs/spec/contract/policy_v1.yaml#LIBRARY_SINGLE_PUBLIC_SYMBOL_PER_CASE_REQUIRED` | 1 | 1 | 0 | 3 | 3 |
| `LIBRARY_VERB_FIRST_SCHEMA_KEYS_REQUIRED` | `docs/spec/contract/policy_v1.yaml#LIBRARY_VERB_FIRST_SCHEMA_KEYS_REQUIRED` | 1 | 2 | 2 | 1 | 1 |
| `NAMING_FILENAME_STRICT_SEPARATORS` | `docs/spec/contract/policy_v1.yaml#NAMING_FILENAME_STRICT_SEPARATORS` | 1 | 0 | 0 | 1 | 2 |
| `NORMALIZATION_CHECK_GATE_REQUIRED` | `docs/spec/contract/policy_v1.yaml#NORMALIZATION_CHECK_GATE_REQUIRED` | 1 | 1 | 0 | 2 | 4 |
| `NORMALIZATION_CONTRACT_SCHEMA_BOOK_SYNC` | `docs/spec/contract/policy_v1.yaml#NORMALIZATION_CONTRACT_SCHEMA_BOOK_SYNC` | 2 | 2 | 0 | 2 | 3 |
| `NORMALIZATION_FIX_COMMAND_AVAILABLE` | `docs/spec/contract/policy_v1.yaml#NORMALIZATION_FIX_COMMAND_AVAILABLE` | 1 | 1 | 0 | 1 | 4 |
| `NORMALIZATION_MAPPING_AST_ONLY` | `docs/spec/contract/policy_v1.yaml#NORMALIZATION_MAPPING_AST_ONLY` | 2 | 2 | 1 | 2 | 4 |
| `NORMALIZATION_PROFILE_DEFINED` | `docs/spec/contract/policy_v1.yaml#NORMALIZATION_PROFILE_DEFINED` | 2 | 1 | 0 | 1 | 2 |
| `NORMALIZATION_VIRTUAL_ROOT_PATHS_ONLY` | `docs/spec/contract/policy_v1.yaml#NORMALIZATION_VIRTUAL_ROOT_PATHS_ONLY` | 2 | 1 | 0 | 1 | 3 |
| `NO_EXECUTABLE_YAML_JSON_CASES_IN_CANONICAL_TREES` | `docs/spec/contract/policy_v1.yaml#NO_EXECUTABLE_YAML_JSON_CASES_IN_CANONICAL_TREES` | 2 | 1 | 0 | 2 | 3 |
| `OBJECTIVE_COURSE_CORRECTION_POLICY_DEFINED` | `docs/spec/contract/policy_v1.yaml#OBJECTIVE_COURSE_CORRECTION_POLICY_DEFINED` | 1 | 1 | 0 | 2 | 4 |
| `OBJECTIVE_METRIC_MANIFEST_VALID` | `docs/spec/contract/policy_v1.yaml#OBJECTIVE_METRIC_MANIFEST_VALID` | 1 | 1 | 0 | 2 | 4 |
| `OBJECTIVE_SCORECARD_NON_REGRESSION_REQUIRED` | `docs/spec/contract/policy_v1.yaml#OBJECTIVE_SCORECARD_NON_REGRESSION_REQUIRED` | 1 | 1 | 0 | 2 | 3 |
| `OBJECTIVE_SCORECARD_REPORTED` | `docs/spec/contract/policy_v1.yaml#OBJECTIVE_SCORECARD_REPORTED` | 1 | 1 | 0 | 3 | 5 |
| `OBJECTIVE_TRIPWIRES_ENFORCED` | `docs/spec/contract/policy_v1.yaml#OBJECTIVE_TRIPWIRES_ENFORCED` | 1 | 1 | 0 | 1 | 3 |
| `ORCHESTRATION_OPS_CAPABILITY_BINDING_REQUIRED` | `docs/spec/contract/policy_v1.yaml#ORCHESTRATION_OPS_CAPABILITY_BINDING_REQUIRED` | 1 | 1 | 0 | 1 | 3 |
| `ORCHESTRATION_OPS_DEEP_DOT_REQUIRED` | `docs/spec/contract/policy_v1.yaml#ORCHESTRATION_OPS_DEEP_DOT_REQUIRED` | 1 | 1 | 0 | 1 | 3 |
| `ORCHESTRATION_OPS_REGISTRY_DECLARED_REQUIRED` | `docs/spec/contract/policy_v1.yaml#ORCHESTRATION_OPS_REGISTRY_DECLARED_REQUIRED` | 1 | 1 | 0 | 1 | 4 |
| `ORCHESTRATION_OPS_UNDERSCORE_LEGACY_FORBIDDEN` | `docs/spec/contract/policy_v1.yaml#ORCHESTRATION_OPS_UNDERSCORE_LEGACY_FORBIDDEN` | 1 | 1 | 0 | 1 | 3 |
| `ORCHESTRATION_POLICY_VIA_SPEC_LANG_ONLY` | `docs/spec/contract/policy_v1.yaml#ORCHESTRATION_POLICY_VIA_SPEC_LANG_ONLY` | 1 | 0 | 0 | 2 | 2 |
| `PORTABLE_SPEC_CANONICAL_SINGLE_SET` | `docs/spec/contract/policy_v1.yaml#PORTABLE_SPEC_CANONICAL_SINGLE_SET` | 3 | 1 | 0 | 2 | 2 |
| `PORTABLE_SPEC_DETERMINISM_BY_CONSTRUCTION` | `docs/spec/contract/policy_v1.yaml#PORTABLE_SPEC_DETERMINISM_BY_CONSTRUCTION` | 2 | 1 | 2 | 1 | 1 |
| `PORTABLE_SPEC_EXPECT_PORTABLE_IMPL_OVERLAY` | `docs/spec/contract/policy_v1.yaml#PORTABLE_SPEC_EXPECT_PORTABLE_IMPL_OVERLAY` | 2 | 1 | 0 | 2 | 1 |
| `REFERENCE_CHECK_IDS_EXIST` | `docs/spec/contract/policy_v1.yaml#REFERENCE_CHECK_IDS_EXIST` | 1 | 1 | 0 | 1 | 2 |
| `REFERENCE_CONTRACT_PATHS_EXIST` | `docs/spec/contract/policy_v1.yaml#REFERENCE_CONTRACT_PATHS_EXIST` | 1 | 1 | 0 | 1 | 2 |
| `REFERENCE_EXTERNAL_REFS_POLICY` | `docs/spec/contract/policy_v1.yaml#REFERENCE_EXTERNAL_REFS_POLICY` | 2 | 1 | 0 | 1 | 3 |
| `REFERENCE_LIBRARY_EXPORTS_USED` | `docs/spec/contract/policy_v1.yaml#REFERENCE_LIBRARY_EXPORTS_USED` | 2 | 1 | 0 | 1 | 2 |
| `REFERENCE_POLICY_SYMBOLS_RESOLVE` | `docs/spec/contract/policy_v1.yaml#REFERENCE_POLICY_SYMBOLS_RESOLVE` | 2 | 1 | 0 | 1 | 2 |
| `REFERENCE_PRIVATE_SYMBOLS_FORBIDDEN` | `docs/spec/contract/policy_v1.yaml#REFERENCE_PRIVATE_SYMBOLS_FORBIDDEN` | 2 | 1 | 0 | 1 | 2 |
| `REFERENCE_SYMBOLS_EXIST` | `docs/spec/contract/policy_v1.yaml#REFERENCE_SYMBOLS_EXIST` | 1 | 1 | 0 | 1 | 3 |
| `REFERENCE_TOKEN_ANCHORS_EXIST` | `docs/spec/contract/policy_v1.yaml#REFERENCE_TOKEN_ANCHORS_EXIST` | 1 | 1 | 0 | 1 | 2 |
| `RUNNER_INDEPENDENCE_METRIC_REPORTED` | `docs/spec/contract/policy_v1.yaml#RUNNER_INDEPENDENCE_METRIC_REPORTED` | 2 | 0 | 0 | 3 | 3 |
| `RUNNER_INDEPENDENCE_NON_REGRESSION_REQUIRED` | `docs/spec/contract/policy_v1.yaml#RUNNER_INDEPENDENCE_NON_REGRESSION_REQUIRED` | 2 | 0 | 0 | 2 | 3 |
| `RUNTIME_ASSERTIONS_VIA_SPEC_LANG` | `docs/spec/contract/policy_v1.yaml#RUNTIME_ASSERTIONS_VIA_SPEC_LANG` | 2 | 1 | 0 | 2 | 7 |
| `RUNTIME_CIGATE_GOVERNANCE_TRIAGE_REQUIRED` | `docs/spec/contract/policy_v1.yaml#RUNTIME_CIGATE_GOVERNANCE_TRIAGE_REQUIRED` | 2 | 0 | 0 | 2 | 3 |
| `RUNTIME_CI_ARTIFACT_UPLOAD_PATHS_VALID` | `docs/spec/contract/policy_v1.yaml#RUNTIME_CI_ARTIFACT_UPLOAD_PATHS_VALID` | 1 | 0 | 0 | 2 | 2 |
| `RUNTIME_CI_GATE_CHECK_SETS_FAST_PATH_REQUIRED` | `docs/spec/contract/policy_v1.yaml#RUNTIME_CI_GATE_CHECK_SETS_FAST_PATH_REQUIRED` | 1 | 0 | 0 | 2 | 2 |
| `RUNTIME_CI_GATE_OWNERSHIP_CONTRACT_REQUIRED` | `docs/spec/contract/policy_v1.yaml#RUNTIME_CI_GATE_OWNERSHIP_CONTRACT_REQUIRED` | 1 | 0 | 0 | 2 | 4 |
| `RUNTIME_DECISIONS_VIA_SPEC_LANG_ONLY` | `docs/spec/contract/policy_v1.yaml#RUNTIME_DECISIONS_VIA_SPEC_LANG_ONLY` | 2 | 1 | 0 | 2 | 3 |
| `RUNTIME_DEFAULT_GATE_RUST_ADAPTER_REQUIRED` | `docs/spec/contract/policy_v1.yaml#RUNTIME_DEFAULT_GATE_RUST_ADAPTER_REQUIRED` | 2 | 0 | 0 | 1 | 3 |
| `RUNTIME_GATE_FAIL_FAST_BEHAVIOR_REQUIRED` | `docs/spec/contract/policy_v1.yaml#RUNTIME_GATE_FAIL_FAST_BEHAVIOR_REQUIRED` | 2 | 0 | 0 | 1 | 3 |
| `RUNTIME_GATE_POLICY_SKIPPED_ROWS_REQUIRED` | `docs/spec/contract/policy_v1.yaml#RUNTIME_GATE_POLICY_SKIPPED_ROWS_REQUIRED` | 2 | 0 | 0 | 1 | 3 |
| `RUNTIME_GATE_SCRIPT_ONLY_FAST_PATH_REQUIRED` | `docs/spec/contract/policy_v1.yaml#RUNTIME_GATE_SCRIPT_ONLY_FAST_PATH_REQUIRED` | 1 | 0 | 0 | 2 | 3 |
| `RUNTIME_GATE_SKIPPED_STEPS_CONTRACT_REQUIRED` | `docs/spec/contract/policy_v1.yaml#RUNTIME_GATE_SKIPPED_STEPS_CONTRACT_REQUIRED` | 1 | 0 | 0 | 1 | 3 |
| `RUNTIME_GIT_HOOK_PREPUSH_ENFORCED` | `docs/spec/contract/policy_v1.yaml#RUNTIME_GIT_HOOK_PREPUSH_ENFORCED` | 1 | 0 | 0 | 2 | 4 |
| `RUNTIME_GOVERNANCE_PREFIX_SELECTION_FROM_CHANGED_PATHS` | `docs/spec/contract/policy_v1.yaml#RUNTIME_GOVERNANCE_PREFIX_SELECTION_FROM_CHANGED_PATHS` | 1 | 0 | 0 | 2 | 2 |
| `RUNTIME_GOVERNANCE_TRIAGE_ARTIFACT_SELECTION_METADATA_REQUIRED` | `docs/spec/contract/policy_v1.yaml#RUNTIME_GOVERNANCE_TRIAGE_ARTIFACT_SELECTION_METADATA_REQUIRED` | 1 | 0 | 0 | 2 | 2 |
| `RUNTIME_GOVERNANCE_TRIAGE_ENTRYPOINT_REQUIRED` | `docs/spec/contract/policy_v1.yaml#RUNTIME_GOVERNANCE_TRIAGE_ENTRYPOINT_REQUIRED` | 2 | 0 | 0 | 2 | 3 |
| `RUNTIME_GOVERNANCE_TRIAGE_TARGETED_FIRST_REQUIRED` | `docs/spec/contract/policy_v1.yaml#RUNTIME_GOVERNANCE_TRIAGE_TARGETED_FIRST_REQUIRED` | 1 | 0 | 0 | 2 | 2 |
| `RUNTIME_LOCAL_CI_PARITY_ENTRYPOINT_DOCUMENTED` | `docs/spec/contract/policy_v1.yaml#RUNTIME_LOCAL_CI_PARITY_ENTRYPOINT_DOCUMENTED` | 2 | 0 | 0 | 2 | 5 |
| `RUNTIME_LOCAL_PREPUSH_BROAD_GOVERNANCE_FORBIDDEN` | `docs/spec/contract/policy_v1.yaml#RUNTIME_LOCAL_PREPUSH_BROAD_GOVERNANCE_FORBIDDEN` | 1 | 0 | 0 | 2 | 2 |
| `RUNTIME_LOCAL_PREPUSH_CHECK_SETS_FAST_PATH_REQUIRED` | `docs/spec/contract/policy_v1.yaml#RUNTIME_LOCAL_PREPUSH_CHECK_SETS_FAST_PATH_REQUIRED` | 1 | 0 | 0 | 2 | 2 |
| `RUNTIME_NON_PYTHON_LANES_FORBID_PYTHON_EXEC` | `docs/spec/contract/policy_v1.yaml#RUNTIME_NON_PYTHON_LANES_FORBID_PYTHON_EXEC` | 2 | 0 | 0 | 2 | 2 |
| `RUNTIME_PREPUSH_GOVERNANCE_TRIAGE_REQUIRED` | `docs/spec/contract/policy_v1.yaml#RUNTIME_PREPUSH_GOVERNANCE_TRIAGE_REQUIRED` | 1 | 0 | 0 | 2 | 2 |
| `RUNTIME_PREPUSH_PARITY_DEFAULT_REQUIRED` | `docs/spec/contract/policy_v1.yaml#RUNTIME_PREPUSH_PARITY_DEFAULT_REQUIRED` | 2 | 0 | 0 | 2 | 4 |
| `RUNTIME_PREPUSH_PYTHON_PARITY_NOT_OPTIONAL_BY_DEFAULT` | `docs/spec/contract/policy_v1.yaml#RUNTIME_PREPUSH_PYTHON_PARITY_NOT_OPTIONAL_BY_DEFAULT` | 1 | 0 | 0 | 2 | 2 |
| `RUNTIME_PROFILE_ARTIFACTS_ON_FAIL_REQUIRED` | `docs/spec/contract/policy_v1.yaml#RUNTIME_PROFILE_ARTIFACTS_ON_FAIL_REQUIRED` | 1 | 1 | 0 | 1 | 3 |
| `RUNTIME_PROFILING_CONTRACT_ARTIFACTS_REQUIRED` | `docs/spec/contract/policy_v1.yaml#RUNTIME_PROFILING_CONTRACT_ARTIFACTS_REQUIRED` | 2 | 1 | 0 | 1 | 2 |
| `RUNTIME_PROFILING_REDACTION_POLICY_REQUIRED` | `docs/spec/contract/policy_v1.yaml#RUNTIME_PROFILING_REDACTION_POLICY_REQUIRED` | 1 | 1 | 0 | 1 | 2 |
| `RUNTIME_PROFILING_SPAN_TAXONOMY_REQUIRED` | `docs/spec/contract/policy_v1.yaml#RUNTIME_PROFILING_SPAN_TAXONOMY_REQUIRED` | 1 | 1 | 0 | 1 | 3 |
| `RUNTIME_PUBLIC_DOCS_NO_DIRECT_RUST_ADAPTER_INVOCATION` | `docs/spec/contract/policy_v1.yaml#RUNTIME_PUBLIC_DOCS_NO_DIRECT_RUST_ADAPTER_INVOCATION` | 1 | 1 | 0 | 1 | 4 |
| `RUNTIME_PUBLIC_ENTRYPOINT_RUST_DEFAULT_REQUIRED` | `docs/spec/contract/policy_v1.yaml#RUNTIME_PUBLIC_ENTRYPOINT_RUST_DEFAULT_REQUIRED` | 2 | 1 | 0 | 1 | 3 |
| `RUNTIME_PYTHON_DEPENDENCY_EVIDENCE_REPORTED` | `docs/spec/contract/policy_v1.yaml#RUNTIME_PYTHON_DEPENDENCY_EVIDENCE_REPORTED` | 2 | 0 | 0 | 3 | 3 |
| `RUNTIME_PYTHON_DEPENDENCY_NON_REGRESSION_REQUIRED` | `docs/spec/contract/policy_v1.yaml#RUNTIME_PYTHON_DEPENDENCY_NON_REGRESSION_REQUIRED` | 2 | 0 | 0 | 2 | 3 |
| `RUNTIME_PYTHON_LANE_EXPLICIT_OPT_IN_ONLY` | `docs/spec/contract/policy_v1.yaml#RUNTIME_PYTHON_LANE_EXPLICIT_OPT_IN_ONLY` | 1 | 1 | 0 | 1 | 3 |
| `RUNTIME_PYTHON_USAGE_SCOPED_TO_PYTHON_RUNNER` | `docs/spec/contract/policy_v1.yaml#RUNTIME_PYTHON_USAGE_SCOPED_TO_PYTHON_RUNNER` | 2 | 0 | 0 | 2 | 3 |
| `RUNTIME_RUNNER_INTERFACE_CI_LANE_REQUIRED` | `docs/spec/contract/policy_v1.yaml#RUNTIME_RUNNER_INTERFACE_CI_LANE_REQUIRED` | 1 | 0 | 0 | 1 | 3 |
| `RUNTIME_RUNNER_INTERFACE_GATE_SYNC` | `docs/spec/contract/policy_v1.yaml#RUNTIME_RUNNER_INTERFACE_GATE_SYNC` | 1 | 0 | 0 | 2 | 5 |
| `RUNTIME_RUNNER_INTERFACE_SUBCOMMANDS_DECLARED` | `docs/spec/contract/policy_v1.yaml#RUNTIME_RUNNER_INTERFACE_SUBCOMMANDS_DECLARED` | 1 | 0 | 0 | 1 | 3 |
| `RUNTIME_RUST_ADAPTER_NO_DELEGATION` | `docs/spec/contract/policy_v1.yaml#RUNTIME_RUST_ADAPTER_NO_DELEGATION` | 1 | 0 | 0 | 1 | 3 |
| `RUNTIME_RUST_ADAPTER_NO_PYTHON_EXEC` | `docs/spec/contract/policy_v1.yaml#RUNTIME_RUST_ADAPTER_NO_PYTHON_EXEC` | 2 | 1 | 0 | 1 | 3 |
| `RUNTIME_RUST_ADAPTER_TARGET_FALLBACK_REQUIRED` | `docs/spec/contract/policy_v1.yaml#RUNTIME_RUST_ADAPTER_TARGET_FALLBACK_REQUIRED` | 1 | 0 | 0 | 2 | 2 |
| `RUNTIME_RUST_ADAPTER_TRANSITIVE_NO_PYTHON` | `docs/spec/contract/policy_v1.yaml#RUNTIME_RUST_ADAPTER_TRANSITIVE_NO_PYTHON` | 2 | 0 | 0 | 1 | 2 |
| `RUNTIME_SCOPE_BOUNDED_FOR_V1` | `docs/spec/contract/policy_v1.yaml#RUNTIME_SCOPE_BOUNDED_FOR_V1` | 2 | 0 | 0 | 2 | 2 |
| `RUNTIME_SINGLE_PUBLIC_RUNNER_ENTRYPOINT_REQUIRED` | `docs/spec/contract/policy_v1.yaml#RUNTIME_SINGLE_PUBLIC_RUNNER_ENTRYPOINT_REQUIRED` | 1 | 1 | 0 | 1 | 5 |
| `RUNTIME_TRIAGE_ARTIFACTS_EMITTED_REQUIRED` | `docs/spec/contract/policy_v1.yaml#RUNTIME_TRIAGE_ARTIFACTS_EMITTED_REQUIRED` | 1 | 0 | 0 | 2 | 3 |
| `RUNTIME_TRIAGE_BYPASS_LOGGING_REQUIRED` | `docs/spec/contract/policy_v1.yaml#RUNTIME_TRIAGE_BYPASS_LOGGING_REQUIRED` | 1 | 0 | 0 | 2 | 2 |
| `RUNTIME_TRIAGE_FAILURE_ID_PARSING_REQUIRED` | `docs/spec/contract/policy_v1.yaml#RUNTIME_TRIAGE_FAILURE_ID_PARSING_REQUIRED` | 1 | 0 | 0 | 2 | 3 |
| `RUST_PRIMARY_ADAPTER_EXEC_SMOKE_REQUIRED` | `docs/spec/contract/policy_v1.yaml#RUST_PRIMARY_ADAPTER_EXEC_SMOKE_REQUIRED` | 2 | 0 | 0 | 1 | 3 |
| `RUST_PRIMARY_DOCS_ADOPTION_SYNC` | `docs/spec/contract/policy_v1.yaml#RUST_PRIMARY_DOCS_ADOPTION_SYNC` | 2 | 0 | 0 | 1 | 4 |
| `RUST_PRIMARY_GATE_PATH_REQUIRED` | `docs/spec/contract/policy_v1.yaml#RUST_PRIMARY_GATE_PATH_REQUIRED` | 2 | 0 | 0 | 1 | 3 |
| `RUST_PRIMARY_INTERFACE_STABILITY_REQUIRED` | `docs/spec/contract/policy_v1.yaml#RUST_PRIMARY_INTERFACE_STABILITY_REQUIRED` | 2 | 0 | 0 | 1 | 3 |
| `RUST_PRIMARY_NO_PYTHON_GATE_DEPENDENCY` | `docs/spec/contract/policy_v1.yaml#RUST_PRIMARY_NO_PYTHON_GATE_DEPENDENCY` | 2 | 0 | 0 | 1 | 5 |
| `RUST_PRIMARY_SHARED_CAPABILITY_PARITY_REQUIRED` | `docs/spec/contract/policy_v1.yaml#RUST_PRIMARY_SHARED_CAPABILITY_PARITY_REQUIRED` | 2 | 0 | 0 | 2 | 4 |
| `RUST_PRIMARY_SUBCOMMAND_PARITY_REQUIRED` | `docs/spec/contract/policy_v1.yaml#RUST_PRIMARY_SUBCOMMAND_PARITY_REQUIRED` | 2 | 0 | 0 | 1 | 4 |
| `SCHEMA_DOCS_GENERATED_FROM_REGISTRY_REQUIRED` | `docs/spec/contract/policy_v1.yaml#SCHEMA_DOCS_GENERATED_FROM_REGISTRY_REQUIRED` | 1 | 1 | 1 | 1 | 1 |
| `SCHEMA_PROSE_ONLY_RULES_FORBIDDEN` | `docs/spec/contract/policy_v1.yaml#SCHEMA_PROSE_ONLY_RULES_FORBIDDEN` | 1 | 1 | 1 | 1 | 1 |
| `SCHEMA_REGISTRY_SOURCE_OF_TRUTH_REQUIRED` | `docs/spec/contract/policy_v1.yaml#SCHEMA_REGISTRY_SOURCE_OF_TRUTH_REQUIRED` | 1 | 2 | 1 | 1 | 2 |
| `SCHEMA_REGISTRY_VALIDATION_REQUIRED` | `docs/spec/contract/policy_v1.yaml#SCHEMA_REGISTRY_VALIDATION_REQUIRED` | 1 | 1 | 2 | 1 | 2 |
| `SCHEMA_TYPE_PROFILE_COVERAGE_REQUIRED` | `docs/spec/contract/policy_v1.yaml#SCHEMA_TYPE_PROFILE_COVERAGE_REQUIRED` | 1 | 4 | 1 | 1 | 2 |
| `SCHEMA_UNKNOWN_KEYS_HARD_FAIL` | `docs/spec/contract/policy_v1.yaml#SCHEMA_UNKNOWN_KEYS_HARD_FAIL` | 1 | 1 | 1 | 1 | 1 |
| `SCHEMA_VERB_FIRST_CONTRACT_SYNC_REQUIRED` | `docs/spec/contract/policy_v1.yaml#SCHEMA_VERB_FIRST_CONTRACT_SYNC_REQUIRED` | 2 | 1 | 0 | 1 | 1 |
| `SPEC_DOMAIN_INDEX_SYNC` | `docs/spec/contract/policy_v1.yaml#SPEC_DOMAIN_INDEX_SYNC` | 1 | 1 | 0 | 1 | 3 |
| `SPEC_LANG_ADOPTION_METRIC_REPORTED` | `docs/spec/contract/policy_v1.yaml#SPEC_LANG_ADOPTION_METRIC_REPORTED` | 2 | 1 | 0 | 3 | 3 |
| `SPEC_LANG_ADOPTION_NON_REGRESSION_REQUIRED` | `docs/spec/contract/policy_v1.yaml#SPEC_LANG_ADOPTION_NON_REGRESSION_REQUIRED` | 2 | 1 | 0 | 2 | 3 |
| `SPEC_LANG_COLLECTION_FORMS_CONTRACTED` | `docs/spec/contract/policy_v1.yaml#SPEC_LANG_COLLECTION_FORMS_CONTRACTED` | 1 | 1 | 3 | 1 | 2 |
| `SPEC_LANG_CURRY_ALL_BUILTINS` | `docs/spec/contract/policy_v1.yaml#SPEC_LANG_CURRY_ALL_BUILTINS` | 1 | 1 | 4 | 1 | 3 |
| `SPEC_LANG_DEEP_EQUALITY_DETERMINISTIC` | `docs/spec/contract/policy_v1.yaml#SPEC_LANG_DEEP_EQUALITY_DETERMINISTIC` | 1 | 1 | 2 | 1 | 2 |
| `SPEC_LANG_ERROR_CLASSIFICATION` | `docs/spec/contract/policy_v1.yaml#SPEC_LANG_ERROR_CLASSIFICATION` | 2 | 1 | 4 | 2 | 3 |
| `SPEC_LANG_EVALUATE_LIST_SHAPE` | `docs/spec/contract/policy_v1.yaml#SPEC_LANG_EVALUATE_LIST_SHAPE` | 2 | 1 | 3 | 2 | 4 |
| `SPEC_LANG_EVAL_BUDGETS_REQUIRED` | `docs/spec/contract/policy_v1.yaml#SPEC_LANG_EVAL_BUDGETS_REQUIRED` | 1 | 1 | 1 | 2 | 3 |
| `SPEC_LANG_LIBRARY_INCLUDE_FORMAT_SCOPE` | `docs/spec/contract/policy_v1.yaml#SPEC_LANG_LIBRARY_INCLUDE_FORMAT_SCOPE` | 2 | 1 | 0 | 2 | 2 |
| `SPEC_LANG_LIBRARY_REUSE_MODEL` | `docs/spec/contract/policy_v1.yaml#SPEC_LANG_LIBRARY_REUSE_MODEL` | 2 | 1 | 0 | 2 | 5 |
| `SPEC_LANG_PREFERRED_AUTHORING` | `docs/spec/contract/policy_v1.yaml#SPEC_LANG_PREFERRED_AUTHORING` | 2 | 1 | 0 | 1 | 2 |
| `SPEC_LANG_PROPER_TCO_REQUIRED` | `docs/spec/contract/policy_v1.yaml#SPEC_LANG_PROPER_TCO_REQUIRED` | 1 | 1 | 1 | 1 | 3 |
| `SPEC_LANG_PURE_EVALUATOR` | `docs/spec/contract/policy_v1.yaml#SPEC_LANG_PURE_EVALUATOR` | 2 | 1 | 2 | 1 | 3 |
| `SPEC_LANG_PURE_NO_EFFECT_BUILTINS` | `docs/spec/contract/policy_v1.yaml#SPEC_LANG_PURE_NO_EFFECT_BUILTINS` | 2 | 1 | 0 | 2 | 4 |
| `SPEC_LANG_SET_ALGEBRA_PARITY` | `docs/spec/contract/policy_v1.yaml#SPEC_LANG_SET_ALGEBRA_PARITY` | 1 | 1 | 4 | 2 | 3 |
| `SPEC_LANG_STDLIB_CONFORMANCE_COVERAGE_REQUIRED` | `docs/spec/contract/policy_v1.yaml#SPEC_LANG_STDLIB_CONFORMANCE_COVERAGE_REQUIRED` | 2 | 1 | 2 | 1 | 2 |
| `SPEC_LANG_STDLIB_DOCS_SYNC_REQUIRED` | `docs/spec/contract/policy_v1.yaml#SPEC_LANG_STDLIB_DOCS_SYNC_REQUIRED` | 2 | 2 | 0 | 1 | 3 |
| `SPEC_LANG_STDLIB_PROFILE_COMPLETE` | `docs/spec/contract/policy_v1.yaml#SPEC_LANG_STDLIB_PROFILE_COMPLETE` | 1 | 1 | 2 | 1 | 3 |
| `SPEC_LANG_STDLIB_PROFILE_DEFINED` | `docs/spec/contract/policy_v1.yaml#SPEC_LANG_STDLIB_PROFILE_DEFINED` | 2 | 1 | 0 | 1 | 3 |
| `SPEC_LANG_STDLIB_PY_PHP_PARITY_REQUIRED` | `docs/spec/contract/policy_v1.yaml#SPEC_LANG_STDLIB_PY_PHP_PARITY_REQUIRED` | 1 | 1 | 0 | 2 | 4 |
| `SPEC_LAYOUT_DOMAIN_TREES` | `docs/spec/contract/policy_v1.yaml#SPEC_LAYOUT_DOMAIN_TREES` | 2 | 1 | 0 | 1 | 3 |
| `SPEC_PORTABILITY_METRIC_REPORTED` | `docs/spec/contract/policy_v1.yaml#SPEC_PORTABILITY_METRIC_REPORTED` | 2 | 1 | 0 | 3 | 3 |
| `SPEC_PORTABILITY_NON_REGRESSION_REQUIRED` | `docs/spec/contract/policy_v1.yaml#SPEC_PORTABILITY_NON_REGRESSION_REQUIRED` | 2 | 1 | 0 | 2 | 3 |
| `SPEC_PORTABILITY_THRESHOLD_ENFORCED` | `docs/spec/contract/policy_v1.yaml#SPEC_PORTABILITY_THRESHOLD_ENFORCED` | 2 | 1 | 0 | 2 | 2 |
| `UNIVERSAL_CHAIN_SUPPORT_REQUIRED` | `docs/spec/contract/policy_v1.yaml#UNIVERSAL_CHAIN_SUPPORT_REQUIRED` | 1 | 1 | 0 | 1 | 2 |
<!-- GENERATED:END traceability_catalog -->
