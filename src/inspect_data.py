import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

with open(BASE_DIR / "sample_candidates.json", "r", encoding="utf-8") as f:
    candidates = json.load(f)

print("=" * 50)
print("Total Candidates :", len(candidates))
print("=" * 50)

first_candidate = candidates[0]

print("\nKeys Available:\n")
for key in first_candidate.keys():
    print("-", key)