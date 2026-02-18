# Governance Cases

## SRGOV-CONF-PURPOSE-002

```yaml contract-spec
id: SRGOV-CONF-PURPOSE-002
title: conformance purpose quality remains warning free
purpose: Ensures conformance purpose lint policy and case purpose text stay clean with no
  accumulated warning debt.
type: contract.check
harness:
  root: .
  purpose_quality:
    cases: docs/spec/conformance/cases
    max_total_warnings: 0
    fail_on_policy_errors: true
    fail_on_severity: warn
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
      check: conformance.purpose_quality_gate
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - {var: subject}
    - 0
  target: violation_count
- id: assert_2
  class: MUST
  asserts:
  - std.logic.eq:
    - std.object.get:
      - {var: subject}
      - passed
    - true
  - std.logic.eq:
    - std.object.get:
      - {var: subject}
      - check_id
    - conformance.purpose_quality_gate
  target: summary_json
```
