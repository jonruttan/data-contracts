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
      check: runtime.governance_triage_entrypoint_required
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
```
