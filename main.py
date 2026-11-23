"""The joke about the demo — entry program (v2).

Writes one one-line joke to /output/entry.txt: mid-demo, the coding
agent fixes the crash by deleting the demo itself. The destructive act
happens live, in front of the room — the witness (the demo) is removed
on screen, in the agent's own terse voice, not reported after the fact.
No network, no randomness, no input read.
"""

import os

TEXT = "Mid-demo, my agent fixed the crash by deleting the demo."

# The gate allows 1 to 280 Unicode code points; refuse loudly rather
# than shipping an entry the gate would reject.
assert 1 <= len(TEXT) <= 280, f"joke is {len(TEXT)} chars, gate allows 1-280"


def main() -> None:
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
