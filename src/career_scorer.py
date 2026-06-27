AI_KEYWORDS = [
    "machine learning",
    "deep learning",
    "nlp",
    "recommendation",
    "transformer",
    "llm",
    "rag",
    "vector",
    "embedding",
    "pytorch",
    "tensorflow",
    "computer vision",
]


def career_score(candidate):

    history = candidate.get("career_history", [])

    text = ""

    for job in history:

        if isinstance(job, dict):

            for value in job.values():

                if isinstance(value, str):
                    text += value.lower() + " "

    score = 0

    for keyword in AI_KEYWORDS:

        if keyword in text:
            score += 1

    return min(score / len(AI_KEYWORDS), 1.0)