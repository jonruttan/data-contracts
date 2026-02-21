# Governance Cases

## DCGOV-PACK-002

```yaml contract-spec
id: DCGOV-PACK-002
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: runner contract pack is complete
purpose: Ensures runner-contract pack includes CLI and status exchange surfaces.
type: contract.check
harness:
  root: .
  pack:
    path: /specs/packs/runner_contract_pack_v1.yaml
    required_tokens:
      - pack_id: runner_contract_pack_v1
      - /specs/contract/29_runner_cli_interface.md
      - /specs/contract/30_build_tool_command_set.md
      - /specs/schema/runner_cli_contract_v1.yaml
      - /specs/schema/runner_build_tool_contract_v1.yaml
      - /specs/conformance/cases/runner_cli/runner_cli_required_help.spec.md
      - /specs/conformance/cases/runner_build_tool/runner_build_tool_required_core.spec.md
  check:
    profile: governance.scan
    config:
      check: packs.runner_contract_pack_complete
contract:
  defaults: {}
  imports:
    - from: artifact
      names: [violation_count]
  steps:
    - id: assert_1
      assert:
        call:
      - {var: policy.assert.no_violations}
      - std.object.assoc:
        - violation_count
        - {var: violation_count}
        - lit: {}
```
