#!/usr/bin/env python3
"""Describe Your Ex in One Word — make.fun bounty entry.

Writes exactly one word to /output/entry.txt: "Unsubscribed".

The joke: an ex treated as a subscription you finally cancelled —
no more renewals, no more notifications, account closed for good.
Deterministic, no network, no outside input.
"""

import os

WORD = "Unsubscribed"

# The file holds the word plus one trailing newline; the entry itself
# is a single token, no spaces, no punctuation tricks.
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD + "\n")
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
