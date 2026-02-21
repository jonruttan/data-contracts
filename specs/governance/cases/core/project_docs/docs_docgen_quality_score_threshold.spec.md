# Governance Cases

## DCGOV-DOCS-GEN-026

```yaml contract-spec
id: DCGOV-DOCS-GEN-026
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: docgen quality score meets minimum threshold
purpose: Ensures generated runner/harness/stdlib catalogs meet minimum semantic quality score.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: docs.docgen_quality_score_threshold
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
      - docs.docgen_quality_score_threshold
    - call:
      - {var: policy.assert.summary_passed}
      - std.object.assoc:
        - summary_json
        - {var: summary_json}
        - lit: {}
```
