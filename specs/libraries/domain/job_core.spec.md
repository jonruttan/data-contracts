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
    doc:
      summary: Contract export for `domain.job.scan_bundle_has_result`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: scan_path
        type: any
        required: true
        description: Input parameter `scan_path`.
      - name: pattern
        type: any
        required: true
        description: Input parameter `pattern`.
      returns:
        type: any
        description: Result payload for this symbol.
      errors:
      - code: SCHEMA_ERROR
        when: Input payload does not satisfy contract shape requirements.
        category: schema
      examples:
      - title: Basic usage
        input:
          scan_path: <scan_path>
          pattern: <pattern>
        expected: <result>
        notes: Replace with a concrete scenario.
      portability:
        python: true
        php: true
        rust: true
        notes: Confirm per-runtime behavior and caveats.
      see_also: []
      since: v1
contract:
  defaults:
    class: MUST
  imports:
    subject:
      from: artifact
      key: subject
  steps:
  - id: __export__domain.job.scan_bundle_has_result
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
library:
  id: domain.job.core
  module: domain
  stability: alpha
  owner: spec_runner
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-JOB-001-000A-DOMAIN-JOB-SCAN-BUNDLE-HAS-RESULT` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```

