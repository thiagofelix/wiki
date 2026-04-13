---
title: Porting with AI
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Porting with AI

Porting a codebase from one language to another using AI is a structured application of [[ralph-loops]] in reverse mode. [[source-ghuntley-collected|Geoffrey Huntley]] describes a technique that uses specifications with citations as an intermediate representation, decoupling the source language from the target language.

## The Process

### Stage 1: Extract Test Specifications
Run a Ralph loop that compresses all tests into `/specs/*.md`:
> "Study every file in tests/** using separate sub-agents and document in /specs/*.md and link the implementation as citations in the specification."

### Stage 2: Extract Product Specifications
Run a separate Ralph loop for all product functionality:
> "Study every file in src/* using separate sub-agents per file and link the implementation as citations in the specification."

### Stage 3: Implement in Target Language
Within the same repo, run a Ralph loop to:
1. Create a TODO file from the specifications
2. Execute a classic Ralph — one task per loop, most important thing first
3. The agent studies the specifications and follows citations to reference the original source code

### Stage 4: Strict Compilation
Configure the target language to have **strict compilation** for maximum [[back-pressure]].

## The Key Theory

**Citations in specifications** are the crucial technique. When the agent encounters a citation pointing to a source file, it triggers the `file_read` tool to study the original implementation. This gives the agent concrete reference material during the porting stage.

Stages 1 and 2 reduce the codebase to **high-level PRDs** without coupling the implementation to the source language. This is essentially the same principle as [[prd-workflow]] — describe the destination, then let the agent build the journey.

## Why It Works

- Specifications serve as a language-agnostic intermediate representation
- Citations tease the file_read tool to study original implementations
- Strict typing in the target language provides immediate [[back-pressure]]
- One task per loop keeps the agent focused
- Sub-agents parallelize the extraction work

## Related

- [[ralph-loops]] — The core execution pattern (reverse mode)
- [[back-pressure]] — Strict compilation as feedback
- [[prd-workflow]] — Same principle: specifications → implementation
- [[software-development-vs-engineering]] — Engineering the porting process
