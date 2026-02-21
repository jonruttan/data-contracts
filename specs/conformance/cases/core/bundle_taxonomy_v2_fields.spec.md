```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
defaults:
  type: contract.check
contracts:
  - id: DCCONF-BUNDLE-001
    title: v2 schema docs define optional bundle suite metadata
    purpose: Ensures schema_v2 suite fields describe canonical bundle metadata keys.
    expect:
      portable:
        status: pass
        category: null
    clauses:
      defaults: {}
      imports:
      - from: artifact
        names:
        - text
      predicates:
      - id: assert_1
        assert:
        - std.string.contains:
          - {var: text}
          - - `bundle` (mapping, optional)
        - std.string.contains:
          - {var: text}
          - - `bundle.bundle_version` (string, optional)
        - std.string.contains:
          - {var: text}
          - - `bundle.maintainers` (list, optional)
    harness:
      check:
        profile: text.file
        config:
          path: /specs/schema/schema_v2.md
  - id: DCCONF-BUNDLE-002
    title: v2 core registry includes bundle taxonomy fields
    purpose: Ensures schema registry v2 core profile codifies optional bundle mappings.
    expect:
      portable:
        status: pass
        category: null
    clauses:
      defaults: {}
      imports:
      - from: artifact
        names:
        - text
      predicates:
      - id: assert_1
        assert:
        - std.string.contains:
          - {var: text}
          - "bundle:"
        - std.string.contains:
          - {var: text}
          - "bundle.bundle_version:"
        - std.string.contains:
          - {var: text}
          - "bundle.domains[].modules[].artifacts[].kind:"
    harness:
      check:
        profile: text.file
        config:
          path: /specs/schema/registry/v2/core.yaml
```
