---
title: SchemaTransformation
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# SchemaTransformation

`SchemaTransformation` defines bidirectional transformations used by `Schema.decodeTo`, `Schema.encodeTo`, `Schema.decode`, `Schema.encode`, and `Schema.link`. A `Transformation` pairs a decode `Getter` with an encode `Getter` so values round-trip between a decoded type `T` and an encoded type `E`. A `Middleware` is the effect-level equivalent: it wraps the entire parsing `Effect` pipeline rather than individual values, enabling retries, fallbacks, and side effects.

## Mental Model
- `flip()` swaps decode/encode; `compose()` chains transformations left-to-right.
- `passthrough` is the identity transformation; string helpers like `trim` and `toLowerCase` are lossy on encode.
- Use `Transformation` for value-level rewrites and `Middleware` when you need the surrounding `Effect`.

## Key Exports
- `Transformation` — bidirectional class with `flip`, `compose`
- `Middleware` — effect-pipeline-level transformation
- `transform`, `transformOrFail`, `transformOptional` — primary constructors
- `make` — build a `Transformation` from existing getters
- `passthrough`, `passthroughSupertype`, `passthroughSubtype` — identity transforms
- `isTransformation` — type guard
- `trim`, `toLowerCase`, `toUpperCase`, `capitalize`, `uncapitalize`, `snakeToCamel`, `splitKeyValue` — string transforms
- `numberFromString`, `bigintFromString`, `dateFromString`, `urlFromString` — parsing transforms
- `durationFromNanos`, `durationFromMillis` — duration transforms
- `optionFromNullOr`, `optionFromOptionalKey`, `optionFromOptional` — Option wrappers
- `uint8ArrayFromBase64String`, `stringFromBase64String`, `stringFromUriComponent` — encoding transforms
- `fromJsonString`, `fromFormData`, `fromURLSearchParams` — serialization transforms

## Source
- `raw/effect-smol/packages/effect/src/SchemaTransformation.ts`

## Related
- [[effect-ts-v4]]
- [[effect-schema]]
- [[effect-schema-getter]]
- [[effect-schema-issue]]
