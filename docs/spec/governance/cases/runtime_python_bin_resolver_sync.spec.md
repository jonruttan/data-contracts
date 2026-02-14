# Governance Cases

## SRGOV-RUNTIME-CONFIG-002

```yaml spec-test
id: SRGOV-RUNTIME-CONFIG-002
title: gate scripts use shared python-bin resolver helper
purpose: Prevents drift by enforcing a single shared python interpreter resolver in shell gate scripts.
type: governance.check
check: runtime.python_bin_resolver_sync
harness:
  root: .
  python_bin_resolver:
    helper: scripts/lib/python_bin.sh
    files:
      - scripts/ci_gate.sh
    required_tokens:
      - source "${ROOT_DIR}/scripts/lib/python_bin.sh"
      - resolve_python_bin "${ROOT_DIR}"
    forbidden_tokens:
      - ROOT_DIR}/.venv/bin/python
      - ROOT_DIR}/../../.venv/bin/python
assert:
  - target: text
    must:
      - contain: ["PASS: runtime.python_bin_resolver_sync"]
```
