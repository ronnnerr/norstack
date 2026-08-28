#!/usr/bin/env python3
"""Structural checks across every skill in the suite."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"

# Words that would mean personal context leaked back into the public tree.
FORBIDDEN = re.compile(
    r"\bron\b|advero|nullpsych|nightos|nightcloud|alcheclip|gmgn|higgsfield"
    r"|crunchyroll|rognor|/Users/",
    re.I,
)


def main() -> int:
    dirs = sorted(p for p in SKILLS.iterdir() if p.is_dir())
    assert dirs, "no skills found"

    names = set()
    failures = []

    for d in dirs:
        skill = d / "SKILL.md"
        if not skill.exists():
            failures.append(f"{d.name}: no SKILL.md")
            continue

        text = skill.read_text(encoding="utf-8")

        m = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
        if not m:
            failures.append(f"{d.name}: missing YAML frontmatter")
            continue
        front = m.group(1)

        name_m = re.search(r"^name:\s*(\S+)", front, re.M)
        if not name_m:
            failures.append(f"{d.name}: frontmatter has no name")
            continue
        if name_m.group(1) != d.name:
            failures.append(f"{d.name}: name is '{name_m.group(1)}', expected '{d.name}'")
        names.add(d.name)

        if not re.search(r"^description:", front, re.M):
            failures.append(f"{d.name}: frontmatter has no description")

        if len(text.splitlines()) < 8:
            failures.append(f"{d.name}: SKILL.md is a stub")

    # Personal context must not leak into the public tree.
    for path in SKILLS.rglob("*.md"):
        if path.name == "profile.md":  # gitignored, user-owned
            continue
        for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if FORBIDDEN.search(line):
                rel = path.relative_to(ROOT)
                failures.append(f"{rel}:{i}: personal reference leaked")

    # Every `skill` reference in backticks must resolve to a real skill.
    known_nonskill = {
        "profile.md", "shots.json", "SKILL.md", "text", "html [sel]", "links",
        "forms", "accessibility", "data", "media", "voice", "see", "inbox set",
        "matte", "style.md", "script.md",
    }
    for path in SKILLS.rglob("SKILL.md"):
        for token in set(re.findall(r"`([a-z][a-z-]{2,20})`", path.read_text(encoding="utf-8"))):
            if token in known_nonskill or token in names:
                continue
            # Only flag tokens that look like a skill invocation in a routing table.
            if re.search(rf"\|\s*`{re.escape(token)}`", path.read_text(encoding="utf-8")):
                failures.append(f"{path.relative_to(ROOT)}: routes to unknown skill '{token}'")

    if failures:
        for f in failures:
            print(f"FAIL {f}")
        return 1

    print(f"ok skills ({len(names)} skills, frontmatter valid, no personal references)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
