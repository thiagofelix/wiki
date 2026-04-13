---
title: effect/unstable/ai (hub)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# effect/unstable/ai (hub)

Provider-agnostic AI subsystem for Effect v4. Defines a unified `LanguageModel` service (text, structured object, streaming), an `EmbeddingModel` service with batching, a stateful `Chat` built on top, and pluggable `Model`/`Tool`/`Toolkit` abstractions so code can target any LLM provider interchangeably. Ships structured-output codec transformers for Anthropic and OpenAI, full Prompt/Response data structures, a tagged `AiError` hierarchy, tokenizer and ID-generator services, OpenTelemetry GenAI telemetry helpers, and an MCP (Model Context Protocol) server implementation over the `unstable/rpc` stack.

## Modules
- [[effect-ai-ai-error]] — tagged error model with retryability and provider context
- [[effect-ai-anthropic-structured-output]] — codec transformer for Anthropic structured output
- [[effect-ai-chat]] — stateful chat service over `LanguageModel`
- [[effect-ai-embedding-model]] — batched embedding service with `RequestResolver`
- [[effect-ai-id-generator]] — pluggable ID generator service
- [[effect-ai-language-model]] — core `generateText`/`generateObject`/`streamText` service
- [[effect-ai-mcp-schema]] — Model Context Protocol wire schemas
- [[effect-ai-mcp-server]] — MCP server runtime over RPC (stdio/http)
- [[effect-ai-model]] — provider+model pairing as a `Layer`
- [[effect-ai-open-ai-structured-output]] — codec transformer for OpenAI structured output
- [[effect-ai-prompt]] — message/part data structures for prompts
- [[effect-ai-response]] — response part union (incl. streaming deltas)
- [[effect-ai-response-id-tracker]] — previous-response-id tracking for stateful APIs
- [[effect-ai-telemetry]] — OpenTelemetry GenAI span attributes
- [[effect-ai-tokenizer]] — tokenization and prompt truncation service
- [[effect-ai-tool]] — user/provider-defined/dynamic tool definitions
- [[effect-ai-toolkit]] — bundled tools with handler contexts/layers
- [[effect-ai-index]] — barrel re-export of the subsystem
- [[effect-ai-internal]] — internal default codec transformer

## Related
- [[effect-ts-v4]]
- [[source-effect-smol-repo]]
