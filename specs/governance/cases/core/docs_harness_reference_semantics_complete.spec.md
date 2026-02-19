# Governance Cases

## SRGOV-DOCS-GEN-023

```yaml contract-spec
id: SRGOV-DOCS-GEN-023
title: harness reference includes semantic sections
purpose: Ensures generated harness reference includes summary/defaults/failure modes/examples
  per case type.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: docs.harness_reference_semantics_complete
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
      - docs.harness_reference_semantics_complete
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
