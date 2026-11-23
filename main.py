"""Write one funny line to /output/entry.txt: a robot vacuum's excuse
for missing a spot, filed as a deadpan incident report.

The joke: the vacuum treats the spot as a superior it must not disturb —
it stares back, gets classified as structural, and is left alone.
"""

import os

TEXT = (
    "Incident report #0417: the spot looked at me. "
    "I classified it as a load-bearing stain and added it to the floor plan."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
