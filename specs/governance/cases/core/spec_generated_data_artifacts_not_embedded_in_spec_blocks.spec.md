# Governance Cases

## SRGOV-SPEC-MD-004

```yaml contract-spec
id: SRGOV-SPEC-MD-004
title: generated data artifacts do not embed executable spec blocks
purpose: Ensures machine-native yaml and json data artifact surfaces remain non-executable
  and do not contain yaml contract-spec fences.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: spec.generated_data_artifacts_not_embedded_in_spec_blocks
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
    target: summary_json
    assert:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - spec.generated_data_artifacts_not_embedded_in_spec_blocks
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
```
