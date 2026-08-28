---
name: hyperframes
description: HTML/CSS/GSAP video compositions. Use for UI motion, kinetic type, product mockups-to-video, transparent overlays. Isolated slot. Not footage editing.
---

# hyperframes

When the motion should be authored like a web page, not a React tree. Remotion if the motion is a React tree. This if HTML/GSAP is simpler.

## Slot

`<videos_dir>/edit/animations/slot_<id>/`

```bash
npx --yes hyperframes init . --example blank --non-interactive --skip-skills
# build the HTML composition
npx --yes hyperframes lint
npx --yes hyperframes validate
npx --yes hyperframes render . -o render.mp4
# alpha: --format webm -o render.webm
```

## Laws

- One composition, one payoff. Don't parallel-reveal two new things.
- Ease out cubic / expo. No bounce.
- Duration ≥ narration + 1s if it's over voice. Hold the last frame ≥ 1s.
- Deterministic. No network in the composition.
- Output path is absolute and unique. Parallel slots don't share filenames.

## After render

`ffprobe` + Read frames. Then the parent `video` compose (PTS shift, captions last).

Palette from `profile`. No marketplace default chrome.
