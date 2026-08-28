# norstack

Agent skills for solo operators who build, film, write, and ship in the same week.

Plain Markdown. No runtime, no build step, no dependencies. Every skill is one
`SKILL.md` an agent reads when the work matches. Works with any agent that supports
skills.

## Install

```bash
git clone https://github.com/ronnnerr/norstack.git ~/norstack
cd ~/norstack && ./install.sh
```

The installer symlinks `skills/` into `~/.claude/skills` and `~/.grok/skills`,
whichever exist. It backs up anything already sitting at those names into
`~/.norstack/backups/skills/` rather than overwriting it. Re-running is a no-op.

Then fill in your projects:

```bash
$EDITOR skills/profile/profile.md
```

That file is gitignored. It holds your project names, palettes, and paths, and it
stays on your machine.

## What is here

37 skills across the work a solo operator actually does.

| Slot | Skills |
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

Start with `norstack`. It indexes and routes to the rest.

## The idea

Most agent skill collections are a pile of prompts. This one has two opinions that
hold it together.

**Load the project before producing anything.** `profile` holds your projects,
palettes, registers, and paths. Skills that make something visible read it first.
Without that, agents produce the same generic look for every project, which is how
work starts reading as templated.

**Look at the output.** A transcript is not the video. Code that compiles is not a
working page. Skills here end by opening the page, reading the frame, or running the
test, and they say what they saw.

## humanizer

The one worth trying first if you only try one.

It rewrites AI-sounding prose without changing what it says. 37 signals across six
groups: manufactured significance and unnamed sources, verb avoidance and brochure
vocabulary, formatting tells, assistant residue, padding, and narrative structure.

The hard rule is that the pass changes how a draft reads and never what it says. No
invented number, no dropped claim. That constraint is what separates it from asking
a model to "make this sound more human," which reliably invents a statistic.

The taxonomy is informed by Wikipedia's
[Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
(WikiProject AI Cleanup, CC BY-SA), and by
[StoryScope](https://www.alphaxiv.org/abs/2604.03136) (arXiv 2604.03136) for the
narrative layer, which found AI fiction is detectable at 93.2% macro-F1 from plot
shape alone, with prose style contributing under 3%.

## Requirements

The Markdown skills need nothing. Some skills drive tools you supply yourself:

- `browse` `headed` `scrape` `qa` expect a headless Chromium CLI on your machine.
- `video` `portrait` `clip` `film` expect `ffmpeg` and `ffprobe`.
- `remotion` expects a Remotion project. `postgres` expects a database.

A skill tells you what is missing rather than guessing around it.

## Tests

```bash
python3 tests/test_skills.py
python3 tests/test_humanizer.py
```

Structural checks only: frontmatter is valid, skill names match directories, no
skill references one that does not exist, and `humanizer` does not violate its own
formatting rules.

## What is not here

This is the tool half of a larger personal stack. Project-specific skills, brand
kits, and business context are not published. `profile` is the seam where yours go.

## License

MIT. See [LICENSE](LICENSE).
