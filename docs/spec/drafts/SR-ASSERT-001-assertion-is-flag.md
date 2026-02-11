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
- `not_contains` and `not_regex` remain supported as backward-compatible aliases.

## Examples

Canonical shape:

```yaml
assert:
  - target: stderr
    contains: ["ERROR:"]
    is: false
```

Equivalent legacy shape (still supported):

```yaml
assert:
  - target: stderr
    not_contains: ["ERROR:"]
```

Default `is: true` (omitted):

```yaml
assert:
  - target: stdout
    regex: ["^usage:"]
```

## Compatibility

- Existing specs using `not_contains` and `not_regex` continue to pass.
- New docs and examples should prefer canonical `contains`/`regex` plus `is`.
