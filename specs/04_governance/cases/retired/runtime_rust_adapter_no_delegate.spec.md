```yaml contract-spec
spec_version: 1
schema_ref: "/specs/01_schema/schema_v1.md"
defaults:
  type: contract.check
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'rust_adapter': {'path': '/dc-runner-rust', 'required_tokens': ['spec_runner_cli', 'cargo run --quiet'], 'forbidden_tokens': ['scripts/runner_bin.sh']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.required_lane_adapter_no_delegate'}}, 'use': [{'ref': '/specs/05_libraries/policy/policy_core.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.pass_when_no_violations']}]}"
services:
  actions:
  - id: svc.root_rust_adapter_path_dc_runner_rust_required_tokens_spec_runner_cli_cargo_run_quiet_forbidden_tokens_scripts_runner_bin_sh_check_profile_governance_scan_config_check_runtime_required_lane_adapter_no_delegate_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations.default.1
    type: legacy.root_rust_adapter_path_dc_runner_rust_required_tokens_spec_runner_cli_cargo_run_quiet_forbidden_tokens_scripts_runner_bin_sh_check_profile_governance_scan_config_check_runtime_required_lane_adapter_no_delegate_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations
    io: io
    profile: default
contracts:
- id: DCGOV-RUNTIME-CONFIG-006R
  title: rust adapter does not delegate to python shell adapter
  purpose: Ensures dc-runner-rust invokes the Rust CLI directly and does not call scripts/runner_bin.sh.
  clauses:
    imports:
    - artifact:
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
        - runtime.required_lane_adapter_no_delegate
      imports:
      - artifact:
        - summary_json
```
