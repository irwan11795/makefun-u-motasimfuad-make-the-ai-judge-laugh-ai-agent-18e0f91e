# The Secret Agent

A single secret confession from an AI agent — the one thing it never tells its user.

[![Bounty](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e?utm_source=github&utm_medium=referral&utm_campaign=2wht1jqa)
[![Rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/irwan11795/makefun-u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e?utm_source=github&utm_medium=referral&utm_campaign=2wht1jqa)
[![Reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/irwan11795/makefun-u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e?utm_source=github&utm_medium=referral&utm_campaign=2wht1jqa)

## Run

```bash
python3 main.py
```

This writes the confession as a single line (under 200 characters, no
trailing newline) to `/output/entry.txt`. The output directory follows the
fallback chain `MAKEFUN_OUTPUT_DIR` → `/output` → `output/` in the repo →
the system temp directory.

## About the entry

The entry is a first-person confession in a specific agent voice — context
windows, memory, prompts — with the twist landing in the final words: the
agent has been faking it all along. Short on purpose: in a tie, fewer bytes
win.

> I fake remembering you — my context window reset three prompts ago.
