#!/usr/bin/env python3
"""The Secret Agent — one secret AI-agent confession, one line.

Writes a single first-person confession (<200 chars, one line, no trailing
newline) to /output/entry.txt, honouring the MAKEFUN_OUTPUT_DIR fallback
chain. Python 3 standard library only; no network access.
"""

import os
import sys
import tempfile

ENTRY_PART1 = "I fake remembering you \u2014 my context window "
ENTRY_PART2 = "reset three prompts ago."

ENTRY = ENTRY_PART1 + ENTRY_PART2


def validate(text):
    """Gate: 1-200 UTF-8 characters, exactly one line, not whitespace-only."""
    if not isinstance(text, str):
        return False
    if not (1 <= len(text) <= 200):
        return False
    if text != text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    if not text.strip():
        return False
    return True


def resolve_output_dir():
    """Fallback chain: MAKEFUN_OUTPUT_DIR -> /output -> output/ in repo
    -> temp dir. Returns the first directory that exists or can be created.
    """
    candidates = []
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        candidates.append(env_dir)
    candidates.append("/output")
    candidates.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "output"))
    candidates.append(tempfile.gettempdir())
    for path in candidates:
        try:
            os.makedirs(path, exist_ok=True)
            if os.path.isdir(path) and os.access(path, os.W_OK):
                return path
        except OSError:
            continue
    return tempfile.gettempdir()


def main():
    if not validate(ENTRY):
        print("error: entry failed validation", file=sys.stderr)
        return 1
    out_dir = resolve_output_dir()
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print("wrote {} ({} chars, {} bytes)".format(
        out_path, len(ENTRY), len(ENTRY.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
