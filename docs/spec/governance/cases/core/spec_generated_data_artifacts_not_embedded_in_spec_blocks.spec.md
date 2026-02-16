# Governance Cases

## SRGOV-SPEC-MD-004

```yaml spec-test
id: SRGOV-SPEC-MD-004
title: generated data artifacts do not embed executable spec blocks
purpose: Ensures machine-native yaml and json data artifact surfaces remain non-executable
  and do not contain yaml spec-test fences.
type: governance.check
check: spec.generated_data_artifacts_not_embedded_in_spec_blocks
harness:
  root: .
  spec_lang:
    includes:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
assert:
- target: summary_json
  must:
  - evaluate:
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
