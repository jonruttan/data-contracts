```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'docs_guides_index': {'path': '/docs/book/guides/index.md', 'required_paths': ['/docs/book/guides/guide_01_onboarding.md', '/docs/book/guides/guide_02_first_spec_authoring.md', '/docs/book/guides/guide_03_running_checks_and_gates.md', '/docs/book/guides/guide_04_debugging_failures.md', '/docs/book/guides/guide_05_release_and_change_control.md', '/docs/book/guides/guide_06_governance_tuning.md', '/docs/book/guides/guide_07_schema_extension_workflow.md', '/docs/book/guides/guide_08_ci_integration.md', '/docs/book/guides/guide_09_status_exchange_operations.md', '/docs/book/guides/guide_10_reference_navigation_patterns.md']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'docs.usage_guides_index_sync'}}}"
services:
  entries:
  - id: svc.root_docs_guides_index_path_docs_book_guides_index_md_required_paths_docs_book_guides_guide_01_onboarding_md_docs_book_guides_guide_02_first_spec_authoring_md_docs_book_guides_guide_03_running_checks_and_gates_md_docs_book_guides_guide_04_debugging_failures_md_docs_book_guides_guide_05_release_and_change_control_md_docs_book_guides_guide_06_governance_tuning_md_docs_book_guides_guide_07_schema_extension_workflow_md_docs_book_guides_guide_08_ci_integration_md_docs_book_guides_guide_09_status_exchange_operations_md_docs_book_guides_guide_10_reference_navigation_patterns_md_check_profile_governance_scan_config_check_docs_usage_guides_index_sync.default.1
    type: legacy.root_docs_guides_index_path_docs_book_guides_index_md_required_paths_docs_book_guides_guide_01_onboarding_md_docs_book_guides_guide_02_first_spec_authoring_md_docs_book_guides_guide_03_running_checks_and_gates_md_docs_book_guides_guide_04_debugging_failures_md_docs_book_guides_guide_05_release_and_change_control_md_docs_book_guides_guide_06_governance_tuning_md_docs_book_guides_guide_07_schema_extension_workflow_md_docs_book_guides_guide_08_ci_integration_md_docs_book_guides_guide_09_status_exchange_operations_md_docs_book_guides_guide_10_reference_navigation_patterns_md_check_profile_governance_scan_config_check_docs_usage_guides_index_sync
    io: io
    profile: default
contracts:
- id: DCGOV-DOCS-REF-020
  title: usage guides index is synchronized
  purpose: Ensures the guides index includes the canonical guide set.
  clauses:
    imports:
    - from: artifact
      names:
      - violation_count
    predicates:
    - id: assert_1
      assert:
        call:
        - var: policy.assert.no_violations
        - std.object.assoc:
          - violation_count
          - var: violation_count
          - lit: {}
```
