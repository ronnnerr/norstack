#!/usr/bin/env python3
"""Structural checks on the humanizer skill, plus a fixture the pass must satisfy."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "humanizer" / "SKILL.md"

SECTIONS = ["§A", "§B", "§C", "§D", "§E", "§F"]

# A rewrite of the fixture must kill every pattern on the left and keep every
# fact on the right. Used by hand when changing the skill; see docstring above.
MUST_DIE = [
    r"pivotal moment", r"experts agree", r"not extensively documented",
    r"serves as", r"boasts", r"vibrant", r"seamless", r"nestled",
    r"showcas", r"not just a", r"Everything from", r"—", r"–",
    r"I hope this helps", r"Let's dive", r"future looks bright",
]
MUST_LIVE = [
    "2.4 seconds", "310 milliseconds", "ClickHouse", "March 2025",
    "Kestrel", "Vantage", "Orbit Labs", "end-to-end encryption",
]


def main() -> int:
    text = SKILL.read_text(encoding="utf-8")

    assert text.startswith("---\n"), "SKILL.md must open with YAML frontmatter"
    assert "name: humanizer" in text, "frontmatter must declare name: humanizer"

    for s in SECTIONS:
        assert f"## {s}" in text, f"missing section {s}"

    signals = re.findall(r"^\*\*([A-F]\d+)\.", text, re.M)
    assert len(signals) == len(set(signals)), f"duplicate signal ids: {signals}"
    assert len(signals) >= 35, f"expected at least 35 signals, found {len(signals)}"

    # Every section must contribute at least one signal.
    for s in SECTIONS:
        letter = s[-1]
        assert any(sig.startswith(letter) for sig in signals), f"{s} has no signals"

    # Dogfood C1: the only dashes allowed are on the line that names the rule.
    offenders = [
        (i, ln) for i, ln in enumerate(text.splitlines(), 1)
        if ("—" in ln or "–" in ln) and "C1. Em and en dashes" not in ln
    ]
    assert not offenders, f"C1 violated in its own skill file: {offenders}"

    assert "CC BY-SA" in text, "Wikipedia attribution must stay"
    assert "2604.03136" in text, "StoryScope citation must stay"
    assert "never changes what it says" in text, "the hard rule must stay"

    print(f"ok humanizer ({len(signals)} signals, {len(SECTIONS)} sections)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
