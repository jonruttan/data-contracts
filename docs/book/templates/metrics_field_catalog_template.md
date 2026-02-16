## Generated Metrics Field Catalog

- baseline_count: {{metrics.summary.baseline_count}}
- unique_summary_field_count: {{metrics.summary.unique_summary_field_count}}
- unique_segment_field_count: {{metrics.summary.unique_segment_field_count}}

| baseline | summary_fields | segment_count |
|---|---|---|
{{#metrics.baselines}}| `{{file}}` | {{summary_field_count}} | {{segment_count}} |
{{/metrics.baselines}}
