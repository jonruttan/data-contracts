# Governance Cases

## SRGOV-RUNTIME-PREPUSH-002

```yaml contract-spec
id: SRGOV-RUNTIME-PREPUSH-002
title: makefile contains no python parity prepush targets
purpose: Ensures contributor-facing make targets do not expose python runner lane
  execution.
type: governance.check
check: runtime.make_python_parity_targets_forbidden
harness:
  root: .
  make_python_parity:
    path: /Makefile
    required_tokens:
    - 'prepush: ## Required local pre-push gate (default rust critical-gate path)'
    - SPEC_PREPUSH_MODE=critical ./scripts/local_ci_parity.sh
    - 'prepush-fast: ## Rust-only critical pre-push mode'
    forbidden_tokens:
    - 'python-parity:'
    - --impl python
    - SPEC_PREPUSH_MODE=parity
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
