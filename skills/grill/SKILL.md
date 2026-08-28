---
name: grill
description: Relentless interview to lock a plan. Use when you say grill this, stress-test the plan, or a design has unmade forks. User-invoked. Do not grill after you already said build it.
---

# grill

One question at a time. Recommended answer first. Read the repo before asking.

## When

you want a plan sharpened. New product surface, a fork that is expensive to undo, or "is this the right cut?"

**Do not grill** when you already ordered a build. That's `tdd` / implement.

## Loop

1. Name the decision tree in one sentence.
2. Ask the highest-leverage unresolved branch. Format:

> **Q:** …
> **Pick B.** Because …
> A) …
> B) … (recommended)
> C) …

3. After you answer, lock it. Next branch. Don't re-ask.
4. Prefer reading the codebase over asking what the file already says.
5. Stop when every branch is resolved or you say lock it. Write the decisions into the plan file or `~/.norstack/handoffs/`.

## Operator overlays

- Detect the project (`profile`). Grill a tool like a tool, an agency like an agency, a money product like money.
- No "should I continue?" The grill *is* the questions. When the tree is done, stop and write.
- Max ~8 questions unless you want more. Don't interview them to death.

## Output

A short locked plan: decisions, rejected forks, next command (`tdd`, `ship`, `portrait`, …).
