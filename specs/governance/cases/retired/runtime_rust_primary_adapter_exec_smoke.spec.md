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
    - "{'root': '.', 'rust_adapter_exec_smoke': {'command': ['dc-runner-rust', 'critical-gate'], 'expected_exit_codes': [0], 'required_output_tokens': ['critical-gate-summary.json'], 'forbidden_output_tokens': [], 'timeout_seconds': 30}, 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.required_lane_adapter_exec_smoke'}}, 'use': [{'ref': '/specs/libraries/policy/policy_core.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.pass_when_no_violations']}]}"
services:
  actions:
  - id: svc.root_rust_adapter_exec_smoke_command_dc_runner_rust_critical_gate_expected_exit_codes_0_required_output_tokens_critical_gate_summary_json_forbidden_output_tokens_timeout_seconds_30_check_profile_governance_scan_config_check_runtime_required_lane_adapter_exec_smoke_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations.default.1
    type: legacy.root_rust_adapter_exec_smoke_command_dc_runner_rust_critical_gate_expected_exit_codes_0_required_output_tokens_critical_gate_summary_json_forbidden_output_tokens_timeout_seconds_30_check_profile_governance_scan_config_check_runtime_required_lane_adapter_exec_smoke_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations
    io: io
    profile: default
contracts:
- id: DCGOV-RUST-PRIMARY-005
  title: rust-primary adapter executes and returns deterministic smoke output
  purpose: Ensures the Rust adapter is executable in governance and emits deterministic output/exit-code behavior for a smoke command.
  clauses:
    imports:
    - from: artifact
      names:
      - violation_count
    predicates:
    - id: assert_1
      assert:
        std.logic.eq:
        - var: violation_count
        - 0
    - id: assert_2
      assert:
      - std.logic.eq:
        - std.object.get:
          - var: summary_json
          - passed
        - true
      - std.logic.eq:
        - std.object.get:
          - var: summary_json
          - check_id
        - runtime.required_lane_adapter_exec_smoke
      imports:
      - from: artifact
        names:
        - summary_json
```
