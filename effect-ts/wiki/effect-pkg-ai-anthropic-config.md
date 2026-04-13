---
title: AnthropicConfig (@effect/ai-anthropic)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# AnthropicConfig (@effect/ai-anthropic)

Request-scoped configuration service for the Anthropic client. Currently holds a `transformClient` hook that allows composing middleware (e.g. retries, logging) around the shared `HttpClient` on a per-Effect basis without rebuilding the client layer.

## Key Exports
- `AnthropicConfig` — `Context.Service` at `@effect/ai-anthropic/AnthropicConfig` with `Service` shape `{ transformClient? }`
- `AnthropicConfig.getOrUndefined` — reads the service from the current context without failing when absent
- `withClientTransform` — dual helper that provides an `AnthropicConfig` with the given `HttpClient => HttpClient` to the wrapped Effect

## Source
- `raw/effect-smol/packages/ai/anthropic/src/AnthropicConfig.ts`

## Related
- [[effect-pkg-ai]]
- [[effect-pkg-ai-anthropic-client]]
