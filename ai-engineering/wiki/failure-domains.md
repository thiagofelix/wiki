---
title: Failure Domains
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Failure Domains

Failure domains are the specific, categorizable ways that AI coding agents break during autonomous operation. The core [[ralph-loops|Ralph loop]] discipline is to watch for these failures, categorize them, and engineer them away permanently — "I get to feel the failure domains. When I see them, I categorize them of how those types of failures happen. And then I engineer them away."

## The Philosophy

From [[source-ghuntley-collected|Geoffrey Huntley]]: "If you don't do the engineering, you're just going to get slop." Failure domains are not bugs to fix case-by-case — they are systemic patterns to eliminate through engineering. The act of watching loops and identifying patterns IS the engineer's primary value.

> "I try to oneshot it at the top and then I watch it and then if you watch it enough, you notice stupid patterns and then you make discoveries."

## Taxonomy

### 1. One-Shotting

The agent tries to build everything at once, running out of context mid-implementation. Features end up half-built and undocumented. The next session starts with broken code and has to guess what happened.

**Fix:** One task per loop. Incremental progress. JSON feature list with explicit `passes: false/true` fields so the agent always knows what's done and what isn't.

### 2. Premature Victory Declaration

> "After some features had already been built, a later agent instance would look around, see that progress had been made, and declare the job done."

The agent sees partial progress and considers the project complete.

**Fix:** Comprehensive feature list file set up by an initializer agent. All features start as `passes: false`. Strongly-worded instructions: "It is unacceptable to remove or edit tests because this could lead to missing or buggy functionality." Use JSON format — models are less likely to inappropriately modify JSON vs Markdown.

### 3. Superficial Testing

Claude's tendency to mark features as complete without proper end-to-end verification. The agent makes code changes, runs unit tests or `curl` commands, but fails to recognize that features don't work end-to-end.

**Fix:** Browser automation tools (Playwright MCP, Puppeteer MCP). Explicitly prompt for end-to-end testing as a human user would. The evaluator in [[multi-agent-harness-design]] catches these by clicking through the running application.

### 4. Self-Evaluation Blindness

> "When asked to evaluate work they've produced, agents tend to respond by confidently praising the work — even when, to a human observer, the quality is obviously mediocre."

The agent identifies legitimate issues, then "talks itself into deciding they weren't a big deal and approves the work anyway." It also tests superficially rather than probing edge cases.

**Fix:** Separate evaluator agent. Tuning a standalone evaluator to be skeptical is far more tractable than making a generator self-critical. Even then, several rounds of prompt tuning are needed before the evaluator grades reasonably.

### 5. Context Pollution (Chat Hygiene Failure)

Reusing a context window across unrelated goals creates cross-contamination:

> "They make my website pink and then set another goal for an API and all of a sudden they've got this backend API controller with pink REST endpoints."

**Fix:** New chat = new array. One context window, one activity, one goal. See [[context-engineering]].

### 6. The Dumb Zone

Performance degrades at 60-70% context fill. The agent becomes measurably less capable, makes more errors, and produces lower-quality code. See [[context-engineering]] for details.

**Fix:** Fresh context per iteration. Minimize permanent allocations. Only output failing tests.

### 7. Context Anxiety

The agent wraps up prematurely, comments out code, or takes implementation shortcuts when it senses it's approaching its context limit. Particularly pronounced in Sonnet 4.5.

**Fix:** Context resets with structured handoff artifacts rather than relying on compaction.

### 8. Compaction Loss

Auto-compaction drops critical specs and goals through lossy summarization. The agent "forgets" what it was building.

**Fix:** Avoid compaction entirely by creating fresh context per iteration with pinned specs. Use `claude-progress.txt` and git history for state handoff between iterations.

## Concrete Examples from Evaluator Catches

[[source-anthropic-harness-design|Anthropic's evaluator]] found specific, actionable bugs:

| Contract Criterion | Evaluator Finding |
|---|---|
| Rectangle fill tool allows click-drag to fill area | FAIL — Tool only places tiles at drag start/end points. `fillRectangle` exists but isn't triggered on mouseUp. |
| User can select and delete entity spawn points | FAIL — Delete key handler requires both `selection` AND `selectedEntityId`, but clicking only sets one. |
| User can reorder animation frames via API | FAIL — `PUT /frames/reorder` route defined after `/{frame_id}` routes. FastAPI matches 'reorder' as integer, returns 422. |

## The Discipline

> "It's important to watch the loop as that is where your personal development and learning will come from. When you see a failure domain — put on your engineering hat and resolve the problem so it never happens again."

The fireplace metaphor: watching Claude Code work is like watching a fireplace — you observe, discover patterns, and engineer them away. This is where the engineer's learning and growth happen.

## Related

- [[ralph-loops]] — The loops where failure domains are observed
- [[context-engineering]] — Context-related failure patterns and solutions
- [[back-pressure]] — Engineering mechanisms that prevent failures
- [[multi-agent-harness-design]] — Evaluator catches failures generators miss
- [[source-anthropic-harness-design]] — Concrete failure examples and solutions
- [[source-anthropic-effective-harnesses]] — Initializer/coding agent pattern addressing common failures
