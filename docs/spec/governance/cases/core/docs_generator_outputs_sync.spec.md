# Governance Cases

## SRGOV-DOCS-GEN-002

```yaml contract-spec
id: SRGOV-DOCS-GEN-002
title: docs generator outputs are synchronized
purpose: Ensures all registry-backed docs generator outputs are up-to-date in check mode.
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
      check: docs.generator_outputs_sync
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
            - docs.generator_outputs_sync
          - std.logic.eq:
            - std.object.get:
              - {var: subject}
              - passed
            - true
  target: summary_json
```
