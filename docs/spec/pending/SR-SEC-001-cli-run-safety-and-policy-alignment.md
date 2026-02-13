---
id: SR-SEC-001
title: CLI Run Safety Controls and Entrypoint Policy Alignment
priority: P1
---

# CLI Run Safety Controls and Entrypoint Policy Alignment

## Problem

Final-boss review identified three merge blockers:

- policy/docs contradiction around `cli.run` entrypoint requirements vs runtime
  env fallback behavior
- no explicit execution safe-mode for untrusted spec contexts
- ambient environment leakage risk for PHP `cli.run` subprocess execution

These gaps increase adoption risk for CI/security-sensitive use and blur the
portable contract boundary.

## Proposal

1. Align contract/policy wording with actual runtime model:
   - portable conformance requires explicit `harness.entrypoint`
   - implementation fallback remains ergonomic/optional behavior
2. Add Python `cli.run` safe mode:
   - `SPEC_RUNNER_SAFE_MODE=1` disables `hook_before` and `hook_after`
   - `SPEC_RUNNER_SAFE_MODE=1` disables entrypoint env fallback; requires
     explicit `harness.entrypoint`
3. Add PHP environment allowlist mode for `cli.run`:
   - `SPEC_RUNNER_ENV_ALLOWLIST=K1,K2,...` filters inherited env passed to
     subprocesses
   - `harness.env` overlay still applies deterministically

## Compatibility

- Default behavior remains backward compatible when the new controls are not
  enabled.
- Safe mode and env allowlist are opt-in hardening controls.

## Test Plan

- Add Python unit tests for safe mode hook/fallback restrictions.
- Add PHP runner integration test verifying env allowlist filtering behavior.
- Keep full `./scripts/ci_gate.sh` green.
