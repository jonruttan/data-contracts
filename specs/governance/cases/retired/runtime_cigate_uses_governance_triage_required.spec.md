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
    - "{'root': '.', 'cigate_governance_triage': {'files': ['/dc-runner-python', '/dc-runner-rust'], 'required_tokens': ['governance_broad', 'triage_attempted', 'triage_mode', 'triage_result', 'failing_check_ids', 'failing_check_prefixes', 'stall_detected', 'stall_phase']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.cigate_uses_governance_triage_required'}}, 'use': [{'ref': '/specs/libraries/policy/policy_core.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.pass_when_no_violations']}]}"
services:
  actions:
  - id: svc.root_cigate_governance_triage_files_dc_runner_python_dc_runner_rust_required_tokens_governance_broad_triage_attempted_triage_mode_triage_result_failing_check_ids_failing_check_prefixes_stall_detected_stall_phase_check_profile_governance_scan_config_check_runtime_cigate_uses_governance_triage_required_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations.default.1
    type: legacy.root_cigate_governance_triage_files_dc_runner_python_dc_runner_rust_required_tokens_governance_broad_triage_attempted_triage_mode_triage_result_failing_check_ids_failing_check_prefixes_stall_detected_stall_phase_check_profile_governance_scan_config_check_runtime_cigate_uses_governance_triage_required_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations
    io: io
    profile: default
contracts:
- id: DCGOV-RUNTIME-TRIAGE-003
  title: ci gate summary uses governance triage and emits triage metadata
  purpose: Ensures both Python and Rust ci-gate-summary paths reference governance triage flow.
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
