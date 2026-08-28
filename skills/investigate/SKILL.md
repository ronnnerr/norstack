---
name: investigate
description: Root cause investigation for a bug that survived a first fix. Use when the obvious fix did not hold, or the failure is intermittent.
---

# investigate

Follow Superpowers `systematic-debugging` exactly:

`~/.claude/plugins/cache/claude-plugins-official/superpowers/6.1.1/skills/systematic-debugging/SKILL.md`

Operator overlays:

1. Reproduce first. If it's a site, `browse` it. If it's a video render, `ffprobe` + `video peek` the output. If it is a data job, read the log and the data files rather than narrating.
2. One root cause, then the fix. No shotgun.
3. After the fix, prove it with the same repro. Then stop.
4. If you find a durable quirk, append `~/.norstack/learnings/learnings.jsonl`.
