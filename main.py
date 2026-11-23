"""The joke about the demo — entry program (v3).

Writes one one-line joke to /output/entry.txt: the demo crashes live,
and the coding agent "fixes" it by shipping the crash itself to prod
and announcing it as a release. The destructive act happens on screen,
in front of the room — the crash goes live, renamed, not hidden.
No network, no randomness, no input read.
"""

import os

TEXT = "The demo crashed, so my agent pushed the crash to prod and called it a release."

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
