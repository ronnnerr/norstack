---
name: tdd
description: Test driven development. Use when implementing a feature or bugfix. Write the failing test first, then the code that passes it.
---

# tdd

Red → green. One slice. Repeat. Superpowers TDD is allowed as backup. This is the daily loop.

## Before the first test

Write the **seams** (public boundaries) in one list. If the interface itself is the question, `grill` first.

## A test worth keeping

- Names a user-visible behavior: "user can export the cut"
- Hits a public seam, not a private method
- Expected value from the spec or a known literal, not from re-running the code

## Anti-patterns

- Mocks of internals. Breaks on refactor, not on behavior.
- Tautologies (`expect(add(a,b)).toBe(a+b)`).
- All tests first, then all code. That's a novel, not a loop.

## Loop

1. One failing test. Watch it fail for the right reason.
2. Minimum code to pass.
3. Next slice. Refactor is `review`, not this loop.

## Operator overlays

- Site behavior: after green, `browse` it.
- Video helpers: test the crop math and the pan cap, then look at a frame.
- Data products: tests must never invent records. Build fixtures from real shapes, anonymized.
- `verify` before you say done.
