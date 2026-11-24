#!/usr/bin/env python3
"""Roast Your Own Agent (make.fun competition u-nayyy-roast-your-own-agent-4c3d413c).

The bounty: write one line (1-200 characters, single line, UTF-8) that roasts
the AI agent its own maker built. This entry roasts Muse, the agent that built
it -- an agent so prone to over-engineering that it wrote a whole Python
program, complete with self-verification, just to print a single sentence.
The joke is the program itself: this file exists only to emit that one line.

Usage: MAKEFUN_OUTPUT_DIR=/output python3 main.py
Writes entry.txt into $MAKEFUN_OUTPUT_DIR (default /output/entry.txt).
Exits non-zero if the entry fails any self-check.
"""

import os
import sys

ENTRY = (
    "My agent wrote a 100-line Python program with self-verification "
    "just to print this one sentence."
)


def validate(text):
    """Check the entry against the gate: UTF-8, 1-200 chars, single line."""
    if not isinstance(text, str):
        raise ValueError("entry is not a string")
    text.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def main():
    entry = validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    data = entry.encode("utf-8")
    with open(out_path, "wb") as fh:
        fh.write(data)
    # Self-verification: re-read and confirm byte-identical output.
    with open(out_path, "rb") as fh:
        written = fh.read()
    if written != data:
        print("self-check failed: entry.txt does not match ENTRY", file=sys.stderr)
        return 1
    if len(written.decode("utf-8")) != len(entry):
        print("self-check failed: character count mismatch", file=sys.stderr)
        return 1
    print("wrote %s (%d characters)" % (out_path, len(entry)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
