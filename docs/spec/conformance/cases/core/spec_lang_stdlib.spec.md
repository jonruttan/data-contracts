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
