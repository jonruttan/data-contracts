# Governance Cases

## DCGOV-SPECLAYOUT-DOMAIN-001

```yaml contract-spec
id: DCGOV-SPECLAYOUT-DOMAIN-001
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: spec layout uses domain tree directories
purpose: Ensures conformance, governance, and library specs are organized under domain subdirectories
  with index files.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: spec.layout_domain_trees
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
      call:
      - {var: policy.assert.summary_check_id}
      - std.object.assoc:
        - summary_json
        - {var: summary_json}
        - lit: {}
      - spec.layout_domain_trees
```
