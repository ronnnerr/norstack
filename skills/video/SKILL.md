---
name: video
description: "your video stack. Use for any video: watch, understand, cut, grade, captions, shorts, 'what's in this clip', quality check a render. Replaces video-use. You MUST extract and look at frames. Transcript-only editing is a failure."
---

# video

Stock video-use cannot see. It transcribes, reasons from text, and only peeks at a filmstrip at decision points. That is why it was bad.

norstack inverts the pipeline: **see first, hear second, cut third.**

Helpers live in `~/norstack/video/helpers/`. CLI: `norstack video <cmd>`.

Portrait / face-follow (every frame, damped pan):

```bash
norstack video portrait VIDEO -o OUT.mp4 [--logo LOGO.png]
```

Then Read frames of the **output**, not just the source. Jumpy pan = bug. Re-render.

```
<videos_dir>/
  <sources, never overwrite>
  edit/
    visual_index.json      machine index
    visual_index.md        human/agent reading view
    seeing.md              visual + speech aligned (after pack)
    frames/                extracted jpgs — READ THESE
    transcripts/
    takes_packed.md
    edl.json
    animations/
    preview.mp4
    final.mp4
    project.md
```

## Hard rules

Production correctness (keep these even when inventing):

1. Subtitles LAST in the filter chain.
2. Per-segment extract → lossless concat. No single-pass filtergraph when overlays exist.
3. 30ms audio fades at every segment boundary.
4. Overlay `setpts=PTS-STARTPTS+T/TB`.
5. Master SRT uses output-timeline offsets.
6. Never cut inside a word if a word-level transcript exists. Snap to word boundaries.
7. Pad cut edges 30–200ms.
8. Cache transcripts and the visual index per source file mtime. Don't redo unless the file changed.
9. All outputs in `<videos_dir>/edit/`.
10. **You must Read real frame images before describing or cutting the video.** Filmstrip optional. Individual frames required. If you have not opened at least the MUST_READ frames from `see.py`, you have not seen the video.

## Process

### 0. Paths

```bash
HELPERS="$HOME/norstack/video/helpers"
PY=python3
# videos_dir = directory containing the source(s)
# edit = $videos_dir/edit
mkdir -p "$edit/frames"
```

### 1. SEE — never skip

```bash
$PY "$HELPERS/see.py" /path/to/source.mp4 --out "$edit"
```

This writes `visual_index.md`, `visual_index.json`, `faces.json`, and `frames/` (plus `frames/*/annotated/` with boxes and F-ids).

Then **Read** every path listed under `MUST_READ`. Prefer the annotated face frames when they exist. That is the model using its eyes.

If the clip has a person and `faces` reports 0 tracks, say so. Do not pretend you tracked a face.

If the user pointed at a specific moment, also:

```bash
$PY "$HELPERS/peek.py" /path/to/source.mp4 START END --out "$edit/peek" --n 8
```

Read those frames too.

Write 4–8 sentences of what you actually saw: who is on camera (F1, F2…), whether they look at lens, framing, on-screen text, jump cuts already in the source, garbage frames, brand colors, talking-head vs screen vs B-roll. If you cannot say what the picture looks like, you cheated. Go back.

### 2. HEAR — optional until you need cuts on speech

```bash
$PY "$HELPERS/transcribe.py" /path/to/source.mp4 --out "$edit"
$PY "$HELPERS/pack.py" --edit-dir "$edit"
```

Read `seeing.md` (aligned visual + speech). `takes_packed.md` is speech only — never sufficient alone.

If transcription is unavailable, continue on the visual index. Say so. Do not invent dialogue.

### 3. TALK

Describe the material in plain English from what you *saw* and *heard*. Ask only what the pictures don't answer: target length, platform, what must stay, what must die, captions or not.

### 4. STRATEGY

4–8 sentences. Wait for confirmation if you are choosing among looks. If you already said "just cut the ums and make it tight," don't workshop a treatment.

### 5. CUT

Write `edl.json`. Drill with `peek.py` at every ambiguous cut (±1.5s). Read those frames.

```json
{
  "version": 1,
  "sources": {"TAKE": "/abs/path.mp4"},
  "ranges": [
    {"source": "TAKE", "start": 2.42, "end": 6.85, "beat": "HOOK", "quote": "...", "reason": "..."}
  ],
  "grade": "none",
  "overlays": [],
  "subtitles": null,
  "total_duration_s": 0
}
```

### 6. RENDER

```bash
$PY "$HELPERS/render.py" "$edit/edl.json" -o "$edit/preview.mp4" --preview
```

Then see the *output*:

```bash
$PY "$HELPERS/see.py" "$edit/preview.mp4" --out "$edit/verify" --max-read 12
```

Read the verify MUST_READ frames. Check jump cuts, black frames, captions covering faces, grade wrecking skin.

Cap 3 self-eval loops. Then show the user.

### 7. FINAL

On confirmation, render without `--preview`. Append `edit/project.md`.

## When you say "what's in this video?"

Stop after step 1–2. Answer from frames + OCR + transcript. This is the common case stock video-use failed.

## Animations

One sub-agent per slot, parallel. Pick the engine: `remotion` if React, `hyperframes` if HTML/GSAP, Manim for diagrams, PIL for simple cards. Palette from the frames you saw and from `profile`. Never the old orange launch-video kit.

## Downloads

If the source is a URL and `yt-dlp` is missing, say so. Don't pretend you watched a YouTube page.

## Do not

- Reason from the packed transcript alone
- Call `timeline.py` a substitute for Reading frames
- Skip `see.py` because "it's a talking head"
- Use stock `~/.claude/skills/video-use` or `~/Developer/video-use/SKILL.md` as the process
