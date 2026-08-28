---
name: profile
description: |
  Your projects, brands, voice, and paths. Load this first in any session that
  produces something with a look or a voice: design, copy, video, thumbnails,
  scripts, ads, SEO. Other skills call it to answer "which project is this and
  what does it look like." Edit profile.md to make it yours.
metadata:
  version: "1.0.0"
---

# profile

Every skill that produces something visible needs to know which project it is
producing for. This is where that lives. Without it, agents default to the same
generic look for everything, which is how work starts to read as templated.

Read `profile.md` next to this file. If it is still the shipped template, say so
and ask which project this is instead of guessing.

## What it answers

- Which project is this? Where does its code live? What URL does it run at?
- What is its palette, type, and register?
- What must never appear in it?
- Which projects must never be blended?

## How other skills use it

| Skill | What it takes from here |
|---|---|
| `copy` `content` `seo` `ads` | register, audience, forbidden claims |
| `ui` `taste` | palette, type, spacing, anti-references |
| `thumb` `post` `publish` | channel identity, safe zones, end cards |
| `video` `portrait` `clip` `film` | brand marks, aspect, logo placement |
| `remotion` `hyperframes` | palette, fps |
| `qa` `browse` | local and production URLs |
| `grill` `react` `postgres` | what kind of product this is |

## Rules

Isolation is the point. One project's palette does not travel to another. A client
gets their brand, not yours. If a request spans two projects, ask which one wins
before producing anything.

Do not invent a brand value that is not written down. An agent guessing a hex code
is how a design system rots.

If a project has ended, remove it. Ended work should not resurface in new drafts.

## Setup

Copy the template, then fill it in:

```bash
cp skills/profile/profile.example.md skills/profile/profile.md
```

`profile.md` is gitignored. It holds your projects, so it stays on your machine.
