# Governance Cases

## SRGOV-DOCS-MD-001

```yaml spec-test
id: SRGOV-DOCS-MD-001
title: markdown checks use structured markdown helper library
purpose: Prevent brittle plain string-contains markdown assertions in governed docs cases.
type: governance.check
check: docs.markdown_structured_assertions_required
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
      - docs.markdown_structured_assertions_required
  target: summary_json
```
