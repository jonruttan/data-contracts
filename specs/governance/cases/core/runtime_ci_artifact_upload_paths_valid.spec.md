# Governance Cases

## SRGOV-RUNTIME-TRIAGE-013

```yaml contract-spec
id: SRGOV-RUNTIME-TRIAGE-013
title: ci workflow uploads artifacts from canonical .artifacts path
purpose: Ensures CI uploads gate and triage artifacts using a recursive .artifacts path.
type: contract.check
harness:
  root: .
  ci_artifact_upload:
    path: /.github/workflows/ci.yml
    required_tokens:
    - actions/upload-artifact@v4
    - .artifacts/**
    - 'if: always()'
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /specs/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
  check:
    profile: governance.scan
    config:
      check: runtime.ci_artifact_upload_paths_valid
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - {var: subject}
    - 0
  target: violation_count
```
