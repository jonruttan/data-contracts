# Governance Cases

## SRGOV-SCHEMA-REG-004

```yaml contract-spec
id: SRGOV-SCHEMA-REG-004
title: schema contract avoids prose-only rules
purpose: Ensures schema contract docs explicitly tie behavior to registry source-of-truth
  wording.
type: contract.check
harness:
  root: .
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
      check: schema.no_prose_only_rules
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
      lit:
        lit:
          MUST:
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
