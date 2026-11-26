"""Write the robot vacuum's funniest excuse to entry.txt.

Bounty: The Robot Vacuum's Funniest Excuse
(u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2)
Standard library only.
"""

import os

LINE = "The pet hair under the couch was so thick my suction filed a workplace complaint."

MAX_CHARS = 120


def main() -> None:
    if not (1 <= len(LINE) <= MAX_CHARS) or not LINE.strip():
        raise ValueError(
            f"entry line must be 1-{MAX_CHARS} non-whitespace characters, got {len(LINE)}"
        )
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
