# Spec-Test Schema (v1)

This schema defines the stable shape of executable spec tests embedded in
`docs/spec/*.md` as fenced blocks:

```text
```yaml spec-test
...
```
```

## Common Fields

- `id` (string, required): stable identifier like `CK-CLI-001`
- `type` (string, required): dispatch key (e.g. `cli.run`)
- `title` (string, optional): human description
- `assert_health` (mapping, optional): assertion-health policy override
- `expect` (mapping, optional): conformance outcome expectations
- `requires` (mapping, optional): capability requirements metadata

Parser behavior:

- discovery scans `*.md` in the provided directory (non-recursive)
- fence extraction accepts Markdown fences using either backticks or tildes
  (3+), with info tokens including `spec-test` and `yaml`/`yml`
- closing fences must use the same fence character and at least the opener
  length
- legacy `kind` is accepted and normalized to `type`

`assert_health`:

- `mode` (string): one of `ignore`, `warn`, `error`
- if omitted, implementations may use a global default (for example env policy)
- policy-driven diagnostics may include redundant sibling assertion branches

`expect` (conformance metadata):

- `portable` (mapping): shared expectation baseline
- `impl` (mapping): per-implementation overlays keyed by runtime name
- expected keys in `portable`/`impl.*`:
  - `status`: `pass`, `fail`, or `skip`
  - `category`: `schema` / `assertion` / `runtime` / `null`
  - `message_tokens`: optional list of expected message tokens
- for conformance fixture cases, `expect.portable` with `status` is required

`requires` (metadata):

- `capabilities` (list[string], optional): declared capabilities for the case
- `when_missing` (string, optional): `skip` or `fail` (default `fail`)

## Type-Specific Fields

### `type: text.file`

`text.file` asserts against file content.

- If `path` is omitted, the runner asserts against the spec document that
  contains the `yaml spec-test` block.
- If `path` is provided, it MUST be a relative path and is resolved relative to
  the spec document path.
- Resolved `path` MUST remain within the implementation's configured contract
  root/workspace boundary (path traversal outside that boundary is invalid).

Fields:

- `path` (string, optional): relative path to the file to read

Assertion targets for `text.file`:

- `text`

## `harness` Namespace

Runner-only inputs MUST live under `harness:` to preserve separation of
concerns and keep the spec format portable.

For `type: cli.run`, supported `harness` keys include:

- `entrypoint` (string, required): CLI entrypoint to call (e.g. `myproj.cli:main`)
- `env` (mapping): env vars to set/unset before running the CLI
- `stdin_isatty` (bool): simulate TTY vs piped stdin
- `stdin_text` (string): text to provide on stdin
- `block_imports` (list[string]): make imports fail with `ModuleNotFoundError`
- `stub_modules` (list[string]): pre-populate `sys.modules` with stubs
- `setup_files` (list[{path, text}]): write files under the runner temp dir
- `hook_before` (string): hook entrypoint invoked before running the CLI
- `hook_after` (string): hook entrypoint invoked after running the CLI
- `hook_kwargs` (mapping): keyword arguments passed through to the hook

`setup_files[*].path` constraints:

- MUST be relative
- MUST resolve within the runner temp directory (no path escape)

Implementation note (non-portable convenience):

- Runners MAY offer an environment fallback (for example
  `SPEC_RUNNER_ENTRYPOINT`) when `harness.entrypoint` is omitted.
- Conformance fixtures SHOULD always set `harness.entrypoint` explicitly.

Assertion targets for `cli.run`:

- `stdout`: text output from command stdout
- `stderr`: text output from command stderr
- `stdout_path`: path printed on first non-empty stdout line (supports `exists` only)
- `stdout_path_text`: UTF-8 text from file at `stdout_path`

## Types

Currently supported types:

- `cli.run` (core)
- `text.file` (core)

Other kinds are adapters provided by the system under test.

## Assertion Leaf Shape

Assertion leaves are mappings with:

- one or more operator keys with list values

Assertion group nodes (`must` / `can` / `cannot`) MAY include `target`; child leaves
inherit that target.
Each group node MUST include exactly one of `must`, `can`, or `cannot`.

Leaf constraints:

- leaf assertions MUST NOT include `target`
- leaves require inherited target from a parent group

Supported operators:

- text operators: `contain`, `regex`
- additional per-harness operators such as `json_type` and `exists`

Operator constraints:

- all operator values MUST be lists
- `regex` SHOULD use a portable subset; implementations SHOULD diagnose
  non-portable constructs via assertion-health policy
- the portable profile is defined in
  `docs/spec/contract/03a-regex-portability-v1.md`
- `json_type` supports `dict` and `list`
- `exists` is currently supported only for `target: stdout_path`
- `stdout_path.exists` only accepts `true` (or `null`) values

Group constraints:

- `must`, `can`, and `cannot` values MUST be lists
- `must`, `can`, and `cannot` lists MUST NOT be empty

Canonical negation uses `cannot`:

```yaml
assert:
  - target: stderr
    cannot:
      - contain: ["ERROR:"]
```

Legacy negated text operators (`not_contains`, `not_regex`) are not supported.
Legacy aliases/shorthand (`all`, `any`, `contains`, leaf-level `is`) are not
supported.

Example with target inheritance:

```yaml
assert:
  - target: stderr
    must:
      - contain: ["WARN:"]
  - target: stderr
    cannot:
      - contain: ["ERROR:"]
  - target: stdout
    can:
      - json_type: ["list"]
      - contain: ["[]"]
```
