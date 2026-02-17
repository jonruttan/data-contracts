## Summary

- What changed:
- Why:

## Validation

- [ ] `make verify-docs`
- [ ] `make core-check`
- [ ] `make check`
- [ ] `make prepush`
- [ ] `make prepush-parity`
- [ ] `make ci-cleanroom`

## Docs Drift Checklist

- [ ] If reference chapters changed, `/Users/jon/Workspace/Development/spec_runner/docs/book/reference_index.md` is still synchronized.
- [ ] New or edited examples are parseable/runnable, or explicitly marked with `DOCS-EXAMPLE-OPT-OUT: <reason>`.
- [ ] Public CLI flag changes are reflected in `/Users/jon/Workspace/Development/spec_runner/docs/development.md` and relevant impl docs.
- [ ] Assertion behavior changes do not add direct leaf-op execution branches outside spec-lang paths.
