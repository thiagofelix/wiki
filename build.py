#!/usr/bin/env python3
"""
Build script for the LLM Wiki.

Assembles wiki pages from topic folders into a MkDocs-compatible docs/ directory.
Converts [[wikilinks]] to standard markdown links and generates navigation.
"""

from __future__ import annotations

import os
import re
import shutil
import yaml
from pathlib import Path

ROOT = Path(__file__).parent
DOCS = ROOT / "docs"
WIKI_DIR_NAME = "wiki"

# Files to skip when copying wiki pages
SKIP_FILES = {"log.md", "_schema.md"}


def find_topics() -> list[Path]:
    """Find all topic directories (those containing a wiki/ subdirectory)."""
    topics = []
    for entry in sorted(ROOT.iterdir()):
        if entry.is_dir() and (entry / WIKI_DIR_NAME).is_dir():
            topics.append(entry)
    return topics


def slugify_title(name: str) -> str:
    """Convert kebab-case filename to a readable title."""
    return name.replace("-", " ").title()


def convert_wikilinks(content: str, topic_slug: str) -> str:
    """Convert [[wikilinks]] to standard markdown links.

    [[page-name]] -> [Page Name](page-name.md)
    [[page-name|display text]] -> [display text](page-name.md)
    """

    def replace_wikilink(match: re.Match) -> str:
        inner = match.group(1)
        if "|" in inner:
            target, display = inner.split("|", 1)
        else:
            target = inner
            display = slugify_title(inner)
        target = target.strip()
        display = display.strip()
        # Links within the same topic are relative
        return f"[{display}]({target}.md)"

    return re.sub(r"\[\[([^\]]+)\]\]", replace_wikilink, content)


def strip_frontmatter(content: str) -> tuple[dict, str]:
    """Extract YAML frontmatter and return (metadata, body)."""
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            try:
                meta = yaml.safe_load(parts[1]) or {}
            except yaml.YAMLError:
                meta = {}
            return meta, parts[2].lstrip("\n")
    return {}, content


TYPE_ICONS = {
    "entity": ":material-domain:",
    "concept": ":material-lightbulb-outline:",
    "summary": ":material-file-document-outline:",
    "comparison": ":material-scale-balance:",
    "overview": ":material-map-outline:",
    "synthesis": ":material-merge:",
}


def render_properties(meta: dict, topic_slug: str) -> str:
    """Render frontmatter as an Obsidian-style properties block using admonition."""
    rows = []

    if page_type := meta.get("type", ""):
        icon = TYPE_ICONS.get(page_type, ":material-tag-outline:")
        label = page_type.title()
        rows.append(f"    **Type** {{ .prop-key }}\n    :   {icon} {label}")

    if created := meta.get("created", ""):
        rows.append(f"    **Created** {{ .prop-key }}\n    :   :material-calendar-plus: {created}")

    if updated := meta.get("updated", ""):
        rows.append(f"    **Updated** {{ .prop-key }}\n    :   :material-calendar-edit: {updated}")

    if tags := meta.get("tags", []):
        tag_str = " ".join(f"`{t}`" for t in tags)
        rows.append(f"    **Tags** {{ .prop-key }}\n    :   :material-tag-multiple: {tag_str}")

    if sources := meta.get("sources", []):
        source_items = []
        for s in sources:
            # Extract readable name from path
            name = Path(s).stem
            source_items.append(f"`{name}`")
        sources_str = ", ".join(source_items)
        rows.append(f"    **Sources** {{ .prop-key }}\n    :   :material-link-variant: {sources_str}")

    if not rows:
        return ""

    block = '??? info "Properties"\n'
    block += "\n\n".join(rows)
    block += "\n\n"
    return block


def build_page(src: Path, dest: Path, topic_slug: str) -> dict | None:
    """Process a single wiki page. Returns metadata dict or None if skipped."""
    if src.name in SKIP_FILES:
        return None

    content = src.read_text(encoding="utf-8")
    meta, body = strip_frontmatter(content)

    title = meta.get("title", slugify_title(src.stem))
    page_type = meta.get("type", "")

    # Convert wikilinks
    body = convert_wikilinks(body, topic_slug)

    # Rebuild with title, properties block, and body
    output = f"# {title}\n\n"
    output += render_properties(meta, topic_slug)
    output += body

    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(output, encoding="utf-8")

    return {"title": title, "type": page_type, "file": src.name, "stem": src.stem}


def build_topic_index(topic_name: str, pages: list[dict], dest: Path):
    """Generate a landing page for a topic from its pages."""
    title = slugify_title(topic_name)
    lines = [f"# {title}\n"]

    # Group by type
    groups: dict[str, list[dict]] = {}
    for p in pages:
        t = p["type"] or "other"
        groups.setdefault(t, []).append(p)

    type_order = ["entity", "concept", "overview", "synthesis", "summary", "comparison", "other"]
    type_labels = {
        "entity": "Entities",
        "concept": "Concepts",
        "overview": "Overviews",
        "synthesis": "Syntheses",
        "summary": "Summaries",
        "comparison": "Comparisons",
        "other": "Other",
    }

    for t in type_order:
        if t not in groups:
            continue
        lines.append(f"\n## {type_labels.get(t, t.title())}\n")
        for p in sorted(groups[t], key=lambda x: x["title"]):
            lines.append(f"- [{p['title']}]({p['stem']}.md)")

    dest.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_site_index(topics: list[tuple[str, list[dict]]]):
    """Generate the top-level docs/index.md."""
    lines = [
        "# Wiki\n",
        "A personal knowledge base maintained by an LLM.\n",
    ]

    for topic_name, pages in topics:
        title = slugify_title(topic_name)
        entity_count = sum(1 for p in pages if p["type"] == "entity")
        concept_count = sum(1 for p in pages if p["type"] == "concept")
        total = len(pages)
        desc = f"{total} pages"
        parts = []
        if entity_count:
            parts.append(f"{entity_count} entities")
        if concept_count:
            parts.append(f"{concept_count} concepts")
        if parts:
            desc = ", ".join(parts) + f" — {total} pages total"

        lines.append(f"\n## [{title}]({topic_name}/index.md)\n")
        lines.append(f"{desc}\n")

    (DOCS / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def generate_nav(topics: list[tuple[str, list[dict]]]) -> list:
    """Generate mkdocs nav structure."""
    nav = [{"Home": "index.md"}]
    for topic_name, pages in topics:
        title = slugify_title(topic_name)
        topic_nav = [{"Overview": f"{topic_name}/index.md"}]
        for p in sorted(pages, key=lambda x: (x["type"] or "zzz", x["title"])):
            topic_nav.append({p["title"]: f"{topic_name}/{p['stem']}.md"})
        nav.append({title: topic_nav})
    return nav


def main():
    # Clean docs/
    if DOCS.exists():
        shutil.rmtree(DOCS)
    DOCS.mkdir()

    topics_data: list[tuple[str, list[dict]]] = []

    for topic_path in find_topics():
        topic_name = topic_path.name
        wiki_path = topic_path / WIKI_DIR_NAME
        dest_dir = DOCS / topic_name

        pages: list[dict] = []
        for md_file in sorted(wiki_path.glob("*.md")):
            if md_file.name == "index.md":
                # We'll generate our own index
                continue
            result = build_page(md_file, dest_dir / md_file.name, topic_name)
            if result:
                pages.append(result)

        if pages:
            build_topic_index(topic_name, pages, dest_dir / "index.md")
            topics_data.append((topic_name, pages))

    build_site_index(topics_data)

    # Write nav to a file that mkdocs.yml can reference
    nav = generate_nav(topics_data)
    nav_path = ROOT / "_nav.yml"
    nav_path.write_text(yaml.dump(nav, default_flow_style=False, allow_unicode=True), encoding="utf-8")

    print(f"Built {sum(len(p) for _, p in topics_data)} pages across {len(topics_data)} topics into docs/")


if __name__ == "__main__":
    main()
