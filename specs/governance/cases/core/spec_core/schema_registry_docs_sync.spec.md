# Governance Cases

## DCGOV-SCHEMA-REG-002

```yaml contract-spec
id: DCGOV-SCHEMA-REG-002
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: schema registry docs snapshot is synchronized
purpose: Ensures schema_v1 markdown contains synchronized generated registry snapshot markers
  and tokens.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: schema.registry_docs_sync
  use:
  - ref: /specs/libraries/policy/policy_assertions.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.assert.no_violations
    - policy.assert.summary_passed
    - policy.assert.summary_check_id
    - policy.assert.scan_pass
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - summary_json
  steps:
  - id: assert_1
    assert:
    - call:
      - {var: policy.assert.summary_check_id}
      - std.object.assoc:
        - summary_json
        - {var: summary_json}
        - lit: {}
      - schema.registry_docs_sync
    - call:
      - {var: policy.assert.summary_passed}
      - std.object.assoc:
        - summary_json
        - {var: summary_json}
        - lit: {}
```
