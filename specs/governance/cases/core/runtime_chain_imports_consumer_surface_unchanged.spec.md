```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.chain_imports_consumer_surface_unchanged'}}}"
services:
- type: legacy.root_check_profile_governance_scan_config_check_runtime_chain_imports_consumer_surface_unchanged
  operations:
  - id: svc.root_check_profile_governance_scan_config_check_runtime_chain_imports_consumer_surface_unchanged.default.1
    mode: default
    direction: bidirectional
contracts:
  clauses:
  - id: DCGOV-HARNESS-EXPORTS-004
    title: chain imports consumer surface remains unchanged
    purpose: Ensures consumer bindings continue to use harness.chain.imports semantics.
    asserts:
      imports:
      - from: artifact
        names:
        - summary_json
      checks:
      - id: assert_1
        assert:
          call:
          - var: policy.assert.summary_passed
          - std.object.assoc:
            - summary_json
            - var: summary_json
            - lit: {}
```
