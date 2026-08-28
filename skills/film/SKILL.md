---
name: film
description: Assemble a finished film from parts. Use when matting a character to PNG, ingesting a voice take, writing shots.json, or checking the episode inbox. Seeing raw footage is video. Writing the words is script.
---

# film

The missing factory. CLI lives on `norstack film`.

```
norstack film matte ~/norstack/brands/channel/character -o ~/norstack/brands/channel/character
norstack film voice TAKE.wav --out <videos_dir>/edit
norstack film assemble <videos_dir>/edit/shots.json -o <videos_dir>/edit/preview.mp4
norstack film inbox set --episode 1134 --title "..." --angle "..."
norstack film inbox show
norstack film drop
norstack thumb --title "YOU ARE" --accent "BARGAINING" --look explainer -o edit/thumb.png
norstack card --author Wilson --year 2014 --finding "..." -o edit/cards/01.png
```

Drop folder is `~/Media/norstack/drop`. `film drop` classifies: wav is a voice take, mp4 while the inbox is waiting is an episode file.

## Narrated film

1. `script`, then you record.
2. `film voice` your take → `shots.json` + transcript.
3. Agent fills titles / receipts on the skeleton. Do not invent a VO.
4. `film assemble`. Then `video` `see` the preview.

## Episode workflow

1. Name the episode. `film inbox set`. Stop.
2. You drop the file.
3. `video` `see` it. Write `shots.json` (CLIP rows from your file + TITLE/DIAGRAM).
4. Generate AI VO, set `voice` in shots.json.
5. `film assemble`. `publish` the package.

## Shots

`edit/shots.json`. Types: TITLE, HOST_VOID, HOST_SET, DIAGRAM, EVIDENCE, CLIP.

CLIP is only from a path you dropped. Character PNGs from `film matte`.
