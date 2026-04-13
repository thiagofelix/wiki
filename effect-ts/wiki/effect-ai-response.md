---
title: Response (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Response (unstable)

Data structures representing LLM outputs, covering both full responses and streaming deltas. Defines a tagged union of parts (text, reasoning, tool calls, files, sources, metadata, finish, error) along with start/delta/end streaming variants and helpers to construct them.

## Key Exports
- `AnyPart` / `AnyPartEncoded` — union of all response parts
- `AllParts<Tools>` — tool-aware part union
- `StreamPart<Tools>` — streaming-friendly part union
- `TextPart`, `TextStartPart`, `TextDeltaPart`, `TextEndPart` — text parts
- `ReasoningPart`, `ReasoningStartPart`, `ReasoningDeltaPart`, `ReasoningEndPart` — reasoning parts
- `ToolCallPart`, `ToolResultPart`, `ToolApprovalRequestPart` — tool-call parts
- `ToolParamsStartPart`, `ToolParamsDeltaPart`, `ToolParamsEndPart` — streaming tool-parameter parts
- `FilePart`, `DocumentSourcePart`, `UrlSourcePart` — multimodal/source parts
- `ResponseMetadataPart`, `FinishPart`, `ErrorPart` — terminal/metadata parts
- `makePart` — constructor for any part by tag
- `isPart` — type guard
- `HttpRequestDetails`, `HttpResponseDetails` — structured HTTP context shared with `AiError`

## Source
- `raw/effect-smol/packages/effect/src/unstable/ai/Response.ts`

## Related
- [[effect-ts-v4]]
- [[effect-ai]]
- [[effect-ai-prompt]]
- [[effect-ai-language-model]]
