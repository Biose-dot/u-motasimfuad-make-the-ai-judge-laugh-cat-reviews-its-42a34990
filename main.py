#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human — make.fun entry.

Writes the entry text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Deadpan review shape with complaints only a cat would file: the food, the lap, the glowing rectangle, and staff who shed.
"""
import os

ENTRY = 'One star. Food arrives late, the lap is often occupied by a glowing rectangle, and the staff sheds almost as much as I do.'


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
