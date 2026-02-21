# runtime_chain_imports_consumer_surface_unchanged

```yaml contract-spec
id: DCGOV-HARNESS-EXPORTS-004
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: chain imports consumer surface remains unchanged
purpose: Ensures consumer bindings continue to use harness.chain.imports semantics.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: runtime.chain_imports_consumer_surface_unchanged
contract:
  defaults: {}
  imports:
  - from: artifact
    names:
    - summary_json
  steps:
  - id: assert_1
    assert:
      call:
      - {var: policy.assert.summary_passed}
      - std.object.assoc:
        - summary_json
        - {var: summary_json}
        - lit: {}
```
