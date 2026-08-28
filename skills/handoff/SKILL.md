---
name: handoff
description: Compact the session so the next one can continue. Use when you say handoff, continue later, or switch models.
---

# handoff

Write a file the next session can read in one pass. No novel.

## Where

Prefer `~/.norstack/handoffs/<venture>-<YYYYMMDD>-<slug>.md`
If you are in a repo, also drop `HANDOFF.md` at the root only if you asked.

## Shape

```markdown
# Handoff — <venture> — <one line>

## Now
What is true. Branch, URLs, files touched, commands that work.

## Decisions
Locked calls only. Not options.

## Don't
Traps. Ended work. Secrets not to invent.

## Next
The first command. Not a menu.
```

After the file: 0–3 durable lessons.

```
norstack learn add --venture VENTURE --key short-kebab --insight "the lesson"
```

Skip trivia. Skip things already in `norstack learn search`.

## Rules

- Include file paths and the last verification command + its result.
- Include unmade forks as **open**, not as recommendations dressed as fact.
- Drop transcript fluff. Keep load-bearing numbers and names.
- project isolation. Do not mix one project's state into another project's handoff.
