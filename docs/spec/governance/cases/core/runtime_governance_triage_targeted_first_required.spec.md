# Governance Cases

## SRGOV-RUNTIME-TRIAGE-008

```yaml contract-spec
id: SRGOV-RUNTIME-TRIAGE-008
title: governance triage auto mode is targeted-first by default
purpose: Ensures triage auto mode resolves to targeted-first and exposes broad-first as an
  explicit mode.
type: governance.check
check: runtime.governance_triage_targeted_first_required
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
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
contract:
- id: assert_1
  class: must
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
```
