# Governance Cases

## SRGOV-RUNTIME-CONFIG-002

```yaml contract-spec
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
- id: assert_2
  class: must
  asserts:
  - must:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - runtime.python_bin_resolver_sync
  target: summary_json
```
