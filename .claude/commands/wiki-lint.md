# Lint a wiki topic

Lint the following topic: $ARGUMENTS

If no topic is specified, list available topics and ask which one to lint. If the user says "all", lint each topic.

Follow the lint workflow defined in CLAUDE.md:

1. Read `<topic>/wiki/index.md` and all wiki pages in the topic.
2. Check for:
   - Contradictions between pages
   - Stale claims that newer sources may have superseded
   - Orphan pages (no inbound links from other pages)
   - Important concepts mentioned in pages but lacking their own page
   - Missing cross-references between related pages
   - Data gaps — suggest sources to look for or web searches to run
   - Pages that have grown too large and should be split
   - index.md entries that are out of date or missing
3. Present findings as a checklist grouped by severity (errors, warnings, suggestions).
4. Ask the user which issues to fix, then apply the fixes.
5. Append a lint entry to `<topic>/wiki/log.md`.
