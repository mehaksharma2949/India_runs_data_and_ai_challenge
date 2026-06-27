import json
from pathlib import Path
from pprint import pprint

BASE_DIR = Path(__file__).resolve().parent.parent

with open(BASE_DIR / "sample_candidates.json", "r", encoding="utf-8") as f:
    candidates = json.load(f)

candidate = candidates[0]

print("=" * 70)
print("Candidate ID")
print("=" * 70)
print(candidate["candidate_id"])

print("\n")

print("=" * 70)
print("PROFILE")
print("=" * 70)
pprint(candidate["profile"])

print("\n")

print("=" * 70)
print("CAREER HISTORY")
print("=" * 70)
pprint(candidate["career_history"])

print("\n")

print("=" * 70)
print("SKILLS")
print("=" * 70)
pprint(candidate["skills"])

print("\n")

print("=" * 70)
print("EDUCATION")
print("=" * 70)
pprint(candidate["education"])

print("\n")

print("=" * 70)
print("REDROB SIGNALS")
print("=" * 70)
pprint(candidate["redrob_signals"])