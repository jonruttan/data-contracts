# Reference Index

1. [implicit_ids_v1.spec.md](/specs/03_conformance/cases/core/implicit_ids_v1.spec.md)
   - **implicit_ids_v1.doc.1.1.maintainer**: contract docs id intentionally omitted (maintainer)

2. [schema_case_validation.spec.md](/specs/03_conformance/cases/core/schema_case_validation.spec.md)
   - **schema_case_validation.doc.1.1.maintainer**: schema export validation case (maintainer)
   - **schema_case_validation.doc.2.1.maintainer**: schema export invalid imports case (maintainer)
   - **schema_case_validation.doc.3.1.maintainer**: missing status (maintainer)
   - **schema_case_validation.doc.4.1.maintainer**: invalid docs type (maintainer)
   - **schema_case_validation.doc.5.1.maintainer**: docs entry one (maintainer)
   - **schema_case_validation.doc.5.2.maintainer**: docs entry two (maintainer)
   - **schema_case_validation.doc.6.1.maintainer**: docs entry with unknown key (maintainer)
   - **schema_case_validation.doc.9.1.maintainer**: schema registry assertions yaml input (maintainer)
   - **schema_case_validation.doc.11.1.maintainer**: schema text export (maintainer)

3. [assertion_core.spec.md](/specs/05_libraries/conformance/assertion_core.spec.md)
   - **conf.json_type_is.doc.1.maintainer**: Assert that a value is of the requested JSON schema type for system maintenance checks.
   - **conformance.assertion.core.maintainer**: Case `LIB-CONF-ASSERT-001` for `contract.export`. (maintainer)

4. [chain_export_validation.spec.md](/specs/05_libraries/conformance/chain_export_validation.spec.md)
   - **bad.path.symbol.doc.1.maintainer**: Validate chain-export failure signaling for an invalid or missing path symbol during maintenance.
   - **conformance.chain.export.validation.maintainer**: Case `BAD-EXPORT-PATH` for `contract.export`. (maintainer)

5. [artifact_core.spec.md](/specs/05_libraries/domain/artifact_core.spec.md)
   - **domain.artifact.write_yaml.doc.1.maintainer**: Persist a structured artifact payload as YAML for downstream consumers in maintenance.
   - **domain.artifact.core.maintainer**: Case `LIB-DOMAIN-ARTIFACT-001-001-DOMAIN-ARTIFACT-WRITE-YAML` for `contract.export`. (maintainer)

6. [conformance_core.spec.md](/specs/05_libraries/domain/conformance_core.spec.md)
   - **domain.conformance.validate_report_errors.doc.1.maintainer**: Validate conformance report errors and fail when reported issues violate expectations for maintenance.
   - **domain.conformance.core.maintainer**: Case `LIB-DOMAIN-CONFORMANCE-001-000-DOMAIN-CONFORMANCE-ERROR-WHEN-FALSE` for `contract.export`. (maintainer)

7. [contract_set_core.spec.md](/specs/05_libraries/domain/contract_set_core.spec.md)
   - **domain.contract_set.applies_to_runners.doc.1.maintainer**: Evaluate whether a contract set should execute under the current runner for maintenance decisions.
   - **domain.contract_set.core.maintainer**: Case `LIB-DOMAIN-CONTRACT-SET-001` for `contract.export`. (maintainer)

8. [fs_core.spec.md](/specs/05_libraries/domain/fs_core.spec.md)
   - **domain.fs.sort_spec_files.doc.1.maintainer**: Sort discovered spec files into stable, deterministic ordering for maintenance.
   - **domain.fs.core.maintainer**: Case `LIB-DOMAIN-FS-001-001-DOMAIN-FS-IS-DOCS-SPEC-FILE` for `contract.export`. (maintainer)

9. [http_core.spec.md](/specs/05_libraries/domain/http_core.spec.md)
   - **domain.http.step_status_is.doc.1.maintainer**: Assert that a HTTP workflow step reports the expected status for maintainers.
   - **domain.http.core.maintainer**: Case `LIB-DOMAIN-HTTP-001-001-DOMAIN-HTTP-STATUS` for `contract.export`. (maintainer)

10. [job_core.spec.md](/specs/05_libraries/domain/job_core.spec.md)
   - **domain.job.scan_bundle_has_result.doc.1.maintainer**: Verify job scan bundle output includes the expected result marker for maintenance workflows.
   - **domain.job.core.maintainer**: Case `LIB-DOMAIN-JOB-001-000A-DOMAIN-JOB-SCAN-BUNDLE-HAS-RESULT` for `contract.export`. (maintainer)

11. [make_core.spec.md](/specs/05_libraries/domain/make_core.spec.md)
   - **make.has_target.doc.1.maintainer**: Check whether a Make target exists and is resolvable for maintenance.
   - **domain.make.core.maintainer**: Case `LIB-DOMAIN-MAKE-001` for `contract.export`. (maintainer)

12. [markdown_core.spec.md](/specs/05_libraries/domain/markdown_core.spec.md)
   - **domain.markdown.tokens_all_present.doc.1.maintainer**: Assert required Markdown tokens appear in source markdown content for maintainers.
   - **domain.markdown.core.maintainer**: Case `LIB-DOMAIN-MD-001-001-DOMAIN-MARKDOWN-HAS-HEADING` for `contract.export`. (maintainer)

13. [meta_core.spec.md](/specs/05_libraries/domain/meta_core.spec.md)
   - **domain.meta.has_artifact_target.doc.1.maintainer**: Detect whether contract metadata declares an artifact target for maintenance.
   - **domain.meta.core.maintainer**: Case `LIB-DOMAIN-META-001-001-DOMAIN-META-CASE-ID-EQ` for `contract.export`. (maintainer)

14. [os_core.spec.md](/specs/05_libraries/domain/os_core.spec.md)
   - **domain.os.exec_ok.doc.1.maintainer**: Assert that an OS command execution completed successfully for maintenance.
   - **domain.os.core.maintainer**: Case `LIB-DOMAIN-OS-001-001-DOMAIN-OS-EXEC-OK` for `contract.export`. (maintainer)

15. [path_core.spec.md](/specs/05_libraries/domain/path_core.spec.md)
   - **domain.path.sorted.doc.1.maintainer**: Return path inputs sorted in deterministic lexicographic order for maintainers.
   - **domain.path.core.maintainer**: Case `LIB-DOMAIN-PATH-001-001-DOMAIN-PATH-NORMALIZE` for `contract.export`. (maintainer)

16. [php_core.spec.md](/specs/05_libraries/domain/php_core.spec.md)
   - **php.is_assoc_projection.doc.1.maintainer**: Assert a PHP projection result is associative for maintenance verification.
   - **domain.php.core.maintainer**: Case `LIB-DOMAIN-PHP-001` for `contract.export`. (maintainer)

17. [process_core.spec.md](/specs/05_libraries/domain/process_core.spec.md)
   - **domain.process.exec_capture_ex_code.doc.1.maintainer**: Capture and assert process exit/exception code behavior for maintainers.
   - **domain.process.core.maintainer**: Case `LIB-DOMAIN-PROCESS-001-001-DOMAIN-PROCESS-EXEC-CAPTURE-EX-CODE` for `contract.export`. (maintainer)

18. [python_core.spec.md](/specs/05_libraries/domain/python_core.spec.md)
   - **py.is_tuple_projection.doc.1.maintainer**: Assert that a Python projection result is tuple-shaped as expected for maintenance.
   - **domain.python.core.maintainer**: Case `LIB-DOMAIN-PY-001` for `contract.export`. (maintainer)

19. [repo_core.spec.md](/specs/05_libraries/domain/repo_core.spec.md)
   - **domain.repo.walk_matching.doc.1.maintainer**: Walk repository paths and return files matching configured selectors for maintenance.
   - **domain.repo.core.maintainer**: Case `LIB-DOMAIN-REPO-001-001-DOMAIN-REPO-WALK-MATCHING` for `contract.export`. (maintainer)

20. [yaml_core.spec.md](/specs/05_libraries/domain/yaml_core.spec.md)
   - **domain.yaml.stringify.doc.1.maintainer**: Serialize structured data into canonical YAML text for maintainers.
   - **domain.yaml.core.maintainer**: Case `LIB-DOMAIN-YAML-001-001-DOMAIN-YAML-PARSE-GET-OR` for `contract.export`. (maintainer)

21. [path_core.spec.md](/specs/05_libraries/path/path_core.spec.md)
   - **path.matches.doc.1.maintainer**: Evaluate whether path values satisfy the provided matcher rules for maintenance.
   - **path.path.core.maintainer**: Case `LIB-PATH-001-001-PATH-NORMALIZE-SLASHES` for `contract.export`. (maintainer)

22. [policy_core.spec.md](/specs/05_libraries/policy/policy_core.spec.md)
   - **policy.violation_count_is.doc.1.maintainer**: Assert the exact number of policy violations for maintainers.
   - **policy.policy.core.maintainer**: Case `LIB-POLICY-001` for `contract.export`. (maintainer)

23. [policy_metrics.spec.md](/specs/05_libraries/policy/policy_metrics.spec.md)
   - **policy.metric_non_increase.doc.1.maintainer**: Assert a policy metric does not increase compared to a baseline for maintainers.
   - **policy.policy.metrics.maintainer**: Case `LIB-POLICY-002-001-POLICY-METRIC-NON-DECREASE` for `contract.export`. (maintainer)

