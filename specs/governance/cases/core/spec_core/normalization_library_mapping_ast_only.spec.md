# Governance Cases

## DCGOV-NORM-005

```yaml contract-spec
id: DCGOV-NORM-005
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: library function expressions use mapping-ast authoring
purpose: Enforces spec-lang library function defines use canonical mapping-ast expression
  syntax only.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: normalization.library_mapping_ast_only
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
      - normalization.library_mapping_ast_only
    imports:
    - from: artifact
      names:
      - summary_json
```
