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
    - "{'root': '.', 'liveness_trace_tokens': {'trace_path': 'specs/governance/cases/fixtures/run_trace_liveness_sample.json',
      'required_tokens': ['stall.runner.no_progress', 'stall.subprocess.no_output_no_event']},
      'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.liveness_stall_token_emitted'}},
      'use': [{'ref': '/specs/libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec',
      'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id',
      'policy.assert.scan_pass']}]}"
services:
  actions:
  - id: svc.root_liveness_trace_tokens_trace_path_specs_governance_cases_fixtures_run_trace_liveness_sample_json_required_tokens_stall_runner_no_progress_stall_subprocess_no_output_no_event_check_profile_governance_scan_config_check_runtime_liveness_stall_token_emitted_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    type: legacy.root_liveness_trace_tokens_trace_path_specs_governance_cases_fixtures_run_trace_liveness_sample_json_required_tokens_stall_runner_no_progress_stall_subprocess_no_output_no_event_check_profile_governance_scan_config_check_runtime_liveness_stall_token_emitted_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
    io: io
    profile: default
contracts:
- id: DCGOV-LIVENESS-STALL-001
  title: run trace contains liveness stall reason tokens
  purpose: Ensures watchdog reason tokens for runner/subprocess stall semantics are
    observable in run trace artifacts.
  clauses:
    imports:
    - artifact:
      - violation_count
    predicates:
    - id: assert_1
      assert:
        call:
        - var: policy.assert.no_violations
        - std.object.assoc:
          - violation_count
          - var: violation_count
          - lit: {}
```
