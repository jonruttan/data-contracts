# Governance Cases

## SRGOV-LIB-VERB-002

```yaml spec-test
id: SRGOV-LIB-VERB-002
title: legacy definitions key is forbidden in library cases
purpose: Ensures spec_lang.export cases do not use the legacy definitions key.
type: governance.check
check: library.legacy_definitions_key_forbidden
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
    - std.object.get:
      - var: subject
      - check_id
    - library.legacy_definitions_key_forbidden
  target: summary_json
```
