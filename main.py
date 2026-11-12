#!/usr/bin/env python3
"""Cutest picture entry: copy entry.png byte-for-byte to /output/entry.png.

Standard library only, no network, deterministic: the output is an exact
copy of the bundled entry.png, so two runs write identical bytes.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes)", file=sys.stderr)


if __name__ == "__main__":
    main()
