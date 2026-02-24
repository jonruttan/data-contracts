# Auditor Audience Docs

Audience-targeted documentation entries are rendered from executable spec metadata.

## [implicit_ids_v1.spec.md](/specs/03_conformance/cases/core/implicit_ids_v1.spec.md)
### implicit_ids_v1.doc.1.1.auditor
- Location: `contracts[1].clauses[1].docs[]`
- Summary: contract docs id intentionally omitted (auditor)
- Description:
  contract docs id intentionally omitted for auditors validating evidence and traceability.
  
  This entry is tailored for auditor. Inputs are the contract parameters for this symbol, and output is the return payload from the underlying assertion/export.
  
  Caveats and errors include schema mismatches, contract binding failures, and environment-specific runtime behavior differences.

## [schema_case_validation.spec.md](/specs/03_conformance/cases/core/schema_case_validation.spec.md)
### schema_case_validation.doc.3.1.auditor
- Location: `contracts[1].clauses[18].docs[]`
- Summary: missing status (auditor)
- Description:
  missing status for auditors validating evidence and traceability.
  
  This entry is tailored for auditor. Inputs are the contract parameters for this symbol, and output is the return payload from the underlying assertion/export.
  
  Caveats and errors include schema mismatches, contract binding failures, and environment-specific runtime behavior differences.

### schema_case_validation.doc.4.1.auditor
- Location: `contracts[1].clauses[19].docs[]`
- Summary: invalid docs type (auditor)
- Description:
  invalid docs type for auditors validating evidence and traceability.
  
  This entry is tailored for auditor. Inputs are the contract parameters for this symbol, and output is the return payload from the underlying assertion/export.
  
  Caveats and errors include schema mismatches, contract binding failures, and environment-specific runtime behavior differences.

### schema_case_validation.doc.5.1.auditor
- Location: `contracts[1].clauses[20].docs[]`
- Summary: docs entry one (auditor)
- Description:
  docs entry one for auditors validating evidence and traceability.
  
  This entry is tailored for auditor. Inputs are the contract parameters for this symbol, and output is the return payload from the underlying assertion/export.
  
  Caveats and errors include schema mismatches, contract binding failures, and environment-specific runtime behavior differences.

### schema_case_validation.doc.5.2.auditor
- Location: `contracts[1].clauses[20].docs[]`
- Summary: docs entry two (auditor)
- Description:
  docs entry two for auditors validating evidence and traceability.
  
  This entry is tailored for auditor. Inputs are the contract parameters for this symbol, and output is the return payload from the underlying assertion/export.
  
  Caveats and errors include schema mismatches, contract binding failures, and environment-specific runtime behavior differences.

### schema_case_validation.doc.6.1.auditor
- Location: `contracts[1].clauses[21].docs[]`
- Summary: docs entry with unknown key (auditor)
- Description:
  docs entry with unknown key for auditors validating evidence and traceability.
  
  This entry is tailored for auditor. Inputs are the contract parameters for this symbol, and output is the return payload from the underlying assertion/export.
  
  Caveats and errors include schema mismatches, contract binding failures, and environment-specific runtime behavior differences.

### schema_case_validation.doc.1.1.auditor
- Location: `contracts[1].clauses[3].docs[]`
- Summary: schema export validation case (auditor)
- Description:
  schema export validation case for auditors validating evidence and traceability.
  
  This entry is tailored for auditor. Inputs are the contract parameters for this symbol, and output is the return payload from the underlying assertion/export.
  
  Caveats and errors include schema mismatches, contract binding failures, and environment-specific runtime behavior differences.

### schema_case_validation.doc.2.1.auditor
- Location: `contracts[1].clauses[4].docs[]`
- Summary: schema export invalid imports case (auditor)
- Description:
  schema export invalid imports case for auditors validating evidence and traceability.
  
  This entry is tailored for auditor. Inputs are the contract parameters for this symbol, and output is the return payload from the underlying assertion/export.
  
  Caveats and errors include schema mismatches, contract binding failures, and environment-specific runtime behavior differences.

## [assertion_core.spec.md](/specs/05_libraries/conformance/assertion_core.spec.md)
### conf.json_type_is.doc.1.auditor
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `conf.json_type_is`. (auditor)
- Description:
  Contract export for `conf.json_type_is` for evidence and audit-ready documentation.
  
  for auditors validating evidence for compliance and traceability.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [chain_export_validation.spec.md](/specs/05_libraries/conformance/chain_export_validation.spec.md)
### bad.path.symbol.doc.1.auditor
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `bad.path.symbol`. (auditor)
- Description:
  Contract export for `bad.path.symbol` for evidence and audit-ready documentation.
  
  for auditors validating evidence for compliance and traceability.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [artifact_core.spec.md](/specs/05_libraries/domain/artifact_core.spec.md)
### domain.artifact.write_yaml.doc.1.auditor
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `domain.artifact.write_yaml`. (auditor)
- Description:
  Contract export for `domain.artifact.write_yaml` for evidence and audit-ready documentation.
  
  for auditors validating evidence for compliance and traceability.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [conformance_core.spec.md](/specs/05_libraries/domain/conformance_core.spec.md)
### domain.conformance.validate_report_errors.doc.1.auditor
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `domain.conformance.validate_report_errors`. (auditor)
- Description:
  Contract export for `domain.conformance.validate_report_errors` for evidence and audit-ready documentation.
  
  for auditors validating evidence for compliance and traceability.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [contract_set_core.spec.md](/specs/05_libraries/domain/contract_set_core.spec.md)
### domain.contract_set.applies_to_runners.doc.1.auditor
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `domain.contract_set.applies_to_runners`. (auditor)
- Description:
  Contract export for `domain.contract_set.applies_to_runners` for evidence and audit-ready documentation.
  
  for auditors validating evidence for compliance and traceability.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [fs_core.spec.md](/specs/05_libraries/domain/fs_core.spec.md)
### domain.fs.sort_spec_files.doc.1.auditor
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `domain.fs.sort_spec_files`. (auditor)
- Description:
  Contract export for `domain.fs.sort_spec_files` for evidence and audit-ready documentation.
  
  for auditors validating evidence for compliance and traceability.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [http_core.spec.md](/specs/05_libraries/domain/http_core.spec.md)
### domain.http.step_status_is.doc.1.auditor
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `domain.http.step_status_is`. (auditor)
- Description:
  Contract export for `domain.http.step_status_is` for evidence and audit-ready documentation.
  
  for auditors validating evidence for compliance and traceability.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [job_core.spec.md](/specs/05_libraries/domain/job_core.spec.md)
### domain.job.scan_bundle_has_result.doc.1.auditor
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `domain.job.scan_bundle_has_result`. (auditor)
- Description:
  Contract export for `domain.job.scan_bundle_has_result` for evidence and audit-ready documentation.
  
  for auditors validating evidence for compliance and traceability.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [make_core.spec.md](/specs/05_libraries/domain/make_core.spec.md)
### make.has_target.doc.1.auditor
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `make.has_target`. (auditor)
- Description:
  Contract export for `make.has_target` for evidence and audit-ready documentation.
  
  for auditors validating evidence for compliance and traceability.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [markdown_core.spec.md](/specs/05_libraries/domain/markdown_core.spec.md)
### domain.markdown.tokens_all_present.doc.1.auditor
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `domain.markdown.tokens_all_present`. (auditor)
- Description:
  Contract export for `domain.markdown.tokens_all_present` for evidence and audit-ready documentation.
  
  for auditors validating evidence for compliance and traceability.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [meta_core.spec.md](/specs/05_libraries/domain/meta_core.spec.md)
### domain.meta.has_artifact_target.doc.1.auditor
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `domain.meta.has_artifact_target`. (auditor)
- Description:
  Contract export for `domain.meta.has_artifact_target` for evidence and audit-ready documentation.
  
  for auditors validating evidence for compliance and traceability.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [os_core.spec.md](/specs/05_libraries/domain/os_core.spec.md)
### domain.os.exec_ok.doc.1.auditor
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `domain.os.exec_ok`. (auditor)
- Description:
  Contract export for `domain.os.exec_ok` for evidence and audit-ready documentation.
  
  for auditors validating evidence for compliance and traceability.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [domain/path_core.spec.md](/specs/05_libraries/domain/path_core.spec.md)
### domain.path.sorted.doc.1.auditor
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `domain.path.sorted`. (auditor)
- Description:
  Contract export for `domain.path.sorted` for evidence and audit-ready documentation.
  
  for auditors validating evidence for compliance and traceability.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [php_core.spec.md](/specs/05_libraries/domain/php_core.spec.md)
### php.is_assoc_projection.doc.1.auditor
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `php.is_assoc_projection`. (auditor)
- Description:
  Contract export for `php.is_assoc_projection` for evidence and audit-ready documentation.
  
  for auditors validating evidence for compliance and traceability.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [process_core.spec.md](/specs/05_libraries/domain/process_core.spec.md)
### domain.process.exec_capture_ex_code.doc.1.auditor
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `domain.process.exec_capture_ex_code`. (auditor)
- Description:
  Contract export for `domain.process.exec_capture_ex_code` for evidence and audit-ready documentation.
  
  for auditors validating evidence for compliance and traceability.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [python_core.spec.md](/specs/05_libraries/domain/python_core.spec.md)
### py.is_tuple_projection.doc.1.auditor
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `py.is_tuple_projection`. (auditor)
- Description:
  Contract export for `py.is_tuple_projection` for evidence and audit-ready documentation.
  
  for auditors validating evidence for compliance and traceability.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [repo_core.spec.md](/specs/05_libraries/domain/repo_core.spec.md)
### domain.repo.walk_matching.doc.1.auditor
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `domain.repo.walk_matching`. (auditor)
- Description:
  Contract export for `domain.repo.walk_matching` for evidence and audit-ready documentation.
  
  for auditors validating evidence for compliance and traceability.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [yaml_core.spec.md](/specs/05_libraries/domain/yaml_core.spec.md)
### domain.yaml.stringify.doc.1.auditor
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `domain.yaml.stringify`. (auditor)
- Description:
  Contract export for `domain.yaml.stringify` for evidence and audit-ready documentation.
  
  for auditors validating evidence for compliance and traceability.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [path/path_core.spec.md](/specs/05_libraries/path/path_core.spec.md)
### path.matches.doc.1.auditor
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `path.matches`. (auditor)
- Description:
  Contract export for `path.matches` for evidence and audit-ready documentation.
  
  for auditors validating evidence for compliance and traceability.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [policy_core.spec.md](/specs/05_libraries/policy/policy_core.spec.md)
### policy.violation_count_is.doc.1.auditor
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `policy.violation_count_is`. (auditor)
- Description:
  Contract export for `policy.violation_count_is` for evidence and audit-ready documentation.
  
  for auditors validating evidence for compliance and traceability.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [policy_metrics.spec.md](/specs/05_libraries/policy/policy_metrics.spec.md)
### policy.metric_non_increase.doc.1.auditor
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `policy.metric_non_increase`. (auditor)
- Description:
  Contract export for `policy.metric_non_increase` for evidence and audit-ready documentation.
  
  for auditors validating evidence for compliance and traceability.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

