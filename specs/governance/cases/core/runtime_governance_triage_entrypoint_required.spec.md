# Governance Cases

## SRGOV-RUNTIME-TRIAGE-001

```yaml contract-spec
id: SRGOV-RUNTIME-TRIAGE-001
title: governance triage entrypoint exists with required surface
purpose: Ensures canonical governance triage script exists and exposes required flags.
type: contract.check
harness:
  root: .
  governance_triage:
    path: /scripts/governance_triage.sh
    required_tokens:
    - --mode auto
    - --mode auto|targeted|broad-first
    - --from-failures
    - --check-prefix
    - --check-id
    - .artifacts/governance-triage.json
    - .artifacts/governance-triage-summary.md
  check:
    profile: governance.scan
    config:
      check: runtime.governance_triage_entrypoint_required
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
