# i ran Claude in a loop for three months, and it created a genz programming language called cursed

**Author:** Geoffrey Huntley  
**Source:** https://ghuntley.com/cursed/  
**Category:** Vibe Coding  
**Date:** ~Sep 2025  

---

It's a strange feeling knowing that you can create anything, and I'm starting to wonder if there's a seventh stage to the "people stages of AI adoption by software developers" whereby that seventh stage is essentially this scene in the matrix...

It's where you deeply understand that 'you can now do anything' and just start doing it because it's possible and fun, and doing so is faster than explaining yourself. Outcomes speak louder than words.

There's a falsehood that AI results in SWE's skill atrophy, and there's no learning potential.

> If you're using AI only to "do" and not "learn", you are missing out
> - David Fowler

I've never written a compiler, yet I've always wanted to do one, so I've been working on one for the last three months by running Claude in a while true loop (aka "Ralph Wiggum") with a simple prompt:

> Hey, can you make me a programming language like Golang but all the lexical keywords are swapped so they're Gen Z slang?

Why? I really don't know. But it exists. And it produces compiled programs. During this period, Claude was able to implement anything that Claude desired.

The programming language is called "cursed". It's cursed in its lexical structure, it's cursed in how it was built, it's cursed that this is possible, it's cursed in how cheap this was, and it's cursed through how many times I've sworn at Claude.

- https://cursed-lang.org/
- https://github.com/ghuntley/cursed

For the last three months, Claude has been running in this loop with a single goal:

> "Produce me a Gen-Z compiler, and you can implement anything you like."

## What's included?

Anything that Claude thought was appropriate to add. Currently...

- The compiler has two modes: interpreted mode and compiled mode. It's able to produce binaries on Mac OS, Linux, and Windows via LLVM.
- There are some half-completed VSCode, Emacs, and Vim editor extensions, and a Treesitter grammar.
- A whole bunch of really wild and incomplete standard library packages.

## Lexical structure

**Control Flow:**
- `ready` → if
- `otherwise` → else
- `bestie` → for
- `periodt` → while
- `vibe_check` → switch
- `mood` → case
- `basic` → default

**Declaration:**
- `vibe` → package
- `yeet` → import
- `slay` → func
- `sus` → var
- `facts` → const
- `be_like` → type
- `squad` → struct

**Flow Control:**
- `damn` → return
- `ghosted` → break
- `simp` → continue
- `later` → defer
- `stan` → go
- `flex` → range

**Values & Types:**
- `based` → true
- `cringe` → false
- `nah` → nil
- `normie` → int
- `tea` → string
- `drip` → float
- `lit` → bool
- `ඞT` (Amogus) → pointer to type T

**Comments:**
- `fr fr` → line comment
- `no cap...on god` → block comment

## Example program

Here is leetcode 104 - maximum depth for a binary tree:

```
vibe main
yeet "vibez"
yeet "mathz"

struct TreeNode {
    sus val normie
    sus left ඞTreeNode
    sus right ඞTreeNode
}

slay max_depth(root ඞTreeNode) normie {
    ready (root == null) {
        damn 0
    }
    sus left_depth normie = max_depth(root.left)
    sus right_depth normie = max_depth(root.right)
    damn 1 + mathz.max(left_depth, right_depth)
}

slay main_character() {
    test_maximum_depth()
}
```

If this is your sort of chaotic vibe, and you'd like to turn this into the dogecoin of programming languages, head on over to GitHub and run a few more Claude code loops with the following prompt.

> study specs/* to learn about the programming language. When authoring the cursed standard library think extra extra hard as the CURSED programming language is not in your training data set and may be invalid. Come up with a plan to implement XYZ as markdown then do it

There is no roadmap; the roadmap is whatever the community decides to ship from this point forward.

At this point, I'm pretty much convinced that any problems found in cursed can be solved by just running more Ralph loops by skilled operators (ie. people *with* experience with compilers who shape it through prompts from their expertise vs letting Claude just rip unattended). There's still a lot to be fixed, happy to take pull-requests.

The most high-IQ thing is perhaps the most low-IQ thing: run an agent in a loop.

LLMs amplify the skills that developers already have and enable people to do things where they don't have that expertise yet.

Success is defined as cursed ending up in the Stack Overflow developer survey as either the "most loved" or "most hated" programming language, and continuing the work to bootstrap the compiler to be written in cursed itself.

ps. socials:

- X - https://x.com/GeoffreyHuntley/status/1965258228314636524
- Discord - https://discord.gg/CRbJcKaGNT
