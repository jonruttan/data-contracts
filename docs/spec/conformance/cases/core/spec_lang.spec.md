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
harness:
  spec_lang:
    library_paths:
    - /docs/spec/libraries/conformance/assertion_core.spec.md
    exports:
    - conf.pass_when_text_contains
assert:
- target: text
  must:
  - evaluate:
    - call:
      - {var: conf.pass_when_text_contains}
      - {var: subject}
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
harness:
  spec_lang:
    library_paths:
    - /docs/spec/libraries/conformance/assertion_core.spec.md
    exports:
    - conf.pass_when_text_contains
assert:
- target: text
  must:
  - evaluate:
    - and:
      - call:
        - {var: conf.pass_when_text_contains}
        - {var: subject}
        - version
      - starts_with:
        - {var: subject}
        - '#'
```

## SRCONF-EXPR-003

```yaml spec-test
id: SRCONF-EXPR-003
title: evaluate tail recursion is stack safe
purpose: Verifies unsupported mixed literal-expression recursive forms fail deterministically
  under mapping AST hard-cut rules.
type: text.file
requires:
  capabilities:
  - evaluate.spec_lang.v1
expect:
  portable:
    status: fail
    category: schema
    message_tokens:
    - spec_lang let binding must be [name, expr]
assert:
- target: text
  must:
  - evaluate:
    - let:
      - lit:
        - - loop
          - fn:
            - [n, acc]
            - if:
              - eq:
                - {var: n}
                - 0
              - {var: acc}
              - call:
                - {var: loop}
                - sub:
                  - {var: n}
                  - 1
                - add:
                  - {var: acc}
                  - 1
      - eq:
        - call:
          - {var: loop}
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
      - {var: subject}
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
purpose: Verifies unsupported recursive literal-expression authoring shape fails deterministically
  as schema.
type: text.file
requires:
  capabilities:
  - evaluate.spec_lang.v1
expect:
  portable:
    status: fail
    category: schema
    message_tokens:
    - spec_lang let binding must be [name, expr]
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
            - [n]
            - if:
              - eq:
                - {var: n}
                - 0
              - true
              - call:
                - {var: loop}
                - sub:
                  - {var: n}
                  - 1
      - call:
        - {var: loop}
        - 1000
```

## SRCONF-EXPR-008

```yaml spec-test
id: SRCONF-EXPR-008
title: evaluate contains supports explicit subject form
purpose: Verifies evaluate contains succeeds with explicit subject arguments for the same
  target subject.
type: text.file
requires:
  capabilities:
  - evaluate.spec_lang.v1
expect:
  portable:
    status: pass
    category: null
harness:
  spec_lang:
    library_paths:
    - /docs/spec/libraries/conformance/assertion_core.spec.md
    exports:
    - conf.pass_when_text_contains
assert:
- target: text
  must:
  - evaluate:
    - call:
      - {var: conf.pass_when_text_contains}
      - {var: subject}
      - 'version: 1'
  - evaluate:
    - call:
      - {var: conf.pass_when_text_contains}
      - {var: subject}
      - 'version: 1'
```

## SRCONF-EXPR-009

```yaml spec-test
id: SRCONF-EXPR-009
title: evaluate set intersection supports deep structural equality
purpose: Verifies intersection deduplicates and compares nested values structurally with stable
  left-first output.
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
            - {var: add}
            - 10
          - json_parse:
            - '[1,2,3]'
        - json_parse:
          - '[11,12,13]'
      - eq:
        - filter:
          - call:
            - {var: lt}
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
purpose: Verifies reduce, reject, find, partition, group_by, and uniq_by behavior with curried
  predicates.
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
          - {var: add}
          - 0
          - json_parse:
            - '[1,2,3,4]'
        - 10
      - eq:
        - reject:
          - call:
            - {var: lt}
            - 2
          - json_parse:
            - '[1,2,3,4]'
        - json_parse:
          - '[1,2]'
      - eq:
        - find:
          - call:
            - {var: lt}
            - 3
          - json_parse:
            - '[1,2,3,4]'
        - 4
      - eq:
        - partition:
          - call:
            - {var: lt}
            - 2
          - json_parse:
            - '[1,2,3,4]'
        - json_parse:
          - '[[3,4],[1,2]]'
      - eq:
        - group_by:
          - fn:
            - [x]
            - if:
              - gt:
                - {var: x}
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
            - [x]
            - get:
              - {var: x}
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
purpose: Verifies repeated partial application resolves deterministically to a final non-callable
  value.
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
          - {var: add}
          - 2
        - 3
      - 5
```

## SRCONF-EXPR-017

```yaml spec-test
id: SRCONF-EXPR-017
title: evaluate over-application of non-callable result is schema failure
purpose: Verifies deterministic schema failure when extra call arguments remain after returning
  non-callable value.
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
        - {var: add}
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

## SRCONF-EXPR-019

```yaml spec-test
id: SRCONF-EXPR-019
title: evaluate ramda v2 arithmetic and list utilities behave deterministically
purpose: Verifies expanded numeric and list utility forms remain pure, strict-typed, and deterministic.
type: text.file
requires:
  capabilities:
  - evaluate.spec_lang.ramda.v2
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
        - mul:
          - 3
          - 4
        - 12
      - eq:
        - div:
          - 9
          - 2
        - 4.5
      - eq:
        - mod:
          - 9
          - 4
        - 1
      - eq:
        - pow:
          - 2
          - 5
        - 32
      - eq:
        - clamp:
          - 1
          - 5
          - 9
        - 5
      - eq:
        - round:
          - 2.5
        - 3
      - eq:
        - slice:
          - 1
          - 3
          - json_parse:
            - '[0,1,2,3]'
        - json_parse:
          - '[1,2]'
      - eq:
        - reverse:
          - json_parse:
            - '[1,2,3]'
        - json_parse:
          - '[3,2,1]'
      - eq:
        - zip:
          - json_parse:
            - '[1,2,3]'
          - json_parse:
            - '[4,5]'
        - json_parse:
          - '[[1,4],[2,5]]'
      - eq:
        - zip_with:
          - {var: add}
          - json_parse:
            - '[1,2,3]'
          - json_parse:
            - '[4,5,6]'
        - json_parse:
          - '[5,7,9]'
      - eq:
        - range:
          - 2
          - 5
        - json_parse:
          - '[2,3,4]'
      - eq:
        - repeat:
          - x
          - 3
        - json_parse:
          - '["x","x","x"]'
      - is_null:
        - null
      - is_bool:
        - true
      - is_number:
        - 3.14
      - is_string:
        - x
      - is_list:
        - json_parse:
          - '[1,2]'
      - is_dict:
        - json_parse:
          - '{"a":1}'
```

## SRCONF-EXPR-020

```yaml spec-test
id: SRCONF-EXPR-020
title: evaluate ramda v2 object utilities
purpose: Verifies expanded object helpers keep deterministic dictionary semantics.
type: text.file
requires:
  capabilities:
  - evaluate.spec_lang.ramda.v2
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
        - keys:
          - json_parse:
            - '{"a":1,"b":2}'
        - json_parse:
          - '["a","b"]'
      - eq:
        - values:
          - json_parse:
            - '{"a":1,"b":2}'
        - json_parse:
          - '[1,2]'
      - eq:
        - entries:
          - json_parse:
            - '{"a":1}'
        - json_parse:
          - '[["a",1]]'
      - eq:
        - merge:
          - json_parse:
            - '{"a":1}'
          - json_parse:
            - '{"b":2}'
        - json_parse:
          - '{"a":1,"b":2}'
      - eq:
        - assoc:
          - b
          - 2
          - json_parse:
            - '{"a":1}'
        - json_parse:
          - '{"a":1,"b":2}'
      - eq:
        - dissoc:
          - a
          - json_parse:
            - '{"a":1,"b":2}'
        - json_parse:
          - '{"b":2}'
      - eq:
        - pick:
          - json_parse:
            - '["a"]'
          - json_parse:
            - '{"a":1,"b":2}'
        - json_parse:
          - '{"a":1}'
      - eq:
        - omit:
          - json_parse:
            - '["a"]'
          - json_parse:
            - '{"a":1,"b":2}'
        - json_parse:
          - '{"b":2}'
      - prop_eq:
        - a
        - 1
        - json_parse:
          - '{"a":1}'
      - where:
        - json_parse:
          - '{"a":1}'
        - json_parse:
          - '{"a":1,"b":2}'
```

## SRCONF-EXPR-021

```yaml spec-test
id: SRCONF-EXPR-021
title: evaluate ramda v2 combinators and string helpers
purpose: Verifies compose/pipe, constant-function behavior, and string transforms are deterministic.
type: text.file
requires:
  capabilities:
  - evaluate.spec_lang.ramda.v2
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
        - compose:
          - call:
            - {var: add}
            - 1
          - call:
            - {var: mul}
            - 2
          - 3
        - 7
      - eq:
        - pipe:
          - call:
            - {var: mul}
            - 2
          - call:
            - {var: add}
            - 1
          - 3
        - 7
      - eq:
        - call:
          - call:
            - {var: always}
            - k
          - 999
        - k
      - eq:
        - replace:
          - a-b-c
          - '-'
          - ':'
        - a:b:c
      - eq:
        - pad_left:
          - '7'
          - 3
          - '0'
        - '007'
      - eq:
        - pad_right:
          - '7'
          - 3
          - '0'
        - '700'
```

## SRCONF-EXPR-022

```yaml spec-test
id: SRCONF-EXPR-022
title: evaluate ramda v2 unary numeric and compare helpers
purpose: Verifies unary numeric helpers and comparison helpers produce deterministic values
  for policy expressions.
type: text.file
requires:
  capabilities:
  - evaluate.spec_lang.ramda.v2
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
        - abs:
          - -7
        - 7
      - eq:
        - negate:
          - 3
        - -3
      - eq:
        - inc:
          - 3
        - 4
      - eq:
        - dec:
          - 3
        - 2
      - eq:
        - floor:
          - 3.9
        - 3
      - eq:
        - ceil:
          - 3.1
        - 4
      - eq:
        - compare:
          - 3
          - 5
        - -1
      - eq:
        - compare:
          - 5
          - 5
        - 0
      - eq:
        - compare:
          - 7
          - 5
        - 1
      - between:
        - 1
        - 3
        - 2
      - xor:
        - true
        - false
      - not:
        - xor:
          - true
          - true
```

## SRCONF-EXPR-023

```yaml spec-test
id: SRCONF-EXPR-023
title: evaluate ramda v2 utility and predicate helpers
purpose: Verifies utility and predicate helpers used by governance logic are deterministic
  and pure.
type: text.file
requires:
  capabilities:
  - evaluate.spec_lang.ramda.v2
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
        - count:
          - json_parse:
            - '[1,2,3]'
        - 3
      - eq:
        - first:
          - json_parse:
            - '[9,8,7]'
        - 9
      - eq:
        - rest:
          - json_parse:
            - '[9,8,7]'
        - json_parse:
          - '[8,7]'
      - eq:
        - trim:
          - '  x  '
        - x
      - eq:
        - lower:
          - AbC
        - abc
      - eq:
        - upper:
          - AbC
        - ABC
      - eq:
        - split:
          - a,b,c
          - ','
        - json_parse:
          - '["a","b","c"]'
      - eq:
        - join:
          - json_parse:
            - '["a","b","c"]'
          - '-'
        - a-b-c
      - eq:
        - coalesce:
          - null
          - x
        - x
      - eq:
        - distinct:
          - json_parse:
            - '[1,1,2,2,3]'
        - json_parse:
          - '[1,2,3]'
      - eq:
        - sort_by:
          - json_parse:
            - '[3,1,2]'
          - {var: identity}
        - json_parse:
          - '[1,2,3]'
      - eq:
        - pluck:
          - json_parse:
            - '[{"k":1},{"k":2}]'
          - k
        - json_parse:
          - '[1,2]'
      - all:
        - json_parse:
          - '[true,true,true]'
      - any:
        - json_parse:
          - '[false,true,false]'
      - none:
        - json_parse:
          - '[false,false]'
      - is_empty:
        - json_parse:
          - '[]'
      - matches:
        - a42
        - a[0-9]+
      - matches_all:
        - a42
        - json_parse:
          - '["^a","[0-9]+$"]'
      - regex_match:
        - a42
        - a[0-9]+
      - eq:
        - json_type:
          - json_parse:
            - '[1,2]'
          - list
        - true
      - eq:
        - json_type:
          - json_parse:
            - '{"x":1}'
          - object
        - true
      - eq:
        - json_type:
          - json_parse:
            - '[1,2]'
          - array
        - true
      - eq:
        - json_type:
          - true
          - boolean
        - true
      - has_key:
        - json_parse:
          - '{"x":1}'
        - x
      - in:
        - x
        - json_parse:
          - '{"x":1}'
      - eq:
        - len:
          - abcd
        - 4
      - is_boolean:
        - true
      - is_array:
        - json_parse:
          - '[1,2]'
      - is_object:
        - json_parse:
          - '{"x":1}'
      - eq:
        - sum:
          - json_parse:
            - '[1,2,3]'
        - 6
      - eq:
        - min:
          - json_parse:
            - '[4,2,8]'
        - 2
      - eq:
        - max:
          - json_parse:
            - '[4,2,8]'
        - 8
```

## SRCONF-EXPR-024

```yaml spec-test
id: SRCONF-EXPR-024
title: evaluate ramda v2 schema failures are deterministic
purpose: Verifies representative arity and type failures stay in schema category for the expanded
  builtin surface.
type: text.file
requires:
  capabilities:
  - evaluate.spec_lang.ramda.v2
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
      - arity error
assert:
- target: text
  must:
  - evaluate:
    - compare:
      - 1
```
