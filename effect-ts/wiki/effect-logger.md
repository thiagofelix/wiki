---
title: Logger
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Logger

Structured logging system integrated with the Effect runtime's fiber context, spans, and annotations. Loggers are composable values that can emit to the console (JSON, LogFmt, pretty), files, or custom sinks, and can be batched or transformed. Provide a logger via `Logger.layer(...)` to install it at runtime.

## Key Exports
- `Logger<Message, Output>` — interface with a `log(options)` method
- `Options` — per-call context: message, logLevel, cause, fiber, date
- `make` — build a custom logger from a function
- `isLogger` — type guard
- `consoleJson` / `consolePretty` / `consoleLogFmt` — stock console loggers
- `formatJson` / `formatPretty` / `formatLogFmt` — format-only loggers
- `layer` — install one or more loggers as the active set
- `add` / `replace` / `remove` — layer transformers
- `batched` — wrap a logger to buffer messages over a duration window
- `file` — write formatted log lines to a file with batching
- `map` / `mapInput` — transform output or input message type

## Source
- `raw/effect-smol/packages/effect/src/Logger.ts`

## Related
- [[effect-ts-v4]]
- [[effect-log-level]]
- [[effect-layer]]
