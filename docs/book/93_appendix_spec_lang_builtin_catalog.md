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
- parity_count: 0
- all_parity: false

| symbol | arity | category | python | php | parity |
|---|---|---|---|---|---|
| `std.collection.all` | 1 | `collection` | true | false | false |
| `std.collection.any` | 1 | `collection` | true | false | false |
| `std.collection.append` | 2 | `collection` | true | false | false |
| `std.collection.concat` | 2 | `collection` | true | false | false |
| `std.collection.contains_all` | 2 | `collection` | true | false | false |
| `std.collection.contains_any` | 2 | `collection` | true | false | false |
| `std.collection.count` | 1 | `collection` | true | false | false |
| `std.collection.distinct` | 1 | `collection` | true | false | false |
| `std.collection.drop` | 2 | `collection` | true | false | false |
| `std.collection.filter` | 2 | `collection` | true | false | false |
| `std.collection.find` | 2 | `collection` | true | false | false |
| `std.collection.first` | 1 | `collection` | true | false | false |
| `std.collection.flatten` | 1 | `collection` | true | false | false |
| `std.collection.group_by` | 2 | `collection` | true | false | false |
| `std.collection.in` | 2 | `collection` | true | false | false |
| `std.collection.includes` | 2 | `collection` | true | false | false |
| `std.collection.is_empty` | 1 | `collection` | true | false | false |
| `std.collection.last` | 1 | `collection` | true | false | false |
| `std.collection.len` | 1 | `collection` | true | false | false |
| `std.collection.map` | 2 | `collection` | true | false | false |
| `std.collection.none` | 1 | `collection` | true | false | false |
| `std.collection.nth` | 2 | `collection` | true | false | false |
| `std.collection.partition` | 2 | `collection` | true | false | false |
| `std.collection.prepend` | 2 | `collection` | true | false | false |
| `std.collection.reduce` | 3 | `collection` | true | false | false |
| `std.collection.reject` | 2 | `collection` | true | false | false |
| `std.collection.repeat` | 2 | `collection` | true | false | false |
| `std.collection.rest` | 1 | `collection` | true | false | false |
| `std.collection.reverse` | 1 | `collection` | true | false | false |
| `std.collection.slice` | 3 | `collection` | true | false | false |
| `std.collection.sort` | 1 | `collection` | true | false | false |
| `std.collection.sort_by` | 2 | `collection` | true | false | false |
| `std.collection.take` | 2 | `collection` | true | false | false |
| `std.collection.uniq_by` | 2 | `collection` | true | false | false |
| `std.collection.zip` | 2 | `collection` | true | false | false |
| `std.collection.zip_with` | 3 | `collection` | true | false | false |
| `std.core.subject` | 0 | `core` | true | false | false |
| `std.fn.always` | 2 | `fn` | true | false | false |
| `std.fn.compose` | 3 | `fn` | true | false | false |
| `std.fn.identity` | 1 | `fn` | true | false | false |
| `std.fn.pipe` | 3 | `fn` | true | false | false |
| `std.json.parse` | 1 | `json` | true | false | false |
| `std.json.stringify` | 1 | `json` | true | false | false |
| `std.logic.and` | 2 | `logic` | true | false | false |
| `std.logic.between` | 3 | `logic` | true | false | false |
| `std.logic.compare` | 2 | `logic` | true | false | false |
| `std.logic.eq` | 2 | `logic` | true | false | false |
| `std.logic.equals` | 2 | `logic` | true | false | false |
| `std.logic.gt` | 2 | `logic` | true | false | false |
| `std.logic.gte` | 2 | `logic` | true | false | false |
| `std.logic.lt` | 2 | `logic` | true | false | false |
| `std.logic.lte` | 2 | `logic` | true | false | false |
| `std.logic.neq` | 2 | `logic` | true | false | false |
| `std.logic.not` | 1 | `logic` | true | false | false |
| `std.logic.or` | 2 | `logic` | true | false | false |
| `std.logic.xor` | 2 | `logic` | true | false | false |
| `std.math.abs` | 1 | `math` | true | false | false |
| `std.math.add` | 2 | `math` | true | false | false |
| `std.math.ceil` | 1 | `math` | true | false | false |
| `std.math.clamp` | 3 | `math` | true | false | false |
| `std.math.dec` | 1 | `math` | true | false | false |
| `std.math.div` | 2 | `math` | true | false | false |
| `std.math.floor` | 1 | `math` | true | false | false |
| `std.math.inc` | 1 | `math` | true | false | false |
| `std.math.max` | 1 | `math` | true | false | false |
| `std.math.min` | 1 | `math` | true | false | false |
| `std.math.mod` | 2 | `math` | true | false | false |
| `std.math.mul` | 2 | `math` | true | false | false |
| `std.math.negate` | 1 | `math` | true | false | false |
| `std.math.pow` | 2 | `math` | true | false | false |
| `std.math.range` | 2 | `math` | true | false | false |
| `std.math.round` | 1 | `math` | true | false | false |
| `std.math.sub` | 2 | `math` | true | false | false |
| `std.math.sum` | 1 | `math` | true | false | false |
| `std.null.coalesce` | 2 | `null` | true | false | false |
| `std.null.default_to` | 2 | `null` | true | false | false |
| `std.object.assoc` | 3 | `object` | true | false | false |
| `std.object.dissoc` | 2 | `object` | true | false | false |
| `std.object.entries` | 1 | `object` | true | false | false |
| `std.object.get` | 2 | `object` | true | false | false |
| `std.object.get_in` | 2 | `object` | true | false | false |
| `std.object.get_or` | 3 | `object` | true | false | false |
| `std.object.has_key` | 2 | `object` | true | false | false |
| `std.object.has_path` | 2 | `object` | true | false | false |
| `std.object.keys` | 1 | `object` | true | false | false |
| `std.object.keys_exact` | 2 | `object` | true | false | false |
| `std.object.keys_exclude` | 2 | `object` | true | false | false |
| `std.object.keys_include` | 2 | `object` | true | false | false |
| `std.object.merge` | 2 | `object` | true | false | false |
| `std.object.merge_deep` | 2 | `object` | true | false | false |
| `std.object.omit` | 2 | `object` | true | false | false |
| `std.object.pick` | 2 | `object` | true | false | false |
| `std.object.pluck` | 2 | `object` | true | false | false |
| `std.object.prop_eq` | 3 | `object` | true | false | false |
| `std.object.values` | 1 | `object` | true | false | false |
| `std.object.where` | 2 | `object` | true | false | false |
| `std.schema.errors` | 2 | `schema` | true | false | false |
| `std.schema.match` | 2 | `schema` | true | false | false |
| `std.set.difference` | 2 | `set` | true | false | false |
| `std.set.intersection` | 2 | `set` | true | false | false |
| `std.set.is_subset` | 2 | `set` | true | false | false |
| `std.set.is_superset` | 2 | `set` | true | false | false |
| `std.set.set_equals` | 2 | `set` | true | false | false |
| `std.set.symmetric_difference` | 2 | `set` | true | false | false |
| `std.set.union` | 2 | `set` | true | false | false |
| `std.string.contains` | 2 | `string` | true | false | false |
| `std.string.ends_with` | 2 | `string` | true | false | false |
| `std.string.join` | 2 | `string` | true | false | false |
| `std.string.lower` | 1 | `string` | true | false | false |
| `std.string.matches` | 2 | `string` | true | false | false |
| `std.string.matches_all` | 2 | `string` | true | false | false |
| `std.string.pad_left` | 3 | `string` | true | false | false |
| `std.string.pad_right` | 3 | `string` | true | false | false |
| `std.string.regex_match` | 2 | `string` | true | false | false |
| `std.string.replace` | 3 | `string` | true | false | false |
| `std.string.split` | 2 | `string` | true | false | false |
| `std.string.starts_with` | 2 | `string` | true | false | false |
| `std.string.trim` | 1 | `string` | true | false | false |
| `std.string.upper` | 1 | `string` | true | false | false |
| `std.type.is_array` | 1 | `type` | true | false | false |
| `std.type.is_bool` | 1 | `type` | true | false | false |
| `std.type.is_boolean` | 1 | `type` | true | false | false |
| `std.type.is_dict` | 1 | `type` | true | false | false |
| `std.type.is_integer` | 1 | `type` | true | false | false |
| `std.type.is_list` | 1 | `type` | true | false | false |
| `std.type.is_null` | 1 | `type` | true | false | false |
| `std.type.is_number` | 1 | `type` | true | false | false |
| `std.type.is_object` | 1 | `type` | true | false | false |
| `std.type.is_string` | 1 | `type` | true | false | false |
| `std.type.json_type` | 2 | `type` | true | false | false |
<!-- GENERATED:END spec_lang_builtin_catalog -->
