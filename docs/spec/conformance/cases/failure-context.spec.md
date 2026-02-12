# Failure Context Conformance Cases

## SRCONF-ERR-001

```yaml spec-test
id: SRCONF-ERR-001
title: failing assertion includes context tokens in message
purpose: Guarantees failure messages carry deterministic context tokens for debugging and parity.
type: text.file
expect:
  portable:
    status: fail
    category: assertion
    message_tokens:
      - case_id=SRCONF-ERR-001
      - assert_path=assert[0].must[0]
      - target=text
      - op=regex
assert:
  - target: text
    must:
      - regex: ["\\A\\Z"]
```
