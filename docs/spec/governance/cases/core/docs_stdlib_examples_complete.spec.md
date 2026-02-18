# Governance Cases

## SRGOV-DOCS-GEN-022

```yaml contract-spec
id: SRGOV-DOCS-GEN-022
title: stdlib symbols include examples
purpose: Ensures generated stdlib reference includes at least one complete example
  per symbol.
type: governance.check
check: docs.stdlib_examples_complete
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
  - MUST:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - docs.stdlib_examples_complete
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
  target: summary_json
```
