# Governance Cases

## SRGOV-CONF-SPECLANG-001

```yaml spec-test
id: SRGOV-CONF-SPECLANG-001
title: conformance and governance fixtures require evaluate-only assertions
purpose: Enforces evaluate-only assertion authoring in conformance and governance case surfaces.
type: governance.check
check: conformance.spec_lang_preferred
harness:
  root: .
  spec_lang:
    library_paths:
    - ../../libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  spec_lang_preferred:
    roots:
    - docs/spec/conformance/cases
    - docs/spec/governance/cases
    policy_evaluate:
    - eq:
      - count:
        - filter:
          - fn:
            - [row]
            - gt:
              - count:
                - {get: [{var: row}, non_evaluate_ops]}
              - 0
          - {var: subject}
      - 0
  policy_evaluate:
  - {call: [{var: policy.pass_when_no_violations}, {var: subject}]}
assert:
- target: violation_count
  must:
  - evaluate:
    - {eq: [{var: subject}, 0]}
- target: summary_json
  must:
  - evaluate:
    - eq:
      - {get: [{var: subject}, passed]}
      - true
    - eq:
      - {get: [{var: subject}, check_id]}
      - conformance.spec_lang_preferred
```
