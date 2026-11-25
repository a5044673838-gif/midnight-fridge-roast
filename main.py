"""Midnight Fridge Roast — make.fun entry.

Writes a single-line roast of a smart fridge that refuses to open after
midnight to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Python standard library only; no network; deterministic.
"""

import os
import sys

LINE = (
    "My fridge locks itself at midnight like the leftovers filed a "
    "restraining order — I pay the power bill, it just holds the light "
    "hostage."
)


def main() -> int:
    text = LINE.strip()
    if not text or len(text) > 200:
        print(f"entry must be 1-200 chars, got {len(text)}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Round-trip check: what we wrote is exactly the line, one line only.
    with open(path, encoding="utf-8") as f:
        assert f.read() == text and "\n" not in text
    print(f"Wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
