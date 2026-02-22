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
    - "{'root': '.', 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.chain_imports_consumer_surface_unchanged'}}}"
services:
  actions:
  - id: svc.root_check_profile_governance_scan_config_check_runtime_chain_imports_consumer_surface_unchanged.default.1
    type: legacy.root_check_profile_governance_scan_config_check_runtime_chain_imports_consumer_surface_unchanged
    io: io
    profile: default
contracts:
- id: DCGOV-HARNESS-EXPORTS-004
  title: chain imports consumer surface remains unchanged
  purpose: Ensures consumer bindings continue to use harness.chain.imports semantics.
  clauses:
    imports:
    - artifact:
      - summary_json
    predicates:
    - id: assert_1
      assert:
        call:
        - var: policy.assert.summary_passed
        - std.object.assoc:
          - summary_json
          - var: summary_json
          - lit: {}
```
