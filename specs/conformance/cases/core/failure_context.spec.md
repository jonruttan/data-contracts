These fixtures ensure assertion failures expose stable context tokens so
debugging and parity checks remain deterministic.


```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - check
services:
- type: io.fs
  operations:
  - id: svc.check.text_file.1
    mode: read.text
    direction: input
contracts:
  asserts:
  - id: DCCONF-ERR-001
    title: failing assertion includes context tokens in message
    purpose: Guarantees failure messages carry deterministic context tokens for debugging and parity.
    expect:
      portable:
        status: fail
        category: assertion
        message_tokens:
        - case_id=DCCONF-ERR-001
        - contract_path=contract[0]
        - target=text
        - op=evaluate
    asserts:
      imports:
      - from: artifact
        names:
        - text
      checks:
      - id: assert_1
        assert:
          std.string.regex_match:
          - var: text
          - "\\A\\Z"
```
