# Governance Cases

## SRGOV-RUNTIME-OPS-OS-CAP-001

```yaml contract-spec
id: SRGOV-RUNTIME-OPS-OS-CAP-001
title: ops.os usage requires explicit capability gate
purpose: Ensures spec-lang enforces capability.ops_os.required and harness capability parsing.
type: contract.check
harness:
  root: .
  ops_os_capability:
    path: /runners/python/spec_runner/spec_lang.py
    required_tokens:
    - capability.ops_os.required
    - def capabilities_from_harness
    - ops.os.exec
  check:
    profile: governance.scan
    config:
      check: runtime.ops_os_capability_required
contract:
  defaults:
    class: MUST
  imports:
    subject:
      from: artifact
      key: violation_count
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
```
