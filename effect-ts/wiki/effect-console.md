---
title: Console
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Console

Functional interface for console operations inside Effect. The `Console` service wraps the standard `console` API (log, error, warn, debug, assert, group, time, table, dir, etc.) as typed Effects, making output composable, testable, and swappable per environment. Reach for it instead of raw `console.log` whenever you want logs to be part of an Effect program so they can be captured, suppressed, or redirected in tests.

## Key Exports
- `Console` — service interface mirroring the standard browser/Node console
- `log`, `error`, `warn`, `info`, `debug` — basic logging effects
- `assert` — conditional logging
- `group`, `groupCollapsed`, `groupEnd`, `withGroup` — organized output
- `time`, `timeEnd`, `timeLog`, `withTime` — performance timing
- `table`, `dir`, `dirxml` — structured data display
- `clear`, `count`, `countReset`, `trace` — misc
- `consoleWith` — access the current `Console` from the context
- `withConsole` — swap in a custom console implementation for a scoped computation

## Source
- `raw/effect-smol/packages/effect/src/Console.ts`

## Related
- [[effect-ts-v4]]
- [[effect-context]]
