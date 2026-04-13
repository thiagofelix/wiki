---
title: LanguageModel (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# LanguageModel (unstable)

Core service abstraction for large language models. Provides provider-agnostic `generateText`, `generateObject`, and `streamText` operations with rich typing around toolkits, structured output schemas, provider metadata, telemetry, and error handling. Concrete providers implement this service; consumer code programs against the interface.

## Key Exports
- `LanguageModel` — `Context.Service` tag for the LLM service
- `Service` — interface with `generateText`, `generateObject`, `streamText`
- `generateText` / `generateObject` / `streamText` — module-level helpers that pull the service from context
- `GenerateTextOptions` / `GenerateObjectOptions` — input option shapes
- `GenerateTextResponse` / `GenerateObjectResponse` — result shapes
- `ToolkitInput` / `ToolkitOption` / `ExtractTools` / `ExtractError` / `ExtractServices` — type helpers for toolkit inference
- `CodecTransformer` — pluggable codec→JSON-schema transformer (defaults from internal)
- `ProviderOptions` — per-call provider-specific options
- `make` — constructs a `Service` from a provider `ProviderLanguageModel`
- Integrates `IdGenerator`, `ResponseIdTracker`, `Telemetry` (`CurrentSpanTransformer`), and `AiError`

## Source
- `raw/effect-smol/packages/effect/src/unstable/ai/LanguageModel.ts`

## Related
- [[effect-ts-v4]]
- [[effect-ai]]
- [[effect-ai-chat]]
- [[effect-ai-toolkit]]
