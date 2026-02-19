# Chain Exports Conformance Cases

## SRCONF-CHAIN-EXPORT-002

```yaml contract-spec
id: SRCONF-CHAIN-EXPORT-002
title: producer export path must resolve to producer assert step id
purpose: Ensures from=assert.function exports fail with schema category when export path does
  not resolve to a producer assert step.
type: contract.check
harness:
  check:
    profile: text.file
    config:
      path: /specs/libraries/conformance/chain_export_validation.spec.md
  use:
  - ref: /specs/libraries/conformance/chain_export_validation.spec.md#BAD-EXPORT-PATH
    as: bad_export_path_fixture
    symbols:
    - bad.path.symbol
expect:
  portable:
    status: fail
    category: schema
contract:
  defaults:
    class: MUST
  steps: []
```

## SRCONF-CHAIN-EXPORT-003

```yaml contract-spec
id: SRCONF-CHAIN-EXPORT-003
title: producer export source assert step must use class must
purpose: Ensures from=assert.function exports fail with schema category when source step class
  is not must.
type: contract.check
harness:
  check:
    profile: text.file
    config:
      path: /specs/libraries/conformance/chain_export_validation.spec.md
  use:
  - ref: /specs/libraries/conformance/chain_export_validation.spec.md#BAD-EXPORT-CLASS
    as: bad_export_class_fixture
    symbols:
    - bad.class.symbol
expect:
  portable:
    status: fail
    category: schema
contract:
  defaults:
    class: MUST
  steps: []
```
