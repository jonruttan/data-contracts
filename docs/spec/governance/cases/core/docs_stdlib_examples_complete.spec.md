# Governance Cases

## SRGOV-DOCS-GEN-022

```yaml spec-test
id: SRGOV-DOCS-GEN-022
title: stdlib symbols include examples
purpose: Ensures generated stdlib reference includes at least one complete example per symbol.
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
assert:
- id: assert_1
  class: must
  checks:
  - must:
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
