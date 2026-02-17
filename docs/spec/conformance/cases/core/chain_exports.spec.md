# Chain Exports Conformance Cases

## SRCONF-CHAIN-EXPORT-001

```yaml spec-test
id: SRCONF-CHAIN-EXPORT-001
title: chain exports negative fixture file is present
purpose: Ensures the legacy chain exports fixture is available for script-level
  negative-path coverage.
type: text.file
path: /fixtures/chain_exports_list_only_negative/docs/spec/conformance/cases/core/bad_chain.spec.md
expect:
  portable:
    status: pass
    category: null
assert:
- id: assert_1
  class: must
  target: text
  checks:
  - std.string.contains:
    - var: subject
    - non-executable
```
