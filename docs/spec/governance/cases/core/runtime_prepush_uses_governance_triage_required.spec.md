# Governance Cases

## SRGOV-RUNTIME-TRIAGE-002

```yaml spec-test
id: SRGOV-RUNTIME-TRIAGE-002
title: prepush lane uses governance triage entrypoint
purpose: Ensures prepush parity lane calls governance triage instead of direct broad governance.
type: governance.check
check: runtime.prepush_uses_governance_triage_required
harness:
  root: .
  prepush_governance_triage:
    path: /scripts/local_ci_parity.sh
    required_tokens:
    - governance-triage
    - ./scripts/governance_triage.sh --mode auto --impl
    forbidden_tokens:
    - run_step governance "${SPEC_RUNNER_BIN}" --impl "${SPEC_RUNNER_IMPL}" governance
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- id: assert_1
  class: must
  checks:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
```
