---
title: SchemaIssue
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# SchemaIssue

`SchemaIssue` defines the structured validation errors produced by `Schema.decode`, `Schema.encode`, and filters. An `Issue` is a recursive discriminated union describing what went wrong and where, with leaf nodes like `InvalidType`, `MissingKey`, `Forbidden` and composite nodes like `Filter`, `Pointer`, `Composite`, and `AnyOf` that wrap inner issues to add context. The module also provides formatters that turn an `Issue` tree into a human-readable string or a Standard Schema V1 failure.

## Mental Model
- Leaves carry the failure reason; composites add path/context around inner issues.
- `Pointer` adds a property-key path pinpointing where the error occurred.
- Every `Issue` has a `toString()` that uses the default formatter.
- `getActual` uniformly extracts the offending value wrapped in `Option`.

## Key Exports
- `Issue` — root discriminated union
- `Leaf` — union of terminal issue types
- `InvalidType`, `InvalidValue`, `MissingKey`, `UnexpectedKey`, `Forbidden`, `OneOf` — leaves
- `Filter`, `Encoding`, `Pointer`, `Composite`, `AnyOf` — composite nodes
- `isIssue` — type guard
- `getActual` — extract input value as `Option<unknown>`
- `makeFormatterDefault` — plain-string formatter factory
- `makeFormatterStandardSchemaV1` — Standard Schema V1 formatter factory
- `defaultLeafHook`, `defaultCheckHook` — hooks for custom formatting

## Source
- `raw/effect-smol/packages/effect/src/SchemaIssue.ts`

## Related
- [[effect-ts-v4]]
- [[effect-schema]]
- [[effect-schema-parser]]
- [[effect-schema-getter]]
