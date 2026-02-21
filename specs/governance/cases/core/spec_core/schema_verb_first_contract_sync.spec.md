# Governance Cases

## DCGOV-SCHEMA-VERB-001

```yaml contract-spec
id: DCGOV-SCHEMA-VERB-001
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: verb-first contract wording remains synchronized
purpose: Ensures schema/contract/current docs use defines wording and reject non-canonical
  definitions wording.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: schema.verb_first_contract_sync
  use:
  - ref: /specs/libraries/policy/policy_assertions.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.assert.no_violations
    - policy.assert.summary_passed
    - policy.assert.summary_check_id
    - policy.assert.scan_pass
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
      - {var: policy.assert.summary_check_id}
      - std.object.assoc:
        - summary_json
        - {var: summary_json}
        - lit: {}
      - schema.verb_first_contract_sync
```
