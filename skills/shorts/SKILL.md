---
name: shorts
description: Vertical shorts / Reels / TikToks from long-form. Use when you say shorts, Reels, TikToks, clip this, cut clips from this. Runs norstack video + face tracking first. Wraps vertical-shorts.
---

# shorts

Stock vertical-shorts assumed video-use's transcript-first doctrine. That is retired.

## Order

1. Run `~/norstack/skills/video/SKILL.md` through SEE (frames + faces + OCR). No exceptions.
2. Read annotated face frames. Name the format: solo talking-head / interview / screen-share.
3. If the channel, also load `channel`.
4. Then read `~/.claude/skills/vertical-shorts/SKILL.md` for crop/caption/card craft.
5. Crop from `vertical_crop` / primary face track in `faces.json`. Do not center-crop a talking head.
6. Render sequentially. See the output frames, including face boxes if people are on camera.

Helpers in vertical-shorts `scripts/` are still valid for cards and ASS captions. The *seeing* step is norstack's.
