---
name: clip
description: One-shot social video from a talking-head take. Use when you drop raw footage and want a finished, cropped, branded clip back.
---

# clip

Detect the project from the folder and filename.

- else ask one word: which brand?

Then:

1. `norstack video portrait VIDEO -o OUT.mp4` with that venture's logo if one exists under `~/norstack/brands/`
2. Read 5 output frames. The pan must be smooth (every-frame + damped). Jumpy = re-render.
3. Hand back the file path.

`video` is the deeper editor. `post` adds thumb + caption. `shorts` is multi-clip from a long source.
