---
title: "Source: Geoffrey Huntley — Collected Blog Posts"
type: summary
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Source: Geoffrey Huntley — Collected Blog Posts

Geoffrey Huntley is an Australian software engineer, entrepreneur, and prolific writer who has been documenting the AI transformation of software development since late 2024. He discovered the [[ralph-loops|Ralph loop]] pattern, coined the term "[[model-first-companies]]," and is building Latent Patterns — an educational platform that doubles as a [[software-factories|software factory]] demonstrating his ideas in practice.

## Metadata

- **Author:** Geoffrey Huntley (@GeoffreyHuntley)
- **Platforms:** ghuntley.com (blog), YouTube (@geoffreyhuntley)
- **Date range:** Sep 2025 – Mar 2026
- **Raw files:** 12 blog posts in `raw/ghuntley-*.md`, 12 YouTube transcripts, 1 video index in `raw/ghuntley-youtube-index.md`

## Posts and Key Ideas

### Everything Is a Ralph Loop (`ghuntley-loop.md`)
Defines the [[ralph-loops|Ralph loop]] pattern — a monolithic agent running one task per loop. Introduces the progression from brick-by-brick → Ralph → Gastown → Weaving Loom → [[software-factories|evolutionary software]]. Key insight: "software is now clay on the pottery wheel."

### Don't Waste Your Back-Pressure (`ghuntley-pressure.md`)
Defines [[back-pressure]] as the art/engineering of providing just enough resistance to reject hallucinations. Covers language choice, fast test suites, pre-commit hooks. "If you aren't capturing your back-pressure then you are failing as a software engineer."

### RAD: Rapid Application Development Is Back (`ghuntley-rad.md`)
Demonstrates [[software-factories]] through Latent Patterns — an educational platform where the product is the IDE. Built PostHog, PipeDrive, Trello, ZenDesk, and Calendly clones by prompting agents. Introduces risk-based shipping, sales automation via LLM prompts over meeting transcripts, and the vision of killing CI/CD.

### Software Development Costs Less Than Minimum Wage (`ghuntley-real.md`)
Documents [[ai-industry-disruption]]: $10.42/hour development cost, the K-shape economy, destroyed moats (per-seat pricing, lock-in, switching costs). Defines new moats: distribution, utility pricing, taste. Warns of brutal transformation ahead.

### Teleporting Into the Future (`ghuntley-teleport.md`)
Describes the "creative psychosis" phase where AI lets builders teleport to the future and complete retirement projects now. A 2-3 month period of intense creation. The question: consumer of tools, or someone who automates their job function?

### AI as Economic Warfare (`ghuntley-warfare.md`)
Frames free Chinese AI models as potential [[ai-economic-warfare|economic warfare]] — open source used at the national level for the first time. Raises trust questions about all frontier labs and dependency risks.

### Cognitive Security (`ghuntley-cogsec.md`)
Explores [[cognitive-security]] — the risk of outsourcing thinking to AI. Golden Gate Claude showed model weights can be surgically modified. Speculates about advertisers bidding on model weight rankings. Solution: raise your own model.

### I Ran Claude in a Loop and Created Cursed (`ghuntley-cursed.md`)
Three months of [[ralph-loops|Ralph loops]] produced "Cursed" — a Gen-Z programming language with a working compiler (interpreted + LLVM compiled). Proves "the most high-IQ thing is perhaps the most low-IQ thing: run an agent in a loop." Demonstrates that "LLMs amplify the skills that developers already have."

### The Frontier Interview (`ghuntley-frontier.md`)
Defines [[software-development-vs-engineering]] distinction. Declares open source "dead" for most use cases. Describes the abundance era where software is hyper-commodity. New moats are non-technical: contracts, relationships, taste, distribution.

### Porting Software Is Trivial (`ghuntley-porting.md`)
Four-stage [[porting-with-ai]] technique using Ralph loops: extract test specs → extract product specs → implement in target language → strict compilation. Key technique: citations in specs trigger file_read tool.

### LLM Weights vs. Papercuts (`ghuntley-papercuts.md`)
Introduces [[model-first-companies]] concept — businesses built with the "grain" of model weights. Short but foundational framing.

### Secure Code Generation (`ghuntley-secure-codegen.md`)
Argues [[secure-code-generation]] can't be achieved via MCP tools or Cursor rules. Must be engineered through [[back-pressure]], sandboxing, credential management, and architecture.

## YouTube Videos

See [[source-ghuntley-videos]] for a full index with key insights per video. 11 videos totaling ~7 hours of content, covering Ralph from first principles, Loom infrastructure, agent construction, agents.md history, and industry disruption.

### Most Important Videos

- **Inventing the Ralph Wiggum Loop** (58 min) — Origin story, context windows as arrays, the fireplace metaphor, test runner optimization
- **AI Giants Interview** (1:08 hr) — Ralph's general theory vs Anthropic's implementation, specs as lookup tables, chat hygiene
- **Early Preview of Loom** (1:17 hr) — Deep dive into Loom architecture, weavers/threads, actor/pub-sub patterns
- **Ralph from 1st Principles** (36 min) — Agent building in 300 lines, LLM quadrant mapping, inferencing loop fundamentals

## Recurring Themes

1. **Ralph is everything** — Loops, not linear development
2. **Watch the loops** — That's where learning happens
3. **Software development is dead; engineering evolves** — The identity crisis
4. **Work with the grain** — Build with model weights, not against them
5. **The models don't stop getting good** — Plan accordingly
6. **Build your own agent** — "Consumption is now the baseline for employment"

## Notable Quotes

> "Software development is dead — I killed it."

> "The most high-IQ thing is perhaps the most low-IQ thing: run an agent in a loop."

> "If you aren't capturing your back-pressure then you are failing as a software engineer."

> "For a lot of people, they haven't noticed AI is knocking on their door because AI is burrowing under their house."

> "After you come out of this phase, I hope you get to where I am, because just because you can build something doesn't mean you necessarily should."
