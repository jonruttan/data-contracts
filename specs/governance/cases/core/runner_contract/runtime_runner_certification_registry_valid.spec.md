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
    - "{'root': '.', 'runner_certification': {'path': '/specs/schema/runner_certification_registry_v2.yaml', 'required_runner_ids': ['rust', 'python', 'php', 'node', 'c']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.runner_certification_registry_valid'}}}"
services:
  entries:
  - id: svc.root_runner_certification_path_specs_schema_runner_certification_registry_v2_yaml_required_runner_ids_rust_python_php_node_c_check_profile_governance_scan_config_check_runtime_runner_certification_registry_valid.default.1
    type: legacy.root_runner_certification_path_specs_schema_runner_certification_registry_v2_yaml_required_runner_ids_rust_python_php_node_c_check_profile_governance_scan_config_check_runtime_runner_certification_registry_valid
    io: io
    profile: default
contracts:
- id: DCGOV-RUNTIME-CERT-001
  title: runner certification registry shape is valid
  purpose: Ensures runner certification registry entries are complete and deterministic.
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
