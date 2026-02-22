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
    - "{'root': '.', 'rust_subcommand_parity': {'adapter_path': '/dc-runner-rust', 'cli_main_path': '/dc-runner-rust'}, 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.required_lane_adapter_subcommand_parity'}}, 'use': [{'ref': '/specs/libraries/policy/policy_core.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.pass_when_no_violations']}]}"
services:
  actions:
  - id: svc.root_rust_subcommand_parity_adapter_path_dc_runner_rust_cli_main_path_dc_runner_rust_check_profile_governance_scan_config_check_runtime_required_lane_adapter_subcommand_parity_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations.default.1
    type: legacy.root_rust_subcommand_parity_adapter_path_dc_runner_rust_cli_main_path_dc_runner_rust_check_profile_governance_scan_config_check_runtime_required_lane_adapter_subcommand_parity_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations
    io: io
    profile: default
contracts:
- id: DCGOV-RUST-PRIMARY-007
  title: rust adapter and rust cli expose the same runner subcommand set
  purpose: Ensures the shell adapter and Rust CLI subcommand surfaces stay synchronized to prevent runtime interface drift.
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
        - runtime.required_lane_adapter_subcommand_parity
      imports:
      - from: artifact
        names:
        - summary_json
```
