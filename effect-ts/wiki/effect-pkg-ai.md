---
title: @effect/ai (packages/ai)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# @effect/ai (packages/ai)

Meta-package containing provider adapters that plug into the in-core `effect/unstable/ai` (see [[effect-ai]]) subsystem. Each sub-package ships a `Client`, a `LanguageModel` (and sometimes `EmbeddingModel`) implementation, a `Config` context service, a telemetry helper, an error metadata augmentation, and the auto-generated OpenAPI types. The core unstable AI package defines the abstractions (`LanguageModel`, `EmbeddingModel`, `Prompt`, `Response`, `Tool`, `AiError`); these packages adapt them to concrete providers.

## Sub-packages
- `@effect/ai-anthropic` — Anthropic Claude Messages API (beta endpoints, extended thinking, provider tools)
- `@effect/ai-openai` — OpenAI Responses API (plus embeddings, realtime websocket mode, provider tools)
- `@effect/ai-openai-compat` — Chat Completions shape for OpenAI-compatible providers (Ollama, Groq, vLLM, Together, etc.)
- `@effect/ai-openrouter` — OpenRouter Chat Completions API with reasoning detail and site attribution headers

## Anthropic modules
[[effect-pkg-ai-anthropic-client]], [[effect-pkg-ai-anthropic-config]], [[effect-pkg-ai-anthropic-error]], [[effect-pkg-ai-anthropic-language-model]], [[effect-pkg-ai-anthropic-telemetry]], [[effect-pkg-ai-anthropic-tool]], [[effect-pkg-ai-anthropic-generated]], [[effect-pkg-ai-anthropic-internal]]

## OpenAI modules
[[effect-pkg-ai-openai-client]], [[effect-pkg-ai-openai-config]], [[effect-pkg-ai-openai-embedding-model]], [[effect-pkg-ai-openai-error]], [[effect-pkg-ai-openai-language-model]], [[effect-pkg-ai-openai-telemetry]], [[effect-pkg-ai-openai-tool]], [[effect-pkg-ai-openai-generated]], [[effect-pkg-ai-openai-internal]]

## OpenAI Compat modules
[[effect-pkg-ai-openai-compat-client]], [[effect-pkg-ai-openai-compat-config]], [[effect-pkg-ai-openai-compat-embedding-model]], [[effect-pkg-ai-openai-compat-error]], [[effect-pkg-ai-openai-compat-language-model]], [[effect-pkg-ai-openai-compat-telemetry]], [[effect-pkg-ai-openai-compat-internal]]

## OpenRouter modules
[[effect-pkg-ai-openrouter-client]], [[effect-pkg-ai-openrouter-config]], [[effect-pkg-ai-openrouter-error]], [[effect-pkg-ai-openrouter-language-model]], [[effect-pkg-ai-openrouter-generated]], [[effect-pkg-ai-openrouter-internal]]

## Related
- [[effect-ts-v4]]
- [[effect-ai]] — the in-core `effect/unstable/ai/*` subsystem providing abstractions
