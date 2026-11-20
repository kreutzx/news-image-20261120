#!/usr/bin/env python3
"""news-image-20261120: "The World in One Day" for Friday 20 November 2026.

A one-image front page summing up the world's news of 20 November 2026:
Trump puts the Iran war decision off to 2027, Anthropic ends its record
IPO debut up 17%, Cyclone Akvan makes landfall in Odisha, Voyager 1
passes one light-day from Earth, and thirteen more stories from the day,
with a UTC timeline. The page was drawn for this entry and ships as
entry.png; this program (Python 3.13, standard library only) copies it to
the output directory the grader reads, /output/entry.png.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)
    if os.path.getsize(dest) != os.path.getsize(SOURCE):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
