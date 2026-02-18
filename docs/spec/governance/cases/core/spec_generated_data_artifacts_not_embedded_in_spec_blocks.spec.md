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
      check: spec.generated_data_artifacts_not_embedded_in_spec_blocks
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
      lit:
        lit:
          MUST:
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
  target: summary_json
```
