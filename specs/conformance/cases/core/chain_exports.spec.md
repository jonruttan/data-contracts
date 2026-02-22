```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
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
      path: "/specs/libraries/conformance/chain_export_validation.spec.md"
      use:
      - ref: "/specs/libraries/conformance/chain_export_validation.spec.md#BAD-EXPORT-PATH"
        as: bad_export_path_fixture
        symbols:
        - bad.path.symbol
  - id: svc.assert_check.text_file.2
    config:
      path: "/specs/libraries/conformance/chain_export_validation.spec.md"
      use:
      - ref: "/specs/libraries/conformance/chain_export_validation.spec.md#BAD-EXPORT-CLASS"
        as: bad_export_class_fixture
        symbols:
        - bad.class.symbol
contracts:
- id: DCCONF-CHAIN-EXPORT-002
  title: producer export path must resolve to producer assert step id
  purpose: Ensures from=assert.function exports fail with schema category when export path does not resolve to a producer assert step.
  expect:
    portable:
      status: fail
      category: schema
  clauses:
    steps: []
- id: DCCONF-CHAIN-EXPORT-003
  title: producer export source assert step must use class must
  purpose: Ensures from=assert.function exports fail with schema category when source step class is not must.
  expect:
    portable:
      status: fail
      category: schema
  clauses:
    steps: []
```


