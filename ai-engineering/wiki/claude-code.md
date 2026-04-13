---
title: Claude Code
type: entity
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Claude Code

Claude Code is Anthropic's AI coding agent that operates from the terminal or VS Code. It is the primary engine used for building, compiling, and querying [[llm-knowledge-bases|LLM Knowledge Bases]], and the tool around which an ecosystem of [[claude-code-skills]] has emerged for steering AI agents through structured engineering processes.

## Role in Knowledge Bases

Claude Code serves as the "compiler" in Karpathy's LLM wiki system:
- Reads raw sources and generates wiki articles
- Maintains indexes and backlinks
- Answers questions against the wiki
- Runs [[health-checks-and-linting|health checks]]
- Files outputs back into the wiki

Both [[source-herk-llm-wiki-setup|Nate Herk]] and [[source-spisak-second-brain|Nick Spisak]] use Claude Code as their primary tool. Herk demonstrated running it from both VS Code and the terminal, noting he prefers the terminal for the status line and additional functionality.

## Role in Engineering

[[source-pocock-claude-code-skills|Matt Pocock]] describes Claude Code as the center of a skills-based engineering workflow:
- Skills are markdown files that encode processes (see [[claude-code-skills]])
- Claude Code reads these skills and follows strict paths for [[design-trees-and-planning|planning]], [[prd-workflow|PRD writing]], [[test-driven-development|TDD]], and [[codebase-architecture|architecture improvement]]
- "Ralph loops" — autonomous loops where Claude Code picks up GitHub issues, implements them, comments, and closes them

## Key Characteristics

From [[source-pocock-claude-code-skills|Matt Pocock]]:
- AI agents are like "middling to good engineers" you can deploy at any time
- They have **no memory** — they don't remember things they've done before
- You need **extremely strict and well-defined processes** to get useful output
- The most successful approach is to "treat them like humans — humans with weird constraints"

## Schema File Integration

Claude Code reads [[schema-files|CLAUDE.md]] files to understand project context. This is used both for:
- Knowledge base organization (wiki rules, folder structure)
- Engineering projects (coding standards, architecture decisions)
- Cross-project references (one CLAUDE.md pointing to another project's wiki)

## Ralph Loops

[[source-ghuntley-collected|Geoffrey Huntley]] uses Claude Code as the primary agent in [[ralph-loops]] — autonomous loops that build software one task at a time. [[source-pocock-claude-code-skills|Matt Pocock]] also runs "Ralph loops" where Claude Code picks up GitHub issues, implements them, and closes them.

## Related

- [[llm-knowledge-bases]] — The system Claude Code powers
- [[claude-code-skills]] — Reusable process instructions
- [[ralph-loops]] — Autonomous loops powered by Claude Code
- [[obsidian]] — Visual frontend complement to Claude Code
- [[schema-files]] — How Claude Code gets its instructions
