# Governance Cases

## SRGOV-SPEC-MD-003

```yaml contract-spec
id: SRGOV-SPEC-MD-003
title: spec-lang library cases are markdown only
purpose: Ensures type spec_lang.export cases are authored only in .spec.md files under docs/spec/libraries.
type: governance.check
check: spec.library_cases_markdown_only
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
  class: must
  asserts:
  - must:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - spec.library_cases_markdown_only
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
  target: summary_json
```
