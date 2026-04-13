---
title: AnthropicLanguageModel (@effect/ai-anthropic)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# AnthropicLanguageModel (@effect/ai-anthropic)

Implements the core `LanguageModel` service for Anthropic Claude models. Converts Effect AI prompts into Messages API payloads (handling system messages, cache control, extended thinking, tool calls, and structured output), then streams or batches responses back through `AnthropicClient`. Also declares Claude-specific provider options on `Prompt` message parts via module augmentation.

## Key Exports
- `Model` — branded type derived from `Generated.Model` (Claude model IDs)
- `Config` — `Context.Service` for per-request Anthropic params (`max_tokens`, `temperature`, `thinking`, `disableParallelToolCalls`, `strictJsonSchema`, `output_config.effort`, etc.)
- `model` — builds an `AiModel.Model<"anthropic", LanguageModel, AnthropicClient>` from a model id and optional config
- `make` — effectful constructor producing a `LanguageModel.Service` with `generateText` and `streamText` wired to `client.createMessage(Stream)`
- `layer` — `Layer<LanguageModel, never, AnthropicClient>`
- `withConfigOverride` — dual helper that overlays a `Config` override onto an Effect
- `AnthropicUserDefinedTool`, `AnthropicProviderDefinedTool` — supported tool variants

## Source
- `raw/effect-smol/packages/ai/anthropic/src/AnthropicLanguageModel.ts`

## Related
- [[effect-pkg-ai]]
- [[effect-pkg-ai-anthropic-client]]
- [[effect-pkg-ai-anthropic-tool]]
- [[effect-ai]]
