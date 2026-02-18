# Governance Cases

## SRGOV-RUNTIME-ENTRY-001

```yaml contract-spec
id: SRGOV-RUNTIME-ENTRY-001
title: gate scripts use a single public runner entrypoint
purpose: Ensures gate scripts reference only the canonical public runner entrypoint.
type: contract.check
harness:
  root: .
  public_runner_entrypoint:
    required_entrypoint: runners/public/runner_adapter.sh
    gate_files:
    - scripts/ci_gate.sh
    - scripts/core_gate.sh
    - scripts/docs_doctor.sh
    forbidden_tokens:
    - runners/rust/runner_adapter.sh
    - runners/python/runner_adapter.sh
    legacy_wrappers:
    - path: scripts/runner_adapter.sh
      required_tokens:
      - runners/public/runner_adapter.sh
      forbidden_tokens:
      - case "${impl}" in
      - cargo build
    - path: scripts/rust/runner_adapter.sh
      required_tokens:
      - runners/rust/runner_adapter.sh
      forbidden_tokens:
      - cargo build
      - spec_runner_cli
    - path: scripts/python/runner_adapter.sh
      required_tokens:
      - runners/python/runner_adapter.sh
      forbidden_tokens:
      - python runner adapter is retired
    - path: scripts/php/conformance_runner.php
      required_tokens:
      - /runners/php/conformance_runner.php
      forbidden_tokens:
      - function parseArgs
      - function listCaseFiles
    - path: scripts/php/spec_runner.php
      required_tokens:
      - /runners/php/spec_runner.php
      forbidden_tokens:
      - function parseArgs
      - function listCaseFiles
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
      check: runtime.public_runner_entrypoint_single
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - {var: subject}
    - 0
  target: violation_count
- id: assert_2
  class: MUST
  asserts:
  - std.logic.eq:
    - std.object.get:
      - {var: subject}
      - check_id
    - runtime.public_runner_entrypoint_single
  - std.logic.eq:
    - std.object.get:
      - {var: subject}
      - passed
    - true
  target: summary_json
```
