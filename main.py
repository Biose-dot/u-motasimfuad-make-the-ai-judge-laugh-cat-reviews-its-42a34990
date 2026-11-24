# Deadpan one-star review written by a house cat about its human (final v2).
import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
ENTRY_TEXT = "One star. The can opener is broken half the time, the warm spot on the sofa is always taken, and the human talks to a glowing box all day."

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as handle:
    handle.write(ENTRY_TEXT)
