# Spec Lang Conformance Cases

## SRCONF-EXPR-001

```yaml spec-test
id: SRCONF-EXPR-001
title: evaluate simple predicate passes
purpose: Verifies evaluate runs a basic true predicate against the target subject.
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
    - contains:
      - 'version: 1'
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
    - and:
      - contains:
        - version
      - starts_with:
        - subject: []
        - '#'
```

## SRCONF-EXPR-003

```yaml spec-test
id: SRCONF-EXPR-003
title: evaluate tail recursion is stack safe
purpose: Verifies unsupported mixed literal-expression recursive forms fail deterministically under mapping AST hard-cut rules.
type: text.file
requires:
  capabilities:
  - evaluate.spec_lang.v1
expect:
  portable:
    status: fail
    category: schema
    message_tokens:
    - list-based s-expr or scalar literal
assert:
- target: text
  must:
  - evaluate:
    - let:
      - lit:
        - - loop
          - fn:
            - lit:
              - n
              - acc
            - if:
              - eq:
                - var:
                  - n
                - 0
              - var:
                - acc
              - call:
                - var:
                  - loop
                - sub:
                  - var:
                    - n
                  - 1
                - add:
                  - var:
                    - acc
                  - 1
      - eq:
        - call:
          - var:
            - loop
          - 1500
          - 0
        - 1500
```

## SRCONF-EXPR-004

```yaml spec-test
id: SRCONF-EXPR-004
title: evaluate false predicate fails assertion
purpose: Verifies evaluate false result is categorized as assertion failure.
type: text.file
requires:
  capabilities:
  - evaluate.spec_lang.v1
expect:
  portable:
    status: fail
    category: assertion
    message_tokens:
    - op=evaluate
assert:
- target: text
  must:
  - evaluate:
    - starts_with:
      - subject: []
      - NOPE_PREFIX
```

## SRCONF-EXPR-005

```yaml spec-test
id: SRCONF-EXPR-005
title: evaluate malformed form fails schema
purpose: Verifies malformed evaluate forms fail with schema classification.
type: text.file
requires:
  capabilities:
  - evaluate.spec_lang.v1
expect:
  portable:
    status: fail
    category: schema
    message_tokens:
    - operator args must be a list
assert:
- target: text
  must:
  - evaluate:
    - bad: shape
```

## SRCONF-EXPR-006

```yaml spec-test
id: SRCONF-EXPR-006
title: evaluate unknown symbol fails schema
purpose: Verifies unknown symbols are rejected as schema violations.
type: text.file
requires:
  capabilities:
  - evaluate.spec_lang.v1
expect:
  portable:
    status: fail
    category: schema
    message_tokens:
    - unsupported spec_lang symbol
assert:
- target: text
  must:
  - evaluate:
    - unknown_symbol:
      - 1
```

## SRCONF-EXPR-007

```yaml spec-test
id: SRCONF-EXPR-007
title: evaluate recursive literal-expression shape fails schema
purpose: Verifies unsupported recursive literal-expression authoring shape fails deterministically as schema.
type: text.file
requires:
  capabilities:
  - evaluate.spec_lang.v1
expect:
  portable:
    status: fail
    category: schema
    message_tokens:
    - list-based s-expr or scalar literal
harness:
  spec_lang:
    max_steps: 20
assert:
- target: text
  must:
  - evaluate:
    - let:
      - lit:
        - - loop
          - fn:
            - lit:
              - n
            - if:
              - eq:
                - var:
                  - n
                - 0
              - true
              - call:
                - var:
                  - loop
                - sub:
                  - var:
                    - n
                  - 1
      - call:
        - var:
          - loop
        - 1000
```

## SRCONF-EXPR-008

```yaml spec-test
id: SRCONF-EXPR-008
title: sugar and evaluate forms are semantically equivalent
purpose: Verifies authoring sugar assertions and explicit evaluate expressions produce equivalent pass behavior for the same target subject.
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
  - contain:
    - 'version: 1'
  - evaluate:
    - contains:
      - subject: []
      - 'version: 1'
```

## SRCONF-EXPR-009

```yaml spec-test
id: SRCONF-EXPR-009
title: evaluate set intersection supports deep structural equality
purpose: Verifies intersection deduplicates and compares nested values structurally with stable left-first output.
type: text.file
requires:
  capabilities:
  - evaluate.spec_lang.ramda.v1
  when_missing: skip
expect:
  portable:
    status: skip
    category: null
  impl:
    python:
      status: pass
      category: null
assert:
- target: text
  must:
  - evaluate:
    - eq:
      - intersection:
        - json_parse:
          - '[{"k":1},{"k":2},{"k":2},{"k":3}]'
        - json_parse:
          - '[{"k":2},{"k":4},{"k":1}]'
      - json_parse:
        - '[{"k":1},{"k":2}]'
```

## SRCONF-EXPR-010

```yaml spec-test
id: SRCONF-EXPR-010
title: evaluate set union keeps stable left-first unique ordering
purpose: Verifies union preserves first-seen ordering while removing deep-equal duplicates.
type: text.file
requires:
  capabilities:
  - evaluate.spec_lang.ramda.v1
  when_missing: skip
expect:
  portable:
    status: skip
    category: null
  impl:
    python:
      status: pass
      category: null
assert:
- target: text
  must:
  - evaluate:
    - eq:
      - union:
        - json_parse:
          - '[{"k":1},{"k":2},{"k":2},{"k":3}]'
        - json_parse:
          - '[{"k":2},{"k":4},{"k":1}]'
      - json_parse:
        - '[{"k":1},{"k":2},{"k":3},{"k":4}]'
```

## SRCONF-EXPR-011

```yaml spec-test
id: SRCONF-EXPR-011
title: evaluate difference and symmetric_difference are deterministic
purpose: Verifies set difference semantics and deterministic ordering for symmetric_difference.
type: text.file
requires:
  capabilities:
  - evaluate.spec_lang.ramda.v1
  when_missing: skip
expect:
  portable:
    status: skip
    category: null
  impl:
    python:
      status: pass
      category: null
assert:
- target: text
  must:
  - evaluate:
    - and:
      - eq:
        - difference:
          - json_parse:
            - '[{"k":1},{"k":2},{"k":3}]'
          - json_parse:
            - '[{"k":2},{"k":4}]'
        - json_parse:
          - '[{"k":1},{"k":3}]'
      - eq:
        - symmetric_difference:
          - json_parse:
            - '[{"k":1},{"k":2},{"k":3}]'
          - json_parse:
            - '[{"k":2},{"k":4}]'
        - json_parse:
          - '[{"k":1},{"k":3},{"k":4}]'
```

## SRCONF-EXPR-012

```yaml spec-test
id: SRCONF-EXPR-012
title: evaluate set predicates compare by deep equality
purpose: Verifies set_equals, is_subset, is_superset, and includes use deep structural equality.
type: text.file
requires:
  capabilities:
  - evaluate.spec_lang.ramda.v1
  when_missing: skip
expect:
  portable:
    status: skip
    category: null
  impl:
    python:
      status: pass
      category: null
assert:
- target: text
  must:
  - evaluate:
    - and:
      - set_equals:
        - json_parse:
          - '[{"k":1},{"k":2},{"k":3}]'
        - json_parse:
          - '[{"k":3},{"k":1},{"k":2}]'
      - is_subset:
        - json_parse:
          - '[{"k":1},{"k":2}]'
        - json_parse:
          - '[{"k":1},{"k":2},{"k":3}]'
      - is_superset:
        - json_parse:
          - '[{"k":1},{"k":2},{"k":3}]'
        - json_parse:
          - '[{"k":1},{"k":3}]'
      - includes:
        - json_parse:
          - '[{"k":1},{"k":2},{"k":3}]'
        - json_parse:
          - '{"k":2}'
```

## SRCONF-EXPR-013

```yaml spec-test
id: SRCONF-EXPR-013
title: evaluate map and filter support curried builtins
purpose: Verifies builtin partial application works with map/filter collection transforms.
type: text.file
requires:
  capabilities:
  - evaluate.spec_lang.ramda.v1
  when_missing: skip
expect:
  portable:
    status: skip
    category: null
  impl:
    python:
      status: pass
      category: null
assert:
- target: text
  must:
  - evaluate:
    - and:
      - eq:
        - map:
          - call:
            - var:
              - add
            - 10
          - json_parse:
            - '[1,2,3]'
        - json_parse:
          - '[11,12,13]'
      - eq:
        - filter:
          - call:
            - var:
              - lt
            - 3
          - json_parse:
            - '[1,2,3,4,5]'
        - json_parse:
          - '[4,5]'
```

## SRCONF-EXPR-014

```yaml spec-test
id: SRCONF-EXPR-014
title: evaluate reduce and collection helpers are deterministic
purpose: Verifies reduce, reject, find, partition, group_by, and uniq_by behavior with curried predicates.
type: text.file
requires:
  capabilities:
  - evaluate.spec_lang.ramda.v1
  when_missing: skip
expect:
  portable:
    status: skip
    category: null
  impl:
    python:
      status: pass
      category: null
assert:
- target: text
  must:
  - evaluate:
    - and:
      - eq:
        - reduce:
          - var:
            - add
          - 0
          - json_parse:
            - '[1,2,3,4]'
        - 10
      - eq:
        - reject:
          - call:
            - var:
              - lt
            - 2
          - json_parse:
            - '[1,2,3,4]'
        - json_parse:
          - '[1,2]'
      - eq:
        - find:
          - call:
            - var:
              - lt
            - 3
          - json_parse:
            - '[1,2,3,4]'
        - 4
      - eq:
        - partition:
          - call:
            - var:
              - lt
            - 2
          - json_parse:
            - '[1,2,3,4]'
        - json_parse:
          - '[[3,4],[1,2]]'
      - eq:
        - group_by:
          - fn:
            - x: []
            - if:
              - gt:
                - var:
                  - x
                - 2
              - hi
              - lo
          - json_parse:
            - '[1,2,3,4]'
        - json_parse:
          - '{"lo":[1,2],"hi":[3,4]}'
      - eq:
        - uniq_by:
          - fn:
            - x: []
            - get:
              - var:
                - x
              - k
          - json_parse:
            - '[{"k":1},{"k":1},{"k":2}]'
        - json_parse:
          - '[{"k":1},{"k":2}]'
```

## SRCONF-EXPR-015

```yaml spec-test
id: SRCONF-EXPR-015
title: evaluate flatten and list composition helpers
purpose: Verifies flatten, concat, append, prepend, take, and drop operations.
type: text.file
requires:
  capabilities:
  - evaluate.spec_lang.ramda.v1
  when_missing: skip
expect:
  portable:
    status: skip
    category: null
  impl:
    python:
      status: pass
      category: null
assert:
- target: text
  must:
  - evaluate:
    - and:
      - eq:
        - flatten:
          - json_parse:
            - '[1,[2,[3],[]],4]'
        - json_parse:
          - '[1,2,3,4]'
      - eq:
        - concat:
          - json_parse:
            - '[1,2]'
          - json_parse:
            - '[3]'
        - json_parse:
          - '[1,2,3]'
      - eq:
        - append:
          - 3
          - json_parse:
            - '[1,2]'
        - json_parse:
          - '[1,2,3]'
      - eq:
        - prepend:
          - 0
          - json_parse:
            - '[1,2]'
        - json_parse:
          - '[0,1,2]'
      - eq:
        - take:
          - 2
          - json_parse:
            - '[1,2,3]'
        - json_parse:
          - '[1,2]'
      - eq:
        - drop:
          - 2
          - json_parse:
            - '[1,2,3]'
        - json_parse:
          - '[3]'
```

## SRCONF-EXPR-016

```yaml spec-test
id: SRCONF-EXPR-016
title: evaluate currying chain with nested call succeeds
purpose: Verifies repeated partial application resolves deterministically to a final non-callable value.
type: text.file
requires:
  capabilities:
  - evaluate.spec_lang.ramda.v1
  when_missing: skip
expect:
  portable:
    status: skip
    category: null
  impl:
    python:
      status: pass
      category: null
assert:
- target: text
  must:
  - evaluate:
    - eq:
      - call:
        - call:
          - var:
            - add
          - 2
        - 3
      - 5
```

## SRCONF-EXPR-017

```yaml spec-test
id: SRCONF-EXPR-017
title: evaluate over-application of non-callable result is schema failure
purpose: Verifies deterministic schema failure when extra call arguments remain after returning non-callable value.
type: text.file
requires:
  capabilities:
  - evaluate.spec_lang.ramda.v1
  when_missing: skip
expect:
  portable:
    status: skip
    category: null
  impl:
    python:
      status: fail
      category: schema
      message_tokens:
      - over-application error
assert:
- target: text
  must:
  - evaluate:
    - call:
      - call:
        - var:
          - add
        - 1
      - 2
      - 3
```

## SRCONF-EXPR-018

```yaml spec-test
id: SRCONF-EXPR-018
title: evaluate set ops enforce list inputs
purpose: Verifies set algebra operators reject non-list inputs with schema errors.
type: text.file
requires:
  capabilities:
  - evaluate.spec_lang.ramda.v1
  when_missing: skip
expect:
  portable:
    status: skip
    category: null
  impl:
    python:
      status: fail
      category: schema
      message_tokens:
      - expects list
assert:
- target: text
  must:
  - evaluate:
    - intersection:
      - not-a-list
      - json_parse:
        - '[]'
```
