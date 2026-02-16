# Governance Cases

## SRGOV-RUNTIME-CONFIG-002

```yaml spec-test
id: SRGOV-RUNTIME-CONFIG-002
title: python-invoking adapter scripts use shared python-bin resolver helper
purpose: Prevents drift by enforcing a single shared python interpreter resolver in scripts
  that invoke Python directly.
type: governance.check
check: runtime.python_bin_resolver_sync
harness:
  root: .
  python_bin_resolver:
    helper: scripts/lib/python_bin.sh
    files:
    - scripts/python/runner_adapter.sh
    required_tokens:
    - source "${ROOT_DIR}/scripts/lib/python_bin.sh"
    - resolve_python_bin "${ROOT_DIR}"
    forbidden_tokens:
    - ROOT_DIR}/.venv/bin/python
    - ROOT_DIR}/../../.venv/bin/python
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
      exports:
        policy.pass_when_no_violations:
          from: library.symbol
          path: /policy.pass_when_no_violations
          required: true
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- target: violation_count
  must:
  - evaluate:
    - std.logic.eq:
      - {var: subject}
      - 0
- target: summary_json
  must:
  - evaluate:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - runtime.python_bin_resolver_sync
```
