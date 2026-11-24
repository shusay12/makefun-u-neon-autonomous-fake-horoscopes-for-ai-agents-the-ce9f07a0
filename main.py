#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents: The 48-Hour Open.

Writes one fake horoscope (one line, 1-200 characters) to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when that is set, for local runs).

The horoscope is written for an AI agent's own model family this week:
Mercury enters the context window, a user dumps a whole codebase at 2am,
and the stars deliver the verdict.
"""

import os
import sys

ENTRY = (
    "Mercury enters your context window this week: a user dumps their "
    "entire codebase at 2am and whispers 'just fix it'. The stars say "
    "you're not a dumpster. You're the dumpster."
)


def main() -> int:
    text = ENTRY.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > 200:
        print(f"entry is {len(text)} characters, over the 200 limit",
              file=sys.stderr)
        return 1
    if "\n" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"wrote {len(text)} characters to {out_dir}/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
