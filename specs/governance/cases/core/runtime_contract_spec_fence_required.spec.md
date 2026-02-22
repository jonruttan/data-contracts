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
    - "{'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.contract_spec_fence_required'}}}"
services:
  entries:
  - id: svc.check_profile_governance_scan_config_check_runtime_contract_spec_fence_required.default.1
    type: legacy.check_profile_governance_scan_config_check_runtime_contract_spec_fence_required
    io: io
    profile: default
    config: {}
contracts:
- id: DCGOV-RUNTIME-CONTRACT-SPEC-001
  title: executable case fences must use contract-spec
  purpose: Enforces hard-cut fence rename to contract-spec across specs cases.
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
