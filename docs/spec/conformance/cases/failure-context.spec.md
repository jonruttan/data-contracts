# Failure Context Conformance Cases

## SRCONF-ERR-001

```yaml spec-test
id: SRCONF-ERR-001
title: failing assertion includes context tokens in message
why: failing assertion includes context tokens in message
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
