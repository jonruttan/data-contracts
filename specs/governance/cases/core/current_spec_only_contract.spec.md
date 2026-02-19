# Governance Cases

## SRGOV-DOC-CURRENT-001

```yaml contract-spec
id: SRGOV-DOC-CURRENT-001
title: current-spec-only contract forbids prior-schema references and shims
purpose: Ensures pre-v1 docs and parser paths stay focused on current schema only, without
  prior-spec wording or compatibility rewrites.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: docs.current_spec_only_contract
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
    imports:
      subject:
        from: artifact
        key: violation_count
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
      - docs.current_spec_only_contract
    imports:
      subject:
        from: artifact
        key: summary_json
```
