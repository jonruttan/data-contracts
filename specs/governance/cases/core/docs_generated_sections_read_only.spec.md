# Governance Cases

## SRGOV-DOCS-GEN-003

```yaml contract-spec
id: SRGOV-DOCS-GEN-003
title: generated markdown sections are read-only blocks
purpose: Ensures configured generated markdown outputs contain valid generated section markers.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: docs.generated_sections_read_only
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
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - docs.generated_sections_read_only
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
    imports:
      subject:
        from: artifact
        key: summary_json
```
