# Governance Cases

## SRGOV-CONTRACT-001

```yaml contract-spec
id: SRGOV-CONTRACT-001
title: contract governance rules pass via governance harness
purpose: Ensures contract policy and traceability integrity checks are enforced through the
  governance spec pipeline.
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
      check: contract.governance_check
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
    - lit:
        lit:
          lit:
            std.logic.eq:
            - {var: subject}
            - 0
  target: violation_count
- id: assert_2
  class: MUST
  asserts:
  - evaluate:
    - lit:
        lit:
          lit:
            MUST:
            - std.logic.eq:
              - std.object.get:
                - {var: subject}
                - passed
              - true
            - std.logic.eq:
              - std.object.get:
                - {var: subject}
                - check_id
              - contract.governance_check
  target: summary_json
```
