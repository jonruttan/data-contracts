# Governance Cases

## DCGOV-RUNTIME-META-TARGET-001

```yaml contract-spec
id: DCGOV-RUNTIME-META-TARGET-001
title: executable harnesses expose meta_json assertion target
purpose: Ensures all core executable harness adapters project meta_json.
type: contract.check
harness:
  root: .
  meta_json_targets:
    files:
    - /dc-runner-python/spec_runner/harnesses/text_file.py
    - /dc-runner-python/spec_runner/harnesses/cli_run.py
    - /dc-runner-python/spec_runner/harnesses/docs_generate.py
    - /dc-runner-python/spec_runner/harnesses/orchestration_run.py
    - /dc-runner-python/spec_runner/harnesses/api_http.py
    required_tokens:
    - meta_json
  check:
    profile: governance.scan
    config:
      check: runtime.meta_json_target_required
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - violation_count
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - {var: violation_count}
      - 0
```
