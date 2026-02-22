```yaml contract-spec
spec_version: 2
schema_ref: "/specs/01_schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.runner_certification_artifacts_contract_sync'}}}"
contracts:
  clauses:
  - id: DCGOV-RUNTIME-CERT-003
    title: runner certification artifacts follow contract shape
    purpose: Ensures runner-certify generates contract-shaped JSON and markdown artifacts.
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
- type: legacy.root_check_profile_governance_scan_config_check_runtime_runner_certification_artifacts_contract_sync
  actions:
  - id: svc.root_check_profile_governance_scan_config_check_runtime_runner_certification_artifacts_contract_sync.default.1
    direction: bidirectional
    profile: default
services:
- id: svc.root_check_profile_governance_scan_config_check_runtime_runner_certification_artifacts_contract_sync.default.1
  consumes:
  - svc.root_check_profile_governance_scan_config_check_runtime_runner_certification_artifacts_contract_sync.default.1
```
