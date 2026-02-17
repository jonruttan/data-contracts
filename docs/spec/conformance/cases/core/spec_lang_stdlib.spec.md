# Conformance Cases

## SRCONF-STDLIB-001

```yaml spec-test
id: SRCONF-STDLIB-001
title: core numeric and set operators evaluate deterministically
purpose: Validates representative numeric operators in the stdlib profile.
type: text.file
path: /docs/spec/conformance/cases/core/spec_lang_stdlib.spec.md
expect:
  portable:
    status: pass
assert:
- id: assert_1
  class: must
  checks:
  - must:
    - std.logic.eq:
      - std.math.add:
        - 2
        - 3
      - 5
    - std.logic.eq:
      - std.math.sub:
        - 9
        - 4
      - 5
    - std.logic.eq:
      - std.math.add:
        - 1
        - 1
      - 2
    - std.logic.eq:
      - std.math.sub:
        - 3
        - 3
      - 0
  target: text
```

## SRCONF-STDLIB-002

```yaml spec-test
id: SRCONF-STDLIB-002
title: core collection and object operators evaluate deterministically
purpose: Validates representative object and json operators in the stdlib profile.
type: text.file
path: /docs/spec/conformance/cases/core/spec_lang_stdlib.spec.md
expect:
  portable:
    status: pass
assert:
- id: assert_1
  class: must
  checks:
  - must:
    - std.logic.eq:
      - std.type.json_type:
        - std.json.parse:
          - '{"a":1,"b":2}'
        - dict
      - true
    - std.logic.eq:
      - std.object.has_key:
        - std.json.parse:
          - '{"a":{"b":1}}'
        - a
      - true
    - std.logic.eq:
      - std.type.json_type:
        - std.object.get:
          - std.json.parse:
            - '{"a":{"b":1}}'
          - a
        - dict
      - true
  target: text
```

## SRCONF-STDLIB-003

```yaml spec-test
id: SRCONF-STDLIB-003
title: ops fs path operators evaluate deterministically
purpose: Validates pure contract-posix path helpers under ops.fs.path.
type: text.file
path: /docs/spec/conformance/cases/core/spec_lang_stdlib.spec.md
expect:
  portable:
    status: pass
assert:
- id: assert_1
  class: must
  checks:
  - must:
    - std.logic.eq:
      - ops.fs.path.normalize:
        - /a//b/./c
      - /a/b/c
    - std.logic.eq:
      - ops.fs.path.normalize:
        - /a/b/../c
      - /a/c
    - std.logic.eq:
      - ops.fs.path.join:
        - /a/b
        - c
      - /a/b/c
    - std.logic.eq:
      - ops.fs.path.extname:
        - file.tar.gz
      - .gz
    - std.logic.eq:
      - ops.fs.path.stem:
        - file.tar.gz
      - file.tar
    - std.logic.eq:
      - ops.fs.path.change_ext:
        - a/b.txt
        - md
      - a/b.md
    - std.logic.eq:
      - ops.fs.path.change_ext:
        - a/b.txt
        - ''
      - a/b
  target: text
```

## SRCONF-STDLIB-004

```yaml spec-test
id: SRCONF-STDLIB-004
title: ops fs file metadata helpers evaluate deterministically
purpose: Validates metadata-only file predicates and getters under ops.fs.file.
type: text.file
path: /docs/spec/conformance/cases/core/spec_lang_stdlib.spec.md
expect:
  portable:
    status: pass
assert:
- id: assert_1
  class: must
  checks:
  - must:
    - std.logic.eq:
      - ops.fs.file.exists:
        - lit: {path: /docs/spec/conformance/cases/core/spec_lang_stdlib.spec.md, exists: true, type: file, size_bytes: 12}
      - true
    - std.logic.eq:
      - ops.fs.file.is_file:
        - lit: {path: /docs/spec/conformance/cases/core/spec_lang_stdlib.spec.md, exists: true, type: file}
      - true
    - std.logic.eq:
      - ops.fs.file.is_dir:
        - lit: {path: /docs, exists: true, type: dir}
      - true
    - std.logic.eq:
      - ops.fs.file.name:
        - lit: {path: /docs/spec/conformance/cases/core/spec_lang_stdlib.spec.md}
      - spec_lang_stdlib.spec.md
    - std.logic.eq:
      - ops.fs.file.parent:
        - lit: {path: /docs/spec/conformance/cases/core/spec_lang_stdlib.spec.md}
      - /docs/spec/conformance/cases/core
    - std.logic.eq:
      - ops.fs.file.ext:
        - lit: {path: /docs/spec/conformance/cases/core/spec_lang_stdlib.spec.md}
      - .md
    - std.logic.eq:
      - ops.fs.file.get:
        - lit: {path: /docs/spec/conformance/cases/core/spec_lang_stdlib.spec.md, exists: true}
        - missing
        - fallback
      - fallback
  target: text
```

## SRCONF-STDLIB-005

```yaml spec-test
id: SRCONF-STDLIB-005
title: ops fs json helpers evaluate deterministically
purpose: Validates pure json parse/path helpers under ops.fs.json.
type: text.file
path: /docs/spec/conformance/cases/core/spec_lang_stdlib.spec.md
expect:
  portable:
    status: pass
assert:
- id: assert_1
  class: must
  checks:
  - must:
    - std.logic.eq:
      - ops.fs.json.parse:
        - '{"a":{"b":[1,2,3]}}'
      - lit: {a: {b: [1, 2, 3]}}
    - std.logic.eq:
      - ops.fs.json.get:
        - lit: {a: {b: [1, 2, 3]}}
        - lit: [a, b, 1]
      - 2
    - std.logic.eq:
      - ops.fs.json.get_or:
        - lit: {a: {b: [1, 2, 3]}}
        - lit: [a, c]
        - fallback
      - fallback
    - std.logic.eq:
      - ops.fs.json.has_path:
        - lit: {a: {b: [1, 2, 3]}}
        - lit: [a, b, 0]
      - true
  target: text
```

## SRCONF-STDLIB-006

```yaml spec-test
id: SRCONF-STDLIB-006
title: ops fs json helpers fail schema for bad argument shapes
purpose: Ensures ops.fs.json path utilities reject invalid path shapes.
type: text.file
path: /docs/spec/conformance/cases/core/spec_lang_stdlib.spec.md
expect:
  portable:
    status: fail
    category: schema
assert:
- id: assert_1
  class: must
  checks:
  - must:
    - std.logic.eq:
      - ops.fs.json.get:
        - lit: {a: 1}
        - a
      - 1
  target: text
```

## SRCONF-STDLIB-007

```yaml spec-test
id: SRCONF-STDLIB-007
title: ops fs glob helpers evaluate deterministically
purpose: Validates pure glob matching/filter helpers under ops.fs.glob.
type: text.file
path: /docs/spec/conformance/cases/core/spec_lang_stdlib.spec.md
expect:
  portable:
    status: pass
assert:
- id: assert_1
  class: must
  checks:
  - must:
    - std.logic.eq:
      - ops.fs.glob.match:
        - docs/spec/current.md
        - docs/spec/*.md
      - true
    - std.logic.eq:
      - ops.fs.glob.filter:
        - lit: [docs/spec/current.md, docs/book/index.md, README.md]
        - docs/spec/*.md
      - lit: [docs/spec/current.md]
    - std.logic.eq:
      - ops.fs.glob.any:
        - lit: [docs/spec/current.md, docs/book/index.md]
        - docs/spec/*.md
      - true
    - std.logic.eq:
      - ops.fs.glob.all:
        - lit: [docs/spec/current.md]
        - docs/spec/*.md
      - true
  target: text
```

## SRCONF-STDLIB-008

```yaml spec-test
id: SRCONF-STDLIB-008
title: ops fs glob helpers fail schema for bad argument shapes
purpose: Ensures ops.fs.glob helpers reject invalid list element types.
type: text.file
path: /docs/spec/conformance/cases/core/spec_lang_stdlib.spec.md
expect:
  portable:
    status: fail
    category: schema
assert:
- id: assert_1
  class: must
  checks:
  - must:
    - std.logic.eq:
      - ops.fs.glob.any:
        - lit: [7, docs/spec/current.md]
        - docs/spec/*.md
      - true
  target: text
```

## SRCONF-STDLIB-009

```yaml spec-test
id: SRCONF-STDLIB-009
title: ops fs path relativize and common_prefix evaluate deterministically
purpose: Validates pure relative-path and common-prefix helpers.
type: text.file
path: /docs/spec/conformance/cases/core/spec_lang_stdlib.spec.md
expect:
  portable:
    status: pass
assert:
- id: assert_1
  class: must
  checks:
  - must:
    - std.logic.eq:
      - ops.fs.path.relativize:
        - /a/b/c
        - /a/d/e
      - ../../d/e
    - std.logic.eq:
      - ops.fs.path.relativize:
        - a/b
        - a/b/c/d
      - c/d
    - std.logic.eq:
      - ops.fs.path.common_prefix:
        - lit: [/a/b/c.md, /a/b/d.md]
      - /a/b
    - std.logic.eq:
      - ops.fs.path.common_prefix:
        - lit: [docs/spec/current.md, docs/spec/schema/schema_v1.md]
      - docs/spec
  target: text
```

## SRCONF-STDLIB-010

```yaml spec-test
id: SRCONF-STDLIB-010
title: ops fs path common_prefix fails schema for non-string entries
purpose: Ensures common_prefix rejects list entries that are not strings.
type: text.file
path: /docs/spec/conformance/cases/core/spec_lang_stdlib.spec.md
expect:
  portable:
    status: fail
    category: schema
assert:
- id: assert_1
  class: must
  checks:
  - must:
    - std.logic.eq:
      - ops.fs.path.common_prefix:
        - lit: [/a/b, 7]
      - /a
  target: text
```

## SRCONF-STDLIB-011

```yaml spec-test
id: SRCONF-STDLIB-011
title: ops fs path parents and within evaluate deterministically
purpose: Validates pure parent chain and containment helpers.
type: text.file
path: /docs/spec/conformance/cases/core/spec_lang_stdlib.spec.md
expect:
  portable:
    status: pass
assert:
- id: assert_1
  class: must
  checks:
  - must:
    - std.logic.eq:
      - ops.fs.path.parents:
        - /a/b/c
      - lit: [/a/b, /a, /]
    - std.logic.eq:
      - ops.fs.path.parents:
        - a/b/c
      - lit: [a/b, a, .]
    - std.logic.eq:
      - ops.fs.path.within:
        - /a/b
        - /a/b/c/d
      - true
    - std.logic.eq:
      - ops.fs.path.within:
        - docs/spec
        - docs/spec/current.md
      - true
    - std.logic.eq:
      - ops.fs.path.within:
        - /a/b
        - /a/c
      - false
  target: text
```

## SRCONF-STDLIB-012

```yaml spec-test
id: SRCONF-STDLIB-012
title: ops fs path parents fails schema for non-string argument
purpose: Ensures parents rejects non-string input.
type: text.file
path: /docs/spec/conformance/cases/core/spec_lang_stdlib.spec.md
expect:
  portable:
    status: fail
    category: schema
assert:
- id: assert_1
  class: must
  checks:
  - must:
    - std.logic.eq:
      - ops.fs.path.parents:
        - 7
      - lit: []
  target: text
```
