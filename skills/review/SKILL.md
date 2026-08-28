---
name: review
description: Review a diff or PR for the operator. Use before merge, after a big change, or when you ask for a code review.
---

# review

If `~/.claude/skills/gstack/review/SKILL.md` exists, use its checklists as a reference. Write findings in your voice.

## Look for

- Broken user path (then browse it if you can)
- Silent ffmpeg / video pipeline mistakes (double encode, subtitles under overlays, cuts mid-word)
- Invented trading numbers or leaked keys
- the desktop app privacy leaks (journals, local db paths in logs)
- AI slop UI
- Tests that don't test the change

## Don't

- Nitpick style that the repo already uses
- Demand a rewrite when a small fix is enough
- Approve without reading the diff
