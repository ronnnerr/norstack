---
name: explainer
description: Use when making a Trust Me Bro style the channel animation, 10-15 minute psychology explainer, evidence cards, or visuals for a script the operator will voice. the operator talks. The agent draws.
---

# explainer

10–15 min the channel film. **the operator is the voice. The agent is the picture.** Null is on screen. Sticker character + sets + receipts, not one long generated clip.

Style: `style.md`. Host: `~/norstack/brands/channel/character/`. Words: `script`.

## Division of labor

| Who | Does |
|---|---|
| Agent | research, `script.md`, `shots.md`, Null, diagrams, cards, assemble, thumb |
| the operator | records the script (wav / m4a / mov) and drops it |
| Agent | cuts every picture to **your** take |

Do not generate a voiceover for this channel. If you dropped a talking-head, strip the audio and use that.

## Why this shape

TMB *Would You Survive a Nuclear Blast?*: 20.6 min, 213 hard cuts. Reusable character + shot list. A new 10s AI clip per sentence drifts Null.

## Pipeline

1. Research. Every number gets a URL or DOI.
2. `script` → `script.md`. Hand back the script. **Stop until the voice file is in chat.**
3. Transcribe your take. Expand beats into `shots.md`. One row per picture. Target 5–8s. A 12 min film is ~100–140 shots.
4. Most shots are composites: Null pose + set + optional HTML card. Slight bob or push-in. Do not regenerate Null.
5. Hero motion (15–25 shots only): `image_edit` from `null-idle.jpg`, then `image_to_video` 6s. One action.
6. Evidence cards: `norstack card --author Wilson --year 2014 --finding "..." --venue Science -o edit/cards/01.png`. Type is code.
7. `ffmpeg` concat. 1280×720. Your audio is the bed.
8. `video` `see` the cut. If Null's head drifted, throw that shot out and composite.

## Shot types

| Type | When |
|---|---|
| TITLE | Black, 3–6 words, one rust word, Null peek. |
| HOST_VOID | Null on black. idle / point / shrug. |
| HOST_SET | Null in a 2D room we own. |
| DIAGRAM | Icons on black. The receipt is the picture. |
| EVIDENCE | HTML card, 2–4s. |
| BIT | 2–4s joke visual. Back to HOST. |

## Hard rules

- Your voice. Our drawings. No live face unless you asked for talking-head (`portrait`).
- No TMB frames. No other YouTuber's character.
- Load `channel`. Do not diagnose. Do not treat.
