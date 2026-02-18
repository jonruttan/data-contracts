# Governance Cases

## SRGOV-REF-TOKENS-001

```yaml spec-test
id: SRGOV-REF-TOKENS-001
title: configured token anchors exist
purpose: Ensures configured token anchors resolve to existing files and token matches.
type: governance.check
check: reference.token_anchors_exist
harness:
  root: .
  token_anchors:
    files:
    - path: /docs/spec/contract/03b_spec_lang_v1.md
      tokens:
      - operator-keyed mapping AST
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
  - std.logic.eq:
    - std.object.get:
      - var: subject
      - check_id
    - reference.token_anchors_exist
  target: summary_json
```
