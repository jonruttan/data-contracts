```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-RUNTIME-OPS-OS-SURFACE-001
    title: ops.os stdlib symbols are declared in profile and symbol maps
    purpose: Ensures ops.os builtins are synchronized across stdlib mapping and stdlib profile
      contract surfaces.
    harness:
      root: .
      ops_os_stdlib_surface:
        files:
        - /dc-runner-python
        - /specs/schema/spec_lang_stdlib_profile_v1.yaml
        required_symbols:
        - ops.os.exec
        - ops.os.exec_capture
        - ops.os.env_get
        - ops.os.env_has
        - ops.os.cwd
        - ops.os.pid
        - ops.os.sleep_ms
        - ops.os.exit_code
      check:
        profile: governance.scan
        config:
          check: runtime.ops_os_stdlib_surface_sync
    clauses:
      defaults: {}
      imports:
      - from: artifact
        names:
        - violation_count
      predicates:
      - id: assert_1
        assert:
          std.logic.eq:
          - {var: violation_count}
          - 0
```
