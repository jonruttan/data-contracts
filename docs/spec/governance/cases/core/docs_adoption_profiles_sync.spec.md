# Governance Cases

## SRGOV-DOCS-REF-009

```yaml contract-spec
id: SRGOV-DOCS-REF-009
title: core and full adoption profile docs stay synchronized
purpose: Keeps contributor-facing docs aligned on core-check and full-check adoption profile
  wording.
type: contract.check
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
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
  check:
    profile: governance.scan
    config:
      check: docs.adoption_profiles_sync
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - {var: subject}
    - 0
  target: violation_count
- id: assert_2
  class: MUST
  asserts:
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
  target: summary_json
```
