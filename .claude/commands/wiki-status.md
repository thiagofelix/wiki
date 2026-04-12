# Wiki status overview

Show the current state of all research topics in the wiki.

For each topic found (top-level directories that contain `raw/`, `wiki/`, `outputs/`):

1. Read `<topic>/wiki/index.md` — count pages by type.
2. Count files in `<topic>/raw/` — number of sources ingested.
3. Count files in `<topic>/outputs/` — number of artifacts produced.
4. Read the last 3 entries from `<topic>/wiki/log.md` — recent activity.

Present a summary table:

| Topic | Sources | Wiki Pages | Outputs | Last Activity |
|-------|---------|------------|---------|---------------|

Then show recent activity across all topics (last 5 log entries globally, sorted by date).

If `$ARGUMENTS` names a specific topic, show a detailed view of that topic instead: full index, full recent log, and page list with update dates.
