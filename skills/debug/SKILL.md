---
name: debug
description: Systematic debugging for the operator. Use when something is broken, a test fails, or behavior is unexpected. Native norstack. Do not guess-and-patch.
---

# debug

1. Reproduce. Site → `browse`. Video → `ffprobe` + `peek` the output. pred → logs and data files.
2. One root cause, then the fix.
3. Prove it with the same repro.
4. Superpowers `systematic-debugging` is allowed as a deeper reference. Do not run gstack investigate preambles.
