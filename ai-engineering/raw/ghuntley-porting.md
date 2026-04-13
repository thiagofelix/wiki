# porting software has been trivial for a while now. here's how you do it.

**Author:** Geoffrey Huntley  
**Source:** https://ghuntley.com/porting/  
**Category:** AI  
**Date:** 15 Mar 2026  

---

This one is short and sweet. if you want to port a codebase from one language to another here's the approach:

1. Run a ralph loop which compresses all tests into /specs/*.md which looks similar to "study every file in tests/** using separate subagents and document in /specs/*.md and link the implementation as citations in the specification"
2. Then do a separate Ralph loop for all product functionality - ensuring there's citations to the specification. "study every file in src/* using seperate subagents per file and link the implementation as citations in the specification"
3. Once you have that - within the same repo run a Ralph loop to create a TODO file and then execute a classic ralph - doing just one thing and the most important thing per loop. Remind the agent that it can study the specifications and follow the citations to reference source code.
4. For best outcomes you wanna configure your target language to have strict compilation

The key theory here is usage of citations in the specifications which tease the file_read tool to study the original implementation during stage 3. Reducing stage 1 and stage 2 to specs is the precursor which transforms a code base into high level PRDs without coupling the implementation from the source language.
