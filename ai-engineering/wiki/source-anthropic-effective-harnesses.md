---
title: "Source: Effective Harnesses for Long-Running Agents (Anthropic)"
type: summary
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Source: Effective Harnesses for Long-Running Agents (Anthropic)

This Anthropic engineering blog post by Justin Young describes a two-part solution for enabling AI agents to work effectively across many context windows: an **initializer agent** that sets up the environment on the first run, and a **coding agent** that makes incremental progress while leaving structured artifacts for the next session.

## Metadata

- **Author:** Justin Young (Anthropic)
- **Source:** https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- **Raw file:** `raw/Effective harnesses for long-running agents.md`

## The Problem

Out of the box, even frontier models (Opus 4.5) running in a loop across multiple context windows fail to build production-quality apps from a high-level prompt. Two specific failure patterns:

1. **One-shotting**: Agent tries to build everything at once, runs out of context mid-implementation, leaves half-built features
2. **Premature victory**: Later agent instances see partial progress and declare the project complete

## The Two-Agent Solution

### Initializer Agent
First session uses a specialized prompt to set up:
- An `init.sh` script to run the development server
- A `claude-progress.txt` file logging what agents have done
- An initial git commit showing what files were added
- A comprehensive **JSON feature list** (200+ features for a claude.ai clone) all marked `passes: false`

### Coding Agent
Every subsequent session:
1. Runs `pwd` to see working directory
2. Reads git logs and progress files to get up to speed
3. Reads feature list and chooses highest-priority incomplete feature
4. Works on ONE feature at a time (incremental progress)
5. Commits to git with descriptive messages
6. Updates progress file

## Key Design Decisions

- **JSON over Markdown** for feature lists — model is less likely to inappropriately modify JSON
- **Strongly-worded instructions**: "It is unacceptable to remove or edit tests"
- **Browser automation** (Puppeteer MCP) for end-to-end testing — dramatically improved bug detection
- **init.sh bootstrap** — agent always starts dev server and runs basic e2e test before new features

## Failure Mode Summary

| Problem | Initializer Solution | Coding Agent Solution |
|---|---|---|
| Premature victory | JSON feature list, all `passes: false` | Read list, pick single incomplete feature |
| Broken state | Git repo + progress notes | Read progress, run basic test first |
| Features marked done prematurely | Feature list structure | Self-verify before marking `passes: true` |
| Time wasted on setup | `init.sh` script | Read init.sh at session start |

## Key Insight

> "The key insight here was finding a way for agents to quickly understand the state of work when starting with a fresh context window, which is accomplished with the claude-progress.txt file alongside the git history."

## Related

- [[failure-domains]] — The specific failures this harness addresses
- [[ralph-loops]] — This harness is an implementation of the Ralph pattern
- [[multi-agent-harness-design]] — The evolution into three-agent architecture
- [[source-anthropic-harness-design]] — Follow-up research with planner/generator/evaluator
- [[context-engineering]] — State handoff between context windows
