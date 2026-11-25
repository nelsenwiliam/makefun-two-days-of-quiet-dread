#!/usr/bin/env python3
"""Two Days of Quiet Dread — one-line code review comment.

Writes a single line (at most 140 characters) that approves a pull
request while carrying quiet existential dread, to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when the harness sets it).
Pure standard library only.
"""
import os

LINE = "Approved. Nothing here is wrong, which is exactly what worries me."

# The gate requires 1-140 characters, a single line, not only whitespace.
assert 1 <= len(LINE) <= 140 and "\n" not in LINE and LINE.strip() == LINE


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    # Local copy next to the program, for inspection.
    with open("entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
