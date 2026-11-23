"""The One-Line Laugh entry: a single funny line about step counters.

The joke leans on an everyday truth (developers pace while code
compiles) and lands its surprise at the end: the "exercise" was never
exercise at all.
"""

import os

JOKE = (
    "My fitness tracker says I hit 10,000 steps today, but 9,000 of "
    "them were just me pacing while my code compiled."
)

OUTPUT_PATH = "/output/entry.txt"


def validate_line(line):
    """Check the line fits the gate: one sentence, 1-200 characters."""
    cleaned = line.strip()
    if not cleaned:
        raise ValueError("entry must not be blank")
    if len(cleaned) > 200:
        raise ValueError("entry must be at most 200 characters")
    if cleaned.count("\n") > 0:
        raise ValueError("entry must be a single line")
    return cleaned


def main():
    line = validate_line(JOKE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


if __name__ == "__main__":
    main()
