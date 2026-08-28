---
name: review
description: Review a diff or pull request. Use before merge, after a large change, or when you ask for a code review.
---

# review


## Look for

- Broken user path (then browse it if you can)
- Silent ffmpeg / video pipeline mistakes (double encode, subtitles under overlays, cuts mid-word)
- Invented trading numbers or leaked keys
- Privacy leaks: user content, local database paths, or tokens in logs
- AI slop UI
- Tests that don't test the change

## Don't

- Nitpick style that the repo already uses
- Demand a rewrite when a small fix is enough
- Approve without reading the diff
