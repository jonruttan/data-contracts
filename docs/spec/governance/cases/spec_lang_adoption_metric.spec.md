# Governance Cases

## SRGOV-SPEC-LANG-001

```yaml spec-test
id: SRGOV-SPEC-LANG-001
title: spec-lang adoption metric report generation is valid
purpose: Ensures the spec-lang adoption metric report generates with valid shape and segment summary data.
type: governance.check
check: spec.spec_lang_adoption_metric
harness:
  root: .
  spec_lang:
    library_paths:
    - ../../libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  spec_lang_adoption:
    roots:
    - docs/spec/conformance/cases
    - docs/spec/governance/cases
    - docs/spec/impl
    segment_rules:
    - prefix: docs/spec/conformance/cases
      segment: conformance
    - prefix: docs/spec/governance/cases
      segment: governance
    - prefix: docs/spec/impl
      segment: impl
    recursive: true
    policy_evaluate:
    - and:
      - {has_key: [{subject: []}, summary]}
      - {has_key: [{subject: []}, segments]}
      - has_key:
        - {get: [{subject: []}, summary]}
        - overall_logic_self_contained_ratio
  policy_evaluate:
  - {call: [{var: [policy.pass_when_no_violations]}, {subject: []}]}
assert:
- target: violation_count
  must:
  - evaluate:
    - {eq: [{subject: []}, 0]}
- target: summary_json
  must:
  - evaluate:
    - eq:
      - {get: [{subject: []}, passed]}
      - true
    - eq:
      - {get: [{subject: []}, check_id]}
      - spec.spec_lang_adoption_metric
```
