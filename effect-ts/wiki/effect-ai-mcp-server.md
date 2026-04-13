---
title: McpServer (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# McpServer (unstable)

Runtime for exposing tools, prompts, resources, and resource templates over MCP. Wraps the `unstable/rpc` server with MCP schemas and provides layers for running over stdio or streaming HTTP, as well as registration helpers for typed tools built on `effect/unstable/ai/Tool` + `Toolkit`.

## Key Exports
- `McpServer` — `Context.Service` holding tool/prompt/resource registries, RPC notifications, and dispatchers (`addTool`, `callTool`, `addResource`, `addResourceTemplate`, `addPrompt`, `getPromptResult`, `completion`)
- `layer` — constructs a `McpServer` layer over a supplied RPC server
- `layerStdio` — runs the server over stdio with `Stdio` services
- `layerHttp` — mounts the server into an `HttpRouter` using streaming RPC
- `toolkit` — registers a `Toolkit`'s tools with the server
- `registerTool` / `registerPrompt` / `registerResource` / `registerResourceTemplate` — explicit registration helpers
- `prompt` / `resource` / `resourceTemplate` — constructors for MCP entries
- Integrates `Elicit` for interactive client elicitation

## Source
- `raw/effect-smol/packages/effect/src/unstable/ai/McpServer.ts`

## Related
- [[effect-ts-v4]]
- [[effect-ai]]
- [[effect-ai-mcp-schema]]
- [[effect-ai-toolkit]]
