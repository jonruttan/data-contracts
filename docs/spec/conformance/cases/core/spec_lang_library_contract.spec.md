# Spec-Lang Library Contract Conformance Cases

## SRCONF-LIB-CONTRACT-001

```yaml spec-test
id: SRCONF-LIB-CONTRACT-001
title: policy library uses flat defines scopes
purpose: Ensures policy library authoring uses defines.public/defines.private symbol maps
  without nested functions blocks.
type: text.file
path: /docs/spec/libraries/policy/policy_core.spec.md
expect:
  portable:
    status: pass
assert:
- target: text
  must:
  - evaluate:
    - std.string.contains:
      - {var: subject}
      - 'defines:'
    - std.string.contains:
      - {var: subject}
      - 'public:'
    - std.string.contains:
      - {var: subject}
      - 'private:'
    - std.logic.not:
      - std.string.contains:
        - {var: subject}
        - 'functions:'
```

## SRCONF-LIB-CONTRACT-002

```yaml spec-test
id: SRCONF-LIB-CONTRACT-002
title: path library uses flat defines scopes
purpose: Ensures path library authoring uses defines.public/defines.private symbol maps without
  nested functions blocks.
type: text.file
path: /docs/spec/libraries/path/path_core.spec.md
expect:
  portable:
    status: pass
assert:
- target: text
  must:
  - evaluate:
    - std.string.contains:
      - {var: subject}
      - 'defines:'
    - std.string.contains:
      - {var: subject}
      - 'public:'
    - std.string.contains:
      - {var: subject}
      - 'private:'
    - std.logic.not:
      - std.string.contains:
        - {var: subject}
        - 'functions:'
```

## SRCONF-LIB-CONTRACT-003

```yaml spec-test
id: SRCONF-LIB-CONTRACT-003
title: library index exports only public symbols
purpose: Ensures generated library index contains public export symbols and does not expose
  private-only symbols.
type: text.file
path: /docs/spec/libraries/policy/index.md
expect:
  portable:
    status: pass
assert:
- target: text
  must:
  - evaluate:
    - std.string.contains:
      - {var: subject}
      - policy.pass_when_no_violations
    - std.logic.not:
      - std.string.contains:
        - {var: subject}
        - policy.fail_when_has_violations
```
