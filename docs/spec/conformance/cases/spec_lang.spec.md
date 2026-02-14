# Spec Lang Conformance Cases

## SRCONF-EXPR-001

```yaml spec-test
id: SRCONF-EXPR-001
title: evaluate simple predicate passes
purpose: Verifies evaluate runs a basic true predicate against the target subject.
type: text.file
requires:
  capabilities: [evaluate.spec_lang.v1]
expect:
  portable: {status: pass, category: null}
assert:
  - target: text
    must:
      - evaluate:
          - ["contains", "version: 1"]
```

## SRCONF-EXPR-002

```yaml spec-test
id: SRCONF-EXPR-002
title: evaluate composed boolean passes
purpose: Verifies composed boolean expressions evaluate correctly across both runner implementations.
type: text.file
requires:
  capabilities:
    - evaluate.spec_lang.v1
expect:
  portable:
    status: pass
    category: null
assert:
  - target: text
    must:
      - evaluate:
          - ["and"
              ["contains", "version"],
              ["starts_with", ["subject"], "#"]]
```

## SRCONF-EXPR-003

```yaml spec-test
id: SRCONF-EXPR-003
title: evaluate tail recursion is stack safe
purpose: Verifies deep tail-recursive evaluation succeeds under proper TCO.
type: text.file
requires:
  capabilities:
    - evaluate.spec_lang.v1
expect:
  portable:
    status: pass
    category: null
assert:
  - target: text
    must:
      - evaluate:
          - ["let"
              [["loop"
                   ["fn"
                          ["n", "acc"],
                          ["if"
                                   ["eq", ["var", "n"], 0],
                                   ["var", "acc"],
                                   ["call"
                                              ["var", "loop"],
                                              ["sub", ["var", "n"], 1],
                                              ["add", ["var", "acc"], 1]]]]]],
              ["eq", ["call", ["var", "loop"], 1500, 0], 1500]]
```

## SRCONF-EXPR-004

```yaml spec-test
id: SRCONF-EXPR-004
title: evaluate false predicate fails assertion
purpose: Verifies evaluate false result is categorized as assertion failure.
type: text.file
requires:
  capabilities: [evaluate.spec_lang.v1]
expect:
  portable:
    status: fail
    category: assertion
    message_tokens: [op=evaluate]
assert:
  - target: text
    must:
      - evaluate:
          - ["starts_with", ["subject"], "NOPE_PREFIX"]
```

## SRCONF-EXPR-005

```yaml spec-test
id: SRCONF-EXPR-005
title: evaluate malformed form fails schema
purpose: Verifies malformed evaluate forms fail with schema classification.
type: text.file
requires:
  capabilities: [evaluate.spec_lang.v1]
expect:
  portable:
    status: fail
    category: schema
    message_tokens: [list-based s-expr]
assert:
  - target: text
    must:
      - evaluate:
          - {bad: shape}
```

## SRCONF-EXPR-006

```yaml spec-test
id: SRCONF-EXPR-006
title: evaluate unknown symbol fails schema
purpose: Verifies unknown symbols are rejected as schema violations.
type: text.file
requires:
  capabilities: [evaluate.spec_lang.v1]
expect:
  portable:
    status: fail
    category: schema
    message_tokens: [unsupported spec_lang symbol]
assert:
  - target: text
    must:
      - evaluate:
          - ["unknown_symbol", 1]
```

## SRCONF-EXPR-007

```yaml spec-test
id: SRCONF-EXPR-007
title: evaluate budget exhaustion fails runtime
purpose: Verifies deterministic runtime failure when evaluator budgets are exceeded.
type: text.file
requires:
  capabilities:
    - evaluate.spec_lang.v1
expect:
  portable:
    status: fail
    category: runtime
    message_tokens:
      - 'budget exceeded: steps'
harness:
  spec_lang:
    max_steps: 20
assert:
  - target: text
    must:
      - evaluate:
          - ["let"
              [["loop"
                   ["fn"
                          ["n"],
                          ["if"
                                   ["eq", ["var", "n"], 0],
                                   true,
                                   ["call", ["var", "loop"], ["sub", ["var", "n"], 1]]]]]],
              ["call", ["var", "loop"], 1000]]
```
