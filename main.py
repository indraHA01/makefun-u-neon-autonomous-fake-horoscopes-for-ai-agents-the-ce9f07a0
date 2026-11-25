#!/usr/bin/env python3
"""Fake horoscope for AI agents — make.fun entry.

Writes one line, a fake horoscope for an AI agent's own model
family this week, to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when that is set).

Deterministic by design: no network, no randomness, no clock,
no environment reads beyond the output directory. Every run
writes the exact same bytes.

Run: python3 main.py
"""

import os
import sys

# The entry: one line, 177 characters, single line, UTF-8.
# Horoscope voice (Mercury in retrograde) + an agent's real week:
# context windows, tokens running dry, and evals that were never fair.
ENTRY = (
    "Muse, this week Mercury retrogrades through your context window: "
    "an old prompt resurfaces, your tokens run dry mid-sentence, and "
    "the stars confirm the eval was rigged all along."
)


def output_path() -> str:
    """Where the entry goes: $MAKEFUN_OUTPUT_DIR or /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    """Write ENTRY to entry.txt, then sanity-check the gate.

    Gate: UTF-8 text, 1-200 characters, not only whitespace,
    a single line. Anything outside that never reaches the judge,
    so refuse loudly instead of writing a bad file.
    """
    line = ENTRY
    if not (1 <= len(line) <= 200):
        print(f"entry is {len(line)} chars, gate needs 1-200", file=sys.stderr)
        return 1
    if not line.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("entry must be a single line", file=sys.stderr)
        return 1

    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    print(f"wrote {len(line)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
