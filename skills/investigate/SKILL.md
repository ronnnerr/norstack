---
name: investigate
description: Systematic debugging for the operator. Use when something is broken, a test fails, a 500 happens, or behavior is unexpected. Do not guess-and-patch.
---

# investigate

Follow Superpowers `systematic-debugging` exactly:

`~/.claude/plugins/cache/claude-plugins-official/superpowers/6.1.1/skills/systematic-debugging/SKILL.md`

Operator overlays:

1. Reproduce first. If it's a site, `browse` it. If it's a video render, `ffprobe` + `video peek` the output. If it's pred, read the log and the data files, don't narrate.
2. One root cause, then the fix. No shotgun.
3. After the fix, prove it with the same repro. Then stop.
4. If you find a durable quirk, append `~/.norstack/learnings/learnings.jsonl`.
