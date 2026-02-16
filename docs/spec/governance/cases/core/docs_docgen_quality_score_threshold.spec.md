# Governance Cases

## SRGOV-DOCS-GEN-026

```yaml spec-test
id: SRGOV-DOCS-GEN-026
title: docgen quality score meets minimum threshold
purpose: Ensures generated runner/harness/stdlib catalogs meet minimum semantic quality score.
type: governance.check
check: docs.docgen_quality_score_threshold
harness:
  root: .
  spec_lang:
    includes:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
assert:
- target: summary_json
  must:
  - evaluate:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - docs.docgen_quality_score_threshold
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
```
