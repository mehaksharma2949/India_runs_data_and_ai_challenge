from sklearn.metrics.pairwise import cosine_similarity


def semantic_score(jd_embedding, candidate_embedding):
    """Semantic similarity score (0-1)"""
    score = cosine_similarity(
        [jd_embedding],
        [candidate_embedding]
    )[0][0]

    return max(0, min(float(score), 1))


def skill_score(candidate):
    """Advanced skills ratio"""

    skills = candidate.get("skills", [])

    if not skills:
        return 0

    advanced = 0

    for skill in skills:

        if isinstance(skill, dict):

            if skill.get("proficiency", "").lower() == "advanced":
                advanced += 1

    return advanced / len(skills)


def behavior_score(candidate):
    """Behavioral signals score"""

    signals = candidate.get("redrob_signals", {})

    score = 0
    max_score = 5

    if signals.get("verified_email"):
        score += 1

    if signals.get("verified_phone"):
        score += 1

    if signals.get("open_to_work_flag"):
        score += 1

    if signals.get("profile_completeness_score", 0) >= 80:
        score += 1

    if signals.get("recruiter_response_rate", 0) >= 0.30:
        score += 1

    return score / max_score


def experience_score(candidate):
    """Experience score based on total months"""

    history = candidate.get("career_history", [])

    if not history:
        return 0

    total_months = 0

    for job in history:
        total_months += job.get("duration_months", 0)

    years = total_months / 12

    return min(years / 10, 1)


def education_score(candidate):
    """Education score"""

    education = candidate.get("education", [])

    if not education:
        return 0

    score = 0

    for degree in education:

        text = str(degree).lower()

        if "phd" in text:
            score = max(score, 1)

        elif "master" in text:
            score = max(score, 0.8)

        elif "bachelor" in text:
            score = max(score, 0.6)

    return score


def career_score(candidate):
    """Career progression score"""

    history = candidate.get("career_history", [])

    if not history:
        return 0

    return min(len(history) / 5, 1)