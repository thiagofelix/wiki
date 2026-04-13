---
title: Toolkit (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Toolkit (unstable)

Collection of `Tool`s bundled together with an attached set of handlers. A `Toolkit` can be constructed from individual tools and then converted to a `Context` or `Layer` of handlers; `LanguageModel.generateText`/`streamText` accept toolkits directly and preserve per-tool typing through the call site.

## Key Exports
- `Toolkit<Tools>` — interface holding `tools` and producing handler contexts/layers
- `WithHandler<Tools>` — toolkit paired with resolved handlers
- `HandlerContext<Tool>` — context passed to handler functions during execution
- `HandlersFrom<Tools>` — inferred handler record type
- `make` — constructs a toolkit from any number of `Tool`s
- `toHandlers` — converts a toolkit + handlers into a `Context` of handler tags
- `toLayer` — converts a toolkit + handlers into a `Layer` of handler tags
- `of` — identity helper for type-safe handler declarations
- Integrates `AiError` for handler failures
- `TypeId` — brand identifier

## Source
- `raw/effect-smol/packages/effect/src/unstable/ai/Toolkit.ts`

## Related
- [[effect-ts-v4]]
- [[effect-ai]]
- [[effect-ai-tool]]
- [[effect-ai-language-model]]
