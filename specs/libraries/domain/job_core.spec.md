```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.export
contracts:
- id: LIB-DOMAIN-JOB-001-000A-DOMAIN-JOB-SCAN-BUNDLE-HAS-RESULT
  title: domain.job.scan_bundle_has_result
  purpose: Reusable helper-backed predicate for contract.job governance scan helper output.
  harness:
    spec_lang:
      capabilities:
      - ops.helper
    exports:
    - as: domain.job.scan_bundle_has_result
      from: assert.function
      path: "/__export__domain.job.scan_bundle_has_result"
      params:
      - scan_path
      - pattern
      docs:
      - id: domain.job.scan_bundle_has_result.doc.1
        summary: Contract export for `domain.job.scan_bundle_has_result`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  scan_path: \"<scan_path>\"\n  pattern: \"<pattern>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: scan_path\n  type: any\n  required: true\n  description: Input parameter `scan_path`.\n- name: pattern\n  type: any\n  required: true\n  description: Input parameter `pattern`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  clauses:
    imports:
    - from: artifact
      names:
      - subject
    predicates:
    - id: __export__domain.job.scan_bundle_has_result
      assert:
        std.logic.neq:
        - std.object.get:
          - ops.helper.call:
            - lit: helper.governance.scan_bundle
            - lit:
                path:
                  var: scan_path
                patterns:
                - var: pattern
          - scanned_files
        - 
  library:
    id: domain.job.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-JOB-001-000A-DOMAIN-JOB-SCAN-BUNDLE-HAS-RESULT.doc.1
    summary: Case `LIB-DOMAIN-JOB-001-000A-DOMAIN-JOB-SCAN-BUNDLE-HAS-RESULT` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
```

