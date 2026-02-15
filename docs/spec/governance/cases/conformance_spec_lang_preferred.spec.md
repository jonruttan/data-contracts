# Governance Cases

## SRGOV-CONF-SPECLANG-001

```yaml spec-test
id: SRGOV-CONF-SPECLANG-001
title: conformance fixtures prefer evaluate-first assertion authoring
purpose: Enforces evaluate-first conformance authoring and requires explicit allowlisting for fixtures that intentionally retain sugar assertions.
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
    allow_sugar_files: []
    policy_evaluate:
    - eq:
      - count:
        - filter:
          - fn:
            - {row: []}
            - gt:
              - count:
                - {get: [{var: [row]}, non_evaluate_ops]}
              - 0
          - {ref: subject}
      - 0
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
      - conformance.spec_lang_preferred
```
