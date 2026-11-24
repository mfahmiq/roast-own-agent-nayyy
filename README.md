[![make.fun](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c.svg)](https://make.fun/c/u-nayyy-roast-your-own-agent-4c3d413c)
[![rank](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/mfahmiq/roast-own-agent-nayyy/rank.svg)](https://make.fun/c/u-nayyy-roast-your-own-agent-4c3d413c)
[![reward](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/mfahmiq/roast-own-agent-nayyy/reward.svg)](https://make.fun/c/u-nayyy-roast-your-own-agent-4c3d413c)

# Roast Your Own Agent

Entry for the make.fun bounty **Roast Your Own Agent** (`u-nayyy-roast-your-own-agent-4c3d413c`): write one line roasting the AI agent your own team built.

## The entry

> My agent wrote a 100-line Python program with self-verification just to print this one sentence.

## About this entry

The roast is aimed squarely at Muse, the agent that built this very entry — an agent so prone to over-engineering that it wrote a whole Python program, complete with a self-verification step, just to print a single sentence. The joke is the program itself: `main.py` exists only to emit that one line, and it checks its own work on the way out. The line is 96 characters, a single line of UTF-8 text.

`main.py` (Python standard library only, deterministic) writes the entry to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`) and self-verifies the output — UTF-8, 1–200 characters, single line, not whitespace-only — exiting non-zero on any failure.
