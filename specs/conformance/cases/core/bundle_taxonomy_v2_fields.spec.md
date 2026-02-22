```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
contracts:
- id: DCCONF-BUNDLE-001
  title: v2 schema docs forbid bundle suite metadata in contract-spec shape
  purpose: Ensures schema_v2 does not define top-level bundle metadata on 
    executable suites.
  expect:
    portable:
      status: pass
      category:
  clauses:
    imports:
    - from: artifact
      names:
      - text
    predicates:
    - id: assert_1
      assert:
        std.logic.and:
        - std.logic.not:
          - std.string.contains:
            - var: text
            - "- `bundle` (mapping, optional)"
        - std.logic.not:
          - std.string.contains:
            - var: text
            - "- `bundle.bundle_version` (string, optional)"
        - std.logic.not:
          - std.string.contains:
            - var: text
            - "- `bundle.maintainers` (list, optional)"
- id: DCCONF-BUNDLE-002
  title: v2 core registry excludes bundle taxonomy fields
  purpose: Ensures schema registry v2 core profile does not codify top-level 
    bundle mappings.
  expect:
    portable:
      status: pass
      category:
  clauses:
    imports:
    - from: artifact
      names:
      - text
    predicates:
    - id: assert_1
      assert:
        std.logic.and:
        - std.logic.not:
          - std.string.contains:
            - var: text
            - 'bundle:'
        - std.logic.not:
          - std.string.contains:
            - var: text
            - 'bundle.bundle_version:'
        - std.logic.not:
          - std.string.contains:
            - var: text
            - 'bundle.domains[].modules[].artifacts[].kind:'
defaults:
  harness: check
harness:
  type: unit.test
  profile: check
services:
  defaults:
    type: assert.check
    io: input
    profile: text.file
  entries:
  - id: svc.assert_check.text_file.1
    config:
      path: "/specs/schema/schema_v2.md"
  - id: svc.assert_check.text_file.2
    config:
      path: "/specs/schema/registry/v2/core.yaml"
```
