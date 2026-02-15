# Governance Cases

## SRGOV-SPEC-PORT-001

```yaml spec-test
id: SRGOV-SPEC-PORT-001
title: spec self-containment metric computes with configured segmented policy
purpose: Ensures portability metric configuration is schema-valid and report generation succeeds for all canonical spec roots.
type: governance.check
check: spec.portability_metric
harness:
  root: .
  spec_lang:
    library_paths:
    - ../../libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  portability_metric:
    roots:
    - docs/spec/conformance/cases
    - docs/spec/governance/cases
    - docs/spec/impl
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
    - and:
      - {json_type: [{ref: subject}, dict]}
      - {has_key: [{ref: subject}, summary]}
      - {has_key: [{ref: subject}, segments]}
      - {has_key: [{ref: subject}, worst_cases]}
      - json_type:
        - {get: [{ref: subject}, summary]}
        - dict
  policy_evaluate:
  - {call: [{var: [policy.pass_when_no_violations]}, {ref: subject}]}
assert:
- target: violation_count
  must:
  - evaluate:
    - {eq: [{ref: subject}, 0]}
- target: summary_json
  must:
  - evaluate:
    - eq:
      - {get: [{ref: subject}, passed]}
      - true
    - eq:
      - {get: [{ref: subject}, check_id]}
      - spec.portability_metric
```
