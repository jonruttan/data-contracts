# Governance Cases

## SRGOV-SPEC-PORT-001

```yaml contract-spec
id: SRGOV-SPEC-PORT-001
title: spec self-containment metric computes with configured segmented policy
purpose: Ensures portability metric configuration is schema-valid and report generation succeeds
  for all canonical spec roots.
type: governance.check
check: spec.portability_metric
harness:
  root: .
  portability_metric:
    roots:
    - /docs/spec/conformance/cases
    - /docs/spec/governance/cases
    - /docs/spec/impl
    core_types:
    - text.file
    - cli.run
    segment_rules:
    - prefix: docs/spec/conformance/cases
      segment: conformance
    - prefix: docs/spec/governance/cases
      segment: governance
    - prefix: docs/spec/impl
      segment: impl
    runtime_capability_tokens:
    - api.http
    - governance.check
    runtime_capability_prefixes:
    - runtime.
    - php.
    - python.
    weights:
      non_evaluate_leaf_share: 0.45
      expect_impl_overlay: 0.25
      runtime_specific_capability: 0.15
      non_core_type: 0.15
    report:
      top_n: 10
    enforce: false
    policy_evaluate:
    - std.logic.and:
      - std.type.json_type:
        - {var: subject}
        - dict
      - std.object.has_key:
        - {var: subject}
        - summary
      - std.object.has_key:
        - {var: subject}
        - segments
      - std.object.has_key:
        - {var: subject}
        - worst_cases
      - std.type.json_type:
        - std.object.get:
          - {var: subject}
          - summary
        - dict
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
      - spec.portability_metric
  target: summary_json
```
