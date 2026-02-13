# Chapter 1: Quickstart

This chapter gets you from zero to a passing executable spec in minutes.

## 1) Write A Minimal Case

Create a Markdown file with a fenced `yaml spec-test` block:

```yaml
id: BK-QS-001
type: text.file
assert:
  - target: text
    must:
      - contain: ["BK-QS-001"]
```

Why this passes:

- `type: text.file` reads the containing spec file by default.
- The file contains the case id string, so the `contain` assertion succeeds.

## 2) Run The Repo Gate

From repo root:

```sh
./scripts/ci_gate.sh
```

This runs governance checks, conformance reports, parity checks, and tests.

## 3) Add A CLI Case

```yaml
id: BK-QS-002
type: cli.run
argv: ["hello"]
exit_code: 0
harness:
  entrypoint: /bin/echo
assert:
  - target: stdout
    must:
      - contain: ["hello"]
```

## 4) Common Authoring Mistakes

Invalid:

```yaml
id: BK-QS-003
type: cli.run
entrypoint: /bin/echo
assert: []
```

Problem:

- `entrypoint` is a runner-only key and must be under `harness:`.

Expected fix:

```yaml
id: BK-QS-003
type: cli.run
harness:
  entrypoint: /bin/echo
assert: []
```

## 5) Checklist

- Case has `id` and `type`.
- Runner-only config lives under `harness:`.
- `assert` uses canonical groups/operators.
- Case is small and focused.
- `./scripts/ci_gate.sh` passes locally.
