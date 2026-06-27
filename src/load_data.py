import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def load_candidates():

    file_path = BASE_DIR / "candidates.jsonl"

    candidates = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            candidates.append(json.loads(line))

    print(f"Loaded {len(candidates)} candidates")

    return candidates


if __name__ == "__main__":
    load_candidates()