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
    - "{'root': '.', 'profile_on_fail': {'files': ['/dc-runner-python', '/dc-runner-rust'], 'required_tokens': ['profile-on-fail', '.artifacts/run-trace.json', '.artifacts/run-trace-summary.md']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.profile_artifacts_on_fail_required'}}, 'use': [{'ref': '/specs/libraries/policy/policy_core.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.pass_when_no_violations']}]}"
services:
  entries:
  - id: svc.root_profile_on_fail_files_dc_runner_python_dc_runner_rust_required_tokens_profile_on_fail_artifacts_run_trace_json_artifacts_run_trace_summary_md_check_profile_governance_scan_config_check_runtime_profile_artifacts_on_fail_required_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations.default.1
    type: legacy.root_profile_on_fail_files_dc_runner_python_dc_runner_rust_required_tokens_profile_on_fail_artifacts_run_trace_json_artifacts_run_trace_summary_md_check_profile_governance_scan_config_check_runtime_profile_artifacts_on_fail_required_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations
    io: io
    profile: default
    config: {}
contracts:
- id: DCGOV-RUNTIME-FAILFAST-003
  title: gate failures emit profile artifacts when profile-on-fail is enabled
  purpose: Ensures failure paths generate deterministic run-trace and run-trace-summary artifacts.
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
```
