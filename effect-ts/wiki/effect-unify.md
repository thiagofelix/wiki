---
title: Unify
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Unify

Type-level infrastructure that collapses unions of Effect-like types into their canonical form. Uses three brand symbols (`typeSymbol`, `unifySymbol`, `ignoreSymbol`) which each yieldable type (Effect, Option, Result, Stream, Sink, etc.) plants on itself so the type system can merge `Effect<A> | Option<B>` into a single unified type.

## Key Exports
- `unifySymbol` — marker symbol for unifiable types
- `typeSymbol` — marker symbol for the underlying type payload
- `ignoreSymbol` — marker symbol for types excluded from unification
- `Unify<A>` — type-level operator performing unification
- Supporting type aliases `unifySymbol` / `typeSymbol` / `ignoreSymbol` (type forms)

## Source
- `raw/effect-smol/packages/effect/src/Unify.ts`

## Related
- [[effect-ts-v4]]
- Used by Effect, Stream, Sink, Option, Result variance interfaces
