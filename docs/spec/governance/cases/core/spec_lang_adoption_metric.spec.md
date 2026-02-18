# Governance Cases

## SRGOV-SPEC-LANG-001

```yaml contract-spec
id: SRGOV-SPEC-LANG-001
title: spec-lang adoption metric report generation is valid
purpose: Ensures the spec-lang adoption metric report generates with valid shape and segment
  summary data.
type: governance.check
check: spec.spec_lang_adoption_metric
harness:
  root: .
  spec_lang_adoption:
    roots:
    - /docs/spec/conformance/cases
    - /docs/spec/governance/cases
    - /docs/spec/impl
    segment_rules:
    - prefix: docs/spec/conformance/cases
      segment: conformance
    - prefix: docs/spec/governance/cases
      segment: governance
    - prefix: docs/spec/impl
      segment: impl
    recursive: true
    policy_evaluate:
    - std.logic.and:
      - std.object.has_key:
        - {var: subject}
        - summary
      - std.object.has_key:
        - {var: subject}
        - segments
      - std.object.has_key:
        - std.object.get:
          - {var: subject}
          - summary
        - overall_logic_self_contained_ratio
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
contract:
- id: assert_1
  class: must
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
- id: assert_2
  class: must
  asserts:
  - must:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - spec.spec_lang_adoption_metric
  target: summary_json
```
