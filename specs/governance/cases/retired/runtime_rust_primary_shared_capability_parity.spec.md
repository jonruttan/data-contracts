```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-RUST-PRIMARY-004
  title: rust-primary gate path includes shared-capability parity step
  purpose: Ensures gate orchestration keeps conformance parity as part of 
    Rust-primary-compatible gate flow.
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
        - runtime.runner_interface_gate_sync
      imports:
      - from: artifact
        names:
        - summary_json
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'runner_interface': {'required_paths': ['/scripts/runner_bin.sh',
      '/dc-runner-rust'], 'files': ['dc-runner-python'], 'required_tokens': ['conformance-parity'],
      'forbidden_tokens': []}, 'check': {'profile': 'governance.scan', 'config': {'check':
      'runtime.runner_interface_gate_sync'}}, 'use': [{'ref': '/specs/libraries/policy/policy_core.spec.md',
      'as': 'lib_policy_core_spec', 'symbols': ['policy.pass_when_no_violations']}]}"
services:
  entries:
  - id: 
      svc.root_runner_interface_required_paths_scripts_runner_bin_sh_dc_runner_rust_files_dc_runner_python_required_tokens_conformance_parity_forbidden_tokens_check_profile_governance_scan_config_check_runtime_runner_interface_gate_sync_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations.default.1
    type: 
      legacy.root_runner_interface_required_paths_scripts_runner_bin_sh_dc_runner_rust_files_dc_runner_python_required_tokens_conformance_parity_forbidden_tokens_check_profile_governance_scan_config_check_runtime_runner_interface_gate_sync_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations
    io: io
    profile: default
    config: {}
```
