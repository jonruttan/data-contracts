# Reference Index

1. [implicit_ids_v1.spec.md](/specs/03_conformance/cases/core/implicit_ids_v1.spec.md)
   - **implicit_ids_v1.doc.1.1.auditor**: contract docs id intentionally omitted (auditor)

2. [schema_case_validation.spec.md](/specs/03_conformance/cases/core/schema_case_validation.spec.md)
   - **schema_case_validation.doc.1.1.auditor**: schema export validation case (auditor)
   - **schema_case_validation.doc.2.1.auditor**: schema export invalid imports case (auditor)
   - **schema_case_validation.doc.3.1.auditor**: missing status (auditor)
   - **schema_case_validation.doc.4.1.auditor**: invalid docs type (auditor)
   - **schema_case_validation.doc.5.1.auditor**: docs entry one (auditor)
   - **schema_case_validation.doc.5.2.auditor**: docs entry two (auditor)
   - **schema_case_validation.doc.6.1.auditor**: docs entry with unknown key (auditor)
   - **schema_case_validation.doc.9.1.auditor**: schema registry assertions yaml input (auditor)
   - **schema_case_validation.doc.11.1.auditor**: schema text export (auditor)

3. [assertion_core.spec.md](/specs/05_libraries/conformance/assertion_core.spec.md)
   - **conf.json_type_is.doc.1.auditor**: Assert that a value is of the requested JSON schema type for audit evidence.
   - **conformance.assertion.core.auditor**: Case `LIB-CONF-ASSERT-001` for `contract.export`. (auditor)

4. [chain_export_validation.spec.md](/specs/05_libraries/conformance/chain_export_validation.spec.md)
   - **bad.path.symbol.doc.1.auditor**: Validate chain-export failure signaling for an invalid or missing path symbol during audits.
   - **conformance.chain.export.validation.auditor**: Case `BAD-EXPORT-PATH` for `contract.export`. (auditor)

5. [artifact_core.spec.md](/specs/05_libraries/domain/artifact_core.spec.md)
   - **domain.artifact.write_yaml.doc.1.auditor**: Persist a structured artifact payload as YAML for downstream consumers in audit evidence.
   - **domain.artifact.core.auditor**: Case `LIB-DOMAIN-ARTIFACT-001-001-DOMAIN-ARTIFACT-WRITE-YAML` for `contract.export`. (auditor)

6. [conformance_core.spec.md](/specs/05_libraries/domain/conformance_core.spec.md)
   - **domain.conformance.validate_report_errors.doc.1.auditor**: Validate conformance report errors and fail when reported issues violate audit expectations.
   - **domain.conformance.core.auditor**: Case `LIB-DOMAIN-CONFORMANCE-001-000-DOMAIN-CONFORMANCE-ERROR-WHEN-FALSE` for `contract.export`. (auditor)

7. [contract_set_core.spec.md](/specs/05_libraries/domain/contract_set_core.spec.md)
   - **domain.contract_set.applies_to_runners.doc.1.auditor**: Evaluate whether a contract set should execute under the current runner for audit tracking.
   - **domain.contract_set.core.auditor**: Case `LIB-DOMAIN-CONTRACT-SET-001` for `contract.export`. (auditor)

8. [fs_core.spec.md](/specs/05_libraries/domain/fs_core.spec.md)
   - **domain.fs.sort_spec_files.doc.1.auditor**: Sort discovered spec files into stable, deterministic ordering for audit evidence.
   - **domain.fs.core.auditor**: Case `LIB-DOMAIN-FS-001-001-DOMAIN-FS-IS-DOCS-SPEC-FILE` for `contract.export`. (auditor)

9. [http_core.spec.md](/specs/05_libraries/domain/http_core.spec.md)
   - **domain.http.step_status_is.doc.1.auditor**: Assert that a HTTP workflow step reports the expected status for audit trails.
   - **domain.http.core.auditor**: Case `LIB-DOMAIN-HTTP-001-001-DOMAIN-HTTP-STATUS` for `contract.export`. (auditor)

10. [job_core.spec.md](/specs/05_libraries/domain/job_core.spec.md)
   - **domain.job.scan_bundle_has_result.doc.1.auditor**: Verify job scan bundle output includes the expected result marker for audit.
   - **domain.job.core.auditor**: Case `LIB-DOMAIN-JOB-001-000A-DOMAIN-JOB-SCAN-BUNDLE-HAS-RESULT` for `contract.export`. (auditor)

11. [make_core.spec.md](/specs/05_libraries/domain/make_core.spec.md)
   - **make.has_target.doc.1.auditor**: Check whether a Make target exists and is resolvable for auditability.
   - **domain.make.core.auditor**: Case `LIB-DOMAIN-MAKE-001` for `contract.export`. (auditor)

12. [markdown_core.spec.md](/specs/05_libraries/domain/markdown_core.spec.md)
   - **domain.markdown.tokens_all_present.doc.1.auditor**: Assert required Markdown tokens appear in source markdown content for auditors.
   - **domain.markdown.core.auditor**: Case `LIB-DOMAIN-MD-001-001-DOMAIN-MARKDOWN-HAS-HEADING` for `contract.export`. (auditor)

13. [meta_core.spec.md](/specs/05_libraries/domain/meta_core.spec.md)
   - **domain.meta.has_artifact_target.doc.1.auditor**: Detect whether contract metadata declares an artifact target for audit evidence.
   - **domain.meta.core.auditor**: Case `LIB-DOMAIN-META-001-001-DOMAIN-META-CASE-ID-EQ` for `contract.export`. (auditor)

14. [os_core.spec.md](/specs/05_libraries/domain/os_core.spec.md)
   - **domain.os.exec_ok.doc.1.auditor**: Assert that an OS command execution completed successfully for audit checks.
   - **domain.os.core.auditor**: Case `LIB-DOMAIN-OS-001-001-DOMAIN-OS-EXEC-OK` for `contract.export`. (auditor)

15. [path_core.spec.md](/specs/05_libraries/domain/path_core.spec.md)
   - **domain.path.sorted.doc.1.auditor**: Return path inputs sorted in deterministic lexicographic order for audits.
   - **domain.path.core.auditor**: Case `LIB-DOMAIN-PATH-001-001-DOMAIN-PATH-NORMALIZE` for `contract.export`. (auditor)

16. [php_core.spec.md](/specs/05_libraries/domain/php_core.spec.md)
   - **php.is_assoc_projection.doc.1.auditor**: Assert a PHP projection result is associative for audit validation.
   - **domain.php.core.auditor**: Case `LIB-DOMAIN-PHP-001` for `contract.export`. (auditor)

17. [process_core.spec.md](/specs/05_libraries/domain/process_core.spec.md)
   - **domain.process.exec_capture_ex_code.doc.1.auditor**: Capture and assert process exit/exception code behavior for audits.
   - **domain.process.core.auditor**: Case `LIB-DOMAIN-PROCESS-001-001-DOMAIN-PROCESS-EXEC-CAPTURE-EX-CODE` for `contract.export`. (auditor)

18. [python_core.spec.md](/specs/05_libraries/domain/python_core.spec.md)
   - **py.is_tuple_projection.doc.1.auditor**: Assert that a Python projection result is tuple-shaped as expected for audit review.
   - **domain.python.core.auditor**: Case `LIB-DOMAIN-PY-001` for `contract.export`. (auditor)

19. [repo_core.spec.md](/specs/05_libraries/domain/repo_core.spec.md)
   - **domain.repo.walk_matching.doc.1.auditor**: Walk repository paths and return files matching configured selectors for audits.
   - **domain.repo.core.auditor**: Case `LIB-DOMAIN-REPO-001-001-DOMAIN-REPO-WALK-MATCHING` for `contract.export`. (auditor)

20. [yaml_core.spec.md](/specs/05_libraries/domain/yaml_core.spec.md)
   - **domain.yaml.stringify.doc.1.auditor**: Serialize structured data into canonical YAML text for audits.
   - **domain.yaml.core.auditor**: Case `LIB-DOMAIN-YAML-001-001-DOMAIN-YAML-PARSE-GET-OR` for `contract.export`. (auditor)

21. [path_core.spec.md](/specs/05_libraries/path/path_core.spec.md)
   - **path.matches.doc.1.auditor**: Evaluate whether path values satisfy the provided matcher rules for audits.
   - **path.path.core.auditor**: Case `LIB-PATH-001-001-PATH-NORMALIZE-SLASHES` for `contract.export`. (auditor)

22. [policy_core.spec.md](/specs/05_libraries/policy/policy_core.spec.md)
   - **policy.violation_count_is.doc.1.auditor**: Assert the exact number of policy violations for audits.
   - **policy.policy.core.auditor**: Case `LIB-POLICY-001` for `contract.export`. (auditor)

23. [policy_metrics.spec.md](/specs/05_libraries/policy/policy_metrics.spec.md)
   - **policy.metric_non_increase.doc.1.auditor**: Assert a policy metric does not increase compared to a baseline for audits.
   - **policy.policy.metrics.auditor**: Case `LIB-POLICY-002-001-POLICY-METRIC-NON-DECREASE` for `contract.export`. (auditor)

