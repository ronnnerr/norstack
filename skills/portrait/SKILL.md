---
name: portrait
description: Face-following 9:16 vertical crop. Use when you say portrait, vertical, shorts crop, track the face, keep the face centered, or add a logo.
---

# portrait


```bash
norstack video portrait VIDEO -o OUT.mp4 [--logo LOGO.png] [--cta CTA.mp4]
```

What it does:

1. YuNet every other frame
2. EMA-smoothed crop so the primary face stays centered
3. Scale to 1080×1920
4. Optional logo (top center)
5. Optional CTA concat

Then Read output frames. If the face drifts or the logo covers a face, say so and re-render. Do not ship a file you have not looked at.

Logo only if the project has a kit in `~/norstack/brands/<venture>/`. Ask once, then vendor it there.

The tracker samples **every frame**, then median + gaussian + a 90px/s pan cap. If a render still hops, that is a bug — say so and re-run. Do not ship jumpy files.
