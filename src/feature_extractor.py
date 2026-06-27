def extract_candidate_text(candidate):

    text_parts = []

    # ---------- Skills ----------
    skills = candidate.get("skills", [])

    for skill in skills:
        if isinstance(skill, dict):
            text_parts.append(skill.get("name", ""))

    # ---------- Profile ----------
    profile = candidate.get("profile", {})

    for value in profile.values():
        if isinstance(value, str):
            text_parts.append(value)

    # ---------- Career History ----------
    for job in candidate.get("career_history", []):

        if isinstance(job, dict):

            for value in job.values():

                if isinstance(value, str):
                    text_parts.append(value)

    return " ".join(text_parts)
