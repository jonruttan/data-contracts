# Governance Cases

## DCGOV-DOCS-MD-001

```yaml contract-spec
id: DCGOV-DOCS-MD-001
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: markdown checks use structured markdown helper library
purpose: Prevent brittle plain string-contains markdown assertions in governed docs cases.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: docs.markdown_structured_assertions_required
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
      - docs.markdown_structured_assertions_required
    imports:
    - from: artifact
      names:
      - summary_json
```
