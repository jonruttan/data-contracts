# Governance Cases

## DCGOV-DOCS-REF-018

```yaml contract-spec
id: DCGOV-DOCS-REF-018
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: docs book chapter order is canonical
purpose: Enforces the hard-cut Learn -> Do -> Debug chapter order and appendix namespace ordering
  in the reference manifest.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: docs.book_chapter_order_canonical
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
    - violation_count
  steps:
  - id: assert_1
    assert:
      call:
      - {var: policy.assert.no_violations}
      - std.object.assoc:
        - violation_count
        - {var: violation_count}
        - lit: {}
  - id: assert_2
    assert:
    - call:
      - {var: policy.assert.summary_passed}
      - std.object.assoc:
        - summary_json
        - {var: summary_json}
        - lit: {}
    - call:
      - {var: policy.assert.summary_check_id}
      - std.object.assoc:
        - summary_json
        - {var: summary_json}
        - lit: {}
      - docs.book_chapter_order_canonical
    imports:
    - from: artifact
      names:
      - summary_json
```
