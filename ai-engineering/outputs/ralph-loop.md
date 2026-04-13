---
marp: true
theme: default
paginate: true
backgroundColor:
color:
style: |
  section {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }
  h1, h2, h3 {
    color: #e94560;
  }
  blockquote {
    border-left: 4px solid #e94560;
    color: #cccccc;
    font-style: italic;
  }
  strong {
    color: #e94560;
  }
  code {
    background: #16213e;
    color: #0f3460;
  }
  a {
    color: #e94560;
  }
  section.lead h1 {
    font-size: 2.5em;
  }
  section.lead h2 {
    color: #cccccc;
    font-size: 1.2em;
    font-weight: normal;
  }
---

<!-- _class: lead -->

# Ralph Loops

## The foundational pattern behind autonomous AI software development

Coined by **Geoffrey Huntley** (named after Ralph Wiggum)

---

# What is a Ralph Loop?

An AI coding agent running autonomously in a **`while true` loop**, performing **one task per iteration** against a codebase.

> "The most high-IQ thing is perhaps the most low-IQ thing: run an agent in a loop."

---

# The Mindset Shift

### Before: Brick by Brick

Building software vertically, like Jenga blocks — manual, sequential, line by line.

### Now: Clay on a Pottery Wheel

Software is **shaped**, not stacked. If something isn't right, throw it back on the wheel.

> "I'm there as an engineer... but instead am programming the loop, automating my job function."

---

# Why Monolithic?

Ralph is deliberately a **single process** in a **single repository**.

> "Consider microservices and all the complexities that come with them. Now, consider what microservices would look like if the microservices (agents) themselves are non-deterministic — a red hot mess."

The opposite of multi-agent complexity. One agent. One task. One loop.

---

# How It Works

1. **Allocate** an array of tasks with backing specifications
2. **Give** the agent a goal
3. **Loop** the goal — one task per iteration
4. **Watch** the loop — this is where your learning comes from
5. **Engineer away** failure domains so they never happen again

---

# Three Modes of Looping

| Mode | Description |
|------|-------------|
| **Manual** | Prompt the agent, review output, continue |
| **Semi-auto** | Automated with a pause (CTRL+C to progress) |
| **Full autonomy** | Agent runs unattended — "building AFK" |

The goal is to progressively move toward full autonomy as you engineer away failure domains.

---

# Forward Mode vs. Reverse Mode

### Forward Mode
Build new software autonomously. Give the agent a spec, let it generate.

### Reverse Mode (Clean-Rooming)
Study existing code, extract specifications, rebuild from scratch.

> "Ralph isn't just about forwards or reverse mode — it's also a mindset that these computers can be indeed programmed."

---

# Back-Pressure: The Key Engineering Discipline

**Back-pressure** = just enough resistance to reject bad generations without killing loop speed.

- **Too little** &rarr; hallucinations slip through
- **Too much** &rarr; loop spins too slowly

> "If you aren't capturing your back-pressure then you are failing as a software engineer."

---

# Methods of Back-Pressure

| Method | How it helps |
|--------|-------------|
| **Strict typing** | Compiler catches errors instantly |
| **Fast test suites** | Signal on correctness without bottlenecking |
| **Pre-commit hooks** | Enforce linting, formatting, types on every commit |
| **Clean architecture** | Clear module boundaries guide the agent |

Pre-commit hooks are Huntley's favorite: *"Now that humans aren't the ones doing the software development, it really doesn't matter anymore."*

---

# Context Window Management

Each loop iteration should create a **fresh context window**.

- Avoid compaction (agent summarizing and losing older context)
- Start each task with clean context
- Anthropic's research validated this: context resets with structured handoff are essential

**One task. Fresh context. Every time.**

---

# The Cursed Example

Huntley ran Claude in a loop for **three months** with one prompt:

> "Produce me a Gen-Z compiler, and you can implement anything you like."

**Result:** A fully functioning programming language called **Cursed** with:
- Compiled binaries
- Editor extensions
- A standard library

---

# Real-World Ralph Loops

- **Matt Pocock** — Claude Code picks up GitHub issues, implements them with TDD, comments, and closes them automatically
- **Nate Herk** — Ralph-like loops for wiki ingestion and knowledge processing
- **Geoffrey Huntley** — Built an entire programming language (Cursed) over three months

---

# From Ralph to Software Factories

| Level | Description |
|-------|-------------|
| **Brick by brick** | Traditional manual development |
| **Ralph loops** | One agent, one task, one loop |
| **Gastown** | Orchestration across multiple loops |
| **The Weaving Loom** | Infrastructure for evolutionary software |
| **Level 9** | Autonomous loops optimizing for business outcomes |

> "On the loop, not in the loop."

---

# Key Principles

- **One task per loop** — keeps the agent focused
- **Watch the loops** — your learning comes from observing
- **Engineer failure domains away** — fix the system, not just the output
- **Back-pressure is essential** — tests, types, and hooks reject invalid output
- **Fresh context each iteration** — avoid compaction at all costs

---

<!-- _class: lead -->

# The Engineer's New Role

You are no longer writing code line by line.

You are **programming the loop**.

> "Go build your agent, go learn how to program the new computer, fall in love with all the possibilities and then join me in this space race of building automated software factories."
> — Geoffrey Huntley
