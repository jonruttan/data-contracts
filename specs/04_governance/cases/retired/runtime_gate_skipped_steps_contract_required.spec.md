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
    - "{'root': '.', 'gate_skipped_contract': {'files': ['/dc-runner-python', '/dc-runner-rust'], 'required_tokens': ['skipped_step_count', 'first_failure_step', 'aborted_after_step', 'blocked_by', 'skip_reason']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.gate_skipped_steps_contract_required'}}, 'use': [{'ref': '/specs/05_libraries/policy/policy_core.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.pass_when_no_violations']}]}"
services:
  actions:
  - id: svc.root_gate_skipped_contract_files_dc_runner_python_dc_runner_rust_required_tokens_skipped_step_count_first_failure_step_aborted_after_step_blocked_by_skip_reason_check_profile_governance_scan_config_check_runtime_gate_skipped_steps_contract_required_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations.default.1
    type: legacy.root_gate_skipped_contract_files_dc_runner_python_dc_runner_rust_required_tokens_skipped_step_count_first_failure_step_aborted_after_step_blocked_by_skip_reason_check_profile_governance_scan_config_check_runtime_gate_skipped_steps_contract_required_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations
    io: io
    profile: default
contracts:
- id: DCGOV-RUNTIME-FAILFAST-002
  title: gate summary payload includes skipped step contract
  purpose: Ensures gate summary output includes skipped-step and abort metadata fields.
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
```
