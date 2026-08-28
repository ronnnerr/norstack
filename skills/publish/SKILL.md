---
name: publish
description: Preflight before anything goes out. Use when packaging a video or post to upload, writing titles, descriptions, chapters, or captions, or asking whether something is ready to post. Does not log into any platform.
---

# publish

Preflight. You upload. We do not hold platform passwords.

Detect the project (`profile`). Identify the project and the platform.

## Checklist

1. Open the file. `video` `see` the export if it is video. Read frames.
2. Rights: confirm you own or licensed every asset in the cut. If that is not true, stop.
3. Claims: no invented citations, income, or medical. Affiliate disclosed if Shop.
4. Package:
   - YouTube: title (from script), first 2 description lines = hook + promise, sources, chapters from `shots.json`
   - Shorts/TikTok: one line caption, no hashtag soup
   - 3 thumbs already picked
5. Run `humanizer` on every word that ships: title, description, caption, chapter
   names. It runs here, last, after the words are final. It may not add or drop a
   claim. If it wants to cut something to make a sentence read better, keep the
   claim and rewrite around it.
6. Hand back: mp4 path, thumb path, title, description, chapters. You post.

## Do not

- `yt-dlp` an upload
- Automate YouTube Studio / TikTok login
- Promise it will rank
