---
title: Activity (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Activity (unstable)

Building block representing a single step inside a workflow. Activities memoize their success/failure in the workflow engine so that replay skips already-completed work. Each activity has a name (hashed for uniqueness), success/error schemas, retry policies, and runs under the current `WorkflowEngine` + `WorkflowInstance`.

## Key Exports
- `Activity` — yieldable step with schemas, annotations, and `execute`
- `make` — build an activity from a name and an effect
- `retry` — attach a retry schedule to an activity
- `annotate` / `annotateMerge` — attach context annotations
- `CurrentAttempt` — reference exposing the current retry attempt number
- `raiseErrorDefect` / `raiseErrorExit` — helpers for modeling failures

## Source
- `raw/effect-smol/packages/effect/src/unstable/workflow/Activity.ts`

## Related
- [[effect-workflow]]
- [[effect-workflow-workflow]]
- [[effect-workflow-workflow-engine]]
- [[effect-workflow-durable-deferred]]
