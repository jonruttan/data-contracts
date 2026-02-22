```yaml contract-spec
spec_version: 2
schema_ref: "/specs/01_schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'profiling_redaction': {'trace_path': 'specs/04_governance/cases/fixtures/run_trace_sample.json'}, 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.profiling_redaction_policy'}}, 'use': [{'ref': '/specs/05_libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id', 'policy.assert.scan_pass']}]}"
contracts:
  clauses:
  - id: DCGOV-PROFILE-REDACT-001
    title: run trace redaction policy prevents secret leakage
    purpose: Ensures profiling env metadata does not store raw values and trace payloads do not include common secret-like tokens.
    asserts:
      imports:
      - from: artifact
        names:
        - violation_count
      checks:
      - id: assert_1
        assert:
          call:
          - var: policy.assert.no_violations
          - std.object.assoc:
            - violation_count
            - var: violation_count
            - lit: {}
adapters:
- type: legacy.root_profiling_redaction_trace_path_specs_governance_cases_fixtures_run_trace_sample_json_check_profile_governance_scan_config_check_runtime_profiling_redaction_policy_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
  actions:
  - id: svc.root_profiling_redaction_trace_path_specs_governance_cases_fixtures_run_trace_sample_json_check_profile_governance_scan_config_check_runtime_profiling_redaction_policy_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    direction: bidirectional
    profile: default
services:
- id: svc.root_profiling_redaction_trace_path_specs_governance_cases_fixtures_run_trace_sample_json_check_profile_governance_scan_config_check_runtime_profiling_redaction_policy_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
  consumes:
  - svc.root_profiling_redaction_trace_path_specs_governance_cases_fixtures_run_trace_sample_json_check_profile_governance_scan_config_check_runtime_profiling_redaction_policy_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
```

