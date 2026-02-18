# Governance Cases

## SRGOV-RUNTIME-OPS-OS-SURFACE-001

```yaml contract-spec
id: SRGOV-RUNTIME-OPS-OS-SURFACE-001
title: ops.os stdlib symbols are declared in profile and symbol maps
purpose: Ensures ops.os builtins are synchronized across stdlib mapping and
  stdlib profile contract surfaces.
type: governance.check
check: runtime.ops_os_stdlib_surface_sync
harness:
  root: .
  ops_os_stdlib_surface:
    files:
    - /spec_runner/spec_lang_std_names.py
    - /docs/spec/schema/spec_lang_stdlib_profile_v1.yaml
    required_symbols:
    - ops.os.exec
    - ops.os.exec_capture
    - ops.os.env_get
    - ops.os.env_has
    - ops.os.cwd
    - ops.os.pid
    - ops.os.sleep_ms
    - ops.os.exit_code
contract:
- id: assert_1
  class: must
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
```
