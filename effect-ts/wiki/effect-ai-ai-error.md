---
title: AiError (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# AiError (unstable)

Provider-agnostic error model for AI operations. `AiError` is a top-level wrapper carrying `module`, `method`, and a `reason` field containing a semantic, tagged error class. Each reason exposes an `isRetryable` getter (some provide a `retryAfter` Duration) enabling ergonomic retry/backoff logic across providers.

## Key Exports
- `AiError` — wrapper error class with `module`, `method`, `reason`
- `make` — constructs an `AiError` from `{ module, method, reason }`
- `NetworkError` — transport-level failure (retryable)
- `RateLimitError` — 429/provider throttle, carries optional `retryAfter`
- `QuotaExhaustedError` — billing/account limits
- `AuthenticationError` — invalid or expired credentials
- `ContentPolicyError` — input/output policy violation
- `InvalidRequestError` / `InvalidUserInputError` — malformed request / unsupported prompt
- `InternalProviderError` — 5xx provider failure
- `InvalidOutputError` / `StructuredOutputError` — output parse/validation failure
- `UnsupportedSchemaError` — codec transformer rejected a schema
- `ToolNotFoundError`, `ToolParameterValidationError`, `InvalidToolResultError`, `ToolResultEncodingError`, `ToolConfigurationError` — tool-call failures
- `UnknownError` — catch-all
- `HttpRequestDetails` / `HttpResponseDetails` — structured HTTP context embedded in errors

## Source
- `raw/effect-smol/packages/effect/src/unstable/ai/AiError.ts`

## Related
- [[effect-ts-v4]]
- [[effect-ai]]
- [[effect-ai-language-model]]
