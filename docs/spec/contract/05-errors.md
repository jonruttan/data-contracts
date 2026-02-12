# Error Contract (v1)

Implementations SHOULD preserve these error categories:

- schema/config errors (shape/key/type violations)
- assertion failures (conditions not met)
- harness/runtime errors (invocation/setup failures)

Error text can vary by language, but SHOULD be direct and actionable.
