```yaml contract-spec
spec_version: 2
schema_ref: "/specs/01_schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.runner_certification_compat_lanes_non_blocking'}}}"
contracts:
  clauses:
  - id: DCGOV-RUNTIME-CERT-005
    title: compatibility lanes remain non-blocking in certification
    purpose: Ensures compatibility lanes are classified and emitted as non-blocking in certification artifacts.
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
- type: legacy.root_check_profile_governance_scan_config_check_runtime_runner_certification_compat_lanes_non_blocking
  actions:
  - id: svc.root_check_profile_governance_scan_config_check_runtime_runner_certification_compat_lanes_non_blocking.default.1
    direction: bidirectional
    profile: default
services:
- id: svc.root_check_profile_governance_scan_config_check_runtime_runner_certification_compat_lanes_non_blocking.default.1
  consumes:
  - svc.root_check_profile_governance_scan_config_check_runtime_runner_certification_compat_lanes_non_blocking.default.1
```
