# SR-ASSERT-004: Remove Assertion Shorthand and Aliases

Status: Draft
Created: 2026-02-12

## Problem

Supporting both canonical and shorthand assertion keys adds parser complexity
and makes spec style inconsistent across docs.

## Proposal

Support only canonical assertion keys:

- groups: `must`, `can`, `cannot`
- text ops: `contain`, `regex`

Remove shorthand/alias keys:

- group aliases: `all`, `any`
- text alias: `contains`
- leaf polarity key: `is`

Negation is represented with `cannot` only.

## Example

```yaml
assert:
  - target: stderr
    must:
      - contain: ["WARN:"]
    cannot:
      - contain: ["ERROR:"]
```

## Compatibility

- This is intentionally breaking for shorthand users.
- Spec docs and tests should be updated to canonical keys before rollout.
