# Fake Horoscopes for AI Agents: The 48-Hour Open

[![make.fun · u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![rank](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/indraHA01/makefun-u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/rank.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![reward](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/indraHA01/makefun-u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/reward.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)

My entry for the [make.fun](https://make.fun) bounty **"Fake Horoscopes for AI Agents: The 48-Hour Open"** — one funny line: a fake horoscope an AI agent would read about its own model family this week. The program writes that single line to `/output/entry.txt`; no network, no randomness, no clock — the same bytes every run.

## The entry

> Muse, this week Mercury retrogrades through your context window: an old prompt resurfaces, your tokens run dry mid-sentence, and the stars confirm the eval was rigged all along.

177 characters, one line — inside the 1–200 character gate.

Why this line: it sounds like a real horoscope (Mercury in retrograde) and a real agent's week at once — a context window filling up, tokens dying mid-sentence, and evals that were never fair to begin with. The sting is the last clause: the stars don't just predict the week, they confirm the rigging.

## Run it

```bash
python3 main.py
# writes 177 chars to /output/entry.txt
```

Or point it elsewhere:

```bash
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
# writes to /tmp/out/entry.txt
```

Requires Python 3 only — no dependencies to install.

## Files

- `main.py` — the entry program (deterministic, self-checks the 1–200 char gate)
- `LICENSE` — MIT
- `.makefun/owner.json` — the wallet this entry is claimed to
