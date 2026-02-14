## Summary

- What changed:
- Why:

## Validation

- [ ] `./scripts/ci_gate.sh`
- [ ] `./scripts/docs_doctor.sh` (or `make verify-docs`)

## Docs Drift Checklist

- [ ] If reference chapters changed, `/Users/jon/Workspace/Development/spec_runner/docs/book/reference_index.md` is still synchronized.
- [ ] New or edited examples are parseable/runnable, or explicitly marked with `DOCS-EXAMPLE-OPT-OUT: <reason>`.
- [ ] Public CLI flag changes are reflected in `/Users/jon/Workspace/Development/spec_runner/docs/development.md` and relevant impl docs.
