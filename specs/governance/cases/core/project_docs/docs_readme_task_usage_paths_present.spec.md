```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'readme_usage_paths': {'path': '/README.md', 'required_tokens': ['How Users Use This Project', 'Author a spec change', 'Validate docs and contract coherence', 'Read compatibility and status telemetry', 'Debug governance or documentation drift']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'docs.readme_task_usage_paths_present'}}}"
contracts:
  clauses:
  - id: DCGOV-DOCS-REF-025
    title: readme includes task-based usage paths
    purpose: Ensures README is user-oriented and includes concrete task navigation.
    asserts:
      imports:
      - from: artifact
        names:
        - violation_count
      checks:
      - id: assert_1
        assert:
          call:
          - var: policy.assert.no_violations
          - std.object.assoc:
            - violation_count
            - var: violation_count
            - lit: {}
adapters:
- type: legacy.root_readme_usage_paths_path_readme_md_required_tokens_how_users_use_this_project_author_a_spec_change_validate_docs_and_contract_coherence_read_compatibility_and_status_telemetry_debug_governance_or_documentation_drift_check_profile_governance_scan_config_check_docs_readme_task_usage_paths_present
  actions:
  - id: svc.root_readme_usage_paths_path_readme_md_required_tokens_how_users_use_this_project_author_a_spec_change_validate_docs_and_contract_coherence_read_compatibility_and_status_telemetry_debug_governance_or_documentation_drift_check_profile_governance_scan_config_check_docs_readme_task_usage_paths_present.default.1
    direction: bidirectional
    profile: default
services:
- id: svc.root_readme_usage_paths_path_readme_md_required_tokens_how_users_use_this_project_author_a_spec_change_validate_docs_and_contract_coherence_read_compatibility_and_status_telemetry_debug_governance_or_documentation_drift_check_profile_governance_scan_config_check_docs_readme_task_usage_paths_present.default.1
  consumes:
  - svc.root_readme_usage_paths_path_readme_md_required_tokens_how_users_use_this_project_author_a_spec_change_validate_docs_and_contract_coherence_read_compatibility_and_status_telemetry_debug_governance_or_documentation_drift_check_profile_governance_scan_config_check_docs_readme_task_usage_paths_present.default.1
```
