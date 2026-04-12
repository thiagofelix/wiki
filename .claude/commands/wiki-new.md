# Create a new wiki topic

Create a new research topic called: $ARGUMENTS

Follow the instructions in CLAUDE.md to scaffold the topic:

1. Create the folder structure: `<topic>/raw/`, `<topic>/wiki/`, `<topic>/outputs/`
2. Create `<topic>/wiki/index.md` with the standard index template (empty sections for Entities, Concepts, Sources, Syntheses)
3. Create `<topic>/wiki/log.md` with a header and an initial entry recording the topic creation
4. Ask the user if this topic needs any special conventions. If so, create `<topic>/wiki/_schema.md`.

Use lowercase kebab-case for the folder name.

After scaffolding, briefly describe what was created and ask the user if they have sources ready to ingest.
