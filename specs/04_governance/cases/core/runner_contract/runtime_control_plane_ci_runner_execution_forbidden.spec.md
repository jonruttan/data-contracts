```yaml contract-spec
spec_version: 2
schema_ref: "/specs/01_schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'ci_runtime_exec': {'files': ['/.github/workflows/ci.yml', '/scripts/ci_gate.sh', '/scripts/ci_gate.sh', '/scripts/ci_gate.sh'], 'forbidden_tokens': ['scripts/runner_bin.sh']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.control_plane_ci_runner_execution_forbidden'}}}"
contracts:
  clauses:
  - id: DCGOV-RUNTIME-CI-001
    title: control-plane ci forbids runtime runner execution
    purpose: Ensures this repository CI does not execute runtime lanes directly.
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
- type: legacy.root_ci_runtime_exec_files_github_workflows_ci_yml_scripts_ci_gate_sh_scripts_ci_gate_sh_scripts_ci_gate_sh_forbidden_tokens_scripts_runner_bin_sh_check_profile_governance_scan_config_check_runtime_control_plane_ci_runner_execution_forbidden
  actions:
  - id: svc.root_ci_runtime_exec_files_github_workflows_ci_yml_scripts_ci_gate_sh_scripts_ci_gate_sh_scripts_ci_gate_sh_forbidden_tokens_scripts_runner_bin_sh_check_profile_governance_scan_config_check_runtime_control_plane_ci_runner_execution_forbidden.default.1
    direction: bidirectional
    profile: default
services:
- id: svc.root_ci_runtime_exec_files_github_workflows_ci_yml_scripts_ci_gate_sh_scripts_ci_gate_sh_scripts_ci_gate_sh_forbidden_tokens_scripts_runner_bin_sh_check_profile_governance_scan_config_check_runtime_control_plane_ci_runner_execution_forbidden.default.1
  consumes:
  - svc.root_ci_runtime_exec_files_github_workflows_ci_yml_scripts_ci_gate_sh_scripts_ci_gate_sh_scripts_ci_gate_sh_forbidden_tokens_scripts_runner_bin_sh_check_profile_governance_scan_config_check_runtime_control_plane_ci_runner_execution_forbidden.default.1
```
