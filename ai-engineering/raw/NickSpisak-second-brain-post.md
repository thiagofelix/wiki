# How to Build Your Second Brain — Nick Spisak (@NickSpisak_)

Source: https://x.com/NickSpisak_/status/2040448463540830705
Date: Apr 4, 2026

---

@karpathy dropped a post describing how he uses AI to build personal knowledge bases.

The idea is simple: instead of keeping notes scattered across apps, you dump everything into one folder. Then you tell your AI to organize all of it into a personal wiki - summaries, connections, articles - that gets smarter every time you use it.

No special software. No database. Just folders and text files.

In under 7 minutes you'll learn:
- The exact folder structure to set up (takes 2 minutes)
- How to automate web scraping into your knowledge base with one CLI tool
- The one-file "schema" that makes the whole system work
- How to get your AI to compile raw notes into an organized wiki
- The compounding trick that makes it smarter every time you use it
- The health check that catches mistakes before they pile up

## 1. Create Three Folders (2 Minutes)

Open your terminal or file explorer. Create a project folder anywhere on your computer. Inside it, create three subfolders:

```
my-knowledge-base/
  raw/          (your source material - articles, notes, screenshots)
  wiki/         (where your AI will write the organized version)
  outputs/      (answers, reports, and research your AI generates)
```

That's it. This is the same structure @karpathy uses. The raw/ folder is your junk drawer of source material. The wiki/ folder is where the AI turns that mess into something organized. The outputs/ folder is where answers to your questions live.

No apps to install. No accounts to create. Three folders.

## 2. Fill Your Raw Folder (10 Minutes)

This is where most people stall. They create the folders and then stare at an empty raw/ directory wondering what to put in it.

The answer: everything. Copy-paste articles into .md or .txt files. Save screenshots or diagrams as images. Export notes from whatever app you use now. Paste in meeting notes, research papers, project docs. Dump in bookmarks you've been hoarding for months.

Don't organize it. Don't rename anything. Don't clean it up. That's the AI's job.

## 3. Automate Source Collection With Agent Browser (Optional But Powerful)

Vercel Labs just shipped agent-browser - a free CLI tool that lets your AI agent control a real browser. 26K+ GitHub stars. Two commands to install:

```
npm install -g agent-browser
agent-browser install
```

That second command downloads a dedicated Chrome browser. Now your AI can scrape any webpage, extract the text, and save it directly into your raw/ folder.

## 4. Write Your Schema File (5 Minutes)

Create a file in the root of your project called CLAUDE.md (or AGENTS.md or README.md). This file tells your AI what the knowledge base is about and how to organize it.

@karpathy confirmed he keeps his schema "super simple and flat" in an AGENTS.md file. No database. No plugin. Just a text file that tells the AI the rules.

## 5. Tell Your AI to Compile the Wiki (15 Minutes)

Open Claude Code (or Cursor, or any AI coding tool that can read your files). Point it at your project folder and say:

"Read everything in raw/. Then compile a wiki in wiki/ following the rules in CLAUDE.md. Create an INDEX.md first, then create one .md file per major topic. Link related topics. Summarize every source."

The important thing: you don't edit the wiki by hand. That's the AI's job. You read it, you ask questions against it, and the AI keeps it updated.

## 6. Ask Questions and Save the Answers (Ongoing)

Once your wiki has 10+ articles, start asking questions. The AI reads across your entire wiki and gives you answers grounded in your own collected material.

Save those answers back into the knowledge base. Drop the output into outputs/ or have the AI update the relevant wiki article with the new insight. Every question makes the next answer better. That's the loop.

## 7. Run a Health Check (Monthly)

Tell your AI: "Review the entire wiki/ directory. Flag any contradictions between articles. Find topics mentioned but never explained. List any claims that aren't backed by a source in raw/. Suggest 3 new articles that would fill gaps."

The fix is simple: run periodic health checks.

## 8. You Don't Need Obsidian (But You Can Use It)

A folder of text files and a schema file is the entire product. Flat files and a good schema will outperform a fancy tool stack 90% of the time.
