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
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- id: assert_1
  class: must
  checks:
  - must:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - schema.no_prose_only_rules
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
  target: summary_json
```
