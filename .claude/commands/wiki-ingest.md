# Ingest a source into a wiki topic

Ingest the following source: $ARGUMENTS

Follow the ingest workflow defined in CLAUDE.md:

1. Determine which topic this source belongs to. If unclear or multiple topics exist, ask the user.
2. Locate the source. If `$ARGUMENTS` is a file path, read it from there. If it's a URL, fetch it and save it as markdown in `<topic>/raw/`. If the source is already in `raw/`, read it from there.
3. Read the source fully.
4. Discuss the key takeaways with the user before writing anything.
5. After the user confirms the direction, create/update wiki pages:
   - Write a summary page for the source in `<topic>/wiki/`.
   - Update existing entity/concept pages with new information.
   - Create new entity/concept pages as needed.
   - Flag any contradictions with existing wiki content.
6. Update `<topic>/wiki/index.md`.
7. Append an entry to `<topic>/wiki/log.md`.

Always read the topic's `wiki/index.md` first to understand what already exists before making changes.
