# Governance Cases

## SRGOV-RUNTIME-TRIAGE-002

```yaml contract-spec
id: SRGOV-RUNTIME-TRIAGE-002
title: prepush lane uses governance triage entrypoint
purpose: Ensures prepush parity lane calls governance triage instead of direct broad governance.
type: contract.check
harness:
  root: .
  prepush_governance_triage:
    path: /scripts/local_ci_parity.sh
    required_tokens:
    - governance-triage
    - ./scripts/governance_triage.sh --mode broad-first --impl
    forbidden_tokens:
    - run_step governance "${SPEC_RUNNER_BIN}" --impl "${SPEC_RUNNER_IMPL}" governance
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
      check: runtime.prepush_uses_governance_triage_required
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - {var: subject}
    - 0
  target: violation_count
```
