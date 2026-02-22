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
    - "{'root': '.', 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.runner_certification_compat_lanes_non_blocking'}}}"
services:
  actions:
  - id: svc.root_check_profile_governance_scan_config_check_runtime_runner_certification_compat_lanes_non_blocking.default.1
    type: legacy.root_check_profile_governance_scan_config_check_runtime_runner_certification_compat_lanes_non_blocking
    io: io
    profile: default
contracts:
- id: DCGOV-RUNTIME-CERT-005
  title: compatibility lanes remain non-blocking in certification
  purpose: Ensures compatibility lanes are classified and emitted as non-blocking in certification artifacts.
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
