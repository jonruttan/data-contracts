# Governance Cases

## SRGOV-LIB-VERB-001

```yaml spec-test
id: SRGOV-LIB-VERB-001
title: library schema uses verb-first key names
purpose: Ensures spec_lang.library authoring uses defines.public/defines.private and rejects
  legacy definitions keys.
type: governance.check
check: library.verb_first_schema_keys_required
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
- id: assert_1
  class: must
  checks:
  - std.logic.eq:
    - std.object.get:
      - var: subject
      - check_id
    - library.verb_first_schema_keys_required
  target: summary_json
```
