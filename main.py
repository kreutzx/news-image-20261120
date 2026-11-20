#!/usr/bin/env python3
"""news-image-20261120: "The World in One Day" for Friday 20 November 2026.

Dense edition: one front page summing up the world's news of Friday
20 November 2026 in 56 counted stories — 3 heroes (Trump pushes the Iran
strike decision into 2027; Wall Street falls 2% despite Anthropic's record
debut; Voyager 1 phones home from one light-day away), 24 sourced section
cards, sport, by-the-numbers, a UTC timeline and a late wire. The page was
drawn for this entry by build.py (PIL, deterministic) and ships as
entry.png; this program (Python 3.13, standard library only) validates the
PNG and copies it to the output directory the grader reads,
/output/entry.png.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1048576


def main() -> int:
    with open(SOURCE, "rb") as fh:
        head = fh.read(len(PNG_MAGIC))
    if head != PNG_MAGIC:
        return 1
    if os.path.getsize(SOURCE) > MAX_BYTES:
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)
    with open(dest, "rb") as fh:
        if fh.read(len(PNG_MAGIC)) != PNG_MAGIC:
            return 1
    if os.path.getsize(dest) != os.path.getsize(SOURCE):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
