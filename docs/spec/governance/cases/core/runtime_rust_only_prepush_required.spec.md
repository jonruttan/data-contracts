# Governance Cases

## SRGOV-RUNTIME-PREPUSH-006

```yaml contract-spec
id: SRGOV-RUNTIME-PREPUSH-006
title: prepush path is rust-only
purpose: Ensures prepush entrypoints and hook routing remain rust-only.
type: contract.check
harness:
  root: .
  rust_only_prepush:
    file_token_sets:
    - path: /scripts/local_ci_parity.sh
      required_tokens:
      - 'mode=critical: rust-only critical path'
      forbidden_tokens:
      - lane_python_parity
      - --impl python
      - expected critical|parity|fast
    - path: /.githooks/pre-push
      required_tokens:
      - make prepush
      forbidden_tokens:
      - --impl python
      - SPEC_PREPUSH_MODE=parity
    - path: /Makefile
      required_tokens:
      - SPEC_PREPUSH_MODE=critical ./scripts/local_ci_parity.sh
      forbidden_tokens:
      - 'python-parity:'
      - SPEC_PREPUSH_MODE=parity ./scripts/local_ci_parity.sh
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
      check: runtime.rust_only_prepush_required
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
      lit:
        lit:
          std.logic.eq:
          - {var: subject}
          - 0
  target: violation_count
```
