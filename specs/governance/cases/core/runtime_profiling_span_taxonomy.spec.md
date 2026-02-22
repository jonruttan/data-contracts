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
    - "{'root': '.', 'profiling_span_taxonomy': {'trace_path': 'specs/governance/cases/fixtures/run_trace_sample.json',
      'required_spans': ['run.total', 'runner.dispatch', 'case.run', 'case.chain',
      'case.harness', 'check.execute', 'subprocess.exec', 'subprocess.wait']}, 'check':
      {'profile': 'governance.scan', 'config': {'check': 'runtime.profiling_span_taxonomy'}},
      'use': [{'ref': '/specs/libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec',
      'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id',
      'policy.assert.scan_pass']}]}"
services:
- id: svc.root_profiling_span_taxonomy_trace_path_specs_governance_cases_fixtures_run_trace_sample_json_required_spans_run_total_runner_dispatch_case_run_case_chain_case_harness_check_execute_subprocess_exec_subprocess_wait_check_profile_governance_scan_config_check_runtime_profiling_span_taxonomy_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
  type: legacy.root_profiling_span_taxonomy_trace_path_specs_governance_cases_fixtures_run_trace_sample_json_required_spans_run_total_runner_dispatch_case_run_case_chain_case_harness_check_execute_subprocess_exec_subprocess_wait_check_profile_governance_scan_config_check_runtime_profiling_span_taxonomy_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
  mode: default
  direction: bidirectional
contracts:
- id: DCGOV-PROFILE-SPANS-001
  title: run trace records required span taxonomy for timeout diagnosis
  purpose: Ensures the canonical run trace includes required run, case, check, and
    subprocess spans used by timeout diagnostics.
  clauses:
    imports:
    - from: artifact
      names:
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

