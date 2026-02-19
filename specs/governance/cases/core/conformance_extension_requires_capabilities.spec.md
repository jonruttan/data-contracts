# Governance Cases

## SRGOV-CONF-PORT-003

```yaml contract-spec
id: SRGOV-CONF-PORT-003
title: extension type conformance cases declare requires.capabilities
purpose: Ensures non-core type fixtures explicitly declare required capabilities for portable
  parity.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: conformance.extension_requires_capabilities
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  imports:
    subject:
      from: artifact
      key: violation_count
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
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
      - conformance.extension_requires_capabilities
    imports:
      subject:
        from: artifact
        key: summary_json
```
