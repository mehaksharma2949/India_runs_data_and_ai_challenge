import csv
from ranker import results

with open("output/submission.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow([
        "candidate_id",
        "rank",
        "score",
        "reasoning"
    ])

    for rank, candidate in enumerate(results, start=1):

        score = round(candidate["final"], 4)

        reason = (
            f"Semantic {candidate['semantic']:.2f}; "
            f"Skills {candidate['skills']:.2f}; "
            f"Behavior {candidate['behavior']:.2f}."
        )

        writer.writerow([
            candidate["candidate_id"],
            rank,
            score,
            reason
        ])

print("submission.csv created successfully!")