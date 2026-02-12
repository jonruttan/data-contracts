# SR-ASSERT-002: Target-Scoped Assertion Groups

Status: Draft
Created: 2026-02-12

## Problem

Spec-test assertions often repeat the same `target` across many leaves. This is
verbose and makes grouped checks harder to read.

## Proposal

Allow `target` on assertion group nodes (`all` / `any`) and let descendant
leaves inherit it by default.

Rules:

- Group nodes may include `target`.
- Child leaves may omit `target` when inherited from an ancestor group.
- Child leaves may still set their own `target` to override inheritance.
- If no explicit or inherited target is available for a leaf, parsing/evaluation
  fails with a direct schema error.

## Examples

```yaml
assert:
  - target: stderr
    must:
      - contain: ["WARN:"]
    cannot:
      - contain: ["ERROR:"]
```

Per-child override:

```yaml
assert:
  - target: stderr
    must:
      - contain: ["WARN:"]
      - target: stdout
        contain: ["ok"]
```

## Compatibility

- Backward compatible with existing leaf-level `target` assertions.
- Existing assertions remain valid unchanged.
