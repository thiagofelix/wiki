---
title: Cron
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Cron

Typed cron schedule representation with timezone support. A `Cron` instance captures the allowed values for each time field (seconds, minutes, hours, days, months, weekdays) as `ReadonlySet<number>`, plus an optional `TimeZone`. The module parses cron expression strings, matches dates against a schedule, and computes the next firing time. Reach for it when implementing schedulers, recurring jobs, or time-based triggers — it pairs naturally with `Schedule`.

## Key Exports
- `Cron` — interface holding field sets, timezone, and the "first" fireable instant cache
- `make` — build a cron from `{ seconds?, minutes, hours, days, months, weekdays, tz? }`
- `parse` — parse a cron expression string, returning `Result<Cron, ParseError>`
- `parseUnsafe` — throwing variant of `parse`
- `match` — does a given `Date` match the schedule?
- `next` — compute the next matching instant after a given date
- `sequence` — iterate over successive firing times
- `Equivalence`, `Equal` instance — value equality between schedules
- `isCron` — runtime guard

## Source
- `raw/effect-smol/packages/effect/src/Cron.ts`

## Related
- [[effect-ts-v4]]
- [[effect-date-time]]
- [[effect-duration]]
