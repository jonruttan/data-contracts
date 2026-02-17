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

## SRCONF-CHAIN-EXPORT-002

```yaml spec-test
id: SRCONF-CHAIN-EXPORT-002
title: producer export path must resolve to producer assert step id
purpose: Ensures from=assert.function exports fail with schema category when export path
  does not resolve to a producer assert step.
type: text.file
path: /docs/spec/libraries/conformance/chain_export_validation.spec.md
harness:
  chain:
    steps:
    - id: bad_export_path_fixture
      class: must
      ref: /docs/spec/libraries/conformance/chain_export_validation.spec.md#BAD-EXPORT-PATH
    imports:
    - from: bad_export_path_fixture
      names:
      - bad.path.symbol
expect:
  portable:
    status: fail
    category: schema
```

## SRCONF-CHAIN-EXPORT-003

```yaml spec-test
id: SRCONF-CHAIN-EXPORT-003
title: producer export source assert step must use class must
purpose: Ensures from=assert.function exports fail with schema category when source step class
  is not must.
type: text.file
path: /docs/spec/libraries/conformance/chain_export_validation.spec.md
harness:
  chain:
    steps:
    - id: bad_export_class_fixture
      class: must
      ref: /docs/spec/libraries/conformance/chain_export_validation.spec.md#BAD-EXPORT-CLASS
    imports:
    - from: bad_export_class_fixture
      names:
      - bad.class.symbol
expect:
  portable:
    status: fail
    category: schema
```
