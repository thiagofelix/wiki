---
title: SchemaGetter
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# SchemaGetter

`SchemaGetter` provides composable single-direction transformation primitives used by `Schema.decodeTo` and `Schema.decode`. A `Getter<T, E, R>` is a function `Option<E> -> Effect<Option<T>, Issue, R>` that transforms an optional encoded value into an optional decoded value, can fail with an `Issue`, and may require Effect services. Getters are option-aware so they can model missing struct keys and are composed left-to-right.

## Mental Model
- `passthrough` is the identity getter and is optimized away during composition.
- `transform` applies a pure function to present values, skipping `None` inputs.
- `transformOptional` gives full control over the `Option` on both sides.
- A transformation in `SchemaTransformation` is a pair of getters (decode + encode).

## Key Exports
- `Getter` — the core class with `.map`, `.compose`, `.run`
- `passthrough`, `passthroughSupertype`, `passthroughSubtype` — identity getters
- `transform`, `transformOrFail`, `transformOptional` — constructors
- `succeed`, `fail`, `forbidden`, `omit` — constant and failure getters
- `onNone`, `onSome`, `required`, `withDefault` — optionality handling
- `checkEffect` — effectful validation
- `String`, `Number`, `Boolean`, `BigInt`, `Date` — primitive coercions
- `trim`, `capitalize`, `toLowerCase`, `toUpperCase`, `split`, `splitKeyValue`, `joinKeyValue` — string transforms
- `parseJson`, `stringifyJson`, `encodeBase64`, `decodeBase64`, `encodeHex`, `decodeHex` — codec getters
- `decodeFormData`, `encodeFormData`, `decodeURLSearchParams`, `encodeURLSearchParams` — form codecs
- `dateTimeUtcFromInput`, `makeTreeRecord`, `collectBracketPathEntries` — specialized helpers

## Source
- `raw/effect-smol/packages/effect/src/SchemaGetter.ts`

## Related
- [[effect-ts-v4]]
- [[effect-schema]]
- [[effect-schema-transformation]]
- [[effect-schema-issue]]
