# Governance Cases

## SRGOV-REF-TOKENS-001

```yaml contract-spec
id: SRGOV-REF-TOKENS-001
title: configured token anchors exist
purpose: Ensures configured token anchors resolve to existing files and token matches.
type: contract.check
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
      class: MUST
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
  check:
    profile: governance.scan
    config:
      check: reference.token_anchors_exist
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
    - lit:
        lit:
          lit:
            std.logic.eq:
            - std.object.get:
              - {var: subject}
              - check_id
            - reference.token_anchors_exist
  target: summary_json
```
