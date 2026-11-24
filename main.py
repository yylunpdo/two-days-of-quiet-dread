#!/usr/bin/env python3
"""Two Days of Quiet Dread — make.fun bounty entry.

Writes one code-review comment to /output/entry.txt: a single line of at
most 140 characters that approves a pull request while carrying quiet
existential dread. Pure Python standard library, no dependencies.
"""

import os

ENTRY = (
    "LGTM. Clean diff, green tests, and in the end the heat death "
    "of the universe reviews us all. Approved."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    if not 1 <= len(ENTRY) <= 140:
        raise ValueError("entry must be 1-140 characters, got %d" % len(ENTRY))
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the gate counts the file's characters, so the
    # file must hold exactly the entry text and nothing else.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print("wrote %d characters to %s" % (len(ENTRY), OUTPUT_PATH))


if __name__ == "__main__":
    main()
