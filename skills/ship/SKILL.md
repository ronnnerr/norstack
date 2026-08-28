---
name: ship
description: Ship the work. Use when you say ship, PR, push, deploy, or land it. Runs the gates before anything leaves your machine.
---

# ship


## Gates

1. Tests or a real verification command. No "looks good."
2. If the change is a site or UI, `browse` it.
3. If the change is video, inspect the output frames.
4. Don't force-push. Don't skip hooks.
5. Trading / live money / client publish: stop and confirm.

## Voice

PR titles name the user-visible change. No conventional-commit theater unless the repo already uses it.

## After

Report: branch, PR URL or commit, what was verified, what was not.
