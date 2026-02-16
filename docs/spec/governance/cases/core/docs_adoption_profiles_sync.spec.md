# Governance Cases

## SRGOV-DOCS-REF-009

```yaml spec-test
id: SRGOV-DOCS-REF-009
title: core and full adoption profile docs stay synchronized
purpose: Keeps contributor-facing docs aligned on core-check and full-check adoption profile
  wording.
type: governance.check
check: docs.adoption_profiles_sync
harness:
  root: .
  adoption_profiles:
    files:
    - README.md
    - docs/development.md
    required_tokens:
    - Core profile
    - Full profile
    - make core-check
    - make check
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
    - from_step: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- target: violation_count
  must:
  - evaluate:
    - std.logic.eq:
      - {var: subject}
      - 0
- target: summary_json
  must:
  - evaluate:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - docs.adoption_profiles_sync
```
