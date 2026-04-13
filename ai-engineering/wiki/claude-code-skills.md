---
title: Claude Code Skills
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Claude Code Skills

Claude Code skills are short markdown files that encode engineering processes as reusable instructions for AI agents. When invoked, they steer [[claude-code|Claude Code]] down a strict, well-defined path — compensating for the fact that AI agents have no memory and need explicit process guidance to produce quality work.

## The Problem Skills Solve

From [[source-pocock-claude-code-skills|Matt Pocock]]: "You have access to a fleet of middling to good engineers that you can deploy at any time. But the weird thing about these engineers is they have no memory. They do not remember things they've done before. And so you need extremely strict and well-defined processes to get those agents to actually do things that are useful."

Skills encode your process so the AI has a strict path to follow every single time. The result: code quality "shot up."

## Key Insight: Skills Don't Have to Be Long

The "Grill Me" skill is just **three sentences** long, yet it can drive 30-50 question interview sessions lasting 45 minutes. "You've just got to choose the right words for the LLM at the right time."

## The Skills Ecosystem

Matt Pocock's workflow chains several skills in sequence:

1. **[[design-trees-and-planning|Grill Me]]** — Interview relentlessly until shared understanding is reached
2. **[[prd-workflow|Write a PRD]]** — Turn the shared understanding into a Product Requirements Document
3. **[[prd-workflow|PRD to Issues]]** — Break the PRD into vertical slices as GitHub issues
4. **[[test-driven-development|TDD]]** — Implement each issue using red-green-refactor loops
5. **[[codebase-architecture|Improve Codebase Architecture]]** — Periodically refactor to keep module boundaries clean

## How They Work

Each skill is a markdown file that gets loaded into the LLM's context when invoked. The skill contains:
- A description of when it should be used
- Step-by-step workflow instructions
- Philosophy and principles (optional but helpful)
- Links to related concepts or documentation

## The "Treat Them Like Humans" Principle

"If you took all of these skills and just said 'this is a little mini markdown book of processes for humans,' it wouldn't look out of place. The most successful way to get code quality up from agents is just to treat them like humans. Humans with weird constraints — humans that have no memory and come out of the birthing pod and go right to work."

## Relationship to Ralph Loops

[[source-pocock-claude-code-skills|Matt Pocock]] explicitly calls his autonomous implementation loops "Ralph loops" — a term from [[source-ghuntley-collected|Geoffrey Huntley]]. Skills steer the Ralph loop: the Grill Me skill shapes what gets built, the PRD skill defines the destination, and TDD provides [[back-pressure]] during execution.

## Relationship to Knowledge Base Skills

The concept of skills for engineering (steering AI through coding processes) is distinct from but parallel to [[schema-files]] for knowledge bases (steering AI through wiki maintenance). Both use markdown instructions to encode processes.

## Related

- [[claude-code]] — The tool that executes skills
- [[design-trees-and-planning]] — The Grill Me skill
- [[prd-workflow]] — PRD and issue skills
- [[test-driven-development]] — TDD skill
- [[codebase-architecture]] — Architecture improvement skill
- [[ralph-loops]] — The loops that skills steer
- [[back-pressure]] — The engineering complement to skills
