# Domain Job Library

## LIB-DOMAIN-JOB-001-000A-DOMAIN-JOB-SCAN-BUNDLE-HAS-RESULT

```yaml contract-spec
id: LIB-DOMAIN-JOB-001-000A-DOMAIN-JOB-SCAN-BUNDLE-HAS-RESULT
title: domain.job.scan_bundle_has_result
purpose: Reusable helper-backed predicate for contract.job governance scan helper output.
type: contract.export
harness:
  spec_lang:
    capabilities:
    - ops.helper
  exports:
  - as: domain.job.scan_bundle_has_result
    from: assert.function
    path: /__export__domain.job.scan_bundle_has_result
    params:
    - scan_path
    - pattern
contract:
  defaults:
    class: MUST
  steps:
  - id: __export__domain.job.scan_bundle_has_result
    'on': subject
    assert:
      std.logic.neq:
      - std.object.get:
        - ops.helper.call:
          - {lit: helper.governance.scan_bundle}
          - lit:
              path:
                var: scan_path
              patterns:
              - var: pattern
        - scanned_files
      - null
```

