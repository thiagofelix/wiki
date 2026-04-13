---
title: Schema
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Schema

`Schema` is Effect's TypeScript-first library for defining data shapes, validating unknown input, and transforming values between formats. Every schema carries a decoded `Type` (the value you work with) and an `Encoded` representation (the serialized form), making most schemas bidirectional `Codec`s. It is the hub module in the schema family: other `Schema*` modules provide the AST, getters, issues, parser, transformations, representation, and utilities used by this one.

## Mental Model
- Decoding turns unknown input into typed values; encoding goes the other way.
- Checks/filters (e.g. `isMinLength`, `isGreaterThan`) attach runtime constraints via `.check(...)`.
- Transformations (pairs of decode/encode `Getter`s) connect two schemas via `decodeTo` / `encodeTo`.
- Annotations attach metadata (title, description, custom keys) via `.annotate(...)`.

## Key Exports
- `Struct`, `Record`, `Tuple`, `TupleWithRest`, `ArraySchema`, `NonEmptyArray` — composite shapes
- `Union`, `TaggedUnion`, `Literal`, `Literals` — alternatives and constants
- `String`, `Number`, `Boolean`, `BigInt`, `Symbol`, `Null`, `Undefined`, `Unknown` — primitives
- `optional`, `optionalKey`, `mutableKey`, `withConstructorDefault`, `withDecodingDefault` — field modifiers
- `decodeUnknownSync`, `decodeUnknownEffect`, `decodeUnknownExit`, `decodeUnknownOption` — validators
- `encodeUnknownSync`, `encodeUnknownEffect` — encoders
- `is`, `asserts` — type guards and assertions
- `decodeTo`, `encodeTo`, `refine`, `brand`, `suspend` — composition and recursion
- `Class`, `TaggedClass`, `ErrorClass`, `TaggedErrorClass` — class-backed schemas
- `toJsonSchemaDocument`, `toArbitrary`, `toEquivalence` — tooling derivation
- `Bottom`, `Top`, `Schema`, `Codec`, `Decoder`, `Encoder` — type-level views
- `isMinLength`, `isGreaterThan`, `isPattern`, `isUUID` — built-in filters

## Gotchas
- `Schema.optional` produces `T | undefined`; use `optionalKey` for exact-optional properties.
- `decodeTo` is curried: `from.pipe(Schema.decodeTo(to, ...))`.
- Filters do not change TypeScript types — use `refine` or `brand` to narrow.
- Recursive schemas require `suspend` to avoid infinite loops.

## Source
- `raw/effect-smol/packages/effect/src/Schema.ts`
- `raw/effect-smol/packages/effect/SCHEMA.md`

## Related
- [[effect-ts-v4]]
- [[effect-schema-ast]]
- [[effect-schema-parser]]
- [[effect-schema-transformation]]
- [[effect-schema-getter]]
- [[effect-schema-issue]]
- [[effect-json-schema]]
