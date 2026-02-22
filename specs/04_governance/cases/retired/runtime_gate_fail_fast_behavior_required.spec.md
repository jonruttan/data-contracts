```yaml contract-spec
spec_version: 2
schema_ref: "/specs/01_schema/schema_v2.md"
defaults:
  type: contract.check
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'gate_fail_fast': {'files': ['/dc-runner-python', '/dc-runner-rust'], 'required_tokens': ['fail_fast', 'gate.fail_fast.abort', 'fail_fast.after_failure']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.gate_fail_fast_behavior_required'}}, 'use': [{'ref': '/specs/05_libraries/policy/policy_core.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.pass_when_no_violations']}]}"
services:
  actions:
  - id: svc.root_gate_fail_fast_files_dc_runner_python_dc_runner_rust_required_tokens_fail_fast_gate_fail_fast_abort_fail_fast_after_failure_check_profile_governance_scan_config_check_runtime_gate_fail_fast_behavior_required_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations.default.1
    type: legacy.root_gate_fail_fast_files_dc_runner_python_dc_runner_rust_required_tokens_fail_fast_gate_fail_fast_abort_fail_fast_after_failure_check_profile_governance_scan_config_check_runtime_gate_fail_fast_behavior_required_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations
    io: io
    profile: default
contracts:
- id: DCGOV-RUNTIME-FAILFAST-001
  title: gate summary enforces fail-fast orchestration semantics
  purpose: Ensures CI gate orchestration supports deterministic fail-fast with explicit abort markers.
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
