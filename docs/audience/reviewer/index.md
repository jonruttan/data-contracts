# Reviewer Audience Docs

Audience-targeted documentation entries are rendered from executable spec metadata.

## [implicit_ids_v1.spec.md](/specs/03_conformance/cases/core/implicit_ids_v1.spec.md)
### implicit_ids_v1.doc.1.1.reviewer
- Location: `contracts[1].clauses[1].docs[]`
- Summary: contract docs id intentionally omitted (reviewer)
- Description:
  contract docs id intentionally omitted for reviewers checking correctness and risk.
  
  This entry is tailored for reviewer. Inputs are the contract parameters for this symbol, and output is the return payload from the underlying assertion/export.
  
  Caveats and errors include schema mismatches, contract binding failures, and environment-specific runtime behavior differences.

## [schema_case_validation.spec.md](/specs/03_conformance/cases/core/schema_case_validation.spec.md)
### schema_case_validation.doc.3.1.reviewer
- Location: `contracts[1].clauses[18].docs[]`
- Summary: missing status (reviewer)
- Description:
  missing status for reviewers checking correctness and risk.
  
  This entry is tailored for reviewer. Inputs are the contract parameters for this symbol, and output is the return payload from the underlying assertion/export.
  
  Caveats and errors include schema mismatches, contract binding failures, and environment-specific runtime behavior differences.

### schema_case_validation.doc.4.1.reviewer
- Location: `contracts[1].clauses[19].docs[]`
- Summary: invalid docs type (reviewer)
- Description:
  invalid docs type for reviewers checking correctness and risk.
  
  This entry is tailored for reviewer. Inputs are the contract parameters for this symbol, and output is the return payload from the underlying assertion/export.
  
  Caveats and errors include schema mismatches, contract binding failures, and environment-specific runtime behavior differences.

### schema_case_validation.doc.5.1.reviewer
- Location: `contracts[1].clauses[20].docs[]`
- Summary: docs entry one (reviewer)
- Description:
  docs entry one for reviewers checking correctness and risk.
  
  This entry is tailored for reviewer. Inputs are the contract parameters for this symbol, and output is the return payload from the underlying assertion/export.
  
  Caveats and errors include schema mismatches, contract binding failures, and environment-specific runtime behavior differences.

### schema_case_validation.doc.5.2.reviewer
- Location: `contracts[1].clauses[20].docs[]`
- Summary: docs entry two (reviewer)
- Description:
  docs entry two for reviewers checking correctness and risk.
  
  This entry is tailored for reviewer. Inputs are the contract parameters for this symbol, and output is the return payload from the underlying assertion/export.
  
  Caveats and errors include schema mismatches, contract binding failures, and environment-specific runtime behavior differences.

### schema_case_validation.doc.6.1.reviewer
- Location: `contracts[1].clauses[21].docs[]`
- Summary: docs entry with unknown key (reviewer)
- Description:
  docs entry with unknown key for reviewers checking correctness and risk.
  
  This entry is tailored for reviewer. Inputs are the contract parameters for this symbol, and output is the return payload from the underlying assertion/export.
  
  Caveats and errors include schema mismatches, contract binding failures, and environment-specific runtime behavior differences.

### schema_case_validation.doc.1.1.reviewer
- Location: `contracts[1].clauses[3].docs[]`
- Summary: schema export validation case (reviewer)
- Description:
  schema export validation case for reviewers checking correctness and risk.
  
  This entry is tailored for reviewer. Inputs are the contract parameters for this symbol, and output is the return payload from the underlying assertion/export.
  
  Caveats and errors include schema mismatches, contract binding failures, and environment-specific runtime behavior differences.

### schema_case_validation.doc.2.1.reviewer
- Location: `contracts[1].clauses[4].docs[]`
- Summary: schema export invalid imports case (reviewer)
- Description:
  schema export invalid imports case for reviewers checking correctness and risk.
  
  This entry is tailored for reviewer. Inputs are the contract parameters for this symbol, and output is the return payload from the underlying assertion/export.
  
  Caveats and errors include schema mismatches, contract binding failures, and environment-specific runtime behavior differences.

## [assertion_core.spec.md](/specs/05_libraries/conformance/assertion_core.spec.md)
### conf.json_type_is.doc.1.reviewer
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `conf.json_type_is`. (reviewer)
- Description:
  Contract export for `conf.json_type_is` for review and acceptance criteria.
  
  for reviewers evaluating correctness and compliance before release.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [chain_export_validation.spec.md](/specs/05_libraries/conformance/chain_export_validation.spec.md)
### bad.path.symbol.doc.1.reviewer
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `bad.path.symbol`. (reviewer)
- Description:
  Contract export for `bad.path.symbol` for review and acceptance criteria.
  
  for reviewers evaluating correctness and compliance before release.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [artifact_core.spec.md](/specs/05_libraries/domain/artifact_core.spec.md)
### domain.artifact.write_yaml.doc.1.reviewer
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `domain.artifact.write_yaml`. (reviewer)
- Description:
  Contract export for `domain.artifact.write_yaml` for review and acceptance criteria.
  
  for reviewers evaluating correctness and compliance before release.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [conformance_core.spec.md](/specs/05_libraries/domain/conformance_core.spec.md)
### domain.conformance.validate_report_errors.doc.1.reviewer
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `domain.conformance.validate_report_errors`. (reviewer)
- Description:
  Contract export for `domain.conformance.validate_report_errors` for review and acceptance criteria.
  
  for reviewers evaluating correctness and compliance before release.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [contract_set_core.spec.md](/specs/05_libraries/domain/contract_set_core.spec.md)
### domain.contract_set.applies_to_runners.doc.1.reviewer
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `domain.contract_set.applies_to_runners`. (reviewer)
- Description:
  Contract export for `domain.contract_set.applies_to_runners` for review and acceptance criteria.
  
  for reviewers evaluating correctness and compliance before release.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [fs_core.spec.md](/specs/05_libraries/domain/fs_core.spec.md)
### domain.fs.sort_spec_files.doc.1.reviewer
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `domain.fs.sort_spec_files`. (reviewer)
- Description:
  Contract export for `domain.fs.sort_spec_files` for review and acceptance criteria.
  
  for reviewers evaluating correctness and compliance before release.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [http_core.spec.md](/specs/05_libraries/domain/http_core.spec.md)
### domain.http.step_status_is.doc.1.reviewer
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `domain.http.step_status_is`. (reviewer)
- Description:
  Contract export for `domain.http.step_status_is` for review and acceptance criteria.
  
  for reviewers evaluating correctness and compliance before release.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [job_core.spec.md](/specs/05_libraries/domain/job_core.spec.md)
### domain.job.scan_bundle_has_result.doc.1.reviewer
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `domain.job.scan_bundle_has_result`. (reviewer)
- Description:
  Contract export for `domain.job.scan_bundle_has_result` for review and acceptance criteria.
  
  for reviewers evaluating correctness and compliance before release.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [make_core.spec.md](/specs/05_libraries/domain/make_core.spec.md)
### make.has_target.doc.1.reviewer
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `make.has_target`. (reviewer)
- Description:
  Contract export for `make.has_target` for review and acceptance criteria.
  
  for reviewers evaluating correctness and compliance before release.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [markdown_core.spec.md](/specs/05_libraries/domain/markdown_core.spec.md)
### domain.markdown.tokens_all_present.doc.1.reviewer
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `domain.markdown.tokens_all_present`. (reviewer)
- Description:
  Contract export for `domain.markdown.tokens_all_present` for review and acceptance criteria.
  
  for reviewers evaluating correctness and compliance before release.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [meta_core.spec.md](/specs/05_libraries/domain/meta_core.spec.md)
### domain.meta.has_artifact_target.doc.1.reviewer
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `domain.meta.has_artifact_target`. (reviewer)
- Description:
  Contract export for `domain.meta.has_artifact_target` for review and acceptance criteria.
  
  for reviewers evaluating correctness and compliance before release.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [os_core.spec.md](/specs/05_libraries/domain/os_core.spec.md)
### domain.os.exec_ok.doc.1.reviewer
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `domain.os.exec_ok`. (reviewer)
- Description:
  Contract export for `domain.os.exec_ok` for review and acceptance criteria.
  
  for reviewers evaluating correctness and compliance before release.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [domain/path_core.spec.md](/specs/05_libraries/domain/path_core.spec.md)
### domain.path.sorted.doc.1.reviewer
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `domain.path.sorted`. (reviewer)
- Description:
  Contract export for `domain.path.sorted` for review and acceptance criteria.
  
  for reviewers evaluating correctness and compliance before release.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [php_core.spec.md](/specs/05_libraries/domain/php_core.spec.md)
### php.is_assoc_projection.doc.1.reviewer
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `php.is_assoc_projection`. (reviewer)
- Description:
  Contract export for `php.is_assoc_projection` for review and acceptance criteria.
  
  for reviewers evaluating correctness and compliance before release.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [process_core.spec.md](/specs/05_libraries/domain/process_core.spec.md)
### domain.process.exec_capture_ex_code.doc.1.reviewer
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `domain.process.exec_capture_ex_code`. (reviewer)
- Description:
  Contract export for `domain.process.exec_capture_ex_code` for review and acceptance criteria.
  
  for reviewers evaluating correctness and compliance before release.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [python_core.spec.md](/specs/05_libraries/domain/python_core.spec.md)
### py.is_tuple_projection.doc.1.reviewer
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `py.is_tuple_projection`. (reviewer)
- Description:
  Contract export for `py.is_tuple_projection` for review and acceptance criteria.
  
  for reviewers evaluating correctness and compliance before release.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [repo_core.spec.md](/specs/05_libraries/domain/repo_core.spec.md)
### domain.repo.walk_matching.doc.1.reviewer
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `domain.repo.walk_matching`. (reviewer)
- Description:
  Contract export for `domain.repo.walk_matching` for review and acceptance criteria.
  
  for reviewers evaluating correctness and compliance before release.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [yaml_core.spec.md](/specs/05_libraries/domain/yaml_core.spec.md)
### domain.yaml.stringify.doc.1.reviewer
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `domain.yaml.stringify`. (reviewer)
- Description:
  Contract export for `domain.yaml.stringify` for review and acceptance criteria.
  
  for reviewers evaluating correctness and compliance before release.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [path/path_core.spec.md](/specs/05_libraries/path/path_core.spec.md)
### path.matches.doc.1.reviewer
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `path.matches`. (reviewer)
- Description:
  Contract export for `path.matches` for review and acceptance criteria.
  
  for reviewers evaluating correctness and compliance before release.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [policy_core.spec.md](/specs/05_libraries/policy/policy_core.spec.md)
### policy.violation_count_is.doc.1.reviewer
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `policy.violation_count_is`. (reviewer)
- Description:
  Contract export for `policy.violation_count_is` for review and acceptance criteria.
  
  for reviewers evaluating correctness and compliance before release.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

## [policy_metrics.spec.md](/specs/05_libraries/policy/policy_metrics.spec.md)
### policy.metric_non_increase.doc.1.reviewer
- Location: `harness.config.exports[1].docs[]`
- Summary: Contract export for `policy.metric_non_increase`. (reviewer)
- Description:
  Contract export for `policy.metric_non_increase` for review and acceptance criteria.
  
  for reviewers evaluating correctness and compliance before release.
  
  Expected input/output shape: inputs are declared in the contract and map to runtime parameters; output is the documented return payload.
  
  Error/caveat note: validation errors or environment-specific behavior should be reviewed for this audience.

