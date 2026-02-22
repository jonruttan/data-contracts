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
    - "{'root': '.', 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.runner_certification_required_lane_passes'}}}"
services:
  actions:
  - id: svc.root_check_profile_governance_scan_config_check_runtime_runner_certification_required_lane_passes.default.1
    type: legacy.root_check_profile_governance_scan_config_check_runtime_runner_certification_required_lane_passes
    io: io
    profile: default
contracts:
- id: DCGOV-RUNTIME-CERT-004
  title: required rust runner certification lane passes
  purpose: Ensures rust required lane certification passes and remains blocking.
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
