---
title: Ralph Loops
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Ralph Loops

A Ralph loop (named after Ralph Wiggum) is a pattern where an AI coding agent runs autonomously in a `while true` loop, performing one task per iteration against a codebase. Discovered and popularized by [[source-ghuntley-collected|Geoffrey Huntley]], it is the foundational orchestration pattern behind [[software-factories]], autonomous code generation, and the shift from building software "brick by brick" to treating software as clay on a pottery wheel.

## The Core Pattern

Ralph is **monolithic** — a single process in a single repository that performs one task per loop. This is deliberately the opposite of multi-agent architectures:

> "Consider microservices and all the complexities that come with them. Now, consider what microservices would look like if the microservices (agents) themselves are non-deterministic — a red hot mess. Ralph is monolithic. Ralph works autonomously in a single repository as a single process that performs one task per loop."

## How It Works

1. Allocate an array of tasks with backing specifications
2. Give the agent a goal
3. Loop the goal — one task per iteration
4. **Watch the loop** — this is where your learning comes from
5. When you see a failure domain, engineer it away so it never happens again

At its core, Ralph is "a bash loop that deterministically allocates the memory, allows the LLM to pick one thing to do in the task list, and you set it off to the races."

In practice this means either:
- **Manual looping** — prompting the agent, reviewing, then continuing
- **Automated looping with a pause** — pressing CTRL+C to progress to the next task
- **Full autonomy** — the agent runs unattended (forward mode, "building AFK")

## Practical Setup

### Specifications as Lookup Tables

Specifications are maintained as `/specs/*.md` files that serve as "a lookup table to other specifications." Every loop iteration loads these specs to pin and reframe the goal:

> "Every loop I allocate the specifications which is a lookup table to other specifications and that's enough to pin and reframe each loop — this is my domain knowledge."

Token budget: ~5,000 tokens allocated for specs/goals per loop. The specs have "pins" — multiple generative words that improve search tool hit rates.

### State Handoff Between Iterations

Since each iteration creates a fresh context, state must be passed through persistent artifacts:
- **`claude-progress.txt`** — log of what agents have done across sessions
- **Git history** — commit messages and diffs show what changed
- **JSON feature lists** — structured files with explicit `passes: false/true` fields for each feature
- **`init.sh`** — bootstrap script that starts development servers and runs basic e2e tests

JSON is preferred over Markdown for feature tracking because models are less likely to inappropriately modify structured JSON.

### Session Bootstrap

A typical loop iteration begins:
1. Run `pwd` to see working directory
2. Read git logs and progress files
3. Read feature list, choose highest-priority incomplete feature
4. Run `init.sh` to start development server
5. Run basic e2e test to verify app isn't broken
6. Work on ONE feature
7. Commit, update progress file

### Chat Hygiene

One context window = one activity = one goal. Reusing context across unrelated goals causes pollution:

> "They make my website pink and then set another goal for an API and all of a sudden they've got this backend API controller with pink REST endpoints... new chat is a new array."

See [[context-engineering]] and [[failure-domains]] for the full taxonomy of what goes wrong.

## Forward Mode vs. Reverse Mode

Ralph isn't just about building forward (autonomous generation). It also works in **reverse mode** (clean-rooming) — studying existing code, extracting specifications, and rebuilding. See [[porting-with-ai]].

## Ralph as Mindset

> "Ralph isn't just about forwards or reverse mode — it's also a mindset that these computers can be indeed programmed."

The mindset shift: instead of writing code line by line, you are **programming the loop** — automating your job function. The engineer's role becomes designing the loop, tuning [[back-pressure]], and resolving failure domains.

## Relationship to Other Concepts

- [[source-pocock-claude-code-skills|Matt Pocock]] calls his autonomous implementation loops "Ralph loops" — Claude Code picks up GitHub issues from a [[prd-workflow]], implements them with [[test-driven-development|TDD]], comments, and closes them
- [[source-herk-llm-wiki-setup|Nate Herk]] uses Ralph-like loops for wiki ingestion — "Hey, can you go ahead and ingest the new YouTube video"
- [[source-ghuntley-collected|Huntley]] used a Ralph loop to build an entire programming language (Cursed) over three months

## The Cursed Example

Huntley ran Claude in a loop for three months with one prompt: "Produce me a Gen-Z compiler, and you can implement anything you like." The result: a fully functioning programming language called Cursed with compiled binaries, editor extensions, and a standard library. This demonstrated that "the most high-IQ thing is perhaps the most low-IQ thing: run an agent in a loop."

## Key Principles

- **One task per loop** — keeps the agent focused, prevents context confusion
- **Watch the loops** — your personal development and learning comes from observing
- **Engineer failure domains away** — when something breaks, fix the system, not just the output
- **[[back-pressure]] is essential** — tests, type checking, and pre-commit hooks reject invalid generations

## Context Window Management

A critical aspect of Ralph: each loop iteration should create a **fresh context window**. This avoids compaction (the agent summarizing and dropping older context), which Huntley calls "evil." The Anthropic implementation of Ralph runs continuously with compaction; the general theory is to start fresh each time. See [[building-an-agent]] and [[agents-md-history]] for more on context management.

[[source-anthropic-harness-design|Anthropic's harness research]] validated this position: their Sonnet 4.5 experiments found that compaction alone wasn't sufficient for long tasks, and **context resets** (clearing the window entirely with structured handoff) were essential. Newer models like Opus 4.6 reduced but did not eliminate the need.

## From Ralph to Multi-Agent

Ralph is a single-agent pattern. [[multi-agent-harness-design]] extends it by adding specialized agents (planner, generator, evaluator) that decompose and quality-check the work. Anthropic explicitly references Ralph as convergent discovery in their harness research, and [[source-pocock-7-phases|Matt Pocock's 7 Phases framework]] maps the human version of this workflow onto the same principles.

## Related

- [[back-pressure]] — Engineering feedback for loops
- [[failure-domains]] — Taxonomy of what breaks and how to fix it
- [[context-engineering]] — Managing the context window per iteration
- [[software-factories]] — Where Ralph loops lead at scale
- [[loom]] — Infrastructure orchestrator for Ralph loops
- [[porting-with-ai]] — Ralph in reverse mode
- [[test-driven-development]] — TDD as a form of Ralph loop
- [[claude-code-skills]] — Skills that steer Ralph loops
- [[claude-code]] — The agent that runs in the loop
- [[building-an-agent]] — Understanding the agent that runs in the loop
- [[agents-md]] — Configuring the agent for each loop
- [[multi-agent-harness-design]] — Extending Ralph with specialized agents
- [[source-ghuntley-collected]] — Huntley's blog posts on Ralph
- [[source-ghuntley-videos]] — Video deep dives into Ralph mechanics
- [[source-anthropic-harness-design]] — Anthropic's validation and extension of Ralph
- [[source-anthropic-effective-harnesses]] — Initializer/coding agent patterns
- [[source-pocock-7-phases]] — 7-phase framework built on Ralph loops
