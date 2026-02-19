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
    cases: specs/conformance/cases
    max_total_warnings: 0
    fail_on_policy_errors: true
    fail_on_severity: warn
  check:
    profile: governance.scan
    config:
      check: conformance.purpose_quality_gate
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
    imports:
      subject:
        from: artifact
        key: violation_count
  - id: assert_2
    assert:
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
    imports:
      subject:
        from: artifact
        key: summary_json
```
