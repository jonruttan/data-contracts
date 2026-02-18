# Chain Exports Conformance Cases

## SRCONF-CHAIN-EXPORT-002

```yaml contract-spec
id: SRCONF-CHAIN-EXPORT-002
title: producer export path must resolve to producer assert step id
purpose: Ensures from=assert.function exports fail with schema category when export path does
  not resolve to a producer assert step.
type: contract.check
harness:
  chain:
    steps:
    - id: bad_export_path_fixture
      class: MUST
      ref: /docs/spec/libraries/conformance/chain_export_validation.spec.md#BAD-EXPORT-PATH
    imports:
    - from: bad_export_path_fixture
      names:
      - bad.path.symbol
  check:
    profile: text.file
    config:
      path: /docs/spec/libraries/conformance/chain_export_validation.spec.md
expect:
  portable:
    status: fail
    category: schema
contract: []
```

## SRCONF-CHAIN-EXPORT-003

```yaml contract-spec
id: SRCONF-CHAIN-EXPORT-003
title: producer export source assert step must use class must
purpose: Ensures from=assert.function exports fail with schema category when source step class
  is not must.
type: contract.check
harness:
  chain:
    steps:
    - id: bad_export_class_fixture
      class: MUST
      ref: /docs/spec/libraries/conformance/chain_export_validation.spec.md#BAD-EXPORT-CLASS
    imports:
    - from: bad_export_class_fixture
      names:
      - bad.class.symbol
  check:
    profile: text.file
    config:
      path: /docs/spec/libraries/conformance/chain_export_validation.spec.md
expect:
  portable:
    status: fail
    category: schema
contract: []
```
