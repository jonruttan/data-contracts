# Implementer Audience Docs

Audience-targeted documentation entries are rendered from executable spec metadata.

## [implicit_ids_v1.spec.md](/specs/03_conformance/cases/core/implicit_ids_v1.spec.md)
### implicit_ids_v1.doc.1.1
- Location: `contracts[1].clauses[1].docs[]`
- Summary: contract docs id intentionally omitted
- Description:
  contract docs id intentionally omitted

### harness.docs[].1
- Location: `harness.docs[]`
- Summary: harness docs owner id omitted
- Description:
  harness docs owner id omitted

## [schema_case_validation.spec.md](/specs/03_conformance/cases/core/schema_case_validation.spec.md)
### schema_case_validation.doc.4.1
- Location: `contracts[1].clauses[19].docs[]`
- Summary: invalid docs type
- Description:
  invalid docs type

### schema_case_validation.doc.5.1
- Location: `contracts[1].clauses[20].docs[]`
- Summary: docs entry one
- Description:
  docs entry one

### schema_case_validation.doc.5.2
- Location: `contracts[1].clauses[20].docs[]`
- Summary: docs entry two
- Description:
  docs entry two

### schema_case_validation.doc.6.1
- Location: `contracts[1].clauses[21].docs[]`
- Summary: docs entry with unknown key
- Description:
  docs entry with unknown key

### schema_case_validation.doc.1.1
- Location: `contracts[1].clauses[3].docs[]`
- Summary: schema export validation case
- Description:
  Valid contract.export shape without unsupported top-level imports.

### schema_case_validation.doc.2.1
- Location: `contracts[1].clauses[4].docs[]`
- Summary: schema export invalid imports case
- Description:
  unsupported contract.export top-level imports must hard-fail in v1.

## [assertion_core.spec.md](/specs/05_libraries/conformance/assertion_core.spec.md)
### conf.json_type_is.doc.1
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `conf.json_type_is`.
- Description:
  Contract export for `conf.json_type_is` for implementer usage and runtime behavior.
  
  for implementation and runtime integration.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [chain_export_validation.spec.md](/specs/05_libraries/conformance/chain_export_validation.spec.md)
### bad.path.symbol.doc.1
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `bad.path.symbol`.
- Description:
  Contract export for `bad.path.symbol` for implementer usage and runtime behavior.
  
  for implementation and runtime integration.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [artifact_core.spec.md](/specs/05_libraries/domain/artifact_core.spec.md)
### domain.artifact.write_yaml.doc.1
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `domain.artifact.write_yaml`.
- Description:
  Contract export for `domain.artifact.write_yaml` for implementer usage and runtime behavior.
  
  for implementation and runtime integration.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [conformance_core.spec.md](/specs/05_libraries/domain/conformance_core.spec.md)
### domain.conformance.validate_report_errors.doc.1
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `domain.conformance.validate_report_errors`.
- Description:
  Contract export for `domain.conformance.validate_report_errors` for implementer usage and runtime behavior.
  
  for implementation and runtime integration.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [contract_set_core.spec.md](/specs/05_libraries/domain/contract_set_core.spec.md)
### domain.contract_set.applies_to_runners.doc.1
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `domain.contract_set.applies_to_runners`.
- Description:
  Contract export for `domain.contract_set.applies_to_runners` for implementer usage and runtime behavior.
  
  for implementation and runtime integration.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [fs_core.spec.md](/specs/05_libraries/domain/fs_core.spec.md)
### domain.fs.sort_spec_files.doc.1
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `domain.fs.sort_spec_files`.
- Description:
  Contract export for `domain.fs.sort_spec_files` for implementer usage and runtime behavior.
  
  for implementation and runtime integration.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [http_core.spec.md](/specs/05_libraries/domain/http_core.spec.md)
### domain.http.step_status_is.doc.1
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `domain.http.step_status_is`.
- Description:
  Contract export for `domain.http.step_status_is` for implementer usage and runtime behavior.
  
  for implementation and runtime integration.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [job_core.spec.md](/specs/05_libraries/domain/job_core.spec.md)
### domain.job.scan_bundle_has_result.doc.1
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `domain.job.scan_bundle_has_result`.
- Description:
  Contract export for `domain.job.scan_bundle_has_result` for implementer usage and runtime behavior.
  
  for implementation and runtime integration.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [make_core.spec.md](/specs/05_libraries/domain/make_core.spec.md)
### make.has_target.doc.1
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `make.has_target`.
- Description:
  Contract export for `make.has_target` for implementer usage and runtime behavior.
  
  for implementation and runtime integration.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [markdown_core.spec.md](/specs/05_libraries/domain/markdown_core.spec.md)
### domain.markdown.tokens_all_present.doc.1
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `domain.markdown.tokens_all_present`.
- Description:
  Contract export for `domain.markdown.tokens_all_present` for implementer usage and runtime behavior.
  
  for implementation and runtime integration.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [meta_core.spec.md](/specs/05_libraries/domain/meta_core.spec.md)
### domain.meta.has_artifact_target.doc.1
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `domain.meta.has_artifact_target`.
- Description:
  Contract export for `domain.meta.has_artifact_target` for implementer usage and runtime behavior.
  
  for implementation and runtime integration.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [os_core.spec.md](/specs/05_libraries/domain/os_core.spec.md)
### domain.os.exec_ok.doc.1
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `domain.os.exec_ok`.
- Description:
  Contract export for `domain.os.exec_ok` for implementer usage and runtime behavior.
  
  for implementation and runtime integration.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [domain/path_core.spec.md](/specs/05_libraries/domain/path_core.spec.md)
### domain.path.sorted.doc.1
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `domain.path.sorted`.
- Description:
  Contract export for `domain.path.sorted` for implementer usage and runtime behavior.
  
  for implementation and runtime integration.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [php_core.spec.md](/specs/05_libraries/domain/php_core.spec.md)
### php.is_assoc_projection.doc.1
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `php.is_assoc_projection`.
- Description:
  Contract export for `php.is_assoc_projection` for implementer usage and runtime behavior.
  
  for implementation and runtime integration.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [process_core.spec.md](/specs/05_libraries/domain/process_core.spec.md)
### domain.process.exec_capture_ex_code.doc.1
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `domain.process.exec_capture_ex_code`.
- Description:
  Contract export for `domain.process.exec_capture_ex_code` for implementer usage and runtime behavior.
  
  for implementation and runtime integration.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [python_core.spec.md](/specs/05_libraries/domain/python_core.spec.md)
### py.is_tuple_projection.doc.1
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `py.is_tuple_projection`.
- Description:
  Contract export for `py.is_tuple_projection` for implementer usage and runtime behavior.
  
  for implementation and runtime integration.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [repo_core.spec.md](/specs/05_libraries/domain/repo_core.spec.md)
### domain.repo.walk_matching.doc.1
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `domain.repo.walk_matching`.
- Description:
  Contract export for `domain.repo.walk_matching` for implementer usage and runtime behavior.
  
  for implementation and runtime integration.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [yaml_core.spec.md](/specs/05_libraries/domain/yaml_core.spec.md)
### domain.yaml.stringify.doc.1
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `domain.yaml.stringify`.
- Description:
  Contract export for `domain.yaml.stringify` for implementer usage and runtime behavior.
  
  for implementation and runtime integration.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [path/path_core.spec.md](/specs/05_libraries/path/path_core.spec.md)
### path.matches.doc.1
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `path.matches`.
- Description:
  Contract export for `path.matches` for implementer usage and runtime behavior.
  
  for implementation and runtime integration.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [policy_core.spec.md](/specs/05_libraries/policy/policy_core.spec.md)
### policy.violation_count_is.doc.1
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `policy.violation_count_is`.
- Description:
  Contract export for `policy.violation_count_is` for implementer usage and runtime behavior.
  
  for implementation and runtime integration.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [policy_metrics.spec.md](/specs/05_libraries/policy/policy_metrics.spec.md)
### policy.metric_non_increase.doc.1
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `policy.metric_non_increase`.
- Description:
  Contract export for `policy.metric_non_increase` for implementer usage and runtime behavior.
  
  for implementation and runtime integration.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

