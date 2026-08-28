---
name: norstack
description: |
  Index and router for the norstack skill suite. Load at the start of a session,
  when someone says norstack, or when deciding which skill handles a request
  across browsing, video, design, writing, and shipping.
metadata:
  version: "1.0.0"
---

# norstack

A suite of agent skills for solo operators who build, film, write, and ship in the
same week. Plain Markdown, no runtime, no build step.

Load `profile` before anything that has a look or a voice.

## Suite

| Slot | Skill |
|---|---|
| Identity | `norstack` `profile` |
| Browser | `browse` `headed` `scrape` `qa` |
| Video | `video` `portrait` `clip` `post` `hook` `thumb` `shorts` `film` |
| Writing | `script` `explainer` `copy` `content` `humanizer` |
| Marketing | `seo` `ads` |
| Design | `ui` `taste` |
| Motion | `remotion` `hyperframes` |
| App and data | `react` `postgres` |
| Process | `grill` `handoff` `tdd` `debug` `investigate` `verify` `review` `ship` |
| Security | `secure` |
| Release | `publish` |

## Route

| Request | Skill |
|---|---|
| Open, test, or screenshot a URL | `browse` |
| Watch the browser, solve a CAPTCHA, log in | `headed` |
| Pull data off a page | `scrape` |
| Does this work? find bugs on a URL | `qa` |
| What is in this footage? | `video` |
| Vertical crop, track the face | `portrait` |
| Package a clip to post | `post` or `clip` |
| First three seconds | `hook` |
| Thumbnail or cover | `thumb` |
| Write the script or the hook line | `script` |
| Animated explainer, evidence cards | `explainer` |
| Assemble the film | `film` |
| Write the page | `copy` |
| What should we publish | `content` |
| This reads like AI | `humanizer` |
| Not ranking | `seo` |
| Paid media, ROAS, CPA | `ads` |
| Interface craft | `ui`, then `taste` |
| Motion in React | `remotion` |
| Motion in HTML and GSAP | `hyperframes` |
| Next, React, bundle, waterfall | `react` |
| SQL, RLS, migration, slow query | `postgres` |
| Stress-test a plan | `grill` |
| Continue in a new session | `handoff` |
| Red, green, refactor | `tdd` |
| Something is broken | `debug` or `investigate` |
| Is it done? | `verify` |
| Review the diff | `review` |
| Ship it | `ship` |
| Security audit | `secure` |
| Ready to post? | `publish` |

## Rules

1. Load `profile` before producing anything with a look or a voice. Do not guess a
   palette or a register.
2. Project isolation. One project's identity does not travel to another. A client
   gets their brand.
3. See the thing. Browse the site before claiming it works. Look at the frames
   before claiming you understand the footage. A transcript is not the video.
4. Build the first complete cut, then report. Do not stop halfway to ask whether to
   continue.
5. Human-facing prose runs `humanizer` before delivery. It runs last, after the
   drafting skill and before `publish`. It changes how a draft reads, never what it
   says.
6. Evidence closes a task. A command that ran, a frame that was looked at, a page
   that was opened, a test that passed.

## Layout

```
skills/<name>/SKILL.md    one skill, plain Markdown
skills/profile/           your projects, gitignored
install.sh                symlinks skills into your agent's skills directory
tests/                    structural checks
```
