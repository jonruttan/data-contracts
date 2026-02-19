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
  check:
    profile: governance.scan
    config:
      check: docs.adoption_profiles_sync
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  imports:
    subject:
      from: artifact
      key: violation_count
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
  - id: assert_2
    assert:
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
    imports:
      subject:
        from: artifact
        key: summary_json
```
