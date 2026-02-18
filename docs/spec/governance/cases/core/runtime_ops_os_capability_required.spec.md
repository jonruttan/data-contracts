# Governance Cases

## SRGOV-RUNTIME-OPS-OS-CAP-001

```yaml spec-test
id: SRGOV-RUNTIME-OPS-OS-CAP-001
title: ops.os usage requires explicit capability gate
purpose: Ensures spec-lang enforces capability.ops_os.required and harness
  capability parsing.
type: governance.check
check: runtime.ops_os_capability_required
harness:
  root: .
  ops_os_capability:
    path: /spec_runner/spec_lang.py
    required_tokens:
    - capability.ops_os.required
    - def capabilities_from_harness
    - ops.os.exec
assert:
- id: assert_1
  class: must
  checks:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
```
