# Reference Index

1. [implicit_ids_v1.spec.md](/specs/03_conformance/cases/core/implicit_ids_v1.spec.md)
   - **implicit_ids_v1.doc.1.1.governance**: contract docs id intentionally omitted (governance)

2. [schema_case_validation.spec.md](/specs/03_conformance/cases/core/schema_case_validation.spec.md)
   - **schema_case_validation.doc.1.1.governance**: schema export validation case (governance)
   - **schema_case_validation.doc.2.1.governance**: schema export invalid imports case (governance)
   - **schema_case_validation.doc.3.1.governance**: missing status (governance)
   - **schema_case_validation.doc.4.1.governance**: invalid docs type (governance)
   - **schema_case_validation.doc.5.1.governance**: docs entry one (governance)
   - **schema_case_validation.doc.5.2.governance**: docs entry two (governance)
   - **schema_case_validation.doc.6.1.governance**: docs entry with unknown key (governance)
   - **schema_case_validation.doc.9.1.governance**: schema registry assertions yaml input (governance)
   - **schema_case_validation.doc.11.1.governance**: schema text export (governance)

3. [assertion_core.spec.md](/specs/05_libraries/conformance/assertion_core.spec.md)
   - **conf.json_type_is.doc.1.governance**: Assert that a value is of the requested JSON schema type for governance auditability.
   - **conformance.assertion.core.governance**: Case `LIB-CONF-ASSERT-001` for `contract.export`. (governance)

4. [chain_export_validation.spec.md](/specs/05_libraries/conformance/chain_export_validation.spec.md)
   - **bad.path.symbol.doc.1.governance**: Validate chain-export failure signaling for an invalid or missing path symbol for governance checks.
   - **conformance.chain.export.validation.governance**: Case `BAD-EXPORT-PATH` for `contract.export`. (governance)

5. [artifact_core.spec.md](/specs/05_libraries/domain/artifact_core.spec.md)
   - **domain.artifact.write_yaml.doc.1.governance**: Persist a structured artifact payload as YAML for downstream consumers under governance.
   - **domain.artifact.core.governance**: Case `LIB-DOMAIN-ARTIFACT-001-001-DOMAIN-ARTIFACT-WRITE-YAML` for `contract.export`. (governance)

6. [conformance_core.spec.md](/specs/05_libraries/domain/conformance_core.spec.md)
   - **domain.conformance.validate_report_errors.doc.1.governance**: Validate conformance report errors and fail when reported issues violate governance expectations.
   - **domain.conformance.core.governance**: Case `LIB-DOMAIN-CONFORMANCE-001-000-DOMAIN-CONFORMANCE-ERROR-WHEN-FALSE` for `contract.export`. (governance)

7. [contract_set_core.spec.md](/specs/05_libraries/domain/contract_set_core.spec.md)
   - **domain.contract_set.applies_to_runners.doc.1.governance**: Evaluate whether a contract set should execute under the current runner for governance policy.
   - **domain.contract_set.core.governance**: Case `LIB-DOMAIN-CONTRACT-SET-001` for `contract.export`. (governance)

8. [fs_core.spec.md](/specs/05_libraries/domain/fs_core.spec.md)
   - **domain.fs.sort_spec_files.doc.1.governance**: Sort discovered spec files into stable, deterministic ordering for governance reproducibility.
   - **domain.fs.core.governance**: Case `LIB-DOMAIN-FS-001-001-DOMAIN-FS-IS-DOCS-SPEC-FILE` for `contract.export`. (governance)

9. [http_core.spec.md](/specs/05_libraries/domain/http_core.spec.md)
   - **domain.http.step_status_is.doc.1.governance**: Assert that a HTTP workflow step reports the expected status for governance review.
   - **domain.http.core.governance**: Case `LIB-DOMAIN-HTTP-001-001-DOMAIN-HTTP-STATUS` for `contract.export`. (governance)

10. [job_core.spec.md](/specs/05_libraries/domain/job_core.spec.md)
   - **domain.job.scan_bundle_has_result.doc.1.governance**: Verify job scan bundle output includes the expected result marker for governance checks.
   - **domain.job.core.governance**: Case `LIB-DOMAIN-JOB-001-000A-DOMAIN-JOB-SCAN-BUNDLE-HAS-RESULT` for `contract.export`. (governance)

11. [make_core.spec.md](/specs/05_libraries/domain/make_core.spec.md)
   - **make.has_target.doc.1.governance**: Check whether a Make target exists and is resolvable for governance control.
   - **domain.make.core.governance**: Case `LIB-DOMAIN-MAKE-001` for `contract.export`. (governance)

12. [markdown_core.spec.md](/specs/05_libraries/domain/markdown_core.spec.md)
   - **domain.markdown.tokens_all_present.doc.1.governance**: Assert required Markdown tokens appear in source markdown content for governance checks.
   - **domain.markdown.core.governance**: Case `LIB-DOMAIN-MD-001-001-DOMAIN-MARKDOWN-HAS-HEADING` for `contract.export`. (governance)

13. [meta_core.spec.md](/specs/05_libraries/domain/meta_core.spec.md)
   - **domain.meta.has_artifact_target.doc.1.governance**: Detect whether contract metadata declares an artifact target for governance.
   - **domain.meta.core.governance**: Case `LIB-DOMAIN-META-001-001-DOMAIN-META-CASE-ID-EQ` for `contract.export`. (governance)

14. [os_core.spec.md](/specs/05_libraries/domain/os_core.spec.md)
   - **domain.os.exec_ok.doc.1.governance**: Assert that an OS command execution completed successfully for governance review.
   - **domain.os.core.governance**: Case `LIB-DOMAIN-OS-001-001-DOMAIN-OS-EXEC-OK` for `contract.export`. (governance)

15. [path_core.spec.md](/specs/05_libraries/domain/path_core.spec.md)
   - **domain.path.sorted.doc.1.governance**: Return path inputs sorted in deterministic lexicographic order for governance.
   - **domain.path.core.governance**: Case `LIB-DOMAIN-PATH-001-001-DOMAIN-PATH-NORMALIZE` for `contract.export`. (governance)

16. [php_core.spec.md](/specs/05_libraries/domain/php_core.spec.md)
   - **php.is_assoc_projection.doc.1.governance**: Assert a PHP projection result is associative for governance.
   - **domain.php.core.governance**: Case `LIB-DOMAIN-PHP-001` for `contract.export`. (governance)

17. [process_core.spec.md](/specs/05_libraries/domain/process_core.spec.md)
   - **domain.process.exec_capture_ex_code.doc.1.governance**: Capture and assert process exit/exception code behavior for governance review.
   - **domain.process.core.governance**: Case `LIB-DOMAIN-PROCESS-001-001-DOMAIN-PROCESS-EXEC-CAPTURE-EX-CODE` for `contract.export`. (governance)

18. [python_core.spec.md](/specs/05_libraries/domain/python_core.spec.md)
   - **py.is_tuple_projection.doc.1.governance**: Assert that a Python projection result is tuple-shaped as expected for governance.
   - **domain.python.core.governance**: Case `LIB-DOMAIN-PY-001` for `contract.export`. (governance)

19. [repo_core.spec.md](/specs/05_libraries/domain/repo_core.spec.md)
   - **domain.repo.walk_matching.doc.1.governance**: Walk repository paths and return files matching configured selectors for governance.
   - **domain.repo.core.governance**: Case `LIB-DOMAIN-REPO-001-001-DOMAIN-REPO-WALK-MATCHING` for `contract.export`. (governance)

20. [yaml_core.spec.md](/specs/05_libraries/domain/yaml_core.spec.md)
   - **domain.yaml.stringify.doc.1.governance**: Serialize structured data into canonical YAML text for governance.
   - **domain.yaml.core.governance**: Case `LIB-DOMAIN-YAML-001-001-DOMAIN-YAML-PARSE-GET-OR` for `contract.export`. (governance)

21. [path_core.spec.md](/specs/05_libraries/path/path_core.spec.md)
   - **path.matches.doc.1.governance**: Evaluate whether path values satisfy the provided matcher rules for governance.
   - **path.path.core.governance**: Case `LIB-PATH-001-001-PATH-NORMALIZE-SLASHES` for `contract.export`. (governance)

22. [policy_core.spec.md](/specs/05_libraries/policy/policy_core.spec.md)
   - **policy.violation_count_is.doc.1.governance**: Assert the exact number of policy violations for governance.
   - **policy.policy.core.governance**: Case `LIB-POLICY-001` for `contract.export`. (governance)

23. [policy_metrics.spec.md](/specs/05_libraries/policy/policy_metrics.spec.md)
   - **policy.metric_non_increase.doc.1.governance**: Assert a policy metric does not increase compared to a baseline for governance.
   - **policy.policy.metrics.governance**: Case `LIB-POLICY-002-001-POLICY-METRIC-NON-DECREASE` for `contract.export`. (governance)

