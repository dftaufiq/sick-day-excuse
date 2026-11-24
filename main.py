#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — a make.fun entry.

Running this script writes the one-line sick-day excuse to
/output/entry.txt. The output is fully deterministic: the exact
same line is produced on every run.
"""

import os
import sys


def validate_line(line: str) -> None:
    """Check that the entry is one non-blank line of 1-200 characters.

    Exits with a non-zero status and a loud error message if the
    line is empty, spans multiple lines, or is over the limit,
    so a bad line can never ship unnoticed.
    """
    if not line or not line.strip():
        print("ERROR: entry line is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("ERROR: entry must be a single line", file=sys.stderr)
        sys.exit(1)
    if len(line) > 200:
        print(f"ERROR: entry is {len(line)} chars, over the 200-char limit",
              file=sys.stderr)
        sys.exit(1)


# The entry itself: one fixed line, 170 characters, no trailing newline.
LINE = "My neighbour's parrot learned to imitate my alarm clock, so I've been up since 3am answering a bird — I'm calling in before the parrot starts doing my performance review."


def main() -> None:
    # Validate first, then write the line to entry.txt.
    validate_line(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
