---
title: Data
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Data

Base classes and factory functions for immutable value types with structural equality and discriminated-union support. `Data.Class` produces a pipeable immutable record type; `Data.TaggedClass` auto-adds a `_tag` literal; `Data.TaggedEnum` + `Data.taggedEnum()` generate a tagged union with per-variant constructors, `$is` guards, and `$match`. `Data.Error` / `Data.TaggedError` extend `Cause.YieldableError` so instances can be yielded inside `Effect.gen` to fail the effect. Reach for it for all domain models and error types in Effect apps.

## Key Exports
- `Class<Fields>` — base for immutable pipeable value classes
- `TaggedClass<Tag, Fields>` — `Class` with an auto-added `_tag`
- `TaggedEnum<Variants>` — type for tagged unions from a record of variants
- `taggedEnum<T>()` — value-level factory returning constructors, `$is`, and `$match`
- `Error<Fields>` — yieldable error base class
- `TaggedError<Tag, Fields>` — tagged yieldable error, works with `Effect.catchTag`
- `struct`, `tuple`, `array` — structural equality constructors for ad-hoc data
- `case`, `tagged` — factories for constructing case classes without `new`

## Source
- `raw/effect-smol/packages/effect/src/Data.ts`

## Related
- [[effect-ts-v4]]
- [[effect-cause]]
