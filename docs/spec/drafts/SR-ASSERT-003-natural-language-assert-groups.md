# SR-ASSERT-003: Natural-Language Assertion Groups

Status: Draft (Superseded by SR-ASSERT-004)
Created: 2026-02-12

## Problem

Assertion groups `all` / `any` are precise but read less naturally in spec
docs.

## Proposal

Adopt natural-language group keys:

- `must`: all child assertions must pass
- `can`: at least one child assertion may pass
- `cannot`: no child assertion may pass

Also adopt `contain` as the preferred text operator spelling. `contains`
remains accepted as a compatibility alias.

## Examples

```yaml
assert:
  - target: stderr
    must:
      - contain: ["WARN:"]
    cannot:
      - contain: ["ERROR:"]
```

```yaml
assert:
  - target: stdout
    can:
      - json_type: ["list"]
      - contain: ["[]"]
```

## Compatibility

Superseded by `SR-ASSERT-004`, which removes shorthand/alias keys and supports
canonical keys only.
