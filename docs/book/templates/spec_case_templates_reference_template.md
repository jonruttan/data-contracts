## Generated Spec Case Templates

- version: `{{templates.version}}`
- generated_at: `{{templates.generated_at}}`

## Canonical Full Templates

### contract.check

```yaml contract-spec
{{templates.contract_check}}
```

### contract.job

```yaml contract-spec
{{templates.contract_job}}
```

### contract.export

```yaml contract-spec
{{templates.contract_export}}
```

## Notes

- These are canonical authoring templates for v1 shape.
- Use explicit `contract.imports` and `steps[].assert`.
- Keep Rust lane examples canonical in active docs.
