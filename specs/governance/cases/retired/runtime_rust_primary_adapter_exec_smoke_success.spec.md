```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-RUST-PRIMARY-006
  title: rust-primary adapter executes success-path smoke command 
    deterministically
  purpose: Ensures the Rust adapter can execute a supported success-path command
    with deterministic success output and exit-code behavior.
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
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'rust_adapter_exec_smoke': {'command': ['dc-runner-rust', 'style-check'],
      'expected_exit_codes': [0], 'required_output_tokens': ['OK: evaluate style formatting
      is canonical'], 'forbidden_output_tokens': ['unsupported runner adapter subcommand',
      'rust runner adapter subcommand not yet implemented'], 'timeout_seconds': 180},
      'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.required_lane_adapter_exec_smoke'}},
      'use': [{'ref': '/specs/libraries/policy/policy_core.spec.md', 'as': 'lib_policy_core_spec',
      'symbols': ['policy.pass_when_no_violations']}]}"
services:
  entries:
  - id: 
      svc.root_rust_adapter_exec_smoke_command_dc_runner_rust_style_check_expected_exit_codes_0_required_output_tokens_ok_evaluate_style_formatting_is_canonical_forbidden_output_tokens_unsupported_runner_adapter_subcommand_rust_runner_adapter_subcommand_not_yet_implemented_timeout_seconds_180_check_profile_governance_scan_config_check_runtime_required_lane_adapter_exec_smoke_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations.default.1
    type: 
      legacy.root_rust_adapter_exec_smoke_command_dc_runner_rust_style_check_expected_exit_codes_0_required_output_tokens_ok_evaluate_style_formatting_is_canonical_forbidden_output_tokens_unsupported_runner_adapter_subcommand_rust_runner_adapter_subcommand_not_yet_implemented_timeout_seconds_180_check_profile_governance_scan_config_check_runtime_required_lane_adapter_exec_smoke_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations
    io: io
    profile: default
    config: {}
```
