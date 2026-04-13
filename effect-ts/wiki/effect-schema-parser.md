---
title: SchemaParser
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# SchemaParser

`SchemaParser` is the runtime engine that drives decoding, encoding, validation, and constructor execution for Effect schemas. Given a `Schema`, it compiles the AST into a parsing function and exposes synchronous, effectful, `Exit`, `Option`, and `Promise` variants of `decodeUnknown*` and `encodeUnknown*`. It also implements `is` / `asserts` type guards and the `makeEffect` / `makeOption` / `makeUnsafe` constructors used by `Schema.make`.

## Mental Model
- The parser walks the AST recursively, applying checks and encoding links.
- `makeEffect` returns an `Effect<T, Issue>` — every other entry point is a wrapper.
- Missing keys, default values, and class declarations are handled via `recurDefaults`.
- Service-requiring schemas propagate `DecodingServices` / `EncodingServices` on the result.

## Key Exports
- `decodeUnknownEffect`, `decodeEffect` — effectful decoding
- `decodeUnknownSync`, `decodeSync` — synchronous decoding (throws on failure)
- `decodeUnknownExit`, `decodeExit`, `decodeUnknownOption`, `decodeOption`, `decodeUnknownPromise`, `decodePromise` — non-throwing variants
- `encodeUnknownEffect`, `encodeEffect`, `encodeUnknownSync`, `encodeUnknownExit`, `encodeUnknownOption`, `encodeUnknownPromise` — encoding counterparts
- `is`, `asserts` — type-guard and assertion compilers
- `makeEffect`, `makeOption`, `makeUnsafe` — constructor compilers for `Schema.make`
- `run` — internal AST-to-parser compiler (used by the above)

## Source
- `raw/effect-smol/packages/effect/src/SchemaParser.ts`

## Related
- [[effect-ts-v4]]
- [[effect-schema]]
- [[effect-schema-ast]]
- [[effect-schema-issue]]
