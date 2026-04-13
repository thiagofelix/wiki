---
title: McpSchema (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# McpSchema (unstable)

Schema definitions for the Model Context Protocol (MCP) JSON-RPC wire format. Defines request/response/notification shapes, capabilities, tools, prompts, resources, elicitation, and the RPC groups used by the MCP server/client, built on Effect `Schema` and the `unstable/rpc` stack.

## Key Exports
- `RequestId`, `ProgressToken`, `Cursor` — common identifiers
- `RequestMeta`, `ResultMeta`, `NotificationMeta` — `_meta` envelopes
- `ClientCapabilities`, `ServerCapabilities` — capability descriptors
- `Initialize`, `CallTool`, `GetPrompt`, `Complete`, `Elicit` — RPC definitions
- `Tool`, `Prompt`, `Resource`, `ResourceTemplate` — MCP content descriptors
- `TextContent`, `CallToolResult`, `GetPromptResult`, `CompleteResult`, `ReadResourceResult`, `ListToolsResult`, `ListPromptsResult`, `ListResourcesResult`, `ListResourceTemplatesResult`
- `ClientRpcs`, `ClientNotificationRpcs`, `ServerRequestRpcs`, `ServerNotificationRpcs` — `RpcGroup`s
- `McpServerClient`, `McpServerClientMiddleware` — RPC client/middleware tags
- `InternalError`, `InvalidParams`, `ElicitationDeclined` — error schemas
- `Param`, `isParam`, `EnabledWhen`, `optional`, `optionalWithDefault` — schema helpers

## Source
- `raw/effect-smol/packages/effect/src/unstable/ai/McpSchema.ts`

## Related
- [[effect-ts-v4]]
- [[effect-ai]]
- [[effect-ai-mcp-server]]
