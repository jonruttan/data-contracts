```yaml contract-spec
spec_version: 2
schema_ref: "/specs/01_schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'runner_certification': {'path': '/specs/01_schema/runner_certification_registry_v2.yaml', 'required_runner_ids': ['rust', 'python', 'php', 'node', 'c']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.runner_certification_registry_valid'}}}"
contracts:
  clauses:
  - id: DCGOV-RUNTIME-CERT-001
    title: runner certification registry shape is valid
    purpose: Ensures runner certification registry entries are complete and deterministic.
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
- type: legacy.root_runner_certification_path_specs_schema_runner_certification_registry_v2_yaml_required_runner_ids_rust_python_php_node_c_check_profile_governance_scan_config_check_runtime_runner_certification_registry_valid
  actions:
  - id: svc.root_runner_certification_path_specs_schema_runner_certification_registry_v2_yaml_required_runner_ids_rust_python_php_node_c_check_profile_governance_scan_config_check_runtime_runner_certification_registry_valid.default.1
    direction: bidirectional
    profile: default
services:
- id: svc.root_runner_certification_path_specs_schema_runner_certification_registry_v2_yaml_required_runner_ids_rust_python_php_node_c_check_profile_governance_scan_config_check_runtime_runner_certification_registry_valid.default.1
  consumes:
  - svc.root_runner_certification_path_specs_schema_runner_certification_registry_v2_yaml_required_runner_ids_rust_python_php_node_c_check_profile_governance_scan_config_check_runtime_runner_certification_registry_valid.default.1
```
