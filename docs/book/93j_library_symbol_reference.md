```yaml doc-meta
doc_id: DOC-REF-941
title: Library Symbol Reference
status: active
audience: reviewer
owns_tokens:
- library_symbol_reference
requires_tokens:
- generated_docs_sync
commands:
- run: ./runners/public/runner_adapter.sh --impl rust docs-generate-check
  purpose: Verify generated library symbol reference content is in sync.
examples:
- id: EX-REF-LIB-001
  runnable: false
  opt_out_reason: Generated reference page intentionally contains no runnable fenced examples.
sections_required:
- '## Generated Library Symbol Reference'
- '## Symbols'
```

# Library Symbol Reference

Generated API-reference-first documentation for spec library export symbols.

<!-- GENERATED:START library_symbol_reference -->

## Generated Library Symbol Reference

- module_count: 5
- symbol_count: 122
- source_root: `/specs/libraries`


### Module `conformance` {#symbol-conformance}

- symbol_count: 7
- libraries: `conformance.assertion.core` `conformance.chain.export.validation` 


### Module `domain` {#symbol-domain}

- symbol_count: 82
- libraries: `domain.artifact.core` `domain.conformance.core` `domain.fs.core` `domain.http.core` `domain.job.core` `domain.make.core` `domain.markdown.core` `domain.meta.core` `domain.os.core` `domain.path.core` `domain.php.core` `domain.process.core` `domain.python.core` `domain.repo.core` `domain.yaml.core` 


### Module `impl` {#symbol-impl}

- symbol_count: 3
- libraries: `impl.assertion.core` 


### Module `path` {#symbol-path}

- symbol_count: 24
- libraries: `path.path.core` 


### Module `policy` {#symbol-policy}

- symbol_count: 6
- libraries: `policy.policy.core` `policy.policy.metrics` 



## Symbols


### `bad.class.symbol` {#symbol-bad_class_symbol}

Contract-backed: `/specs/libraries/conformance/chain_export_validation.spec.md#BAD-EXPORT-CLASS` via `/non_must_step`

- Signature: `bad.class.symbol(subject)`
- Module: `conformance`
- Library: `conformance.chain.export.validation`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/conformance/chain_export_validation.spec.md#BAD-EXPORT-CLASS`
- Export Path: `/non_must_step`

#### Summary

Contract export for `bad.class.symbol`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `bad.path.symbol` {#symbol-bad_path_symbol}

Contract-backed: `/specs/libraries/conformance/chain_export_validation.spec.md#BAD-EXPORT-PATH` via `/missing_step`

- Signature: `bad.path.symbol(subject)`
- Module: `conformance`
- Library: `conformance.chain.export.validation`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/conformance/chain_export_validation.spec.md#BAD-EXPORT-PATH`
- Export Path: `/missing_step`

#### Summary

Contract export for `bad.path.symbol`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `conf.eq` {#symbol-conf_eq}

Contract-backed: `/specs/libraries/conformance/assertion_core.spec.md#LIB-CONF-ASSERT-001` via `/__export__conf.eq`

- Signature: `conf.eq(subject, value)`
- Module: `conformance`
- Library: `conformance.assertion.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/conformance/assertion_core.spec.md#LIB-CONF-ASSERT-001`
- Export Path: `/__export__conf.eq`

#### Summary

Contract export for `conf.eq`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |
| `value` | `any` | `true` | Input parameter `value`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>', 'value': '<value>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `conf.has_error_category` {#symbol-conf_has_error_category}

Contract-backed: `/specs/libraries/conformance/assertion_core.spec.md#LIB-CONF-ASSERT-001` via `/__export__conf.has_error_category`

- Signature: `conf.has_error_category(subject, category)`
- Module: `conformance`
- Library: `conformance.assertion.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/conformance/assertion_core.spec.md#LIB-CONF-ASSERT-001`
- Export Path: `/__export__conf.has_error_category`

#### Summary

Contract export for `conf.has_error_category`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |
| `category` | `any` | `true` | Input parameter `category`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>', 'category': '<category>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `conf.json_type_is` {#symbol-conf_json_type_is}

Contract-backed: `/specs/libraries/conformance/assertion_core.spec.md#LIB-CONF-ASSERT-001` via `/__export__conf.json_type_is`

- Signature: `conf.json_type_is(subject, type_name)`
- Module: `conformance`
- Library: `conformance.assertion.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/conformance/assertion_core.spec.md#LIB-CONF-ASSERT-001`
- Export Path: `/__export__conf.json_type_is`

#### Summary

Contract export for `conf.json_type_is`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |
| `type_name` | `any` | `true` | Input parameter `type_name`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>', 'type_name': '<type_name>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `conf.pass_when_text_contains` {#symbol-conf_pass_when_text_contains}

Contract-backed: `/specs/libraries/conformance/assertion_core.spec.md#LIB-CONF-ASSERT-001` via `/__export__conf.pass_when_text_contains`

- Signature: `conf.pass_when_text_contains(subject, token)`
- Module: `conformance`
- Library: `conformance.assertion.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/conformance/assertion_core.spec.md#LIB-CONF-ASSERT-001`
- Export Path: `/__export__conf.pass_when_text_contains`

#### Summary

Contract export for `conf.pass_when_text_contains`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |
| `token` | `any` | `true` | Input parameter `token`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>', 'token': '<token>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `conf.pass_when_text_regex` {#symbol-conf_pass_when_text_regex}

Contract-backed: `/specs/libraries/conformance/assertion_core.spec.md#LIB-CONF-ASSERT-001` via `/__export__conf.pass_when_text_regex`

- Signature: `conf.pass_when_text_regex(subject, pattern)`
- Module: `conformance`
- Library: `conformance.assertion.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/conformance/assertion_core.spec.md#LIB-CONF-ASSERT-001`
- Export Path: `/__export__conf.pass_when_text_regex`

#### Summary

Contract export for `conf.pass_when_text_regex`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |
| `pattern` | `any` | `true` | Input parameter `pattern`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>', 'pattern': '<pattern>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.artifact.append_text` {#symbol-domain_artifact_append_text}

Contract-backed: `/specs/libraries/domain/artifact_core.spec.md#LIB-DOMAIN-ARTIFACT-001-002-DOMAIN-ARTIFACT-APPEND-TEXT` via `/__export__domain.artifact.append_text`

- Signature: `domain.artifact.append_text(path, content)`
- Module: `domain`
- Library: `domain.artifact.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/artifact_core.spec.md#LIB-DOMAIN-ARTIFACT-001-002-DOMAIN-ARTIFACT-APPEND-TEXT`
- Export Path: `/__export__domain.artifact.append_text`

#### Summary

Contract export for `domain.artifact.append_text`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `path` | `any` | `true` | Input parameter `path`. |  |
| `content` | `any` | `true` | Input parameter `content`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'path': '<path>', 'content': '<content>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.artifact.write_yaml` {#symbol-domain_artifact_write_yaml}

Contract-backed: `/specs/libraries/domain/artifact_core.spec.md#LIB-DOMAIN-ARTIFACT-001-001-DOMAIN-ARTIFACT-WRITE-YAML` via `/__export__domain.artifact.write_yaml`

- Signature: `domain.artifact.write_yaml(path, value)`
- Module: `domain`
- Library: `domain.artifact.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/artifact_core.spec.md#LIB-DOMAIN-ARTIFACT-001-001-DOMAIN-ARTIFACT-WRITE-YAML`
- Export Path: `/__export__domain.artifact.write_yaml`

#### Summary

Contract export for `domain.artifact.write_yaml`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `path` | `any` | `true` | Input parameter `path`. |  |
| `value` | `any` | `true` | Input parameter `value`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'path': '<path>', 'value': '<value>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.conformance.error_when_false` {#symbol-domain_conformance_error_when_false}

Contract-backed: `/specs/libraries/domain/conformance_core.spec.md#LIB-DOMAIN-CONFORMANCE-001-000-DOMAIN-CONFORMANCE-ERROR-WHEN-FALSE` via `/__export__domain.conformance.error_when_false`

- Signature: `domain.conformance.error_when_false(condition, message)`
- Module: `domain`
- Library: `domain.conformance.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/conformance_core.spec.md#LIB-DOMAIN-CONFORMANCE-001-000-DOMAIN-CONFORMANCE-ERROR-WHEN-FALSE`
- Export Path: `/__export__domain.conformance.error_when_false`

#### Summary

Contract export for `domain.conformance.error_when_false`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `condition` | `any` | `true` | Input parameter `condition`. |  |
| `message` | `any` | `true` | Input parameter `message`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'condition': '<condition>', 'message': '<message>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.conformance.report_results_is_list` {#symbol-domain_conformance_report_results_is_list}

Contract-backed: `/specs/libraries/domain/conformance_core.spec.md#LIB-DOMAIN-CONFORMANCE-001-000B-DOMAIN-CONFORMANCE-REPORT-RESULTS-IS-LIST` via `/__export__domain.conformance.report_results_is_list`

- Signature: `domain.conformance.report_results_is_list(report)`
- Module: `domain`
- Library: `domain.conformance.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/conformance_core.spec.md#LIB-DOMAIN-CONFORMANCE-001-000B-DOMAIN-CONFORMANCE-REPORT-RESULTS-IS-LIST`
- Export Path: `/__export__domain.conformance.report_results_is_list`

#### Summary

Contract export for `domain.conformance.report_results_is_list`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `report` | `any` | `true` | Input parameter `report`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'report': '<report>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.conformance.report_version_is_v1` {#symbol-domain_conformance_report_version_is_v1}

Contract-backed: `/specs/libraries/domain/conformance_core.spec.md#LIB-DOMAIN-CONFORMANCE-001-000A-DOMAIN-CONFORMANCE-REPORT-VERSION-IS-V1` via `/__export__domain.conformance.report_version_is_v1`

- Signature: `domain.conformance.report_version_is_v1(report)`
- Module: `domain`
- Library: `domain.conformance.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/conformance_core.spec.md#LIB-DOMAIN-CONFORMANCE-001-000A-DOMAIN-CONFORMANCE-REPORT-VERSION-IS-V1`
- Export Path: `/__export__domain.conformance.report_version_is_v1`

#### Summary

Contract export for `domain.conformance.report_version_is_v1`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `report` | `any` | `true` | Input parameter `report`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'report': '<report>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.conformance.validate_report_errors` {#symbol-domain_conformance_validate_report_errors}

Contract-backed: `/specs/libraries/domain/conformance_core.spec.md#LIB-DOMAIN-CONFORMANCE-001-000C-DOMAIN-CONFORMANCE-VALIDATE-REPORT-ERRORS` via `/__export__domain.conformance.validate_report_errors`

- Signature: `domain.conformance.validate_report_errors(report)`
- Module: `domain`
- Library: `domain.conformance.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/conformance_core.spec.md#LIB-DOMAIN-CONFORMANCE-001-000C-DOMAIN-CONFORMANCE-VALIDATE-REPORT-ERRORS`
- Export Path: `/__export__domain.conformance.validate_report_errors`

#### Summary

Contract export for `domain.conformance.validate_report_errors`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `report` | `any` | `true` | Input parameter `report`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'report': '<report>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.file.has_ext` {#symbol-domain_file_has_ext}

Contract-backed: `/specs/libraries/domain/path_core.spec.md#LIB-DOMAIN-PATH-001-008-DOMAIN-FILE-HAS-EXT` via `/__export__domain.file.has_ext`

- Signature: `domain.file.has_ext(meta, ext)`
- Module: `domain`
- Library: `domain.path.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/path_core.spec.md#LIB-DOMAIN-PATH-001-008-DOMAIN-FILE-HAS-EXT`
- Export Path: `/__export__domain.file.has_ext`

#### Summary

Contract export for `domain.file.has_ext`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `meta` | `any` | `true` | Input parameter `meta`. |  |
| `ext` | `any` | `true` | Input parameter `ext`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'meta': '<meta>', 'ext': '<ext>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.file.is_existing_dir` {#symbol-domain_file_is_existing_dir}

Contract-backed: `/specs/libraries/domain/path_core.spec.md#LIB-DOMAIN-PATH-001-007-DOMAIN-FILE-IS-EXISTING-DIR` via `/__export__domain.file.is_existing_dir`

- Signature: `domain.file.is_existing_dir(meta)`
- Module: `domain`
- Library: `domain.path.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/path_core.spec.md#LIB-DOMAIN-PATH-001-007-DOMAIN-FILE-IS-EXISTING-DIR`
- Export Path: `/__export__domain.file.is_existing_dir`

#### Summary

Contract export for `domain.file.is_existing_dir`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `meta` | `any` | `true` | Input parameter `meta`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'meta': '<meta>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.file.is_existing_file` {#symbol-domain_file_is_existing_file}

Contract-backed: `/specs/libraries/domain/path_core.spec.md#LIB-DOMAIN-PATH-001-006-DOMAIN-FILE-IS-EXISTING-FILE` via `/__export__domain.file.is_existing_file`

- Signature: `domain.file.is_existing_file(meta)`
- Module: `domain`
- Library: `domain.path.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/path_core.spec.md#LIB-DOMAIN-PATH-001-006-DOMAIN-FILE-IS-EXISTING-FILE`
- Export Path: `/__export__domain.file.is_existing_file`

#### Summary

Contract export for `domain.file.is_existing_file`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `meta` | `any` | `true` | Input parameter `meta`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'meta': '<meta>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.file.name` {#symbol-domain_file_name}

Contract-backed: `/specs/libraries/domain/path_core.spec.md#LIB-DOMAIN-PATH-001-009-DOMAIN-FILE-NAME` via `/__export__domain.file.name`

- Signature: `domain.file.name(meta)`
- Module: `domain`
- Library: `domain.path.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/path_core.spec.md#LIB-DOMAIN-PATH-001-009-DOMAIN-FILE-NAME`
- Export Path: `/__export__domain.file.name`

#### Summary

Contract export for `domain.file.name`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `meta` | `any` | `true` | Input parameter `meta`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'meta': '<meta>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.fs.file_ext_eq` {#symbol-domain_fs_file_ext_eq}

Contract-backed: `/specs/libraries/domain/fs_core.spec.md#LIB-DOMAIN-FS-001-006-DOMAIN-FS-FILE-EXT-EQ` via `/__export__domain.fs.file_ext_eq`

- Signature: `domain.fs.file_ext_eq(meta, ext)`
- Module: `domain`
- Library: `domain.fs.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/fs_core.spec.md#LIB-DOMAIN-FS-001-006-DOMAIN-FS-FILE-EXT-EQ`
- Export Path: `/__export__domain.fs.file_ext_eq`

#### Summary

Contract export for `domain.fs.file_ext_eq`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `meta` | `any` | `true` | Input parameter `meta`. |  |
| `ext` | `any` | `true` | Input parameter `ext`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'meta': '<meta>', 'ext': '<ext>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.fs.glob_all` {#symbol-domain_fs_glob_all}

Contract-backed: `/specs/libraries/domain/fs_core.spec.md#LIB-DOMAIN-FS-001-010-DOMAIN-FS-GLOB-ALL` via `/__export__domain.fs.glob_all`

- Signature: `domain.fs.glob_all(paths, pattern)`
- Module: `domain`
- Library: `domain.fs.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/fs_core.spec.md#LIB-DOMAIN-FS-001-010-DOMAIN-FS-GLOB-ALL`
- Export Path: `/__export__domain.fs.glob_all`

#### Summary

Contract export for `domain.fs.glob_all`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `paths` | `any` | `true` | Input parameter `paths`. |  |
| `pattern` | `any` | `true` | Input parameter `pattern`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'paths': '<paths>', 'pattern': '<pattern>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.fs.glob_any_spec_files` {#symbol-domain_fs_glob_any_spec_files}

Contract-backed: `/specs/libraries/domain/fs_core.spec.md#LIB-DOMAIN-FS-001-005-DOMAIN-FS-GLOB-ANY-SPEC-FILES` via `/__export__domain.fs.glob_any_spec_files`

- Signature: `domain.fs.glob_any_spec_files(paths)`
- Module: `domain`
- Library: `domain.fs.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/fs_core.spec.md#LIB-DOMAIN-FS-001-005-DOMAIN-FS-GLOB-ANY-SPEC-FILES`
- Export Path: `/__export__domain.fs.glob_any_spec_files`

#### Summary

Contract export for `domain.fs.glob_any_spec_files`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `paths` | `any` | `true` | Input parameter `paths`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'paths': '<paths>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.fs.glob_filter` {#symbol-domain_fs_glob_filter}

Contract-backed: `/specs/libraries/domain/fs_core.spec.md#LIB-DOMAIN-FS-001-009-DOMAIN-FS-GLOB-FILTER` via `/__export__domain.fs.glob_filter`

- Signature: `domain.fs.glob_filter(paths, pattern)`
- Module: `domain`
- Library: `domain.fs.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/fs_core.spec.md#LIB-DOMAIN-FS-001-009-DOMAIN-FS-GLOB-FILTER`
- Export Path: `/__export__domain.fs.glob_filter`

#### Summary

Contract export for `domain.fs.glob_filter`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `paths` | `any` | `true` | Input parameter `paths`. |  |
| `pattern` | `any` | `true` | Input parameter `pattern`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'paths': '<paths>', 'pattern': '<pattern>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.fs.is_docs_spec_file` {#symbol-domain_fs_is_docs_spec_file}

Contract-backed: `/specs/libraries/domain/fs_core.spec.md#LIB-DOMAIN-FS-001-001-DOMAIN-FS-IS-DOCS-SPEC-FILE` via `/__export__domain.fs.is_docs_spec_file`

- Signature: `domain.fs.is_docs_spec_file(path)`
- Module: `domain`
- Library: `domain.fs.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/fs_core.spec.md#LIB-DOMAIN-FS-001-001-DOMAIN-FS-IS-DOCS-SPEC-FILE`
- Export Path: `/__export__domain.fs.is_docs_spec_file`

#### Summary

Contract export for `domain.fs.is_docs_spec_file`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `path` | `any` | `true` | Input parameter `path`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'path': '<path>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.fs.json_get_or_text` {#symbol-domain_fs_json_get_or_text}

Contract-backed: `/specs/libraries/domain/fs_core.spec.md#LIB-DOMAIN-FS-001-003-DOMAIN-FS-JSON-GET-OR-TEXT` via `/__export__domain.fs.json_get_or_text`

- Signature: `domain.fs.json_get_or_text(json_text, path_segments, fallback)`
- Module: `domain`
- Library: `domain.fs.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/fs_core.spec.md#LIB-DOMAIN-FS-001-003-DOMAIN-FS-JSON-GET-OR-TEXT`
- Export Path: `/__export__domain.fs.json_get_or_text`

#### Summary

Contract export for `domain.fs.json_get_or_text`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `json_text` | `any` | `true` | Input parameter `json_text`. |  |
| `path_segments` | `any` | `true` | Input parameter `path_segments`. |  |
| `fallback` | `any` | `true` | Input parameter `fallback`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'json_text': '<json_text>', 'path_segments': '<path_segments>', 'fallback': '<fallback>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.fs.json_get_text` {#symbol-domain_fs_json_get_text}

Contract-backed: `/specs/libraries/domain/fs_core.spec.md#LIB-DOMAIN-FS-001-007-DOMAIN-FS-JSON-GET-TEXT` via `/__export__domain.fs.json_get_text`

- Signature: `domain.fs.json_get_text(json_text, path_segments)`
- Module: `domain`
- Library: `domain.fs.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/fs_core.spec.md#LIB-DOMAIN-FS-001-007-DOMAIN-FS-JSON-GET-TEXT`
- Export Path: `/__export__domain.fs.json_get_text`

#### Summary

Contract export for `domain.fs.json_get_text`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `json_text` | `any` | `true` | Input parameter `json_text`. |  |
| `path_segments` | `any` | `true` | Input parameter `path_segments`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'json_text': '<json_text>', 'path_segments': '<path_segments>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.fs.json_has_path_text` {#symbol-domain_fs_json_has_path_text}

Contract-backed: `/specs/libraries/domain/fs_core.spec.md#LIB-DOMAIN-FS-001-004-DOMAIN-FS-JSON-HAS-PATH-TEXT` via `/__export__domain.fs.json_has_path_text`

- Signature: `domain.fs.json_has_path_text(json_text, path_segments)`
- Module: `domain`
- Library: `domain.fs.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/fs_core.spec.md#LIB-DOMAIN-FS-001-004-DOMAIN-FS-JSON-HAS-PATH-TEXT`
- Export Path: `/__export__domain.fs.json_has_path_text`

#### Summary

Contract export for `domain.fs.json_has_path_text`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `json_text` | `any` | `true` | Input parameter `json_text`. |  |
| `path_segments` | `any` | `true` | Input parameter `path_segments`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'json_text': '<json_text>', 'path_segments': '<path_segments>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.fs.json_path_eq_text` {#symbol-domain_fs_json_path_eq_text}

Contract-backed: `/specs/libraries/domain/fs_core.spec.md#LIB-DOMAIN-FS-001-008-DOMAIN-FS-JSON-PATH-EQ-TEXT` via `/__export__domain.fs.json_path_eq_text`

- Signature: `domain.fs.json_path_eq_text(json_text, path_segments, expected)`
- Module: `domain`
- Library: `domain.fs.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/fs_core.spec.md#LIB-DOMAIN-FS-001-008-DOMAIN-FS-JSON-PATH-EQ-TEXT`
- Export Path: `/__export__domain.fs.json_path_eq_text`

#### Summary

Contract export for `domain.fs.json_path_eq_text`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `json_text` | `any` | `true` | Input parameter `json_text`. |  |
| `path_segments` | `any` | `true` | Input parameter `path_segments`. |  |
| `expected` | `any` | `true` | Input parameter `expected`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'json_text': '<json_text>', 'path_segments': '<path_segments>', 'expected': '<expected>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.fs.sort_spec_files` {#symbol-domain_fs_sort_spec_files}

Contract-backed: `/specs/libraries/domain/fs_core.spec.md#LIB-DOMAIN-FS-001-002-DOMAIN-FS-SORT-SPEC-FILES` via `/__export__domain.fs.sort_spec_files`

- Signature: `domain.fs.sort_spec_files(paths)`
- Module: `domain`
- Library: `domain.fs.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/fs_core.spec.md#LIB-DOMAIN-FS-001-002-DOMAIN-FS-SORT-SPEC-FILES`
- Export Path: `/__export__domain.fs.sort_spec_files`

#### Summary

Contract export for `domain.fs.sort_spec_files`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `paths` | `any` | `true` | Input parameter `paths`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'paths': '<paths>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.http.auth_is_oauth` {#symbol-domain_http_auth_is_oauth}

Contract-backed: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-013-DOMAIN-HTTP-AUTH-IS-OAUTH` via `/__export__domain.http.auth_is_oauth`

- Signature: `domain.http.auth_is_oauth(subject)`
- Module: `domain`
- Library: `domain.http.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-013-DOMAIN-HTTP-AUTH-IS-OAUTH`
- Export Path: `/__export__domain.http.auth_is_oauth`

#### Summary

Contract export for `domain.http.auth_is_oauth`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.http.body_json` {#symbol-domain_http_body_json}

Contract-backed: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-010-DOMAIN-HTTP-BODY-JSON` via `/__export__domain.http.body_json`

- Signature: `domain.http.body_json(subject)`
- Module: `domain`
- Library: `domain.http.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-010-DOMAIN-HTTP-BODY-JSON`
- Export Path: `/__export__domain.http.body_json`

#### Summary

Contract export for `domain.http.body_json`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.http.body_json_has_key` {#symbol-domain_http_body_json_has_key}

Contract-backed: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-012-DOMAIN-HTTP-BODY-JSON-HAS-KEY` via `/__export__domain.http.body_json_has_key`

- Signature: `domain.http.body_json_has_key(subject, key)`
- Module: `domain`
- Library: `domain.http.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-012-DOMAIN-HTTP-BODY-JSON-HAS-KEY`
- Export Path: `/__export__domain.http.body_json_has_key`

#### Summary

Contract export for `domain.http.body_json_has_key`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |
| `key` | `any` | `true` | Input parameter `key`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>', 'key': '<key>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.http.body_json_type_is` {#symbol-domain_http_body_json_type_is}

Contract-backed: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-011-DOMAIN-HTTP-BODY-JSON-TYPE-IS` via `/__export__domain.http.body_json_type_is`

- Signature: `domain.http.body_json_type_is(subject, expected_type)`
- Module: `domain`
- Library: `domain.http.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-011-DOMAIN-HTTP-BODY-JSON-TYPE-IS`
- Export Path: `/__export__domain.http.body_json_type_is`

#### Summary

Contract export for `domain.http.body_json_type_is`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |
| `expected_type` | `any` | `true` | Input parameter `expected_type`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>', 'expected_type': '<expected_type>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.http.body_text` {#symbol-domain_http_body_text}

Contract-backed: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-009-DOMAIN-HTTP-BODY-TEXT` via `/__export__domain.http.body_text`

- Signature: `domain.http.body_text(subject)`
- Module: `domain`
- Library: `domain.http.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-009-DOMAIN-HTTP-BODY-TEXT`
- Export Path: `/__export__domain.http.body_text`

#### Summary

Contract export for `domain.http.body_text`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.http.cors_allow_origin` {#symbol-domain_http_cors_allow_origin}

Contract-backed: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-016-DOMAIN-HTTP-CORS-ALLOW-ORIGIN` via `/__export__domain.http.cors_allow_origin`

- Signature: `domain.http.cors_allow_origin(subject)`
- Module: `domain`
- Library: `domain.http.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-016-DOMAIN-HTTP-CORS-ALLOW-ORIGIN`
- Export Path: `/__export__domain.http.cors_allow_origin`

#### Summary

Contract export for `domain.http.cors_allow_origin`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.http.cors_allows_header` {#symbol-domain_http_cors_allows_header}

Contract-backed: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-018-DOMAIN-HTTP-CORS-ALLOWS-HEADER` via `/__export__domain.http.cors_allows_header`

- Signature: `domain.http.cors_allows_header(subject, header_name)`
- Module: `domain`
- Library: `domain.http.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-018-DOMAIN-HTTP-CORS-ALLOWS-HEADER`
- Export Path: `/__export__domain.http.cors_allows_header`

#### Summary

Contract export for `domain.http.cors_allows_header`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |
| `header_name` | `any` | `true` | Input parameter `header_name`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>', 'header_name': '<header_name>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.http.cors_allows_method` {#symbol-domain_http_cors_allows_method}

Contract-backed: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-017-DOMAIN-HTTP-CORS-ALLOWS-METHOD` via `/__export__domain.http.cors_allows_method`

- Signature: `domain.http.cors_allows_method(subject, method_name)`
- Module: `domain`
- Library: `domain.http.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-017-DOMAIN-HTTP-CORS-ALLOWS-METHOD`
- Export Path: `/__export__domain.http.cors_allows_method`

#### Summary

Contract export for `domain.http.cors_allows_method`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |
| `method_name` | `any` | `true` | Input parameter `method_name`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>', 'method_name': '<method_name>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.http.cors_credentials_enabled` {#symbol-domain_http_cors_credentials_enabled}

Contract-backed: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-019-DOMAIN-HTTP-CORS-CREDENTIALS-ENABLED` via `/__export__domain.http.cors_credentials_enabled`

- Signature: `domain.http.cors_credentials_enabled(subject)`
- Module: `domain`
- Library: `domain.http.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-019-DOMAIN-HTTP-CORS-CREDENTIALS-ENABLED`
- Export Path: `/__export__domain.http.cors_credentials_enabled`

#### Summary

Contract export for `domain.http.cors_credentials_enabled`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.http.cors_max_age_gte` {#symbol-domain_http_cors_max_age_gte}

Contract-backed: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-020-DOMAIN-HTTP-CORS-MAX-AGE-GTE` via `/__export__domain.http.cors_max_age_gte`

- Signature: `domain.http.cors_max_age_gte(subject, min_age)`
- Module: `domain`
- Library: `domain.http.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-020-DOMAIN-HTTP-CORS-MAX-AGE-GTE`
- Export Path: `/__export__domain.http.cors_max_age_gte`

#### Summary

Contract export for `domain.http.cors_max_age_gte`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |
| `min_age` | `any` | `true` | Input parameter `min_age`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>', 'min_age': '<min_age>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.http.has_bearer_header` {#symbol-domain_http_has_bearer_header}

Contract-backed: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-014-DOMAIN-HTTP-HAS-BEARER-HEADER` via `/__export__domain.http.has_bearer_header`

- Signature: `domain.http.has_bearer_header(subject)`
- Module: `domain`
- Library: `domain.http.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-014-DOMAIN-HTTP-HAS-BEARER-HEADER`
- Export Path: `/__export__domain.http.has_bearer_header`

#### Summary

Contract export for `domain.http.has_bearer_header`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.http.header_contains` {#symbol-domain_http_header_contains}

Contract-backed: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-008-DOMAIN-HTTP-HEADER-CONTAINS` via `/__export__domain.http.header_contains`

- Signature: `domain.http.header_contains(subject, key, token)`
- Module: `domain`
- Library: `domain.http.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-008-DOMAIN-HTTP-HEADER-CONTAINS`
- Export Path: `/__export__domain.http.header_contains`

#### Summary

Contract export for `domain.http.header_contains`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |
| `key` | `any` | `true` | Input parameter `key`. |  |
| `token` | `any` | `true` | Input parameter `token`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>', 'key': '<key>', 'token': '<token>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.http.header_get` {#symbol-domain_http_header_get}

Contract-backed: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-007-DOMAIN-HTTP-HEADER-GET` via `/__export__domain.http.header_get`

- Signature: `domain.http.header_get(subject, key)`
- Module: `domain`
- Library: `domain.http.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-007-DOMAIN-HTTP-HEADER-GET`
- Export Path: `/__export__domain.http.header_get`

#### Summary

Contract export for `domain.http.header_get`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |
| `key` | `any` | `true` | Input parameter `key`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>', 'key': '<key>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.http.is_preflight_step` {#symbol-domain_http_is_preflight_step}

Contract-backed: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-021-DOMAIN-HTTP-IS-PREFLIGHT-STEP` via `/__export__domain.http.is_preflight_step`

- Signature: `domain.http.is_preflight_step(step)`
- Module: `domain`
- Library: `domain.http.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-021-DOMAIN-HTTP-IS-PREFLIGHT-STEP`
- Export Path: `/__export__domain.http.is_preflight_step`

#### Summary

Contract export for `domain.http.is_preflight_step`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `step` | `any` | `true` | Input parameter `step`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'step': '<step>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.http.oauth_scope_requested` {#symbol-domain_http_oauth_scope_requested}

Contract-backed: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-015-DOMAIN-HTTP-OAUTH-SCOPE-REQUESTED` via `/__export__domain.http.oauth_scope_requested`

- Signature: `domain.http.oauth_scope_requested(subject)`
- Module: `domain`
- Library: `domain.http.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-015-DOMAIN-HTTP-OAUTH-SCOPE-REQUESTED`
- Export Path: `/__export__domain.http.oauth_scope_requested`

#### Summary

Contract export for `domain.http.oauth_scope_requested`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.http.oauth_token_source_is` {#symbol-domain_http_oauth_token_source_is}

Contract-backed: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-014-DOMAIN-HTTP-OAUTH-TOKEN-SOURCE-IS` via `/__export__domain.http.oauth_token_source_is`

- Signature: `domain.http.oauth_token_source_is(subject, expected)`
- Module: `domain`
- Library: `domain.http.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-014-DOMAIN-HTTP-OAUTH-TOKEN-SOURCE-IS`
- Export Path: `/__export__domain.http.oauth_token_source_is`

#### Summary

Contract export for `domain.http.oauth_token_source_is`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |
| `expected` | `any` | `true` | Input parameter `expected`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>', 'expected': '<expected>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.http.ok_2xx` {#symbol-domain_http_ok_2xx}

Contract-backed: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-006-DOMAIN-HTTP-OK-2XX` via `/__export__domain.http.ok_2xx`

- Signature: `domain.http.ok_2xx(subject)`
- Module: `domain`
- Library: `domain.http.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-006-DOMAIN-HTTP-OK-2XX`
- Export Path: `/__export__domain.http.ok_2xx`

#### Summary

Contract export for `domain.http.ok_2xx`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.http.status` {#symbol-domain_http_status}

Contract-backed: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-001-DOMAIN-HTTP-STATUS` via `/__export__domain.http.status`

- Signature: `domain.http.status(subject)`
- Module: `domain`
- Library: `domain.http.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-001-DOMAIN-HTTP-STATUS`
- Export Path: `/__export__domain.http.status`

#### Summary

Contract export for `domain.http.status`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.http.status_in` {#symbol-domain_http_status_in}

Contract-backed: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-002-DOMAIN-HTTP-STATUS-IN` via `/__export__domain.http.status_in`

- Signature: `domain.http.status_in(subject, allowed)`
- Module: `domain`
- Library: `domain.http.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-002-DOMAIN-HTTP-STATUS-IN`
- Export Path: `/__export__domain.http.status_in`

#### Summary

Contract export for `domain.http.status_in`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |
| `allowed` | `any` | `true` | Input parameter `allowed`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>', 'allowed': '<allowed>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.http.status_is` {#symbol-domain_http_status_is}

Contract-backed: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-003-DOMAIN-HTTP-STATUS-IS` via `/__export__domain.http.status_is`

- Signature: `domain.http.status_is(subject, expected)`
- Module: `domain`
- Library: `domain.http.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-003-DOMAIN-HTTP-STATUS-IS`
- Export Path: `/__export__domain.http.status_is`

#### Summary

Contract export for `domain.http.status_is`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |
| `expected` | `any` | `true` | Input parameter `expected`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>', 'expected': '<expected>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.http.status_is_forbidden` {#symbol-domain_http_status_is_forbidden}

Contract-backed: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-005-DOMAIN-HTTP-STATUS-IS-FORBIDDEN` via `/__export__domain.http.status_is_forbidden`

- Signature: `domain.http.status_is_forbidden(subject)`
- Module: `domain`
- Library: `domain.http.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-005-DOMAIN-HTTP-STATUS-IS-FORBIDDEN`
- Export Path: `/__export__domain.http.status_is_forbidden`

#### Summary

Contract export for `domain.http.status_is_forbidden`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.http.status_is_unauthorized` {#symbol-domain_http_status_is_unauthorized}

Contract-backed: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-004-DOMAIN-HTTP-STATUS-IS-UNAUTHORIZED` via `/__export__domain.http.status_is_unauthorized`

- Signature: `domain.http.status_is_unauthorized(subject)`
- Module: `domain`
- Library: `domain.http.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-004-DOMAIN-HTTP-STATUS-IS-UNAUTHORIZED`
- Export Path: `/__export__domain.http.status_is_unauthorized`

#### Summary

Contract export for `domain.http.status_is_unauthorized`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.http.step_body_json_get` {#symbol-domain_http_step_body_json_get}

Contract-backed: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-024-DOMAIN-HTTP-STEP-BODY-JSON-GET` via `/__export__domain.http.step_body_json_get`

- Signature: `domain.http.step_body_json_get(steps, step_id, field)`
- Module: `domain`
- Library: `domain.http.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-024-DOMAIN-HTTP-STEP-BODY-JSON-GET`
- Export Path: `/__export__domain.http.step_body_json_get`

#### Summary

Contract export for `domain.http.step_body_json_get`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `steps` | `any` | `true` | Input parameter `steps`. |  |
| `step_id` | `any` | `true` | Input parameter `step_id`. |  |
| `field` | `any` | `true` | Input parameter `field`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'steps': '<steps>', 'step_id': '<step_id>', 'field': '<field>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.http.step_by_id` {#symbol-domain_http_step_by_id}

Contract-backed: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-022-DOMAIN-HTTP-STEP-BY-ID` via `/__export__domain.http.step_by_id`

- Signature: `domain.http.step_by_id(steps, step_id)`
- Module: `domain`
- Library: `domain.http.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-022-DOMAIN-HTTP-STEP-BY-ID`
- Export Path: `/__export__domain.http.step_by_id`

#### Summary

Contract export for `domain.http.step_by_id`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `steps` | `any` | `true` | Input parameter `steps`. |  |
| `step_id` | `any` | `true` | Input parameter `step_id`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'steps': '<steps>', 'step_id': '<step_id>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.http.step_status_is` {#symbol-domain_http_step_status_is}

Contract-backed: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-023-DOMAIN-HTTP-STEP-STATUS-IS` via `/__export__domain.http.step_status_is`

- Signature: `domain.http.step_status_is(steps, step_id, expected)`
- Module: `domain`
- Library: `domain.http.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/http_core.spec.md#LIB-DOMAIN-HTTP-001-023-DOMAIN-HTTP-STEP-STATUS-IS`
- Export Path: `/__export__domain.http.step_status_is`

#### Summary

Contract export for `domain.http.step_status_is`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `steps` | `any` | `true` | Input parameter `steps`. |  |
| `step_id` | `any` | `true` | Input parameter `step_id`. |  |
| `expected` | `any` | `true` | Input parameter `expected`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'steps': '<steps>', 'step_id': '<step_id>', 'expected': '<expected>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.job.scan_bundle_has_result` {#symbol-domain_job_scan_bundle_has_result}

Contract-backed: `/specs/libraries/domain/job_core.spec.md#LIB-DOMAIN-JOB-001-000A-DOMAIN-JOB-SCAN-BUNDLE-HAS-RESULT` via `/__export__domain.job.scan_bundle_has_result`

- Signature: `domain.job.scan_bundle_has_result(scan_path, pattern)`
- Module: `domain`
- Library: `domain.job.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/job_core.spec.md#LIB-DOMAIN-JOB-001-000A-DOMAIN-JOB-SCAN-BUNDLE-HAS-RESULT`
- Export Path: `/__export__domain.job.scan_bundle_has_result`

#### Summary

Contract export for `domain.job.scan_bundle_has_result`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `scan_path` | `any` | `true` | Input parameter `scan_path`. |  |
| `pattern` | `any` | `true` | Input parameter `pattern`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'scan_path': '<scan_path>', 'pattern': '<pattern>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.markdown.code_fence_language_exists` {#symbol-domain_markdown_code_fence_language_exists}

Contract-backed: `/specs/libraries/domain/markdown_core.spec.md#LIB-DOMAIN-MD-001-015-DOMAIN-MARKDOWN-CODE-FENCE-LANGUAGE-EXISTS` via `/__export__domain.markdown.code_fence_language_exists`

- Signature: `domain.markdown.code_fence_language_exists(subject, language)`
- Module: `domain`
- Library: `domain.markdown.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/markdown_core.spec.md#LIB-DOMAIN-MD-001-015-DOMAIN-MARKDOWN-CODE-FENCE-LANGUAGE-EXISTS`
- Export Path: `/__export__domain.markdown.code_fence_language_exists`

#### Summary

Contract export for `domain.markdown.code_fence_language_exists`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |
| `language` | `any` | `true` | Input parameter `language`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>', 'language': '<language>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.markdown.has_broken_links` {#symbol-domain_markdown_has_broken_links}

Contract-backed: `/specs/libraries/domain/markdown_core.spec.md#LIB-DOMAIN-MD-001-011-DOMAIN-MARKDOWN-HAS-BROKEN-LINKS` via `/__export__domain.markdown.has_broken_links`

- Signature: `domain.markdown.has_broken_links(subject)`
- Module: `domain`
- Library: `domain.markdown.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/markdown_core.spec.md#LIB-DOMAIN-MD-001-011-DOMAIN-MARKDOWN-HAS-BROKEN-LINKS`
- Export Path: `/__export__domain.markdown.has_broken_links`

#### Summary

Contract export for `domain.markdown.has_broken_links`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.markdown.has_heading` {#symbol-domain_markdown_has_heading}

Contract-backed: `/specs/libraries/domain/markdown_core.spec.md#LIB-DOMAIN-MD-001-001-DOMAIN-MARKDOWN-HAS-HEADING` via `/__export__domain.markdown.has_heading`

- Signature: `domain.markdown.has_heading(subject, heading)`
- Module: `domain`
- Library: `domain.markdown.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/markdown_core.spec.md#LIB-DOMAIN-MD-001-001-DOMAIN-MARKDOWN-HAS-HEADING`
- Export Path: `/__export__domain.markdown.has_heading`

#### Summary

Contract export for `domain.markdown.has_heading`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |
| `heading` | `any` | `true` | Input parameter `heading`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>', 'heading': '<heading>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.markdown.has_yaml_spec_test_fence` {#symbol-domain_markdown_has_yaml_spec_test_fence}

Contract-backed: `/specs/libraries/domain/markdown_core.spec.md#LIB-DOMAIN-MD-001-013-DOMAIN-MARKDOWN-HAS-YAML-SPEC-TEST-FENCE` via `/__export__domain.markdown.has_yaml_spec_test_fence`

- Signature: `domain.markdown.has_yaml_spec_test_fence(subject)`
- Module: `domain`
- Library: `domain.markdown.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/markdown_core.spec.md#LIB-DOMAIN-MD-001-013-DOMAIN-MARKDOWN-HAS-YAML-SPEC-TEST-FENCE`
- Export Path: `/__export__domain.markdown.has_yaml_spec_test_fence`

#### Summary

Contract export for `domain.markdown.has_yaml_spec_test_fence`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.markdown.heading_level_exists` {#symbol-domain_markdown_heading_level_exists}

Contract-backed: `/specs/libraries/domain/markdown_core.spec.md#LIB-DOMAIN-MD-001-003-DOMAIN-MARKDOWN-HEADING-LEVEL-EXISTS` via `/__export__domain.markdown.heading_level_exists`

- Signature: `domain.markdown.heading_level_exists(subject, level)`
- Module: `domain`
- Library: `domain.markdown.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/markdown_core.spec.md#LIB-DOMAIN-MD-001-003-DOMAIN-MARKDOWN-HEADING-LEVEL-EXISTS`
- Export Path: `/__export__domain.markdown.heading_level_exists`

#### Summary

Contract export for `domain.markdown.heading_level_exists`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |
| `level` | `any` | `true` | Input parameter `level`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>', 'level': '<level>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.markdown.link_targets_all_resolve` {#symbol-domain_markdown_link_targets_all_resolve}

Contract-backed: `/specs/libraries/domain/markdown_core.spec.md#LIB-DOMAIN-MD-001-009-DOMAIN-MARKDOWN-LINK-TARGETS-ALL-RESOLVE` via `/__export__domain.markdown.link_targets_all_resolve`

- Signature: `domain.markdown.link_targets_all_resolve(subject)`
- Module: `domain`
- Library: `domain.markdown.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/markdown_core.spec.md#LIB-DOMAIN-MD-001-009-DOMAIN-MARKDOWN-LINK-TARGETS-ALL-RESOLVE`
- Export Path: `/__export__domain.markdown.link_targets_all_resolve`

#### Summary

Contract export for `domain.markdown.link_targets_all_resolve`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.markdown.required_sections_present` {#symbol-domain_markdown_required_sections_present}

Contract-backed: `/specs/libraries/domain/markdown_core.spec.md#LIB-DOMAIN-MD-001-007-DOMAIN-MARKDOWN-REQUIRED-SECTIONS-PRESENT` via `/__export__domain.markdown.required_sections_present`

- Signature: `domain.markdown.required_sections_present(subject, headings)`
- Module: `domain`
- Library: `domain.markdown.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/markdown_core.spec.md#LIB-DOMAIN-MD-001-007-DOMAIN-MARKDOWN-REQUIRED-SECTIONS-PRESENT`
- Export Path: `/__export__domain.markdown.required_sections_present`

#### Summary

Contract export for `domain.markdown.required_sections_present`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |
| `headings` | `any` | `true` | Input parameter `headings`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>', 'headings': '<headings>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.markdown.section_order_valid` {#symbol-domain_markdown_section_order_valid}

Contract-backed: `/specs/libraries/domain/markdown_core.spec.md#LIB-DOMAIN-MD-001-005-DOMAIN-MARKDOWN-SECTION-ORDER-VALID` via `/__export__domain.markdown.section_order_valid`

- Signature: `domain.markdown.section_order_valid(subject, headings)`
- Module: `domain`
- Library: `domain.markdown.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/markdown_core.spec.md#LIB-DOMAIN-MD-001-005-DOMAIN-MARKDOWN-SECTION-ORDER-VALID`
- Export Path: `/__export__domain.markdown.section_order_valid`

#### Summary

Contract export for `domain.markdown.section_order_valid`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |
| `headings` | `any` | `true` | Input parameter `headings`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>', 'headings': '<headings>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.markdown.token_dependencies_resolved` {#symbol-domain_markdown_token_dependencies_resolved}

Contract-backed: `/specs/libraries/domain/markdown_core.spec.md#LIB-DOMAIN-MD-001-023-DOMAIN-MARKDOWN-TOKEN-DEPENDENCIES-RESOLVED` via `/__export__domain.markdown.token_dependencies_resolved`

- Signature: `domain.markdown.token_dependencies_resolved(subject)`
- Module: `domain`
- Library: `domain.markdown.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/markdown_core.spec.md#LIB-DOMAIN-MD-001-023-DOMAIN-MARKDOWN-TOKEN-DEPENDENCIES-RESOLVED`
- Export Path: `/__export__domain.markdown.token_dependencies_resolved`

#### Summary

Contract export for `domain.markdown.token_dependencies_resolved`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.markdown.token_ownership_unique` {#symbol-domain_markdown_token_ownership_unique}

Contract-backed: `/specs/libraries/domain/markdown_core.spec.md#LIB-DOMAIN-MD-001-021-DOMAIN-MARKDOWN-TOKEN-OWNERSHIP-UNIQUE` via `/__export__domain.markdown.token_ownership_unique`

- Signature: `domain.markdown.token_ownership_unique(subject)`
- Module: `domain`
- Library: `domain.markdown.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/markdown_core.spec.md#LIB-DOMAIN-MD-001-021-DOMAIN-MARKDOWN-TOKEN-OWNERSHIP-UNIQUE`
- Export Path: `/__export__domain.markdown.token_ownership_unique`

#### Summary

Contract export for `domain.markdown.token_ownership_unique`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.markdown.token_present` {#symbol-domain_markdown_token_present}

Contract-backed: `/specs/libraries/domain/markdown_core.spec.md#LIB-DOMAIN-MD-001-017-DOMAIN-MARKDOWN-TOKEN-PRESENT` via `/__export__domain.markdown.token_present`

- Signature: `domain.markdown.token_present(subject, token)`
- Module: `domain`
- Library: `domain.markdown.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/markdown_core.spec.md#LIB-DOMAIN-MD-001-017-DOMAIN-MARKDOWN-TOKEN-PRESENT`
- Export Path: `/__export__domain.markdown.token_present`

#### Summary

Contract export for `domain.markdown.token_present`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |
| `token` | `any` | `true` | Input parameter `token`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>', 'token': '<token>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.markdown.tokens_all_present` {#symbol-domain_markdown_tokens_all_present}

Contract-backed: `/specs/libraries/domain/markdown_core.spec.md#LIB-DOMAIN-MD-001-019-DOMAIN-MARKDOWN-TOKENS-ALL-PRESENT` via `/__export__domain.markdown.tokens_all_present`

- Signature: `domain.markdown.tokens_all_present(subject, tokens)`
- Module: `domain`
- Library: `domain.markdown.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/markdown_core.spec.md#LIB-DOMAIN-MD-001-019-DOMAIN-MARKDOWN-TOKENS-ALL-PRESENT`
- Export Path: `/__export__domain.markdown.tokens_all_present`

#### Summary

Contract export for `domain.markdown.tokens_all_present`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |
| `tokens` | `any` | `true` | Input parameter `tokens`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>', 'tokens': '<tokens>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.meta.case_id_eq` {#symbol-domain_meta_case_id_eq}

Contract-backed: `/specs/libraries/domain/meta_core.spec.md#LIB-DOMAIN-META-001-001-DOMAIN-META-CASE-ID-EQ` via `/__export__domain.meta.case_id_eq`

- Signature: `domain.meta.case_id_eq(meta, case_id)`
- Module: `domain`
- Library: `domain.meta.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/meta_core.spec.md#LIB-DOMAIN-META-001-001-DOMAIN-META-CASE-ID-EQ`
- Export Path: `/__export__domain.meta.case_id_eq`

#### Summary

Contract export for `domain.meta.case_id_eq`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `meta` | `any` | `true` | Input parameter `meta`. |  |
| `case_id` | `any` | `true` | Input parameter `case_id`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'meta': '<meta>', 'case_id': '<case_id>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.meta.has_artifact_target` {#symbol-domain_meta_has_artifact_target}

Contract-backed: `/specs/libraries/domain/meta_core.spec.md#LIB-DOMAIN-META-001-002-DOMAIN-META-HAS-ARTIFACT-TARGET` via `/__export__domain.meta.has_artifact_target`

- Signature: `domain.meta.has_artifact_target(meta, target_name)`
- Module: `domain`
- Library: `domain.meta.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/meta_core.spec.md#LIB-DOMAIN-META-001-002-DOMAIN-META-HAS-ARTIFACT-TARGET`
- Export Path: `/__export__domain.meta.has_artifact_target`

#### Summary

Contract export for `domain.meta.has_artifact_target`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `meta` | `any` | `true` | Input parameter `meta`. |  |
| `target_name` | `any` | `true` | Input parameter `target_name`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'meta': '<meta>', 'target_name': '<target_name>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.os.env_has` {#symbol-domain_os_env_has}

Contract-backed: `/specs/libraries/domain/os_core.spec.md#LIB-DOMAIN-OS-001-003-DOMAIN-OS-ENV-HAS` via `/__export__domain.os.env_has`

- Signature: `domain.os.env_has(key)`
- Module: `domain`
- Library: `domain.os.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/os_core.spec.md#LIB-DOMAIN-OS-001-003-DOMAIN-OS-ENV-HAS`
- Export Path: `/__export__domain.os.env_has`

#### Summary

Contract export for `domain.os.env_has`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `key` | `any` | `true` | Input parameter `key`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'key': '<key>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.os.exec_capture_code` {#symbol-domain_os_exec_capture_code}

Contract-backed: `/specs/libraries/domain/os_core.spec.md#LIB-DOMAIN-OS-001-002-DOMAIN-OS-EXEC-CAPTURE-CODE` via `/__export__domain.os.exec_capture_code`

- Signature: `domain.os.exec_capture_code(command, timeout_ms, expected_code)`
- Module: `domain`
- Library: `domain.os.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/os_core.spec.md#LIB-DOMAIN-OS-001-002-DOMAIN-OS-EXEC-CAPTURE-CODE`
- Export Path: `/__export__domain.os.exec_capture_code`

#### Summary

Contract export for `domain.os.exec_capture_code`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `command` | `any` | `true` | Input parameter `command`. |  |
| `timeout_ms` | `any` | `true` | Input parameter `timeout_ms`. |  |
| `expected_code` | `any` | `true` | Input parameter `expected_code`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'command': '<command>', 'timeout_ms': '<timeout_ms>', 'expected_code': '<expected_code>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.os.exec_ok` {#symbol-domain_os_exec_ok}

Contract-backed: `/specs/libraries/domain/os_core.spec.md#LIB-DOMAIN-OS-001-001-DOMAIN-OS-EXEC-OK` via `/__export__domain.os.exec_ok`

- Signature: `domain.os.exec_ok(command, timeout_ms)`
- Module: `domain`
- Library: `domain.os.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/os_core.spec.md#LIB-DOMAIN-OS-001-001-DOMAIN-OS-EXEC-OK`
- Export Path: `/__export__domain.os.exec_ok`

#### Summary

Contract export for `domain.os.exec_ok`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `command` | `any` | `true` | Input parameter `command`. |  |
| `timeout_ms` | `any` | `true` | Input parameter `timeout_ms`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'command': '<command>', 'timeout_ms': '<timeout_ms>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.path.eq` {#symbol-domain_path_eq}

Contract-backed: `/specs/libraries/domain/path_core.spec.md#LIB-DOMAIN-PATH-001-002-DOMAIN-PATH-EQ` via `/__export__domain.path.eq`

- Signature: `domain.path.eq(left, right)`
- Module: `domain`
- Library: `domain.path.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/path_core.spec.md#LIB-DOMAIN-PATH-001-002-DOMAIN-PATH-EQ`
- Export Path: `/__export__domain.path.eq`

#### Summary

Contract export for `domain.path.eq`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `left` | `any` | `true` | Input parameter `left`. |  |
| `right` | `any` | `true` | Input parameter `right`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'left': '<left>', 'right': '<right>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.path.is_in_docs` {#symbol-domain_path_is_in_docs}

Contract-backed: `/specs/libraries/domain/path_core.spec.md#LIB-DOMAIN-PATH-001-004-DOMAIN-PATH-IS-IN-DOCS` via `/__export__domain.path.is_in_docs`

- Signature: `domain.path.is_in_docs(path)`
- Module: `domain`
- Library: `domain.path.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/path_core.spec.md#LIB-DOMAIN-PATH-001-004-DOMAIN-PATH-IS-IN-DOCS`
- Export Path: `/__export__domain.path.is_in_docs`

#### Summary

Contract export for `domain.path.is_in_docs`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `path` | `any` | `true` | Input parameter `path`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'path': '<path>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.path.is_spec_md` {#symbol-domain_path_is_spec_md}

Contract-backed: `/specs/libraries/domain/path_core.spec.md#LIB-DOMAIN-PATH-001-003-DOMAIN-PATH-IS-SPEC-MD` via `/__export__domain.path.is_spec_md`

- Signature: `domain.path.is_spec_md(path)`
- Module: `domain`
- Library: `domain.path.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/path_core.spec.md#LIB-DOMAIN-PATH-001-003-DOMAIN-PATH-IS-SPEC-MD`
- Export Path: `/__export__domain.path.is_spec_md`

#### Summary

Contract export for `domain.path.is_spec_md`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `path` | `any` | `true` | Input parameter `path`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'path': '<path>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.path.normalize` {#symbol-domain_path_normalize}

Contract-backed: `/specs/libraries/domain/path_core.spec.md#LIB-DOMAIN-PATH-001-001-DOMAIN-PATH-NORMALIZE` via `/__export__domain.path.normalize`

- Signature: `domain.path.normalize(path)`
- Module: `domain`
- Library: `domain.path.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/path_core.spec.md#LIB-DOMAIN-PATH-001-001-DOMAIN-PATH-NORMALIZE`
- Export Path: `/__export__domain.path.normalize`

#### Summary

Contract export for `domain.path.normalize`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `path` | `any` | `true` | Input parameter `path`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'path': '<path>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.path.sorted` {#symbol-domain_path_sorted}

Contract-backed: `/specs/libraries/domain/path_core.spec.md#LIB-DOMAIN-PATH-001-005-DOMAIN-PATH-SORTED` via `/__export__domain.path.sorted`

- Signature: `domain.path.sorted(paths)`
- Module: `domain`
- Library: `domain.path.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/path_core.spec.md#LIB-DOMAIN-PATH-001-005-DOMAIN-PATH-SORTED`
- Export Path: `/__export__domain.path.sorted`

#### Summary

Contract export for `domain.path.sorted`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `paths` | `any` | `true` | Input parameter `paths`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'paths': '<paths>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.process.exec_capture_ex_code` {#symbol-domain_process_exec_capture_ex_code}

Contract-backed: `/specs/libraries/domain/process_core.spec.md#LIB-DOMAIN-PROCESS-001-001-DOMAIN-PROCESS-EXEC-CAPTURE-EX-CODE` via `/__export__domain.process.exec_capture_ex_code`

- Signature: `domain.process.exec_capture_ex_code(command, options)`
- Module: `domain`
- Library: `domain.process.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/process_core.spec.md#LIB-DOMAIN-PROCESS-001-001-DOMAIN-PROCESS-EXEC-CAPTURE-EX-CODE`
- Export Path: `/__export__domain.process.exec_capture_ex_code`

#### Summary

Contract export for `domain.process.exec_capture_ex_code`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `command` | `any` | `true` | Input parameter `command`. |  |
| `options` | `any` | `true` | Input parameter `options`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'command': '<command>', 'options': '<options>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.repo.walk_matching` {#symbol-domain_repo_walk_matching}

Contract-backed: `/specs/libraries/domain/repo_core.spec.md#LIB-DOMAIN-REPO-001-001-DOMAIN-REPO-WALK-MATCHING` via `/__export__domain.repo.walk_matching`

- Signature: `domain.repo.walk_matching(root, pattern)`
- Module: `domain`
- Library: `domain.repo.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/repo_core.spec.md#LIB-DOMAIN-REPO-001-001-DOMAIN-REPO-WALK-MATCHING`
- Export Path: `/__export__domain.repo.walk_matching`

#### Summary

Contract export for `domain.repo.walk_matching`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `root` | `any` | `true` | Input parameter `root`. |  |
| `pattern` | `any` | `true` | Input parameter `pattern`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'root': '<root>', 'pattern': '<pattern>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.yaml.parse_get_or` {#symbol-domain_yaml_parse_get_or}

Contract-backed: `/specs/libraries/domain/yaml_core.spec.md#LIB-DOMAIN-YAML-001-001-DOMAIN-YAML-PARSE-GET-OR` via `/__export__domain.yaml.parse_get_or`

- Signature: `domain.yaml.parse_get_or(yaml_text, path_segments, fallback)`
- Module: `domain`
- Library: `domain.yaml.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/yaml_core.spec.md#LIB-DOMAIN-YAML-001-001-DOMAIN-YAML-PARSE-GET-OR`
- Export Path: `/__export__domain.yaml.parse_get_or`

#### Summary

Contract export for `domain.yaml.parse_get_or`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `yaml_text` | `any` | `true` | Input parameter `yaml_text`. |  |
| `path_segments` | `any` | `true` | Input parameter `path_segments`. |  |
| `fallback` | `any` | `true` | Input parameter `fallback`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'yaml_text': '<yaml_text>', 'path_segments': '<path_segments>', 'fallback': '<fallback>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `domain.yaml.stringify` {#symbol-domain_yaml_stringify}

Contract-backed: `/specs/libraries/domain/yaml_core.spec.md#LIB-DOMAIN-YAML-001-002-DOMAIN-YAML-STRINGIFY` via `/__export__domain.yaml.stringify`

- Signature: `domain.yaml.stringify(value)`
- Module: `domain`
- Library: `domain.yaml.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/yaml_core.spec.md#LIB-DOMAIN-YAML-001-002-DOMAIN-YAML-STRINGIFY`
- Export Path: `/__export__domain.yaml.stringify`

#### Summary

Contract export for `domain.yaml.stringify`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `value` | `any` | `true` | Input parameter `value`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'value': '<value>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `make.has_target` {#symbol-make_has_target}

Contract-backed: `/specs/libraries/domain/make_core.spec.md#LIB-DOMAIN-MAKE-001` via `/__export__make.has_target`

- Signature: `make.has_target(subject, target)`
- Module: `domain`
- Library: `domain.make.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/make_core.spec.md#LIB-DOMAIN-MAKE-001`
- Export Path: `/__export__make.has_target`

#### Summary

Contract export for `make.has_target`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |
| `target` | `any` | `true` | Input parameter `target`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>', 'target': '<target>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `markdown._context` {#symbol-markdown__context}

Contract-backed: `/specs/libraries/domain/markdown_core.spec.md#LIB-DOMAIN-MD-001-001-DOMAIN-MARKDOWN-HAS-HEADING` via `/__export__markdown._context`

- Signature: `markdown._context(subject)`
- Module: `domain`
- Library: `domain.markdown.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/markdown_core.spec.md#LIB-DOMAIN-MD-001-001-DOMAIN-MARKDOWN-HAS-HEADING`
- Export Path: `/__export__markdown._context`

#### Summary

Contract export for `markdown._context`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `markdown._headings` {#symbol-markdown__headings}

Contract-backed: `/specs/libraries/domain/markdown_core.spec.md#LIB-DOMAIN-MD-001-001-DOMAIN-MARKDOWN-HAS-HEADING` via `/__export__markdown._headings`

- Signature: `markdown._headings(subject)`
- Module: `domain`
- Library: `domain.markdown.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/markdown_core.spec.md#LIB-DOMAIN-MD-001-001-DOMAIN-MARKDOWN-HAS-HEADING`
- Export Path: `/__export__markdown._headings`

#### Summary

Contract export for `markdown._headings`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `markdown._links` {#symbol-markdown__links}

Contract-backed: `/specs/libraries/domain/markdown_core.spec.md#LIB-DOMAIN-MD-001-001-DOMAIN-MARKDOWN-HAS-HEADING` via `/__export__markdown._links`

- Signature: `markdown._links(subject)`
- Module: `domain`
- Library: `domain.markdown.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/markdown_core.spec.md#LIB-DOMAIN-MD-001-001-DOMAIN-MARKDOWN-HAS-HEADING`
- Export Path: `/__export__markdown._links`

#### Summary

Contract export for `markdown._links`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `markdown._text` {#symbol-markdown__text}

Contract-backed: `/specs/libraries/domain/markdown_core.spec.md#LIB-DOMAIN-MD-001-001-DOMAIN-MARKDOWN-HAS-HEADING` via `/__export__markdown._text`

- Signature: `markdown._text(subject)`
- Module: `domain`
- Library: `domain.markdown.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/markdown_core.spec.md#LIB-DOMAIN-MD-001-001-DOMAIN-MARKDOWN-HAS-HEADING`
- Export Path: `/__export__markdown._text`

#### Summary

Contract export for `markdown._text`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `markdown._token_dependencies` {#symbol-markdown__token_dependencies}

Contract-backed: `/specs/libraries/domain/markdown_core.spec.md#LIB-DOMAIN-MD-001-001-DOMAIN-MARKDOWN-HAS-HEADING` via `/__export__markdown._token_dependencies`

- Signature: `markdown._token_dependencies(subject)`
- Module: `domain`
- Library: `domain.markdown.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/markdown_core.spec.md#LIB-DOMAIN-MD-001-001-DOMAIN-MARKDOWN-HAS-HEADING`
- Export Path: `/__export__markdown._token_dependencies`

#### Summary

Contract export for `markdown._token_dependencies`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `markdown._token_owners` {#symbol-markdown__token_owners}

Contract-backed: `/specs/libraries/domain/markdown_core.spec.md#LIB-DOMAIN-MD-001-001-DOMAIN-MARKDOWN-HAS-HEADING` via `/__export__markdown._token_owners`

- Signature: `markdown._token_owners(subject)`
- Module: `domain`
- Library: `domain.markdown.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/markdown_core.spec.md#LIB-DOMAIN-MD-001-001-DOMAIN-MARKDOWN-HAS-HEADING`
- Export Path: `/__export__markdown._token_owners`

#### Summary

Contract export for `markdown._token_owners`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `markdown._tokens_map` {#symbol-markdown__tokens_map}

Contract-backed: `/specs/libraries/domain/markdown_core.spec.md#LIB-DOMAIN-MD-001-001-DOMAIN-MARKDOWN-HAS-HEADING` via `/__export__markdown._tokens_map`

- Signature: `markdown._tokens_map(subject)`
- Module: `domain`
- Library: `domain.markdown.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/markdown_core.spec.md#LIB-DOMAIN-MD-001-001-DOMAIN-MARKDOWN-HAS-HEADING`
- Export Path: `/__export__markdown._tokens_map`

#### Summary

Contract export for `markdown._tokens_map`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `php.is_assoc_projection` {#symbol-php_is_assoc_projection}

Contract-backed: `/specs/libraries/domain/php_core.spec.md#LIB-DOMAIN-PHP-001` via `/__export__php.is_assoc_projection`

- Signature: `php.is_assoc_projection(subject)`
- Module: `domain`
- Library: `domain.php.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/php_core.spec.md#LIB-DOMAIN-PHP-001`
- Export Path: `/__export__php.is_assoc_projection`

#### Summary

Contract export for `php.is_assoc_projection`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `py.is_tuple_projection` {#symbol-py_is_tuple_projection}

Contract-backed: `/specs/libraries/domain/python_core.spec.md#LIB-DOMAIN-PY-001` via `/__export__py.is_tuple_projection`

- Signature: `py.is_tuple_projection(subject)`
- Module: `domain`
- Library: `domain.python.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/domain/python_core.spec.md#LIB-DOMAIN-PY-001`
- Export Path: `/__export__py.is_tuple_projection`

#### Summary

Contract export for `py.is_tuple_projection`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `impl.assert.contains` {#symbol-impl_assert_contains}

Contract-backed: `/specs/libraries/impl/assertion_core.spec.md#LIB-IMPL-ASSERT-001-001-IMPL-ASSERT-CONTAINS` via `/__export__impl.assert.contains`

- Signature: `impl.assert.contains(subject, token)`
- Module: `impl`
- Library: `impl.assertion.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/impl/assertion_core.spec.md#LIB-IMPL-ASSERT-001-001-IMPL-ASSERT-CONTAINS`
- Export Path: `/__export__impl.assert.contains`

#### Summary

Contract export for `impl.assert.contains`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |
| `token` | `any` | `true` | Input parameter `token`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>', 'token': '<token>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `impl.assert.json_type` {#symbol-impl_assert_json_type}

Contract-backed: `/specs/libraries/impl/assertion_core.spec.md#LIB-IMPL-ASSERT-001-003-IMPL-ASSERT-JSON-TYPE` via `/__export__impl.assert.json_type`

- Signature: `impl.assert.json_type(subject, type_name)`
- Module: `impl`
- Library: `impl.assertion.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/impl/assertion_core.spec.md#LIB-IMPL-ASSERT-001-003-IMPL-ASSERT-JSON-TYPE`
- Export Path: `/__export__impl.assert.json_type`

#### Summary

Contract export for `impl.assert.json_type`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |
| `type_name` | `any` | `true` | Input parameter `type_name`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>', 'type_name': '<type_name>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `impl.assert.regex` {#symbol-impl_assert_regex}

Contract-backed: `/specs/libraries/impl/assertion_core.spec.md#LIB-IMPL-ASSERT-001-002-IMPL-ASSERT-REGEX` via `/__export__impl.assert.regex`

- Signature: `impl.assert.regex(subject, pattern)`
- Module: `impl`
- Library: `impl.assertion.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/impl/assertion_core.spec.md#LIB-IMPL-ASSERT-001-002-IMPL-ASSERT-REGEX`
- Export Path: `/__export__impl.assert.regex`

#### Summary

Contract export for `impl.assert.regex`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |
| `pattern` | `any` | `true` | Input parameter `pattern`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>', 'pattern': '<pattern>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `path.basename` {#symbol-path_basename}

Contract-backed: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-003-PATH-BASENAME` via `/__export__path.basename`

- Signature: `path.basename(path)`
- Module: `path`
- Library: `path.path.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-003-PATH-BASENAME`
- Export Path: `/__export__path.basename`

#### Summary

Contract export for `path.basename`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `path` | `any` | `true` | Input parameter `path`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'path': '<path>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `path.dirname` {#symbol-path_dirname}

Contract-backed: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-001-PATH-NORMALIZE-SLASHES` via `/__export__path.dirname`

- Signature: `path.dirname(path)`
- Module: `path`
- Library: `path.path.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-001-PATH-NORMALIZE-SLASHES`
- Export Path: `/__export__path.dirname`

#### Summary

Contract export for `path.dirname`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `path` | `any` | `true` | Input parameter `path`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'path': '<path>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `path.dirname` {#symbol-path_dirname}

Contract-backed: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-002-PATH-SEGMENTS` via `/__export__path.dirname`

- Signature: `path.dirname(path)`
- Module: `path`
- Library: `path.path.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-002-PATH-SEGMENTS`
- Export Path: `/__export__path.dirname`

#### Summary

Contract export for `path.dirname`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `path` | `any` | `true` | Input parameter `path`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'path': '<path>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `path.dirname` {#symbol-path_dirname}

Contract-backed: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-003-PATH-BASENAME` via `/__export__path.dirname`

- Signature: `path.dirname(path)`
- Module: `path`
- Library: `path.path.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-003-PATH-BASENAME`
- Export Path: `/__export__path.dirname`

#### Summary

Contract export for `path.dirname`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `path` | `any` | `true` | Input parameter `path`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'path': '<path>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `path.dirname` {#symbol-path_dirname}

Contract-backed: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-004-PATH-EXTENSION` via `/__export__path.dirname`

- Signature: `path.dirname(path)`
- Module: `path`
- Library: `path.path.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-004-PATH-EXTENSION`
- Export Path: `/__export__path.dirname`

#### Summary

Contract export for `path.dirname`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `path` | `any` | `true` | Input parameter `path`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'path': '<path>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `path.extension` {#symbol-path_extension}

Contract-backed: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-004-PATH-EXTENSION` via `/__export__path.extension`

- Signature: `path.extension(path)`
- Module: `path`
- Library: `path.path.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-004-PATH-EXTENSION`
- Export Path: `/__export__path.extension`

#### Summary

Contract export for `path.extension`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `path` | `any` | `true` | Input parameter `path`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'path': '<path>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `path.has_extension` {#symbol-path_has_extension}

Contract-backed: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-001-PATH-NORMALIZE-SLASHES` via `/__export__path.has_extension`

- Signature: `path.has_extension(path, ext)`
- Module: `path`
- Library: `path.path.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-001-PATH-NORMALIZE-SLASHES`
- Export Path: `/__export__path.has_extension`

#### Summary

Contract export for `path.has_extension`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `path` | `any` | `true` | Input parameter `path`. |  |
| `ext` | `any` | `true` | Input parameter `ext`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'path': '<path>', 'ext': '<ext>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `path.has_extension` {#symbol-path_has_extension}

Contract-backed: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-002-PATH-SEGMENTS` via `/__export__path.has_extension`

- Signature: `path.has_extension(path, ext)`
- Module: `path`
- Library: `path.path.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-002-PATH-SEGMENTS`
- Export Path: `/__export__path.has_extension`

#### Summary

Contract export for `path.has_extension`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `path` | `any` | `true` | Input parameter `path`. |  |
| `ext` | `any` | `true` | Input parameter `ext`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'path': '<path>', 'ext': '<ext>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `path.has_extension` {#symbol-path_has_extension}

Contract-backed: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-003-PATH-BASENAME` via `/__export__path.has_extension`

- Signature: `path.has_extension(path, ext)`
- Module: `path`
- Library: `path.path.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-003-PATH-BASENAME`
- Export Path: `/__export__path.has_extension`

#### Summary

Contract export for `path.has_extension`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `path` | `any` | `true` | Input parameter `path`. |  |
| `ext` | `any` | `true` | Input parameter `ext`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'path': '<path>', 'ext': '<ext>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `path.has_extension` {#symbol-path_has_extension}

Contract-backed: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-004-PATH-EXTENSION` via `/__export__path.has_extension`

- Signature: `path.has_extension(path, ext)`
- Module: `path`
- Library: `path.path.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-004-PATH-EXTENSION`
- Export Path: `/__export__path.has_extension`

#### Summary

Contract export for `path.has_extension`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `path` | `any` | `true` | Input parameter `path`. |  |
| `ext` | `any` | `true` | Input parameter `ext`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'path': '<path>', 'ext': '<ext>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `path.is_under` {#symbol-path_is_under}

Contract-backed: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-001-PATH-NORMALIZE-SLASHES` via `/__export__path.is_under`

- Signature: `path.is_under(path, prefix)`
- Module: `path`
- Library: `path.path.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-001-PATH-NORMALIZE-SLASHES`
- Export Path: `/__export__path.is_under`

#### Summary

Contract export for `path.is_under`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `path` | `any` | `true` | Input parameter `path`. |  |
| `prefix` | `any` | `true` | Input parameter `prefix`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'path': '<path>', 'prefix': '<prefix>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `path.is_under` {#symbol-path_is_under}

Contract-backed: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-002-PATH-SEGMENTS` via `/__export__path.is_under`

- Signature: `path.is_under(path, prefix)`
- Module: `path`
- Library: `path.path.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-002-PATH-SEGMENTS`
- Export Path: `/__export__path.is_under`

#### Summary

Contract export for `path.is_under`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `path` | `any` | `true` | Input parameter `path`. |  |
| `prefix` | `any` | `true` | Input parameter `prefix`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'path': '<path>', 'prefix': '<prefix>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `path.is_under` {#symbol-path_is_under}

Contract-backed: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-003-PATH-BASENAME` via `/__export__path.is_under`

- Signature: `path.is_under(path, prefix)`
- Module: `path`
- Library: `path.path.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-003-PATH-BASENAME`
- Export Path: `/__export__path.is_under`

#### Summary

Contract export for `path.is_under`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `path` | `any` | `true` | Input parameter `path`. |  |
| `prefix` | `any` | `true` | Input parameter `prefix`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'path': '<path>', 'prefix': '<prefix>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `path.is_under` {#symbol-path_is_under}

Contract-backed: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-004-PATH-EXTENSION` via `/__export__path.is_under`

- Signature: `path.is_under(path, prefix)`
- Module: `path`
- Library: `path.path.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-004-PATH-EXTENSION`
- Export Path: `/__export__path.is_under`

#### Summary

Contract export for `path.is_under`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `path` | `any` | `true` | Input parameter `path`. |  |
| `prefix` | `any` | `true` | Input parameter `prefix`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'path': '<path>', 'prefix': '<prefix>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `path.matches` {#symbol-path_matches}

Contract-backed: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-001-PATH-NORMALIZE-SLASHES` via `/__export__path.matches`

- Signature: `path.matches(path, pattern)`
- Module: `path`
- Library: `path.path.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-001-PATH-NORMALIZE-SLASHES`
- Export Path: `/__export__path.matches`

#### Summary

Contract export for `path.matches`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `path` | `any` | `true` | Input parameter `path`. |  |
| `pattern` | `any` | `true` | Input parameter `pattern`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'path': '<path>', 'pattern': '<pattern>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `path.matches` {#symbol-path_matches}

Contract-backed: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-002-PATH-SEGMENTS` via `/__export__path.matches`

- Signature: `path.matches(path, pattern)`
- Module: `path`
- Library: `path.path.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-002-PATH-SEGMENTS`
- Export Path: `/__export__path.matches`

#### Summary

Contract export for `path.matches`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `path` | `any` | `true` | Input parameter `path`. |  |
| `pattern` | `any` | `true` | Input parameter `pattern`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'path': '<path>', 'pattern': '<pattern>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `path.matches` {#symbol-path_matches}

Contract-backed: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-003-PATH-BASENAME` via `/__export__path.matches`

- Signature: `path.matches(path, pattern)`
- Module: `path`
- Library: `path.path.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-003-PATH-BASENAME`
- Export Path: `/__export__path.matches`

#### Summary

Contract export for `path.matches`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `path` | `any` | `true` | Input parameter `path`. |  |
| `pattern` | `any` | `true` | Input parameter `pattern`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'path': '<path>', 'pattern': '<pattern>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `path.matches` {#symbol-path_matches}

Contract-backed: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-004-PATH-EXTENSION` via `/__export__path.matches`

- Signature: `path.matches(path, pattern)`
- Module: `path`
- Library: `path.path.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-004-PATH-EXTENSION`
- Export Path: `/__export__path.matches`

#### Summary

Contract export for `path.matches`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `path` | `any` | `true` | Input parameter `path`. |  |
| `pattern` | `any` | `true` | Input parameter `pattern`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'path': '<path>', 'pattern': '<pattern>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `path.normalize_slashes` {#symbol-path_normalize_slashes}

Contract-backed: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-001-PATH-NORMALIZE-SLASHES` via `/__export__path.normalize_slashes`

- Signature: `path.normalize_slashes(path)`
- Module: `path`
- Library: `path.path.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-001-PATH-NORMALIZE-SLASHES`
- Export Path: `/__export__path.normalize_slashes`

#### Summary

Contract export for `path.normalize_slashes`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `path` | `any` | `true` | Input parameter `path`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'path': '<path>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `path.segments` {#symbol-path_segments}

Contract-backed: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-002-PATH-SEGMENTS` via `/__export__path.segments`

- Signature: `path.segments(path)`
- Module: `path`
- Library: `path.path.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-002-PATH-SEGMENTS`
- Export Path: `/__export__path.segments`

#### Summary

Contract export for `path.segments`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `path` | `any` | `true` | Input parameter `path`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'path': '<path>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `path.trim_dot` {#symbol-path_trim_dot}

Contract-backed: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-001-PATH-NORMALIZE-SLASHES` via `/__export__path.trim_dot`

- Signature: `path.trim_dot(path)`
- Module: `path`
- Library: `path.path.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-001-PATH-NORMALIZE-SLASHES`
- Export Path: `/__export__path.trim_dot`

#### Summary

Contract export for `path.trim_dot`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `path` | `any` | `true` | Input parameter `path`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'path': '<path>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `path.trim_dot` {#symbol-path_trim_dot}

Contract-backed: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-002-PATH-SEGMENTS` via `/__export__path.trim_dot`

- Signature: `path.trim_dot(path)`
- Module: `path`
- Library: `path.path.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-002-PATH-SEGMENTS`
- Export Path: `/__export__path.trim_dot`

#### Summary

Contract export for `path.trim_dot`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `path` | `any` | `true` | Input parameter `path`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'path': '<path>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `path.trim_dot` {#symbol-path_trim_dot}

Contract-backed: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-003-PATH-BASENAME` via `/__export__path.trim_dot`

- Signature: `path.trim_dot(path)`
- Module: `path`
- Library: `path.path.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-003-PATH-BASENAME`
- Export Path: `/__export__path.trim_dot`

#### Summary

Contract export for `path.trim_dot`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `path` | `any` | `true` | Input parameter `path`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'path': '<path>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `path.trim_dot` {#symbol-path_trim_dot}

Contract-backed: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-004-PATH-EXTENSION` via `/__export__path.trim_dot`

- Signature: `path.trim_dot(path)`
- Module: `path`
- Library: `path.path.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/path/path_core.spec.md#LIB-PATH-001-004-PATH-EXTENSION`
- Export Path: `/__export__path.trim_dot`

#### Summary

Contract export for `path.trim_dot`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `path` | `any` | `true` | Input parameter `path`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'path': '<path>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `policy.check_id_is` {#symbol-policy_check_id_is}

Contract-backed: `/specs/libraries/policy/policy_core.spec.md#LIB-POLICY-001` via `/__export__policy.check_id_is`

- Signature: `policy.check_id_is(subject, expected)`
- Module: `policy`
- Library: `policy.policy.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/policy/policy_core.spec.md#LIB-POLICY-001`
- Export Path: `/__export__policy.check_id_is`

#### Summary

Contract export for `policy.check_id_is`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |
| `expected` | `any` | `true` | Input parameter `expected`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>', 'expected': '<expected>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `policy.fail_when_has_violations` {#symbol-policy_fail_when_has_violations}

Contract-backed: `/specs/libraries/policy/policy_core.spec.md#LIB-POLICY-001` via `/__export__policy.fail_when_has_violations`

- Signature: `policy.fail_when_has_violations(subject)`
- Module: `policy`
- Library: `policy.policy.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/policy/policy_core.spec.md#LIB-POLICY-001`
- Export Path: `/__export__policy.fail_when_has_violations`

#### Summary

Contract export for `policy.fail_when_has_violations`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `policy.metric_non_decrease` {#symbol-policy_metric_non_decrease}

Contract-backed: `/specs/libraries/policy/policy_metrics.spec.md#LIB-POLICY-002-001-POLICY-METRIC-NON-DECREASE` via `/__export__policy.metric_non_decrease`

- Signature: `policy.metric_non_decrease(subject, field, baseline_field, epsilon)`
- Module: `policy`
- Library: `policy.policy.metrics`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/policy/policy_metrics.spec.md#LIB-POLICY-002-001-POLICY-METRIC-NON-DECREASE`
- Export Path: `/__export__policy.metric_non_decrease`

#### Summary

Contract export for `policy.metric_non_decrease`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |
| `field` | `any` | `true` | Input parameter `field`. |  |
| `baseline_field` | `any` | `true` | Input parameter `baseline_field`. |  |
| `epsilon` | `any` | `true` | Input parameter `epsilon`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>', 'field': '<field>', 'baseline_field': '<baseline_field>', 'epsilon': '<epsilon>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `policy.metric_non_increase` {#symbol-policy_metric_non_increase}

Contract-backed: `/specs/libraries/policy/policy_metrics.spec.md#LIB-POLICY-002-002-POLICY-METRIC-NON-INCREASE` via `/__export__policy.metric_non_increase`

- Signature: `policy.metric_non_increase(subject, field, baseline_field, epsilon)`
- Module: `policy`
- Library: `policy.policy.metrics`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/policy/policy_metrics.spec.md#LIB-POLICY-002-002-POLICY-METRIC-NON-INCREASE`
- Export Path: `/__export__policy.metric_non_increase`

#### Summary

Contract export for `policy.metric_non_increase`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |
| `field` | `any` | `true` | Input parameter `field`. |  |
| `baseline_field` | `any` | `true` | Input parameter `baseline_field`. |  |
| `epsilon` | `any` | `true` | Input parameter `epsilon`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>', 'field': '<field>', 'baseline_field': '<baseline_field>', 'epsilon': '<epsilon>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `policy.pass_when_no_violations` {#symbol-policy_pass_when_no_violations}

Contract-backed: `/specs/libraries/policy/policy_core.spec.md#LIB-POLICY-001` via `/__export__policy.pass_when_no_violations`

- Signature: `policy.pass_when_no_violations(subject)`
- Module: `policy`
- Library: `policy.policy.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/policy/policy_core.spec.md#LIB-POLICY-001`
- Export Path: `/__export__policy.pass_when_no_violations`

#### Summary

Contract export for `policy.pass_when_no_violations`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -





### `policy.violation_count_is` {#symbol-policy_violation_count_is}

Contract-backed: `/specs/libraries/policy/policy_core.spec.md#LIB-POLICY-001` via `/__export__policy.violation_count_is`

- Signature: `policy.violation_count_is(subject, expected)`
- Module: `policy`
- Library: `policy.policy.core`
- Stability: `alpha`
- Owner: `spec_runner`
- Since: `v1`
- Source: `/specs/libraries/policy/policy_core.spec.md#LIB-POLICY-001`
- Export Path: `/__export__policy.violation_count_is`

#### Summary

Contract export for `policy.violation_count_is`.

#### Description

Auto-generated metadata stub. Replace with authored reference text.

#### Parameters

| name | type | required | description | default |
|---|---|---|---|---|
| `subject` | `any` | `true` | Input parameter `subject`. |  |
| `expected` | `any` | `true` | Input parameter `expected`. |  |


#### Returns

- type: `any`
- description: Result payload for this symbol.

#### Errors

| code | category | when |
|---|---|---|
| `SCHEMA_ERROR` | `schema` | Input payload does not satisfy contract shape requirements. |


#### Portability

- python: `true`
- php: `true`
- rust: `true`
- notes: Confirm per-runtime behavior and caveats.

#### Examples


- **Basic usage**
  - input: `{'subject': '<subject>', 'expected': '<expected>'}`
  - expected: `<result>`
  - notes: Replace with a concrete scenario.


#### See Also

- -
<!-- GENERATED:END library_symbol_reference -->
