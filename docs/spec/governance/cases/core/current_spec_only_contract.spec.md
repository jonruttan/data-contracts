# Governance Cases

## SRGOV-DOC-CURRENT-001

```yaml spec-test
id: SRGOV-DOC-CURRENT-001
title: current-spec-only contract forbids prior-schema references and shims
purpose: Ensures pre-v1 docs and parser paths stay focused on current schema only, without
  prior-spec wording or compatibility rewrites.
type: governance.check
check: docs.current_spec_only_contract
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
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- id: assert_1
  class: must
  checks:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
- id: assert_2
  class: must
  checks:
  - must:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - docs.current_spec_only_contract
  target: summary_json
```
