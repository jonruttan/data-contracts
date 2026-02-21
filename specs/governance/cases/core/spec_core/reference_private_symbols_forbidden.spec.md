# Governance Cases

## DCGOV-REF-SYMBOLS-004

```yaml contract-spec
id: DCGOV-REF-SYMBOLS-004
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: private library symbols are not referenced externally
purpose: Ensures conformance/governance/impl cases do not reference defines.private symbols
  from library docs.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: reference.private_symbols_forbidden
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
      - reference.private_symbols_forbidden
```
