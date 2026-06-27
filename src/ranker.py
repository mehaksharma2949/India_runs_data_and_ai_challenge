import csv
from embedding import model
from feature_extractor import extract_candidate_text
from load_data import load_candidates
from jd_parser import load_job_description

from scorer import (
    semantic_score,
    skill_score,
    behavior_score,
    experience_score,
    education_score,
    career_score
)

print("Loading Job Description...")
jd = load_job_description()
jd_embedding = model.encode(jd)

print("Loading Candidates...")
candidates = load_candidates()

results = []

for idx, candidate in enumerate(candidates):

    text = extract_candidate_text(candidate)
    candidate_embedding = model.encode(text)

    semantic = semantic_score(jd_embedding, candidate_embedding)
    skills = skill_score(candidate)
    behavior = behavior_score(candidate)
    experience = experience_score(candidate)
    education = education_score(candidate)
    career = career_score(candidate)

    final_score = (
        0.40 * semantic +
        0.15 * skills +
        0.15 * behavior +
        0.10 * experience +
        0.10 * education +
        0.10 * career
    )

    results.append({
        "candidate_id": candidate["candidate_id"],
        "semantic": round(semantic, 4),
        "skills": round(skills, 4),
        "behavior": round(behavior, 4),
        "experience": round(experience, 4),
        "education": round(education, 4),
        "career": round(career, 4),
        "final": round(final_score, 4)
    })

    if (idx + 1) % 1000 == 0:
        print(f"Processed {idx + 1} candidates...")

# Sort candidates
results.sort(key=lambda x: x["final"], reverse=True)

# Show Top 10
print("\n==============================")
print("TOP 10 CANDIDATES")
print("==============================\n")

for rank, candidate in enumerate(results[:10], start=1):

    print(f"Rank : {rank}")
    print(f"Candidate : {candidate['candidate_id']}")
    print(f"Semantic : {candidate['semantic']}")
    print(f"Skills : {candidate['skills']}")
    print(f"Behavior : {candidate['behavior']}")
    print(f"Experience : {candidate['experience']}")
    print(f"Education : {candidate['education']}")
    print(f"Career : {candidate['career']}")
    print(f"Final Score : {candidate['final']}")
    print("-" * 60)

# -----------------------------
# EXPORT SUBMISSION CSV
# -----------------------------

print("\nCreating submission.csv ...")

with open("output/submission.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow([
        "candidate_id",
        "rank",
        "score",
        "reasoning"
    ])

    # Top 100 only (validator generally expects ranks 1-100)
    for rank, candidate in enumerate(results[:100], start=1):

        reason = (
            f"Semantic {candidate['semantic']:.2f}; "
            f"Skills {candidate['skills']:.2f}; "
            f"Behavior {candidate['behavior']:.2f}; "
            f"Experience {candidate['experience']:.2f}; "
            f"Education {candidate['education']:.2f}; "
            f"Career {candidate['career']:.2f}"
        )

        writer.writerow([
            candidate["candidate_id"],
            rank,
            candidate["final"],
            reason
        ])

print("\nsubmission.csv created successfully!")
print("Saved at: output/submission.csv")