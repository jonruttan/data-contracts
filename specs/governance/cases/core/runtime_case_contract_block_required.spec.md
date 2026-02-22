```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-RUNTIME-CONTRACT-BLOCK-001
  title: cases must use contract block
  purpose: Enforces top-level contract block requirement for executable cases.
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
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.case_contract_block_required'}}}"
services:
  entries:
  - id: 
      svc.check_profile_governance_scan_config_check_runtime_case_contract_block_required.default.1
    type: 
      legacy.check_profile_governance_scan_config_check_runtime_case_contract_block_required
    io: io
    profile: default
    config: {}
```
