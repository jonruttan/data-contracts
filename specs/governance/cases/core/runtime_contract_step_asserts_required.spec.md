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
    - "{'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.contract_step_asserts_required'}}}"
services:
  actions:
  - id: svc.check_profile_governance_scan_config_check_runtime_contract_step_asserts_required.default.1
    type: legacy.check_profile_governance_scan_config_check_runtime_contract_step_asserts_required
    io: io
    profile: default
contracts:
- id: DCGOV-RUNTIME-CONTRACT-STEP-001
  title: contract steps must declare asserts
  purpose: Enforces step-form contract nodes to use asserts list and non-empty children.
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
