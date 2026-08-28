---
name: shorts
description: Cut vertical shorts from long-form footage. Use for Reels, TikToks, and YouTube Shorts pulled out of a podcast, interview, talk, or screen recording.
---

# shorts


## Order

1. Run `~/norstack/skills/video/SKILL.md` through SEE (frames + faces + OCR). No exceptions.
2. Read annotated face frames. Name the format: solo talking-head / interview / screen-share.
3. Load `profile` for the channel's identity.
5. Crop from `vertical_crop` / primary face track in `faces.json`. Do not center-crop a talking head.
6. Render sequentially. See the output frames, including face boxes if people are on camera.

