# Reference Index

1. [implicit_ids_v1.spec.md](/specs/03_conformance/cases/core/implicit_ids_v1.spec.md)
   - **implicit_ids_v1.doc.1.1.integrator**: contract docs id intentionally omitted (integrator)

2. [schema_case_validation.spec.md](/specs/03_conformance/cases/core/schema_case_validation.spec.md)
   - **schema_case_validation.doc.1.1.integrator**: schema export validation case (integrator)
   - **schema_case_validation.doc.2.1.integrator**: schema export invalid imports case (integrator)
   - **schema_case_validation.doc.3.1.integrator**: missing status (integrator)
   - **schema_case_validation.doc.4.1.integrator**: invalid docs type (integrator)
   - **schema_case_validation.doc.5.1.integrator**: docs entry one (integrator)
   - **schema_case_validation.doc.5.2.integrator**: docs entry two (integrator)
   - **schema_case_validation.doc.6.1.integrator**: docs entry with unknown key (integrator)
   - **schema_case_validation.doc.9.1.integrator**: schema registry assertions yaml input (integrator)
   - **schema_case_validation.doc.11.1.integrator**: schema text export (integrator)

3. [assertion_core.spec.md](/specs/05_libraries/conformance/assertion_core.spec.md)
   - **conf.json_type_is.doc.1.integrator**: Assert that a value is of the requested JSON schema type for integration contracts.
   - **conformance.assertion.core.integrator**: Case `LIB-CONF-ASSERT-001` for `contract.export`. (integrator)

4. [chain_export_validation.spec.md](/specs/05_libraries/conformance/chain_export_validation.spec.md)
   - **bad.path.symbol.doc.1.integrator**: Validate chain-export failure signaling for an invalid or missing path symbol in pipeline integration.
   - **conformance.chain.export.validation.integrator**: Case `BAD-EXPORT-PATH` for `contract.export`. (integrator)

5. [artifact_core.spec.md](/specs/05_libraries/domain/artifact_core.spec.md)
   - **domain.artifact.write_yaml.doc.1.integrator**: Persist a structured artifact payload as YAML for downstream consumers in integrations.
   - **domain.artifact.core.integrator**: Case `LIB-DOMAIN-ARTIFACT-001-001-DOMAIN-ARTIFACT-WRITE-YAML` for `contract.export`. (integrator)

6. [conformance_core.spec.md](/specs/05_libraries/domain/conformance_core.spec.md)
   - **domain.conformance.validate_report_errors.doc.1.integrator**: Validate conformance report errors and fail when reported issues violate expectations for integrations.
   - **domain.conformance.core.integrator**: Case `LIB-DOMAIN-CONFORMANCE-001-000-DOMAIN-CONFORMANCE-ERROR-WHEN-FALSE` for `contract.export`. (integrator)

7. [contract_set_core.spec.md](/specs/05_libraries/domain/contract_set_core.spec.md)
   - **domain.contract_set.applies_to_runners.doc.1.integrator**: Evaluate whether a contract set should execute under the current runner for integration plans.
   - **domain.contract_set.core.integrator**: Case `LIB-DOMAIN-CONTRACT-SET-001` for `contract.export`. (integrator)

8. [fs_core.spec.md](/specs/05_libraries/domain/fs_core.spec.md)
   - **domain.fs.sort_spec_files.doc.1.integrator**: Sort discovered spec files into stable, deterministic ordering for integrations.
   - **domain.fs.core.integrator**: Case `LIB-DOMAIN-FS-001-001-DOMAIN-FS-IS-DOCS-SPEC-FILE` for `contract.export`. (integrator)

9. [http_core.spec.md](/specs/05_libraries/domain/http_core.spec.md)
   - **domain.http.step_status_is.doc.1.integrator**: Assert that a HTTP workflow step reports the expected status for integrations.
   - **domain.http.core.integrator**: Case `LIB-DOMAIN-HTTP-001-001-DOMAIN-HTTP-STATUS` for `contract.export`. (integrator)

10. [job_core.spec.md](/specs/05_libraries/domain/job_core.spec.md)
   - **domain.job.scan_bundle_has_result.doc.1.integrator**: Verify job scan bundle output includes the expected result marker in integrations.
   - **domain.job.core.integrator**: Case `LIB-DOMAIN-JOB-001-000A-DOMAIN-JOB-SCAN-BUNDLE-HAS-RESULT` for `contract.export`. (integrator)

11. [make_core.spec.md](/specs/05_libraries/domain/make_core.spec.md)
   - **make.has_target.doc.1.integrator**: Check whether a Make target exists and is resolvable in integration planning.
   - **domain.make.core.integrator**: Case `LIB-DOMAIN-MAKE-001` for `contract.export`. (integrator)

12. [markdown_core.spec.md](/specs/05_libraries/domain/markdown_core.spec.md)
   - **domain.markdown.tokens_all_present.doc.1.integrator**: Assert required Markdown tokens appear in source markdown content for integration pipelines.
   - **domain.markdown.core.integrator**: Case `LIB-DOMAIN-MD-001-001-DOMAIN-MARKDOWN-HAS-HEADING` for `contract.export`. (integrator)

13. [meta_core.spec.md](/specs/05_libraries/domain/meta_core.spec.md)
   - **domain.meta.has_artifact_target.doc.1.integrator**: Detect whether contract metadata declares an artifact target for integrations.
   - **domain.meta.core.integrator**: Case `LIB-DOMAIN-META-001-001-DOMAIN-META-CASE-ID-EQ` for `contract.export`. (integrator)

14. [os_core.spec.md](/specs/05_libraries/domain/os_core.spec.md)
   - **domain.os.exec_ok.doc.1.integrator**: Assert that an OS command execution completed successfully for integrations.
   - **domain.os.core.integrator**: Case `LIB-DOMAIN-OS-001-001-DOMAIN-OS-EXEC-OK` for `contract.export`. (integrator)

15. [path_core.spec.md](/specs/05_libraries/domain/path_core.spec.md)
   - **domain.path.sorted.doc.1.integrator**: Return path inputs sorted in deterministic lexicographic order for integrations.
   - **domain.path.core.integrator**: Case `LIB-DOMAIN-PATH-001-001-DOMAIN-PATH-NORMALIZE` for `contract.export`. (integrator)

16. [php_core.spec.md](/specs/05_libraries/domain/php_core.spec.md)
   - **php.is_assoc_projection.doc.1.integrator**: Assert a PHP projection result is associative for integration consumers.
   - **domain.php.core.integrator**: Case `LIB-DOMAIN-PHP-001` for `contract.export`. (integrator)

17. [process_core.spec.md](/specs/05_libraries/domain/process_core.spec.md)
   - **domain.process.exec_capture_ex_code.doc.1.integrator**: Capture and assert process exit/exception code behavior for integrations.
   - **domain.process.core.integrator**: Case `LIB-DOMAIN-PROCESS-001-001-DOMAIN-PROCESS-EXEC-CAPTURE-EX-CODE` for `contract.export`. (integrator)

18. [python_core.spec.md](/specs/05_libraries/domain/python_core.spec.md)
   - **py.is_tuple_projection.doc.1.integrator**: Assert that a Python projection result is tuple-shaped as expected for integrations.
   - **domain.python.core.integrator**: Case `LIB-DOMAIN-PY-001` for `contract.export`. (integrator)

19. [repo_core.spec.md](/specs/05_libraries/domain/repo_core.spec.md)
   - **domain.repo.walk_matching.doc.1.integrator**: Walk repository paths and return files matching configured selectors for integrations.
   - **domain.repo.core.integrator**: Case `LIB-DOMAIN-REPO-001-001-DOMAIN-REPO-WALK-MATCHING` for `contract.export`. (integrator)

20. [yaml_core.spec.md](/specs/05_libraries/domain/yaml_core.spec.md)
   - **domain.yaml.stringify.doc.1.integrator**: Serialize structured data into canonical YAML text for integrations.
   - **domain.yaml.core.integrator**: Case `LIB-DOMAIN-YAML-001-001-DOMAIN-YAML-PARSE-GET-OR` for `contract.export`. (integrator)

21. [path_core.spec.md](/specs/05_libraries/path/path_core.spec.md)
   - **path.matches.doc.1.integrator**: Evaluate whether path values satisfy the provided matcher rules for integrations.
   - **path.path.core.integrator**: Case `LIB-PATH-001-001-PATH-NORMALIZE-SLASHES` for `contract.export`. (integrator)

22. [policy_core.spec.md](/specs/05_libraries/policy/policy_core.spec.md)
   - **policy.violation_count_is.doc.1.integrator**: Assert the exact number of policy violations for integrators.
   - **policy.policy.core.integrator**: Case `LIB-POLICY-001` for `contract.export`. (integrator)

23. [policy_metrics.spec.md](/specs/05_libraries/policy/policy_metrics.spec.md)
   - **policy.metric_non_increase.doc.1.integrator**: Assert a policy metric does not increase compared to a baseline for integrations.
   - **policy.policy.metrics.integrator**: Case `LIB-POLICY-002-001-POLICY-METRIC-NON-DECREASE` for `contract.export`. (integrator)

