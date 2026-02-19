# Governance Cases

## SRGOV-RUNTIME-CONFIG-007

```yaml contract-spec
id: SRGOV-RUNTIME-CONFIG-007
title: compatibility lanes remain non-blocking
purpose: Ensures compatibility runtime lanes are present in CI and explicitly non-blocking.
type: contract.check
harness:
  root: .
  compatibility_lanes:
    workflow: /.github/workflows/ci.yml
    required_tokens:
    - compatibility-python-lane:
    - compatibility-php-lane:
    - compatibility-node-lane:
    - compatibility-c-lane:
    - continue-on-error: true
  check:
    profile: governance.scan
    config:
      check: runtime.compatibility_lanes_non_blocking_status
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
    target: violation_count
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
```
