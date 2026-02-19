```yaml doc-meta
doc_id: DOC-REF-944
title: Spec Case Index
status: active
audience: reviewer
owns_tokens:
- spec_case_index
requires_tokens:
- generated_docs_sync
commands:
- run: ./runners/public/runner_adapter.sh --impl rust docs-generate-check
  purpose: Verify generated spec case index content is in sync.
examples:
- id: EX-REF-CASE-002
  runnable: false
  opt_out_reason: Generated reference page intentionally contains no runnable fenced examples.
sections_required:
- '## Generated Spec Case Index'
- '## Case Anchors'
```

# Spec Case Index

Generated compact index for documented spec cases.

<!-- GENERATED:START spec_case_index -->

## Generated Spec Case Index

| domain | case_count |
|---|---|
| `unscoped` | 88 |


## Type Summary

| type | case_count |
|---|---|
| `contract.export` | 88 |


## Case Anchors

| case_id | domain | type | reference |
|---|---|---|---|
| `BAD-EXPORT-CLASS` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-bad_export_class) |
| `BAD-EXPORT-PATH` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-bad_export_path) |
| `LIB-CONF-ASSERT-001` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_conf_assert_001) |
| `LIB-DOMAIN-ARTIFACT-001-001-DOMAIN-ARTIFACT-WRITE-YAML` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_artifact_001_001_domain_artifact_write_yaml) |
| `LIB-DOMAIN-ARTIFACT-001-002-DOMAIN-ARTIFACT-APPEND-TEXT` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_artifact_001_002_domain_artifact_append_text) |
| `LIB-DOMAIN-CONFORMANCE-001-000-DOMAIN-CONFORMANCE-ERROR-WHEN-FALSE` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_conformance_001_000_domain_conformance_error_when_false) |
| `LIB-DOMAIN-CONFORMANCE-001-000A-DOMAIN-CONFORMANCE-REPORT-VERSION-IS-V1` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_conformance_001_000a_domain_conformance_report_version_is_v1) |
| `LIB-DOMAIN-CONFORMANCE-001-000B-DOMAIN-CONFORMANCE-REPORT-RESULTS-IS-LIST` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_conformance_001_000b_domain_conformance_report_results_is_list) |
| `LIB-DOMAIN-CONFORMANCE-001-000C-DOMAIN-CONFORMANCE-VALIDATE-REPORT-ERRORS` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_conformance_001_000c_domain_conformance_validate_report_errors) |
| `LIB-DOMAIN-FS-001-001-DOMAIN-FS-IS-DOCS-SPEC-FILE` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_fs_001_001_domain_fs_is_docs_spec_file) |
| `LIB-DOMAIN-FS-001-002-DOMAIN-FS-SORT-SPEC-FILES` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_fs_001_002_domain_fs_sort_spec_files) |
| `LIB-DOMAIN-FS-001-003-DOMAIN-FS-JSON-GET-OR-TEXT` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_fs_001_003_domain_fs_json_get_or_text) |
| `LIB-DOMAIN-FS-001-004-DOMAIN-FS-JSON-HAS-PATH-TEXT` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_fs_001_004_domain_fs_json_has_path_text) |
| `LIB-DOMAIN-FS-001-005-DOMAIN-FS-GLOB-ANY-SPEC-FILES` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_fs_001_005_domain_fs_glob_any_spec_files) |
| `LIB-DOMAIN-FS-001-006-DOMAIN-FS-FILE-EXT-EQ` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_fs_001_006_domain_fs_file_ext_eq) |
| `LIB-DOMAIN-FS-001-007-DOMAIN-FS-JSON-GET-TEXT` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_fs_001_007_domain_fs_json_get_text) |
| `LIB-DOMAIN-FS-001-008-DOMAIN-FS-JSON-PATH-EQ-TEXT` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_fs_001_008_domain_fs_json_path_eq_text) |
| `LIB-DOMAIN-FS-001-009-DOMAIN-FS-GLOB-FILTER` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_fs_001_009_domain_fs_glob_filter) |
| `LIB-DOMAIN-FS-001-010-DOMAIN-FS-GLOB-ALL` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_fs_001_010_domain_fs_glob_all) |
| `LIB-DOMAIN-HTTP-001-001-DOMAIN-HTTP-STATUS` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_http_001_001_domain_http_status) |
| `LIB-DOMAIN-HTTP-001-002-DOMAIN-HTTP-STATUS-IN` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_http_001_002_domain_http_status_in) |
| `LIB-DOMAIN-HTTP-001-003-DOMAIN-HTTP-STATUS-IS` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_http_001_003_domain_http_status_is) |
| `LIB-DOMAIN-HTTP-001-004-DOMAIN-HTTP-STATUS-IS-UNAUTHORIZED` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_http_001_004_domain_http_status_is_unauthorized) |
| `LIB-DOMAIN-HTTP-001-005-DOMAIN-HTTP-STATUS-IS-FORBIDDEN` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_http_001_005_domain_http_status_is_forbidden) |
| `LIB-DOMAIN-HTTP-001-006-DOMAIN-HTTP-OK-2XX` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_http_001_006_domain_http_ok_2xx) |
| `LIB-DOMAIN-HTTP-001-007-DOMAIN-HTTP-HEADER-GET` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_http_001_007_domain_http_header_get) |
| `LIB-DOMAIN-HTTP-001-008-DOMAIN-HTTP-HEADER-CONTAINS` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_http_001_008_domain_http_header_contains) |
| `LIB-DOMAIN-HTTP-001-009-DOMAIN-HTTP-BODY-TEXT` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_http_001_009_domain_http_body_text) |
| `LIB-DOMAIN-HTTP-001-010-DOMAIN-HTTP-BODY-JSON` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_http_001_010_domain_http_body_json) |
| `LIB-DOMAIN-HTTP-001-011-DOMAIN-HTTP-BODY-JSON-TYPE-IS` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_http_001_011_domain_http_body_json_type_is) |
| `LIB-DOMAIN-HTTP-001-012-DOMAIN-HTTP-BODY-JSON-HAS-KEY` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_http_001_012_domain_http_body_json_has_key) |
| `LIB-DOMAIN-HTTP-001-013-DOMAIN-HTTP-AUTH-IS-OAUTH` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_http_001_013_domain_http_auth_is_oauth) |
| `LIB-DOMAIN-HTTP-001-014-DOMAIN-HTTP-HAS-BEARER-HEADER` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_http_001_014_domain_http_has_bearer_header) |
| `LIB-DOMAIN-HTTP-001-014-DOMAIN-HTTP-OAUTH-TOKEN-SOURCE-IS` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_http_001_014_domain_http_oauth_token_source_is) |
| `LIB-DOMAIN-HTTP-001-015-DOMAIN-HTTP-OAUTH-SCOPE-REQUESTED` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_http_001_015_domain_http_oauth_scope_requested) |
| `LIB-DOMAIN-HTTP-001-016-DOMAIN-HTTP-CORS-ALLOW-ORIGIN` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_http_001_016_domain_http_cors_allow_origin) |
| `LIB-DOMAIN-HTTP-001-017-DOMAIN-HTTP-CORS-ALLOWS-METHOD` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_http_001_017_domain_http_cors_allows_method) |
| `LIB-DOMAIN-HTTP-001-018-DOMAIN-HTTP-CORS-ALLOWS-HEADER` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_http_001_018_domain_http_cors_allows_header) |
| `LIB-DOMAIN-HTTP-001-019-DOMAIN-HTTP-CORS-CREDENTIALS-ENABLED` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_http_001_019_domain_http_cors_credentials_enabled) |
| `LIB-DOMAIN-HTTP-001-020-DOMAIN-HTTP-CORS-MAX-AGE-GTE` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_http_001_020_domain_http_cors_max_age_gte) |
| `LIB-DOMAIN-HTTP-001-021-DOMAIN-HTTP-IS-PREFLIGHT-STEP` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_http_001_021_domain_http_is_preflight_step) |
| `LIB-DOMAIN-HTTP-001-022-DOMAIN-HTTP-STEP-BY-ID` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_http_001_022_domain_http_step_by_id) |
| `LIB-DOMAIN-HTTP-001-023-DOMAIN-HTTP-STEP-STATUS-IS` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_http_001_023_domain_http_step_status_is) |
| `LIB-DOMAIN-HTTP-001-024-DOMAIN-HTTP-STEP-BODY-JSON-GET` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_http_001_024_domain_http_step_body_json_get) |
| `LIB-DOMAIN-JOB-001-000A-DOMAIN-JOB-SCAN-BUNDLE-HAS-RESULT` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_job_001_000a_domain_job_scan_bundle_has_result) |
| `LIB-DOMAIN-MAKE-001` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_make_001) |
| `LIB-DOMAIN-MD-001-001-DOMAIN-MARKDOWN-HAS-HEADING` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_md_001_001_domain_markdown_has_heading) |
| `LIB-DOMAIN-MD-001-003-DOMAIN-MARKDOWN-HEADING-LEVEL-EXISTS` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_md_001_003_domain_markdown_heading_level_exists) |
| `LIB-DOMAIN-MD-001-005-DOMAIN-MARKDOWN-SECTION-ORDER-VALID` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_md_001_005_domain_markdown_section_order_valid) |
| `LIB-DOMAIN-MD-001-007-DOMAIN-MARKDOWN-REQUIRED-SECTIONS-PRESENT` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_md_001_007_domain_markdown_required_sections_present) |
| `LIB-DOMAIN-MD-001-009-DOMAIN-MARKDOWN-LINK-TARGETS-ALL-RESOLVE` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_md_001_009_domain_markdown_link_targets_all_resolve) |
| `LIB-DOMAIN-MD-001-011-DOMAIN-MARKDOWN-HAS-BROKEN-LINKS` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_md_001_011_domain_markdown_has_broken_links) |
| `LIB-DOMAIN-MD-001-013-DOMAIN-MARKDOWN-HAS-YAML-SPEC-TEST-FENCE` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_md_001_013_domain_markdown_has_yaml_spec_test_fence) |
| `LIB-DOMAIN-MD-001-015-DOMAIN-MARKDOWN-CODE-FENCE-LANGUAGE-EXISTS` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_md_001_015_domain_markdown_code_fence_language_exists) |
| `LIB-DOMAIN-MD-001-017-DOMAIN-MARKDOWN-TOKEN-PRESENT` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_md_001_017_domain_markdown_token_present) |
| `LIB-DOMAIN-MD-001-019-DOMAIN-MARKDOWN-TOKENS-ALL-PRESENT` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_md_001_019_domain_markdown_tokens_all_present) |
| `LIB-DOMAIN-MD-001-021-DOMAIN-MARKDOWN-TOKEN-OWNERSHIP-UNIQUE` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_md_001_021_domain_markdown_token_ownership_unique) |
| `LIB-DOMAIN-MD-001-023-DOMAIN-MARKDOWN-TOKEN-DEPENDENCIES-RESOLVED` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_md_001_023_domain_markdown_token_dependencies_resolved) |
| `LIB-DOMAIN-META-001-001-DOMAIN-META-CASE-ID-EQ` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_meta_001_001_domain_meta_case_id_eq) |
| `LIB-DOMAIN-META-001-002-DOMAIN-META-HAS-ARTIFACT-TARGET` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_meta_001_002_domain_meta_has_artifact_target) |
| `LIB-DOMAIN-OS-001-001-DOMAIN-OS-EXEC-OK` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_os_001_001_domain_os_exec_ok) |
| `LIB-DOMAIN-OS-001-002-DOMAIN-OS-EXEC-CAPTURE-CODE` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_os_001_002_domain_os_exec_capture_code) |
| `LIB-DOMAIN-OS-001-003-DOMAIN-OS-ENV-HAS` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_os_001_003_domain_os_env_has) |
| `LIB-DOMAIN-PATH-001-001-DOMAIN-PATH-NORMALIZE` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_path_001_001_domain_path_normalize) |
| `LIB-DOMAIN-PATH-001-002-DOMAIN-PATH-EQ` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_path_001_002_domain_path_eq) |
| `LIB-DOMAIN-PATH-001-003-DOMAIN-PATH-IS-SPEC-MD` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_path_001_003_domain_path_is_spec_md) |
| `LIB-DOMAIN-PATH-001-004-DOMAIN-PATH-IS-IN-DOCS` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_path_001_004_domain_path_is_in_docs) |
| `LIB-DOMAIN-PATH-001-005-DOMAIN-PATH-SORTED` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_path_001_005_domain_path_sorted) |
| `LIB-DOMAIN-PATH-001-006-DOMAIN-FILE-IS-EXISTING-FILE` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_path_001_006_domain_file_is_existing_file) |
| `LIB-DOMAIN-PATH-001-007-DOMAIN-FILE-IS-EXISTING-DIR` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_path_001_007_domain_file_is_existing_dir) |
| `LIB-DOMAIN-PATH-001-008-DOMAIN-FILE-HAS-EXT` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_path_001_008_domain_file_has_ext) |
| `LIB-DOMAIN-PATH-001-009-DOMAIN-FILE-NAME` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_path_001_009_domain_file_name) |
| `LIB-DOMAIN-PHP-001` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_php_001) |
| `LIB-DOMAIN-PROCESS-001-001-DOMAIN-PROCESS-EXEC-CAPTURE-EX-CODE` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_process_001_001_domain_process_exec_capture_ex_code) |
| `LIB-DOMAIN-PY-001` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_py_001) |
| `LIB-DOMAIN-REPO-001-001-DOMAIN-REPO-WALK-MATCHING` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_repo_001_001_domain_repo_walk_matching) |
| `LIB-DOMAIN-YAML-001-001-DOMAIN-YAML-PARSE-GET-OR` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_yaml_001_001_domain_yaml_parse_get_or) |
| `LIB-DOMAIN-YAML-001-002-DOMAIN-YAML-STRINGIFY` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_domain_yaml_001_002_domain_yaml_stringify) |
| `LIB-IMPL-ASSERT-001-001-IMPL-ASSERT-CONTAINS` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_impl_assert_001_001_impl_assert_contains) |
| `LIB-IMPL-ASSERT-001-002-IMPL-ASSERT-REGEX` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_impl_assert_001_002_impl_assert_regex) |
| `LIB-IMPL-ASSERT-001-003-IMPL-ASSERT-JSON-TYPE` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_impl_assert_001_003_impl_assert_json_type) |
| `LIB-PATH-001-001-PATH-NORMALIZE-SLASHES` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_path_001_001_path_normalize_slashes) |
| `LIB-PATH-001-002-PATH-SEGMENTS` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_path_001_002_path_segments) |
| `LIB-PATH-001-003-PATH-BASENAME` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_path_001_003_path_basename) |
| `LIB-PATH-001-004-PATH-EXTENSION` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_path_001_004_path_extension) |
| `LIB-POLICY-001` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_policy_001) |
| `LIB-POLICY-002-001-POLICY-METRIC-NON-DECREASE` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_policy_002_001_policy_metric_non_decrease) |
| `LIB-POLICY-002-002-POLICY-METRIC-NON-INCREASE` | `unscoped` | `contract.export` | [jump](/docs/book/93l_spec_case_reference.md#case-lib_policy_002_002_policy_metric_non_increase) |
<!-- GENERATED:END spec_case_index -->
