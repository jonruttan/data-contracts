# Spec-Lang Builtin Catalog

```yaml doc-meta
doc_id: DOC-REF-093
title: Appendix Spec-Lang Builtin Catalog
status: active
audience: reviewer
owns_tokens:
- appendix_spec_lang_builtin_catalog
requires_tokens:
- spec-lang
commands:
- run: ./scripts/runner_adapter.sh docs-generate-check
  purpose: Verify generated builtin catalog remains synchronized.
examples:
- id: EX-APP-BUILTIN-001
  runnable: false
  opt_out_reason: Generated reference page intentionally contains no runnable fenced examples.
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

Machine-generated spec-lang builtin catalog and parity summary.

## Purpose

Provide generated catalog coverage for the spec-lang builtin surface and parity.

## Inputs

- python and php builtin symbol tables

## Outputs

- symbol/arity/category matrix with parity flags

## Failure Modes

- stale generated block after builtin changes
- parity scan drift
- missing generated markers

<!-- GENERATED:START spec_lang_builtin_catalog -->

## Generated Spec-Lang Builtin Catalog

- builtin_count: 130
- parity_count: 104
- all_parity: false

| symbol | arity | category | python | php | parity |
|---|---|---|---|---|---|
| `abs` | 1 | `numeric` | true | true | true |
| `add` | 2 | `numeric` | true | true | true |
| `all` | 1 | `collection` | true | true | true |
| `always` | 2 | `core` | true | true | true |
| `and` | 2 | `comparison_logic` | true | true | true |
| `any` | 1 | `collection` | true | true | true |
| `append` | 2 | `collection` | true | true | true |
| `assoc` | 3 | `object` | true | true | true |
| `between` | 3 | `comparison_logic` | true | false | false |
| `ceil` | 1 | `numeric` | true | false | false |
| `clamp` | 3 | `numeric` | true | true | true |
| `coalesce` | 2 | `core` | true | true | true |
| `compare` | 2 | `comparison_logic` | true | true | true |
| `compose` | 3 | `core` | true | true | true |
| `concat` | 2 | `collection` | true | true | true |
| `contains` | 2 | `string_regex` | true | true | true |
| `contains_all` | 2 | `collection` | true | true | true |
| `contains_any` | 2 | `collection` | true | false | false |
| `count` | 1 | `collection` | true | false | false |
| `dec` | 1 | `numeric` | true | true | true |
| `default_to` | 2 | `core` | true | true | true |
| `difference` | 2 | `set` | true | true | true |
| `dissoc` | 2 | `object` | true | true | true |
| `distinct` | 1 | `collection` | true | true | true |
| `div` | 2 | `numeric` | true | true | true |
| `drop` | 2 | `collection` | true | false | false |
| `ends_with` | 2 | `string_regex` | true | true | true |
| `entries` | 1 | `object` | true | true | true |
| `eq` | 2 | `comparison_logic` | true | true | true |
| `equals` | 2 | `comparison_logic` | true | true | true |
| `filter` | 2 | `collection` | true | true | true |
| `find` | 2 | `collection` | true | true | true |
| `first` | 1 | `collection` | true | true | true |
| `flatten` | 1 | `collection` | true | true | true |
| `floor` | 1 | `numeric` | true | true | true |
| `get` | 2 | `object` | true | true | true |
| `get_in` | 2 | `object` | true | true | true |
| `get_or` | 3 | `object` | true | true | true |
| `group_by` | 2 | `collection` | true | true | true |
| `gt` | 2 | `comparison_logic` | true | true | true |
| `gte` | 2 | `comparison_logic` | true | false | false |
| `has_key` | 2 | `object` | true | false | false |
| `has_path` | 2 | `object` | true | true | true |
| `identity` | 1 | `core` | true | true | true |
| `in` | 2 | `collection` | true | true | true |
| `inc` | 1 | `numeric` | true | true | true |
| `includes` | 2 | `collection` | true | true | true |
| `intersection` | 2 | `set` | true | true | true |
| `is_array` | 1 | `type_predicate` | true | true | true |
| `is_bool` | 1 | `type_predicate` | true | true | true |
| `is_boolean` | 1 | `type_predicate` | true | true | true |
| `is_dict` | 1 | `type_predicate` | true | false | false |
| `is_empty` | 1 | `collection` | true | true | true |
| `is_integer` | 1 | `type_predicate` | true | true | true |
| `is_list` | 1 | `type_predicate` | true | true | true |
| `is_null` | 1 | `type_predicate` | true | true | true |
| `is_number` | 1 | `type_predicate` | true | true | true |
| `is_object` | 1 | `type_predicate` | true | true | true |
| `is_string` | 1 | `type_predicate` | true | true | true |
| `is_subset` | 2 | `set` | true | true | true |
| `is_superset` | 2 | `set` | true | false | false |
| `join` | 2 | `string_regex` | true | true | true |
| `json_parse` | 1 | `core` | true | true | true |
| `json_stringify` | 1 | `core` | true | true | true |
| `json_type` | 2 | `type_predicate` | true | true | true |
| `keys` | 1 | `object` | true | true | true |
| `keys_exact` | 2 | `object` | true | true | true |
| `keys_exclude` | 2 | `object` | true | false | false |
| `keys_include` | 2 | `object` | true | true | true |
| `last` | 1 | `collection` | true | true | true |
| `len` | 1 | `collection` | true | false | false |
| `lower` | 1 | `string_regex` | true | true | true |
| `lt` | 2 | `comparison_logic` | true | true | true |
| `lte` | 2 | `comparison_logic` | true | true | true |
| `map` | 2 | `collection` | true | true | true |
| `matches` | 2 | `string_regex` | true | false | false |
| `matches_all` | 2 | `string_regex` | true | true | true |
| `max` | 1 | `numeric` | true | false | false |
| `merge` | 2 | `object` | true | true | true |
| `merge_deep` | 2 | `object` | true | true | true |
| `min` | 1 | `numeric` | true | false | false |
| `mod` | 2 | `numeric` | true | true | true |
| `mul` | 2 | `numeric` | true | true | true |
| `negate` | 1 | `numeric` | true | true | true |
| `neq` | 2 | `comparison_logic` | true | true | true |
| `none` | 1 | `collection` | true | false | false |
| `not` | 1 | `comparison_logic` | true | true | true |
| `nth` | 2 | `collection` | true | true | true |
| `omit` | 2 | `object` | true | false | false |
| `or` | 2 | `comparison_logic` | true | true | true |
| `pad_left` | 3 | `string_regex` | true | true | true |
| `pad_right` | 3 | `string_regex` | true | false | false |
| `partition` | 2 | `collection` | true | true | true |
| `pick` | 2 | `object` | true | false | false |
| `pipe` | 3 | `core` | true | false | false |
| `pluck` | 2 | `collection` | true | true | true |
| `pow` | 2 | `numeric` | true | false | false |
| `prepend` | 2 | `collection` | true | true | true |
| `prop_eq` | 3 | `object` | true | true | true |
| `range` | 2 | `collection` | true | true | true |
| `reduce` | 3 | `collection` | true | true | true |
| `regex_match` | 2 | `string_regex` | true | false | false |
| `reject` | 2 | `collection` | true | true | true |
| `repeat` | 2 | `collection` | true | true | true |
| `replace` | 3 | `string_regex` | true | true | true |
| `rest` | 1 | `collection` | true | true | true |
| `reverse` | 1 | `collection` | true | true | true |
| `round` | 1 | `numeric` | true | true | true |
| `schema_errors` | 2 | `core` | true | false | false |
| `schema_match` | 2 | `core` | true | false | false |
| `set_equals` | 2 | `set` | true | true | true |
| `slice` | 3 | `collection` | true | true | true |
| `sort` | 1 | `collection` | true | true | true |
| `sort_by` | 2 | `collection` | true | true | true |
| `split` | 2 | `string_regex` | true | true | true |
| `starts_with` | 2 | `string_regex` | true | true | true |
| `sub` | 2 | `numeric` | true | true | true |
| `subject` | 0 | `core` | true | true | true |
| `sum` | 1 | `numeric` | true | true | true |
| `symmetric_difference` | 2 | `set` | true | false | false |
| `take` | 2 | `collection` | true | true | true |
| `trim` | 1 | `string_regex` | true | true | true |
| `union` | 2 | `set` | true | true | true |
| `uniq_by` | 2 | `collection` | true | false | false |
| `upper` | 1 | `string_regex` | true | false | false |
| `values` | 1 | `object` | true | true | true |
| `where` | 2 | `object` | true | true | true |
| `xor` | 2 | `comparison_logic` | true | true | true |
| `zip` | 2 | `collection` | true | true | true |
| `zip_with` | 3 | `collection` | true | true | true |
<!-- GENERATED:END spec_lang_builtin_catalog -->
