---
name: thumb
description: Thumbnails and cover art. Use for a YouTube thumbnail, Shorts cover, title card, thumbnail text over a face or frame,.
---

# thumb

Type is code. Face or illustration is a picture. Do not ask an image model to spell the title.


## Sizes

| Use | Size |
|---|---|
| YouTube long | 1280×720 |
| Shorts / TikTok cover | 1080×1920 |

Safe: keep the 3–5 title words out of the bottom 28% and the YouTube timestamp corner.

## Recipe

1. **Line.** 3–5 words from the script's Thumb line. High contrast. No question unless the video answers it in 8 seconds. No "POV". No emoji.
2. **Picture.**
   - Talking-head: `see` + faces. Pick 3 frames where the face is large and looking. `peek` them full-res.
   - Explainer: generate one still from the locked style key. Cream paper, one figure, rust accent.
3. **Raster with the CLI.** No browse ritual.

```
norstack thumb --title "YOU ARE" --accent "BARGAINING" --look explainer -o edit/thumb-a.png
norstack thumb --title "YOU ARE" --accent "BARGAINING" --bg FRAME.jpg -o edit/thumb-b.png
```
4. Make 3 options (different crop or different 3-word line). **Read each PNG.** You pick.
5. If any letter is wrong, fix the HTML. Do not `image_edit` the type.

## Look

Talking-head: dark or muted, type-forward, one accent, the face is the product.
Explainer: flat ground, one grotesque, one accent word. It should look like the video.

Never carry one project's accent onto another. Palette comes from `profile`.

## Fail

A thumb you have not opened. Type from an image model. More than 6 words. A face with captions across the mouth.
