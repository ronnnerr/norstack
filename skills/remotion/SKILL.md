---
name: remotion
description: Programmatic React video. Use for Remotion overlays, motion graphics, or a React composition rendered to mp4. Generated motion only, footage stays with video and portrait.
---

# remotion

Footage → `video` / `portrait`. This is for **generated** motion in React.

## Slot

Never at repo root. Always:

`<videos_dir>/edit/animations/slot_<id>/`

Scaffold there. Render to `render.mp4`. Point the EDL overlay at that file.

## Laws

- `durationInFrames` is truth. Don't guess seconds in CSS.
- `interpolate` / `spring`. No linear. No layout animation (top/left/width).
- `Sequence` + `AbsoluteFill`. One idea per composition.
- Preload fonts and audio. A missing font is a re-render.
- `fps` matches the parent (24 film, 30 social) unless you said otherwise.
- Transparent overlay → ProRes 4444 or WebM with alpha. Confirm before you pick.

## After render

```bash
ffprobe render.mp4
# then peek / see the output frames
```

Hard video rules still apply: overlay PTS shift, subtitles last, 30ms audio fades on the parent cut.

## Venture

Palette from `profile` and `taste`. Each project has its own palette. No leftover orange launch-video kit.

Don't ask questions inside a slot agent. Pick the obvious and render.
