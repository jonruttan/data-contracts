```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'runner_status_matrix_schema': {'path': '/specs/schema/runner_status_matrix_v1.yaml', 'required_tokens': [{'type': 'runtime.runner_status_matrix'}, 'matrix_rows', 'freshness_state', 'policy_effect']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.runner_status_matrix_schema_valid'}}}"
contracts:
  clauses:
  - id: DCGOV-RUNTIME-STATUS-002
    title: runner status matrix schema is defined
    purpose: Ensures aggregated status matrix contract shape is declared for governance and docs.
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
- type: legacy.root_runner_status_matrix_schema_path_specs_schema_runner_status_matrix_v1_yaml_required_tokens_type_runtime_runner_status_matrix_matrix_rows_freshness_state_policy_effect_check_profile_governance_scan_config_check_runtime_runner_status_matrix_schema_valid
  actions:
  - id: svc.root_runner_status_matrix_schema_path_specs_schema_runner_status_matrix_v1_yaml_required_tokens_type_runtime_runner_status_matrix_matrix_rows_freshness_state_policy_effect_check_profile_governance_scan_config_check_runtime_runner_status_matrix_schema_valid.default.1
    direction: bidirectional
    profile: default
services:
- id: svc.root_runner_status_matrix_schema_path_specs_schema_runner_status_matrix_v1_yaml_required_tokens_type_runtime_runner_status_matrix_matrix_rows_freshness_state_policy_effect_check_profile_governance_scan_config_check_runtime_runner_status_matrix_schema_valid.default.1
  consumes:
  - svc.root_runner_status_matrix_schema_path_specs_schema_runner_status_matrix_v1_yaml_required_tokens_type_runtime_runner_status_matrix_matrix_rows_freshness_state_policy_effect_check_profile_governance_scan_config_check_runtime_runner_status_matrix_schema_valid.default.1
```

