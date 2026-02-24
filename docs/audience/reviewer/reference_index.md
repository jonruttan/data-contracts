# Reference Index

1. [implicit_ids_v1.spec.md](/specs/03_conformance/cases/core/implicit_ids_v1.spec.md)
   - **implicit_ids_v1.doc.1.1.reviewer**: contract docs id intentionally omitted (reviewer)

2. [schema_case_validation.spec.md](/specs/03_conformance/cases/core/schema_case_validation.spec.md)
   - **schema_case_validation.doc.1.1.reviewer**: schema export validation case (reviewer)
   - **schema_case_validation.doc.2.1.reviewer**: schema export invalid imports case (reviewer)
   - **schema_case_validation.doc.3.1.reviewer**: missing status (reviewer)
   - **schema_case_validation.doc.4.1.reviewer**: invalid docs type (reviewer)
   - **schema_case_validation.doc.5.1.reviewer**: docs entry one (reviewer)
   - **schema_case_validation.doc.5.2.reviewer**: docs entry two (reviewer)
   - **schema_case_validation.doc.6.1.reviewer**: docs entry with unknown key (reviewer)
   - **schema_case_validation.doc.9.1.reviewer**: schema registry assertions yaml input (reviewer)
   - **schema_case_validation.doc.11.1.reviewer**: schema text export (reviewer)

3. [assertion_core.spec.md](/specs/05_libraries/conformance/assertion_core.spec.md)
   - **conf.json_type_is.doc.1.reviewer**: Assert that a value is of the requested JSON schema type for report review.
   - **conformance.assertion.core.reviewer**: Case `LIB-CONF-ASSERT-001` for `contract.export`. (reviewer)

4. [chain_export_validation.spec.md](/specs/05_libraries/conformance/chain_export_validation.spec.md)
   - **bad.path.symbol.doc.1.reviewer**: Validate chain-export failure signaling for an invalid or missing path symbol in review artifacts.
   - **conformance.chain.export.validation.reviewer**: Case `BAD-EXPORT-PATH` for `contract.export`. (reviewer)

5. [artifact_core.spec.md](/specs/05_libraries/domain/artifact_core.spec.md)
   - **domain.artifact.write_yaml.doc.1.reviewer**: Persist a structured artifact payload as YAML for downstream consumers during review.
   - **domain.artifact.core.reviewer**: Case `LIB-DOMAIN-ARTIFACT-001-001-DOMAIN-ARTIFACT-WRITE-YAML` for `contract.export`. (reviewer)

6. [conformance_core.spec.md](/specs/05_libraries/domain/conformance_core.spec.md)
   - **domain.conformance.validate_report_errors.doc.1.reviewer**: Validate conformance report errors and fail when reported issues violate review expectations.
   - **domain.conformance.core.reviewer**: Case `LIB-DOMAIN-CONFORMANCE-001-000-DOMAIN-CONFORMANCE-ERROR-WHEN-FALSE` for `contract.export`. (reviewer)

7. [contract_set_core.spec.md](/specs/05_libraries/domain/contract_set_core.spec.md)
   - **domain.contract_set.applies_to_runners.doc.1.reviewer**: Evaluate whether a contract set should execute under the current runner for review.
   - **domain.contract_set.core.reviewer**: Case `LIB-DOMAIN-CONTRACT-SET-001` for `contract.export`. (reviewer)

8. [fs_core.spec.md](/specs/05_libraries/domain/fs_core.spec.md)
   - **domain.fs.sort_spec_files.doc.1.reviewer**: Sort discovered spec files into stable, deterministic ordering for review.
   - **domain.fs.core.reviewer**: Case `LIB-DOMAIN-FS-001-001-DOMAIN-FS-IS-DOCS-SPEC-FILE` for `contract.export`. (reviewer)

9. [http_core.spec.md](/specs/05_libraries/domain/http_core.spec.md)
   - **domain.http.step_status_is.doc.1.reviewer**: Assert that a HTTP workflow step reports the expected status for reviewers.
   - **domain.http.core.reviewer**: Case `LIB-DOMAIN-HTTP-001-001-DOMAIN-HTTP-STATUS` for `contract.export`. (reviewer)

10. [job_core.spec.md](/specs/05_libraries/domain/job_core.spec.md)
   - **domain.job.scan_bundle_has_result.doc.1.reviewer**: Verify job scan bundle output includes the expected result marker for review.
   - **domain.job.core.reviewer**: Case `LIB-DOMAIN-JOB-001-000A-DOMAIN-JOB-SCAN-BUNDLE-HAS-RESULT` for `contract.export`. (reviewer)

11. [make_core.spec.md](/specs/05_libraries/domain/make_core.spec.md)
   - **make.has_target.doc.1.reviewer**: Check whether a Make target exists and is resolvable for review decisions.
   - **domain.make.core.reviewer**: Case `LIB-DOMAIN-MAKE-001` for `contract.export`. (reviewer)

12. [markdown_core.spec.md](/specs/05_libraries/domain/markdown_core.spec.md)
   - **domain.markdown.tokens_all_present.doc.1.reviewer**: Assert required Markdown tokens appear in source markdown content for reviewers.
   - **domain.markdown.core.reviewer**: Case `LIB-DOMAIN-MD-001-001-DOMAIN-MARKDOWN-HAS-HEADING` for `contract.export`. (reviewer)

13. [meta_core.spec.md](/specs/05_libraries/domain/meta_core.spec.md)
   - **domain.meta.has_artifact_target.doc.1.reviewer**: Detect whether contract metadata declares an artifact target for reviewers.
   - **domain.meta.core.reviewer**: Case `LIB-DOMAIN-META-001-001-DOMAIN-META-CASE-ID-EQ` for `contract.export`. (reviewer)

14. [os_core.spec.md](/specs/05_libraries/domain/os_core.spec.md)
   - **domain.os.exec_ok.doc.1.reviewer**: Assert that an OS command execution completed successfully for review.
   - **domain.os.core.reviewer**: Case `LIB-DOMAIN-OS-001-001-DOMAIN-OS-EXEC-OK` for `contract.export`. (reviewer)

15. [path_core.spec.md](/specs/05_libraries/domain/path_core.spec.md)
   - **domain.path.sorted.doc.1.reviewer**: Return path inputs sorted in deterministic lexicographic order for reviewers.
   - **domain.path.core.reviewer**: Case `LIB-DOMAIN-PATH-001-001-DOMAIN-PATH-NORMALIZE` for `contract.export`. (reviewer)

16. [php_core.spec.md](/specs/05_libraries/domain/php_core.spec.md)
   - **php.is_assoc_projection.doc.1.reviewer**: Assert a PHP projection result is associative for reviewer checks.
   - **domain.php.core.reviewer**: Case `LIB-DOMAIN-PHP-001` for `contract.export`. (reviewer)

17. [process_core.spec.md](/specs/05_libraries/domain/process_core.spec.md)
   - **domain.process.exec_capture_ex_code.doc.1.reviewer**: Capture and assert process exit/exception code behavior for reviewers.
   - **domain.process.core.reviewer**: Case `LIB-DOMAIN-PROCESS-001-001-DOMAIN-PROCESS-EXEC-CAPTURE-EX-CODE` for `contract.export`. (reviewer)

18. [python_core.spec.md](/specs/05_libraries/domain/python_core.spec.md)
   - **py.is_tuple_projection.doc.1.reviewer**: Assert that a Python projection result is tuple-shaped as expected for reviewers.
   - **domain.python.core.reviewer**: Case `LIB-DOMAIN-PY-001` for `contract.export`. (reviewer)

19. [repo_core.spec.md](/specs/05_libraries/domain/repo_core.spec.md)
   - **domain.repo.walk_matching.doc.1.reviewer**: Walk repository paths and return files matching configured selectors for reviewers.
   - **domain.repo.core.reviewer**: Case `LIB-DOMAIN-REPO-001-001-DOMAIN-REPO-WALK-MATCHING` for `contract.export`. (reviewer)

20. [yaml_core.spec.md](/specs/05_libraries/domain/yaml_core.spec.md)
   - **domain.yaml.stringify.doc.1.reviewer**: Serialize structured data into canonical YAML text for reviewers.
   - **domain.yaml.core.reviewer**: Case `LIB-DOMAIN-YAML-001-001-DOMAIN-YAML-PARSE-GET-OR` for `contract.export`. (reviewer)

21. [path_core.spec.md](/specs/05_libraries/path/path_core.spec.md)
   - **path.matches.doc.1.reviewer**: Evaluate whether path values satisfy the provided matcher rules for review.
   - **path.path.core.reviewer**: Case `LIB-PATH-001-001-PATH-NORMALIZE-SLASHES` for `contract.export`. (reviewer)

22. [policy_core.spec.md](/specs/05_libraries/policy/policy_core.spec.md)
   - **policy.violation_count_is.doc.1.reviewer**: Assert the exact number of policy violations for reviewers.
   - **policy.policy.core.reviewer**: Case `LIB-POLICY-001` for `contract.export`. (reviewer)

23. [policy_metrics.spec.md](/specs/05_libraries/policy/policy_metrics.spec.md)
   - **policy.metric_non_increase.doc.1.reviewer**: Assert a policy metric does not increase compared to a baseline for reviewers.
   - **policy.policy.metrics.reviewer**: Case `LIB-POLICY-002-001-POLICY-METRIC-NON-DECREASE` for `contract.export`. (reviewer)

