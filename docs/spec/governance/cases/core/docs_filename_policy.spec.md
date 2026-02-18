# Governance Cases

## SRGOV-DOCS-LAYOUT-003

```yaml spec-test
id: SRGOV-DOCS-LAYOUT-003
title: docs filenames follow canonical lowercase policy
purpose: Enforces lowercase, underscore, and hyphen filename policy across docs.
type: governance.check
check: docs.filename_policy
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
      - docs.filename_policy
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
  target: summary_json
```
