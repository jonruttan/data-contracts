# Governance Cases

## SRGOV-SPEC-MD-003

```yaml spec-test
id: SRGOV-SPEC-MD-003
title: spec-lang library cases are markdown only
purpose: Ensures type spec_lang.library cases are authored only in .spec.md files under docs/spec/libraries.
type: governance.check
check: spec.library_cases_markdown_only
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
      exports:
        policy.pass_when_no_violations:
          from: library.symbol
          path: /policy.pass_when_no_violations
          required: true
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- target: summary_json
  must:
  - evaluate:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - spec.library_cases_markdown_only
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
```
