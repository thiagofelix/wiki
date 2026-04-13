# don't waste your back pressure

**Author:** Geoffrey Huntley  
**Source:** https://ghuntley.com/pressure/  
**Category:** AI  
**Date:** ~Jan/Feb 2026  

---

I am fortunate to be surrounded by folks who listen and the link below post will go down as a seminal reading for people interested in AI context engineering.

A simple convo between mates - well Moss translated it into words and I've been waiting for it to come out so I didn't front run him.

Enjoy. This is what engineering now looks like in the post loom/gastown era or even when doing ralph loops.

If you aren't capturing your back-pressure then you are failing as a software engineer.

Back-pressure is part art, part engineering and a whole bung of performance engineering as you need "just enough" to reject invalid generations (aka "hallucinations") but if the wheel spins too slow ("tests take a long time to run or for the application to compile") then it's too much resistance.

There are many ways to tune back-pressure and as Moss states it starts with choice of programming language, applying engineering knowledge to design a fast test suite that provides signal but perhaps my favorite one is `pre-commit` hooks (aka prek).

Under normal circumstances pre-commit hooks are annoying because they slow down humans but now that humans aren't the ones doing the software development it really doesn't matter anymore.
