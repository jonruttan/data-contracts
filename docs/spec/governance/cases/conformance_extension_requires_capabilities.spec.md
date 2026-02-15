# Governance Cases

## SRGOV-CONF-PORT-003

```yaml spec-test
id: SRGOV-CONF-PORT-003
title: extension type conformance cases declare requires.capabilities
purpose: Ensures non-core type fixtures explicitly declare required capabilities for portable parity.
type: governance.check
check: conformance.extension_requires_capabilities
harness:
  root: .
  spec_lang:
    library_paths:
    - ../../libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
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
      - conformance.extension_requires_capabilities
```
