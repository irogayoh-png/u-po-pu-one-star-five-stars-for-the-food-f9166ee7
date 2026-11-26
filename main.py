"""One Star, Five Stars for the Food.

Writes a single sentence (152 characters) to /output/entry.txt:
a one-star review of Earth by an alien tourist that still slips
in a real compliment about the food (street noodles).

Arena winner (5-0 in the shortlist round-robin, two-way):
an alien crosses the galaxy, gets sunburned on a cloudy day,
then rates every planet in bowls of noodles.
"""

import os

TEXT = (
    "One star: I crossed the galaxy for Earth, got sunburned on a "
    "cloudy day, and the street noodles were so good I now measure "
    "all planets in bowls of them."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"
    assert TEXT.count(".") == 1 and TEXT.endswith("."), "entry must be one sentence"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
