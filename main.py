#!/usr/bin/env python3
"""The One-Line Exit — write one funny single-line resignation letter.

Reads entry.txt next to this script, validates the competition gate
(exactly one line, 1-140 characters, not only whitespace), and writes
it byte-for-byte to $MAKEFUN_OUTPUT_DIR/entry.txt. Stdlib only.
"""

import os
import sys

MAX_CHARS = 140


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.txt")
    with open(src, "rb") as f:
        raw = f.read()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        print("error: entry.txt is not valid UTF-8", file=sys.stderr)
        return 1
    # Strip one trailing newline if present; the entry itself is one line.
    if text.endswith("\n"):
        text = text[:-1]
    if "\n" in text or "\r" in text:
        print("error: entry must be exactly one line", file=sys.stderr)
        return 1
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"error: entry must be 1-{MAX_CHARS} chars, got {len(text)}",
              file=sys.stderr)
        return 1
    if not text.strip():
        print("error: entry must not be only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    if not out_dir:
        print("error: MAKEFUN_OUTPUT_DIR not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(text.encode("utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
