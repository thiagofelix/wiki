---
title: Agents.md History and Design
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Agents.md History and Design

Agents.md (and its variants CLAUDE.md, .cursorrules) is the convention of placing a markdown instruction file at the root of a repository to tell AI coding agents how to work with the project. [[source-ghuntley-collected|Geoffrey Huntley]] led the informal standardization effort and has strong opinions on what makes a good one — and what the problems are.

## Origin Story

The proliferation of tool-specific files (claude.md, jules.md, .cursorrules) was littering repos. Huntley and Sourcegraph championed standardizing on a single file name. They originally pushed for `agent.md` (singular), but:

- `agents.md` was parked by a domain squatter who kept jacking the price
- OpenAI purchased `agents.md` and standardized on the plural form along with Google
- Huntley "took the L" and redirected agent.md → agents.md
- Symlinks handle the migration (CLAUDE.md → agents.md → etc.)

## The Single-File Problem

Huntley argues it may be **too soon to standardize on a single file name** because different models react differently to the same instructions:

- **GPT-5** says "do not use firm language" — yelling (uppercase) makes it timid
- **Anthropic models** respond well to firm, emphatic instructions
- A single agents.md tuned for one model creates noise when switching models

Proposed solution: per-model files (`agents/claude.md`, `agents/gpt5.md`).

## What Makes a Good Agents.md

### Size: ~70 Lines Maximum

"Your agents.md should be super super tiny. Just enough." The file is **permanently allocated** in the context window (slot 0 = harness prompt, slot 1 = agents.md). A large agents.md means:
- Less room for actual work
- Higher likelihood of operating in the "dumb zone"
- More context rot

### Content: Just Enough

The file should contain just enough to:
- Run tests (`make test`)
- Build the project
- Basic layout information
- Nothing more

> "It shouldn't be necessarily completely concrete... just enough to tickle the latent space and create a behavior, but not be hyper-specific."

### The Latent Space Principle

Instead of specifying exact commands, hint at concepts and let the model's latent knowledge fill in the details. Example: saying "check the web server, you should look at journald" is enough — the model knows journald relates to systemd and will use `systemctl` on its own.

### Maintenance: Mow It Regularly

> "Don't be afraid to get the harvester out and just lop it off. Destroy it and create it again from first principles."

In teams, agents.md files grow through PRs into "hidden forgotten knowledge." Regular pruning is essential.

## Relationship to Schema Files

In [[llm-knowledge-bases]], the equivalent concept is the [[schema-files|CLAUDE.md schema file]]. The same principles apply: keep it concise, focus on rules and structure, let the AI figure out the details.

## Related

- [[schema-files]] — The knowledge base version of agents.md
- [[ralph-loops]] — Agents.md must be just enough to run Ralph
- [[claude-code]] — The primary consumer of CLAUDE.md
- [[back-pressure]] — Agents.md tunes the loop behavior
- [[building-an-agent]] — Agents.md is slot 1 in the agent's context
