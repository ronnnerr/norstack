---
name: humanizer
description: |
  Rewrite text so it reads like a person wrote it, without changing what it says.
  Run before delivering any human-facing prose: agency and client copy, landing
  pages, emails, video scripts, hooks, titles, descriptions, captions, READMEs,
  release notes, PR bodies. Use when someone says humanize this, this reads like
  AI, make it sound human, clean up the writing, or does this sound like a robot.
metadata:
  version: "1.0.0"
  norstack: true
---

# humanizer

Strip the machine cadence out of a draft. Keep every claim.

The pattern taxonomy below is norstack's own, informed by Wikipedia's
[Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
(WikiProject AI Cleanup, CC BY-SA) and by StoryScope, arXiv 2604.03136, for the
narrative layer in §F.

## The one hard rule

The pass changes how a draft reads. It never changes what it says.

Do not add a fact, name, number, date, quote, citation, or ranking that is not in
the source. Do not drop a claim because it makes a sentence awkward. If a sentence
resists rewriting, restructure the paragraph around the claim. If a claim needs a
detail nobody supplied, ask for it or write the shorter true sentence.

Fiction is the only exemption. Invented detail is the job there.

## Modes

Pick by what you were handed.

**Pasted text.** Return the rewrite, then a short list of what you changed and
anything still weak. Show the work.

**File path.** Rewrite prose in place. Leave code blocks, frontmatter, data, config,
link targets, and command output exactly as they are. Report a two-line summary.

**Embedded.** Another skill called you for a title, caption, commit body, or PR
description. Return the finished text alone. No commentary, no preamble.

## The pass

1. Read the source. Mark every signal from §A through §F.
2. Rewrite whole. Do not patch flagged phrases one at a time, that leaves a draft
   that reads like it was edited by a machine to sound less like a machine.
3. Read it back and ask two questions:
   - What still sounds generated?
   - Did anything get added or lost?
4. Fix what those two questions surface. Then check §C1 for stray dashes.

Step 2 is where most passes fail. A phrase-level patch keeps the underlying rhythm.
Rebuild the paragraph.

## §A Claims and sourcing

**A1. Manufactured significance.** Ordinary facts described as turning points,
legacies, or evidence of a broader shift. Watch: marks a pivotal moment, stands as
a testament, underscores the importance of, reflects a broader, cements its place,
a defining chapter.

- Before: The agency opened a second office in 2023, marking a pivotal moment in its
  evolution and underscoring its commitment to regional growth.
- After: The agency opened a second office in 2023.

**A2. Unnamed authorities.** A claim handed to experts, observers, critics, or
studies that are never named. Either name the real source or cut the claim. Never
invent one.

- Before: Industry experts agree that short-form video drives the strongest returns.
- After: Cut it, or cite the actual report and its number.

**A3. Credential padding.** Logo lists and follower counts standing in for a reason
to care. Keep a citation that carries information. Drop the ones that only signal.

**A4. Filled gaps.** The model could not find something, said so, then guessed
anyway. Watch: while details are limited, based on available information, likely
began, it is believed that, appears to have. State what the source does not show,
or cut the sentence. A guess presented as a fact is the worst failure mode here.

**A5. Stacked hedges.** Qualifiers piled until nothing is claimed. "It could
potentially be argued that this may have some effect" is one uncertain claim wearing
four hedges. Keep the hedge the evidence supports. Delete the rest.

## §B Verbs and sentence shape

**B1. Verb avoidance.** *Serves as, stands as, represents, features, boasts,
offers* where *is* and *has* would do.

- Before: The dashboard serves as a central hub and features four distinct views.
- After: The dashboard is the central hub. It has four views.

**B2. Brochure vocabulary.** vibrant, robust, seamless, nestled, breathtaking,
renowned, must-have, stunning, groundbreaking, rich (figurative), in the heart of.
Also the reliable tells: delve, crucial, pivotal, comprehensive, testament,
tapestry, landscape (abstract), showcase, underscore, foster, garner, interplay,
intricate, quietly, enduring.

**B3. The -ing tail.** A participle clause bolted on to make a plain fact sound
analyzed. Watch: highlighting, reflecting, symbolizing, ensuring, showcasing,
fostering, contributing to, underscoring.

- Before: The page loads in under a second, reflecting the team's commitment to
  performance.
- After: The page loads in under a second.

**B4. Not X but Y.** "It's not just a tool, it's a workflow." Also the clipped
negative tail: ", no guesswork", ", no setup required". State the thing.

- Before: The importer maps columns automatically, no manual mapping.
- After: The importer maps the columns for you.

**B5. Forced triads.** Three items because three sounds finished, not because there
are three. Use the number the meaning needs. Two is allowed. So is four.

**B6. Fake ranges.** "From X to Y" where X and Y are not ends of any spectrum.
"Everything from onboarding to dark mode" is a list wearing a range. Just list them.

**B7. Buried actors.** Passive voice or a dropped subject hiding who does what.
"The results are preserved automatically" leaves out what preserves them.

**B8. Synonym cycling and stuck openings.** Renaming one subject every sentence
(the founder, the entrepreneur, the executive) or starting five sentences with the
same subject. Fix the pattern, not the word. Merging two sentences usually solves it.
Deliberate anaphora for rhythm is not this.

## §C Format

**C1. Em and en dashes.** The output must contain no — and no –, and no spaced
hyphen or double hyphen standing in for one. Use a period, comma, colon, or
parentheses, or rewrite. Search the finished draft for both characters before
returning it. The only exception is a supplied voice sample that uses them, in which
case match the sample's rate.

**C2. Decorative bold.** Bold that marks no real emphasis, especially every term in
a sentence.

**C3. Bold-label lists.** Every bullet opening with **Label:** and a restatement.
Usually the list should be a paragraph. If it stays a list, the items should carry
information, not headings.

**C4. Title Case Headings.** Sentence case.

**C5. Emoji as decoration.** Rocket next to Launch, bulb next to Insight. Cut them.

**C6. Curly quotes** where the target format wants straight ones. Low signal alone,
a tell when stacked.

**C7. Hyphen spray.** data-driven, cross-functional, end-to-end, high-quality on
every noun. Keep the hyphen before a noun, drop it after: *a high-quality export*,
*the export is high quality*.

## §D Assistant residue

**D1. Chat wrapper left in.** Of course, Certainly, I hope this helps, Let me know
if, Would you like me to, Here is a. Delete outright.

**D2. Praise before answer.** Great question, You're absolutely right, That's an
excellent point. Answer the question.

**D3. Training-date disclaimers.** As of my last update, up to my knowledge cutoff.
These do not belong in delivered prose.

## §E Padding and staging

**E1. Filler phrases.** in order to → to. due to the fact that → because. at this
point in time → now. has the ability to → can. it is important to note that → cut it.

**E2. Announcing the next point.** Let's dive in, here's what you need to know,
let's break this down, without further ado. Casual versions count: "the part that
tripped me up was". Say the thing instead of introducing it.

**E3. Fake candor.** Honestly?, Look,, Here's the thing, Let's be honest, Real talk,
used as a staged pause before an ordinary point. Mid-sentence *honestly* is normal
speech and is fine.

**E4. False depth.** The real question is, at its core, fundamentally, what really
matters, the deeper issue. These dress an ordinary claim as a revelation.

**E5. Aphorism.** "X is the language of Y." "Speed is the currency of trust."
Sounds quotable, says nothing. Replace with the specific claim.

**E6. Heading echo.** A heading followed by a sentence that restates the heading.
Delete the sentence.

**E7. Manufactured stakes.** A run of dramatic fragments. "Then everything changed.
No warnings. No rollback. Just silence." One short sentence lands. Five in a row is
a tic.

**E8. Optimistic sign-off.** A closing paragraph of vague forward-looking warmth.
End on the last real fact.

**E9. Phantom objections.** Answering something nobody raised: To be clear, Don't
get me wrong, I'm not saying, This isn't really about. Also phantom alternatives:
"A tempting approach would be X, but", where X is something no reader considered and
the text never mentions again. Both are usually fossils of an earlier draft. Cut
them and state the constraint directly.

**E10. Version archaeology.** Docs describing what the code used to do. Describe
current behavior. Previous versions belong in changelogs and migration guides.

## §F Structure (narrative work only)

Applies to scripts, story videos, recaps, and long-form narrative. Skip it for
landing pages, docs, and reference prose. Sentence-level fixes do not touch these,
they survive a clean §A through §E pass.

Grounding: StoryScope (arXiv 2604.03136) scored 61,608 stories across ten narrative
dimensions and separated human from AI at 93.2% macro-F1 using narrative shape alone.
Adding prose style back improved it by under 3%. The structure carries the signal.

**F1. Self-explaining theme.** The narration states the meaning instead of letting
events carry it. Cut the line that explains the point. If the point does not survive,
the events are too thin, so fix the events, not the line.

**F2. Single clean track.** One plot line, everything resolved, nothing left hanging.
Real narrative carries a thread that does not close and a detail that mattered less
than it first seemed.

**F3. Costless choices.** The protagonist is never wrong in a way that stands. Human
narrative frames choices as compromised or expensive.

**F4. Flat chronology.** Events in the order they happened, every time. Straight
order is not always wrong. Being the only structure available is the tell.

Fix §F by changing structure, not sentences. Do not invent events to add tension. If
the source has no real tension, say so rather than manufacturing it. §F never
overrides the hard rule.

## Do not flag

These are not evidence on their own. Flag only when several stack.

Clean grammar. Formal vocabulary. One *however*. One em dash in a writer who uses
them. Curly quotes from a word processor. A single short sentence for emphasis.
Deliberate repetition for rhythm. Real scope notes, safety text, and legal
disclaimers. Real alternatives weighed in a design doc. Missing citations, most
writing has none. Clean formatting from a template. A letter-style greeting or
sign-off.

Never rewrite a watched phrase that sits inside a quotation, a title, a proper name,
or an example being discussed rather than used.

## Keep the human residue

Protect these. They are usually the only reason a draft sounds like someone.

Oddly specific detail. Mixed feelings that never resolve. Dated slang and references
that pin a year. Sentence length that varies hard. Genuine asides and mid-sentence
self-correction. A word the writer would defend if asked.

## Voice matching

A supplied writing sample outranks every rule above, including §C1.

Read the sample first. Measure sentence length, opening habits, punctuation rate,
contractions, profanity, repeated constructions, and the transitions actually used.
Then match that rate. Do not formalize casual writing and do not sand off a quirk
that appears more than once, that quirk is the voice.

With no sample, use the operator's default register: direct, concrete, short
paragraphs, named specifics, ending on the last real fact.

## Route

| Draft | Pass |
|---|---|
| Client copy, landing page, proposal | §A to §E |
| Email, DM, outreach | §A to §E |
| Video script, hook, cold open | §A to §F |
| Story video, recap, narration | §A to §F |
| Video title, description, chapters | §A to §E |
| Short-form caption | §A to §E, keep it tight, no hashtag padding |
| README, docs, release notes | §A to §E, stay neutral and plain |
| PR body, commit body | §A to §E |
| Commit subject line | skip |
| Code, config, data, logs, test output | skip |
| Text the operator wrote | skip unless asked |

## Order of operations

Drafting skill writes it. `humanizer` passes it. `publish` preflights it.

Do not run the pass on an unfinished draft. Do not let the pass invent a number to
smooth a sentence, that is the one failure this skill exists to prevent.
