```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'status_visibility': {'path': '/scripts/runner_status_ingest.sh', 'required_tokens': ['freshness_state', 'missing', 'policy_effect', 'non_blocking_fail']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.compatibility_missing_status_visibility_required'}}}"
contracts:
  clauses:
  - id: DCGOV-RUNTIME-STATUS-005
    title: missing compatibility status remains visible
    purpose: Ensures missing compatibility status is visible and policy-scored in matrix output.
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
- type: legacy.root_status_visibility_path_scripts_runner_status_ingest_sh_required_tokens_freshness_state_missing_policy_effect_non_blocking_fail_check_profile_governance_scan_config_check_runtime_compatibility_missing_status_visibility_required
  actions:
  - id: svc.root_status_visibility_path_scripts_runner_status_ingest_sh_required_tokens_freshness_state_missing_policy_effect_non_blocking_fail_check_profile_governance_scan_config_check_runtime_compatibility_missing_status_visibility_required.default.1
    direction: bidirectional
    profile: default
services:
- id: svc.root_status_visibility_path_scripts_runner_status_ingest_sh_required_tokens_freshness_state_missing_policy_effect_non_blocking_fail_check_profile_governance_scan_config_check_runtime_compatibility_missing_status_visibility_required.default.1
  consumes:
  - svc.root_status_visibility_path_scripts_runner_status_ingest_sh_required_tokens_freshness_state_missing_policy_effect_non_blocking_fail_check_profile_governance_scan_config_check_runtime_compatibility_missing_status_visibility_required.default.1
```

