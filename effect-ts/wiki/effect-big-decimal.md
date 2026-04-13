---
title: BigDecimal
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# BigDecimal

Arbitrary-precision decimal arithmetic that avoids floating-point errors such as `0.1 + 0.2 !== 0.3`. Internally represents a number as a `bigint` value paired with a 64-bit scale (decimal point position), giving effectively arbitrary precision up to 2^63 decimal places. Reach for it in financial calculations, accounting systems, and anywhere exact decimal math matters.

## Key Exports
- `BigDecimal` — interface holding `{ value: bigint, scale: number }` plus `Equal`, `Pipeable`, `Inspectable`
- `isBigDecimal` — runtime guard
- `make`, `fromNumber`, `fromNumberUnsafe`, `fromString`, `fromBigInt` — constructors (prefer string or BigInt input over `number` to avoid float surprises)
- `sum`, `subtract`, `multiply`, `divide`, `unsafeDivide`, `remainder`, `negate` — arithmetic
- `equals`, `lessThan`, `greaterThan`, `Order`, `Equivalence` — comparison
- `normalize`, `scale`, `roundTerminal` — precision/scale management
- `format`, `toString` — rendering
- `DEFAULT_PRECISION` — precision used by division

## Source
- `raw/effect-smol/packages/effect/src/BigDecimal.ts`

## Related
- [[effect-ts-v4]]
- [[effect-big-int]]
