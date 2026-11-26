#!/usr/bin/env python3
"""Five Seconds to Explain the Glass — v1.

The cat's one-sentence defence, written to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output) with no trailing newline, and printed to stdout.
"""
import os

ENTRY = "The glass was parked in my sunbeam, I issued one warning tap, and it chose the floor \u2014 I move to dismiss, dinner is at six."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
print(ENTRY)
