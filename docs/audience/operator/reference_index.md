# Reference Index

1. [implicit_ids_v1.spec.md](/specs/03_conformance/cases/core/implicit_ids_v1.spec.md)
   - **implicit_ids_v1.doc.1.1.operator**: contract docs id intentionally omitted (operator)

2. [schema_case_validation.spec.md](/specs/03_conformance/cases/core/schema_case_validation.spec.md)
   - **schema_case_validation.doc.1.1.operator**: schema export validation case (operator)
   - **schema_case_validation.doc.2.1.operator**: schema export invalid imports case (operator)
   - **schema_case_validation.doc.3.1.operator**: missing status (operator)
   - **schema_case_validation.doc.4.1.operator**: invalid docs type (operator)
   - **schema_case_validation.doc.5.1.operator**: docs entry one (operator)
   - **schema_case_validation.doc.5.2.operator**: docs entry two (operator)
   - **schema_case_validation.doc.6.1.operator**: docs entry with unknown key (operator)
   - **schema_case_validation.doc.9.1.operator**: schema registry assertions yaml input (operator)
   - **schema_case_validation.doc.11.1.operator**: schema text export (operator)

3. [assertion_core.spec.md](/specs/05_libraries/conformance/assertion_core.spec.md)
   - **conf.json_type_is.doc.1.operator**: Assert that a value is of the requested JSON schema type for operator workflows.
   - **conformance.assertion.core.operator**: Case `LIB-CONF-ASSERT-001` for `contract.export`. (operator)

4. [chain_export_validation.spec.md](/specs/05_libraries/conformance/chain_export_validation.spec.md)
   - **bad.path.symbol.doc.1.operator**: Validate chain-export failure signaling for an invalid or missing path symbol in operator workflows.
   - **conformance.chain.export.validation.operator**: Case `BAD-EXPORT-PATH` for `contract.export`. (operator)

5. [artifact_core.spec.md](/specs/05_libraries/domain/artifact_core.spec.md)
   - **domain.artifact.write_yaml.doc.1.operator**: Persist a structured artifact payload as YAML for downstream consumers during operators.
   - **domain.artifact.core.operator**: Case `LIB-DOMAIN-ARTIFACT-001-001-DOMAIN-ARTIFACT-WRITE-YAML` for `contract.export`. (operator)

6. [conformance_core.spec.md](/specs/05_libraries/domain/conformance_core.spec.md)
   - **domain.conformance.validate_report_errors.doc.1.operator**: Validate conformance report errors and fail when reported issues violate expectations for operators.
   - **domain.conformance.core.operator**: Case `LIB-DOMAIN-CONFORMANCE-001-000-DOMAIN-CONFORMANCE-ERROR-WHEN-FALSE` for `contract.export`. (operator)

7. [contract_set_core.spec.md](/specs/05_libraries/domain/contract_set_core.spec.md)
   - **domain.contract_set.applies_to_runners.doc.1.operator**: Evaluate whether a contract set should execute under the current runner for operator workflows.
   - **domain.contract_set.core.operator**: Case `LIB-DOMAIN-CONTRACT-SET-001` for `contract.export`. (operator)

8. [fs_core.spec.md](/specs/05_libraries/domain/fs_core.spec.md)
   - **domain.fs.sort_spec_files.doc.1.operator**: Sort discovered spec files into stable, deterministic ordering for operators.
   - **domain.fs.core.operator**: Case `LIB-DOMAIN-FS-001-001-DOMAIN-FS-IS-DOCS-SPEC-FILE` for `contract.export`. (operator)

9. [http_core.spec.md](/specs/05_libraries/domain/http_core.spec.md)
   - **domain.http.step_status_is.doc.1.operator**: Assert that a HTTP workflow step reports the expected status for operators.
   - **domain.http.core.operator**: Case `LIB-DOMAIN-HTTP-001-001-DOMAIN-HTTP-STATUS` for `contract.export`. (operator)

10. [job_core.spec.md](/specs/05_libraries/domain/job_core.spec.md)
   - **domain.job.scan_bundle_has_result.doc.1.operator**: Verify job scan bundle output includes the expected result marker in operations.
   - **domain.job.core.operator**: Case `LIB-DOMAIN-JOB-001-000A-DOMAIN-JOB-SCAN-BUNDLE-HAS-RESULT` for `contract.export`. (operator)

11. [make_core.spec.md](/specs/05_libraries/domain/make_core.spec.md)
   - **make.has_target.doc.1.operator**: Check whether a Make target exists and is resolvable in operator workflows.
   - **domain.make.core.operator**: Case `LIB-DOMAIN-MAKE-001` for `contract.export`. (operator)

12. [markdown_core.spec.md](/specs/05_libraries/domain/markdown_core.spec.md)
   - **domain.markdown.tokens_all_present.doc.1.operator**: Assert required Markdown tokens appear in source markdown content for operators.
   - **domain.markdown.core.operator**: Case `LIB-DOMAIN-MD-001-001-DOMAIN-MARKDOWN-HAS-HEADING` for `contract.export`. (operator)

13. [meta_core.spec.md](/specs/05_libraries/domain/meta_core.spec.md)
   - **domain.meta.has_artifact_target.doc.1.operator**: Detect whether contract metadata declares an artifact target for operations.
   - **domain.meta.core.operator**: Case `LIB-DOMAIN-META-001-001-DOMAIN-META-CASE-ID-EQ` for `contract.export`. (operator)

14. [os_core.spec.md](/specs/05_libraries/domain/os_core.spec.md)
   - **domain.os.exec_ok.doc.1.operator**: Assert that an OS command execution completed successfully for operator workflows.
   - **domain.os.core.operator**: Case `LIB-DOMAIN-OS-001-001-DOMAIN-OS-EXEC-OK` for `contract.export`. (operator)

15. [path_core.spec.md](/specs/05_libraries/domain/path_core.spec.md)
   - **domain.path.sorted.doc.1.operator**: Return path inputs sorted in deterministic lexicographic order for operators.
   - **domain.path.core.operator**: Case `LIB-DOMAIN-PATH-001-001-DOMAIN-PATH-NORMALIZE` for `contract.export`. (operator)

16. [php_core.spec.md](/specs/05_libraries/domain/php_core.spec.md)
   - **php.is_assoc_projection.doc.1.operator**: Assert a PHP projection result is associative for operations.
   - **domain.php.core.operator**: Case `LIB-DOMAIN-PHP-001` for `contract.export`. (operator)

17. [process_core.spec.md](/specs/05_libraries/domain/process_core.spec.md)
   - **domain.process.exec_capture_ex_code.doc.1.operator**: Capture and assert process exit/exception code behavior for operators.
   - **domain.process.core.operator**: Case `LIB-DOMAIN-PROCESS-001-001-DOMAIN-PROCESS-EXEC-CAPTURE-EX-CODE` for `contract.export`. (operator)

18. [python_core.spec.md](/specs/05_libraries/domain/python_core.spec.md)
   - **py.is_tuple_projection.doc.1.operator**: Assert that a Python projection result is tuple-shaped as expected for operators.
   - **domain.python.core.operator**: Case `LIB-DOMAIN-PY-001` for `contract.export`. (operator)

19. [repo_core.spec.md](/specs/05_libraries/domain/repo_core.spec.md)
   - **domain.repo.walk_matching.doc.1.operator**: Walk repository paths and return files matching configured selectors for operators.
   - **domain.repo.core.operator**: Case `LIB-DOMAIN-REPO-001-001-DOMAIN-REPO-WALK-MATCHING` for `contract.export`. (operator)

20. [yaml_core.spec.md](/specs/05_libraries/domain/yaml_core.spec.md)
   - **domain.yaml.stringify.doc.1.operator**: Serialize structured data into canonical YAML text for operators.
   - **domain.yaml.core.operator**: Case `LIB-DOMAIN-YAML-001-001-DOMAIN-YAML-PARSE-GET-OR` for `contract.export`. (operator)

21. [path_core.spec.md](/specs/05_libraries/path/path_core.spec.md)
   - **path.matches.doc.1.operator**: Evaluate whether path values satisfy the provided matcher rules for operators.
   - **path.path.core.operator**: Case `LIB-PATH-001-001-PATH-NORMALIZE-SLASHES` for `contract.export`. (operator)

22. [policy_core.spec.md](/specs/05_libraries/policy/policy_core.spec.md)
   - **policy.violation_count_is.doc.1.operator**: Assert the exact number of policy violations for operators.
   - **policy.policy.core.operator**: Case `LIB-POLICY-001` for `contract.export`. (operator)

23. [policy_metrics.spec.md](/specs/05_libraries/policy/policy_metrics.spec.md)
   - **policy.metric_non_increase.doc.1.operator**: Assert a policy metric does not increase compared to a baseline for operators.
   - **policy.policy.metrics.operator**: Case `LIB-POLICY-002-001-POLICY-METRIC-NON-DECREASE` for `contract.export`. (operator)

