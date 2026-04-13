---
title: Brand
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Brand

Nominal typing via phantom tags. A `Brand<Keys>` adds a compile-time tag to an existing type so that two values with the same underlying representation (e.g. `UserId` and `OrderId`, both `string`) cannot be accidentally interchanged. Brand constructors integrate with `Schema` checks so you get validation at the boundary and type safety throughout your domain model.

## Key Exports
- `Brand<Keys>` — base interface carrying the phantom key(s)
- `Brand.Unbranded` / `Brand.Branded` — type helpers to strip or apply a brand
- `Constructor<B>` — constructor interface with `(unbranded)`, `.option`, `.result`, `.is`
- `BrandError` — error returned when validation fails, wrapping a `SchemaIssue`
- `nominal` — create an unchecked brand constructor (identity at runtime)
- `refined` — create a validated brand constructor from a predicate or schema checks
- `all` — combine multiple brand constructors into one

## Source
- `raw/effect-smol/packages/effect/src/Brand.ts`

## Related
- [[effect-ts-v4]]
