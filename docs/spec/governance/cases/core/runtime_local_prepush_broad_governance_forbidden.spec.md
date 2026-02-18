# Governance Cases

## SRGOV-RUNTIME-TRIAGE-009

```yaml contract-spec
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
    - skip broad governance (set SPEC_PREPUSH_REQUIRE_BROAD=1 to enable)
    - SPEC_PREPUSH_REQUIRE_BROAD=1
    forbidden_tokens:
    - run_step governance "${SPEC_RUNNER_BIN}" --impl "${SPEC_RUNNER_IMPL}" governance
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
```
