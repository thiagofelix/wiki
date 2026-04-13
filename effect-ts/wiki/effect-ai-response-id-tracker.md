---
title: ResponseIdTracker (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# ResponseIdTracker (unstable)

Service that tracks which prompt messages were already delivered in a prior response, so subsequent turns can be sent using a `previousResponseId` (e.g. OpenAI Responses API) plus only the new tail of the conversation. This avoids re-sending full chat history when the provider supports server-side state.

## Key Exports
- `ResponseIdTracker` — `Context.Service` tag
- `Service` — `{ clearUnsafe, markParts, prepareUnsafe }`
- `PrepareResult` — `{ previousResponseId, prompt }` returned by `prepareUnsafe`
- `make` — constructs a `Service` backed by a `Map<object, string>`
- `prepareUnsafe(prompt)` — returns `Some<PrepareResult>` if the prompt extends a tracked response, else `None`
- `markParts(parts, responseId)` — associates prompt messages with the response id they belong to

## Source
- `raw/effect-smol/packages/effect/src/unstable/ai/ResponseIdTracker.ts`

## Related
- [[effect-ts-v4]]
- [[effect-ai]]
- [[effect-ai-language-model]]
- [[effect-ai-prompt]]
