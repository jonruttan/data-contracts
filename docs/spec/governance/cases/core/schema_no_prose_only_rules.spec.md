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
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
      exports:
        policy.pass_when_no_violations:
          from: library.symbol
          path: /policy.pass_when_no_violations
          required: true
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- id: assert_1
  class: must
  checks:
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
  target: summary_json
```
