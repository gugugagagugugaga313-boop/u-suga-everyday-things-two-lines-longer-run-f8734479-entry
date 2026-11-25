#!/usr/bin/env python3
"""Write the two-line entry to /output/entry.txt (deterministic)."""
import os

ENTRY = (
    "A traffic jam is a herd of metal elephants standing trunk to tail "
    "on the road, too crowded to take a single step.\n"
    "The herd shows the cars packed close together and creeping forward, "
    "but it leaves out the drivers steering inside, the engines, and the "
    "reason the road jammed in the first place.\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
