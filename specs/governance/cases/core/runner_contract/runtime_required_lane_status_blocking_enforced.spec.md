```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'required_lane_policy': {'path': '/scripts/runner_status_ingest.sh', 'required_tokens': ['lane_class', 'required', 'blocking_fail']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.required_lane_status_blocking_enforced'}}}"
contracts:
  clauses:
  - id: DCGOV-RUNTIME-STATUS-006
    title: required lane status remains blocking
    purpose: Ensures required-lane status outcomes map to blocking policy effects.
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
- type: legacy.root_required_lane_policy_path_scripts_runner_status_ingest_sh_required_tokens_lane_class_required_blocking_fail_check_profile_governance_scan_config_check_runtime_required_lane_status_blocking_enforced
  actions:
  - id: svc.root_required_lane_policy_path_scripts_runner_status_ingest_sh_required_tokens_lane_class_required_blocking_fail_check_profile_governance_scan_config_check_runtime_required_lane_status_blocking_enforced.default.1
    direction: bidirectional
    profile: default
services:
- id: svc.root_required_lane_policy_path_scripts_runner_status_ingest_sh_required_tokens_lane_class_required_blocking_fail_check_profile_governance_scan_config_check_runtime_required_lane_status_blocking_enforced.default.1
  consumes:
  - svc.root_required_lane_policy_path_scripts_runner_status_ingest_sh_required_tokens_lane_class_required_blocking_fail_check_profile_governance_scan_config_check_runtime_required_lane_status_blocking_enforced.default.1
```

