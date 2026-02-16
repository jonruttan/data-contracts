# Governance Cases

## SRGOV-SCHEMA-REG-004

```yaml spec-test
id: SRGOV-SCHEMA-REG-004
title: schema contract avoids prose-only rules
purpose: Ensures schema contract docs explicitly tie behavior to registry source-of-truth
  wording.
type: governance.check
check: schema.no_prose_only_rules
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
      - schema.no_prose_only_rules
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
```
