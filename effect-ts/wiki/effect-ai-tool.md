---
title: Tool (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Tool (unstable)

Defines and manages tools that language models can call. Supports user-defined, provider-defined, and dynamic tools with parameter/success/failure `Schema`s, per-tool approval policies, failure modes, and handler context. Tools feed into `Toolkit` and `LanguageModel` tool-calling.

## Key Exports
- `Tool` — interface for a user-defined tool with parameters/success/failure schemas
- `ProviderDefined` — provider-hosted tool (e.g. OpenAI web search) with provider-side execution
- `Dynamic` — dynamically-created tool
- `Any`, `AnyStructured`, `AnyProviderDefined` — type aliases
- `make` — constructs a user-defined `Tool` from name and schemas
- `providerDefined` — constructs a `ProviderDefined` tool
- `dynamic` — constructs a `Dynamic` tool
- `FailureMode` — `"error" | "return"` strategy for handler failures
- `NeedsApproval` / `NeedsApprovalFunction` / `NeedsApprovalContext` — approval policy types
- `HandlersFor<Tools>` — inferred context tag for handlers
- `TypeId`, `ProviderDefinedTypeId`, `DynamicTypeId` — brand IDs

## Source
- `raw/effect-smol/packages/effect/src/unstable/ai/Tool.ts`

## Related
- [[effect-ts-v4]]
- [[effect-ai]]
- [[effect-ai-toolkit]]
- [[effect-ai-language-model]]
