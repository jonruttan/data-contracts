# Governance Cases

## SRGOV-DOCS-CURRENT-KEYS-001

```yaml contract-spec
id: SRGOV-DOCS-CURRENT-KEYS-001
title: current spec policy key names stay canonical
purpose: Enforces policy expression naming consistency by allowing only `policy_evaluate`
  in `.spec.md` cases.
type: governance.check
check: docs.current_spec_policy_key_names
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
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
- id: assert_2
  class: MUST
  asserts:
  - MUST:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - docs.current_spec_policy_key_names
  target: summary_json
```
