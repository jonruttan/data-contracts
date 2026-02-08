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
- `kind` (string, required): dispatch key (e.g. `cli.run`)
- `title` (string, optional): human description

## `harness` Namespace

Runner-only inputs MUST live under `harness:` to preserve separation of
concerns and keep the spec format portable.

For `type: cli.run`, supported `harness` keys include:

- `entrypoint` (string): CLI entrypoint to call (e.g. `myproj.cli:main`)
- `env` (mapping): env vars to set/unset before running the CLI
- `stdin_isatty` (bool): simulate TTY vs piped stdin
- `stdin_text` (string): text to provide on stdin
- `block_imports` (list[string]): make imports fail with `ModuleNotFoundError`
- `stub_modules` (list[string]): pre-populate `sys.modules` with stubs
- `setup_files` (list[{path, text}]): write files under the runner temp dir

## Kinds

Currently supported kinds:

- `cli.run` (core)

Other kinds are adapters provided by the system under test.
