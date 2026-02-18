# Governance Cases

## SRGOV-RUNTIME-TRIAGE-004

```yaml contract-spec
id: SRGOV-RUNTIME-TRIAGE-004
title: triage artifacts are emitted by triage and gate flows
purpose: Ensures triage artifacts are produced and referenced by governance-triage and ci-gate-summary.
type: contract.check
harness:
  root: .
  triage_artifacts:
    files:
    - /scripts/governance_triage.sh
    - /scripts/ci_gate_summary.py
    required_tokens:
    - failing_check_ids
    - failing_check_prefixes
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
      check: runtime.triage_artifacts_emitted_required
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - {var: subject}
    - 0
  target: violation_count
```
