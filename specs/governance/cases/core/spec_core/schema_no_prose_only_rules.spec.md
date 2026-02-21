# Governance Cases

## DCGOV-SCHEMA-REG-004

```yaml contract-spec
id: DCGOV-SCHEMA-REG-004
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: schema contract avoids prose-only rules
purpose: Ensures schema contract docs explicitly tie behavior to registry source-of-truth
  wording.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: schema.no_prose_only_rules
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
    - call:
      - {var: policy.assert.summary_check_id}
      - std.object.assoc:
        - summary_json
        - {var: summary_json}
        - lit: {}
      - schema.no_prose_only_rules
    - call:
      - {var: policy.assert.summary_passed}
      - std.object.assoc:
        - summary_json
        - {var: summary_json}
        - lit: {}
```
