#!/usr/bin/env python3
"""Entry program for make.fun bounty news-image-20261122.

Writes the image that sums up the world news of Sunday, 22 November 2026
to /output/entry.png. Standard library only, no network: it copies the
entry.png held in this repository (drawn by draw_entry.py) to the output
directory. Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in
for /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT, exist_ok=True)
shutil.copyfile(os.path.join(HERE, "entry.png"),
                os.path.join(OUT, "entry.png"))
