# Query the wiki

Question: $ARGUMENTS

Follow the query workflow defined in CLAUDE.md:

1. Determine which topic(s) this question relates to. If unclear, list available topics and ask.
2. Read `<topic>/wiki/index.md` to find relevant pages.
3. Read the relevant wiki pages.
4. Synthesize an answer with citations to wiki pages and raw sources.
5. If the answer is substantial and reusable, offer to file it as a new wiki page or as an artifact in `<topic>/outputs/`.
6. If filed, update `<topic>/wiki/index.md` and append to `<topic>/wiki/log.md`.

Answers can take many forms depending on the question — a markdown page, a comparison table, a slide deck (Marp), a chart, a diagram. Ask the user if a particular format would be useful.
