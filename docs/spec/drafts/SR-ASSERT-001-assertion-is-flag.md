# SR-ASSERT-001: Assertion `is` Polarity Flag

Status: Draft
Created: 2026-02-11

## Problem

Negated text assertions currently use separate operator names (`not_contains`,
`not_regex`). This is harder to scan and adds avoidable operator surface area.

## Proposal

Add optional `is` to assertion leaves:

- `is` is optional and defaults to `true`.
- `is: false` inverts assertion polarity.
- For text assertions, canonical operators are `contains` and `regex`.
- `not_contains` and `not_regex` are not supported.

## Examples

Canonical shape:

```yaml
assert:
  - target: stderr
    contains: ["ERROR:"]
    is: false
```

Legacy `not_contains`/`not_regex` shapes are rejected. Use canonical
`contains`/`regex` with `is: false`.

Default `is: true` (omitted):

```yaml
assert:
  - target: stdout
    regex: ["^usage:"]
```

## Compatibility

- This intentionally removes support for legacy `not_*` text operators.
