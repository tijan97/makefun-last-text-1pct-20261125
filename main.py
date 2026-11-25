#!/usr/bin/env python3
"""Last text at one percent: write the dying phone's final text to entry.txt.

The entry is one short message, in the phone's own voice, under 200
characters. The grader runs this on a read-only filesystem, so the output
directory comes from MAKEFUN_OUTPUT_DIR (or OUTPUT_DIR), falling back to
the absolute path /output. Never a relative out/ folder.
"""

import os

ENTRY = (
    "1%. this is my last text. tell the charger I loved him. "
    "delete my 47 open tabs. and if my ex asks, I died doing what "
    "I loved: screenshotting his profile at 2am. bye."
)


def main():
    # Gate check, mirroring the competition's sealed scorer: the entry
    # must be UTF-8 text of 1 to 200 characters and not only whitespace.
    if not ENTRY.strip() or len(ENTRY) > 200:
        raise SystemExit(
            f"invalid entry: {len(ENTRY)} characters, "
            "must be 1-200 non-whitespace characters"
        )
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
