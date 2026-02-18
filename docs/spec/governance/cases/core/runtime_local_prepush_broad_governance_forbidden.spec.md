# Governance Cases

## SRGOV-RUNTIME-TRIAGE-009

```yaml spec-test
id: SRGOV-RUNTIME-TRIAGE-009
title: local prepush does not require broad governance
type: governance.check
purpose: Ensures local parity flow keeps broad governance out of default prepush path.
check: runtime.local_prepush_broad_governance_forbidden
harness:
  root: .
  local_prepush_broad_forbidden:
    path: /scripts/local_ci_parity.sh
    required_tokens:
    - SPEC_GOV_TRIAGE_REQUIRE_BROAD=0
    - governance-triage
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
