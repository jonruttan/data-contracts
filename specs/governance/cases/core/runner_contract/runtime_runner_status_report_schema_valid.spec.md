```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'runner_status_report_schema': {'path': '/specs/schema/runner_status_report_v1.yaml', 'required_tokens': [{'type': 'runtime.runner_status_report'}, 'runner_id', 'implementation_repo', 'generated_at', 'fresh_until', 'command_results', 'artifact_refs']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.runner_status_report_schema_valid'}}}"
contracts:
  clauses:
  - id: DCGOV-RUNTIME-STATUS-001
    title: runner status report schema is defined
    purpose: Ensures runner status exchange producer payload shape is declared and stable.
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
- type: legacy.root_runner_status_report_schema_path_specs_schema_runner_status_report_v1_yaml_required_tokens_type_runtime_runner_status_report_runner_id_implementation_repo_generated_at_fresh_until_command_results_artifact_refs_check_profile_governance_scan_config_check_runtime_runner_status_report_schema_valid
  actions:
  - id: svc.root_runner_status_report_schema_path_specs_schema_runner_status_report_v1_yaml_required_tokens_type_runtime_runner_status_report_runner_id_implementation_repo_generated_at_fresh_until_command_results_artifact_refs_check_profile_governance_scan_config_check_runtime_runner_status_report_schema_valid.default.1
    direction: bidirectional
    profile: default
services:
- id: svc.root_runner_status_report_schema_path_specs_schema_runner_status_report_v1_yaml_required_tokens_type_runtime_runner_status_report_runner_id_implementation_repo_generated_at_fresh_until_command_results_artifact_refs_check_profile_governance_scan_config_check_runtime_runner_status_report_schema_valid.default.1
  consumes:
  - svc.root_runner_status_report_schema_path_specs_schema_runner_status_report_v1_yaml_required_tokens_type_runtime_runner_status_report_runner_id_implementation_repo_generated_at_fresh_until_command_results_artifact_refs_check_profile_governance_scan_config_check_runtime_runner_status_report_schema_valid.default.1
```

