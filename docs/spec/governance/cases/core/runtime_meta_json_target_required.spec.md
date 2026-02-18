# Governance Cases

## SRGOV-RUNTIME-META-TARGET-001

```yaml contract-spec
id: SRGOV-RUNTIME-META-TARGET-001
title: executable harnesses expose meta_json assertion target
purpose: Ensures all core executable harness adapters project meta_json.
type: governance.check
check: runtime.meta_json_target_required
harness:
  root: .
  meta_json_targets:
    files:
    - /spec_runner/harnesses/text_file.py
    - /spec_runner/harnesses/cli_run.py
    - /spec_runner/harnesses/docs_generate.py
    - /spec_runner/harnesses/orchestration_run.py
    - /spec_runner/harnesses/api_http.py
    required_tokens:
    - meta_json
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
```
