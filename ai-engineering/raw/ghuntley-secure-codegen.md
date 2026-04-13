# anti-patterns and patterns for achieving secure generation of code via AI

**Author:** Geoffrey Huntley  
**Source:** https://ghuntley.com/secure-codegen/  
**Category:** AI  
**Date:** ~Sep 2025  

---

I just finished up a phone call with a "stealth startup" that was pitching an idea that agents could generate code securely via an MCP server. Needless to say, the phone call did not go well. What follows is a recap of the conversation where I just shot down the idea and wrapped up the call early because it's a bad idea.

> If anyone pitches you on the idea that you can achieve secure code generation via an MCP tool or Cursor rules, run, don't walk.

Over the last nine months, I've written about the changes that are coming to our industry, where we're entering an arena where most of the code going forward is not going to be written by hand, but instead by agents.

I haven't written code by hand for nine months. I've generated, read, and reviewed a lot of code, and I think perhaps within the next year, the large swaths of code in business will no longer be artisanal hand-crafted. Those days are fast coming to a close.

Thus, naturally, there is a question that's on everyone's mind:

> How do I make the agent generate secure code?

Let's start with what you should not do and build up from first principles.
