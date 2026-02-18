# Governance Cases

## SRGOV-RUNTIME-TRIAGE-008

```yaml contract-spec
id: SRGOV-RUNTIME-TRIAGE-008
title: governance triage auto mode is targeted-first by default
purpose: Ensures triage auto mode resolves to targeted-first and exposes broad-first as an
  explicit mode.
type: contract.check
harness:
  root: .
  triage_targeted_first:
    path: /scripts/governance_triage.sh
    required_tokens:
    - TRIAGE_MODE_DEFAULT
    - targeted-first
    - broad-first
    - resolve_targeted_prefixes
    - selection_source
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /specs/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
  check:
    profile: governance.scan
    config:
      check: runtime.governance_triage_targeted_first_required
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - {var: subject}
    - 0
  target: violation_count
```
