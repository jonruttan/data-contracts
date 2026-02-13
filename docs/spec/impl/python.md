# Python Implementation Notes

This document captures Python-specific implementation details that are not
part of the language-neutral contract.

Current implementation locations:

- parser: `spec_runner/doc_parser.py`
- assertion engine: `spec_runner/assertions.py`
- dispatch: `spec_runner/dispatcher.py`
- harnesses: `spec_runner/harnesses/`

Implementation convenience:

- `cli.run` supports `SPEC_RUNNER_ENTRYPOINT` fallback when
  `harness.entrypoint` is not set.
- `SPEC_RUNNER_SAFE_MODE=1` hardens `cli.run` by disabling hook entrypoints
  and env fallback; explicit `harness.entrypoint` is required in this mode.
- Portable fixtures should still set `harness.entrypoint` explicitly.
