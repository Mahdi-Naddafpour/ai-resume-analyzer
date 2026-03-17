def extract_skills(text: str) -> list[str]:
    known_skills = [
        "python",
        "sql",
        "mysql",
        "git",
        "github",
        "flask",
        "fastapi",
        "api",
        "rest api",
        "backend",
        "docker",
        "javascript",
        "html",
        "css",
    ]

    text_lower = text.lower()
    found_skills = []

    for skill in known_skills:
        if skill in text_lower:
            found_skills.append(skill)

    return sorted(set(found_skills))


def generate_summary(skills: list[str]) -> str:
    if skills:
        skills_text = ", ".join(skills)
        return (
            f"The candidate demonstrates familiarity with {skills_text} "
            f"and shows a clear interest in backend development, practical projects, "
            f"and continuous software engineering growth."
        )

    return (
        "The candidate shows interest in software development and is building practical "
        "skills through projects and hands-on learning."
    )


def find_strengths(skills: list[str]) -> list[str]:
    strengths = []

    if "python" in skills:
        strengths.append("Strong foundation in Python")
    if "sql" in skills or "mysql" in skills:
        strengths.append("Understands relational databases and SQL")
    if "git" in skills or "github" in skills:
        strengths.append("Familiar with version control workflows")
    if "api" in skills or "rest api" in skills:
        strengths.append("Shows awareness of API development concepts")
    if "backend" in skills:
        strengths.append("Clear focus on backend engineering")

    if not strengths:
        strengths.append("Motivated to grow in software development")

    return strengths


def find_weaknesses(skills: list[str]) -> list[str]:
    weaknesses = []

    if "flask" not in skills and "fastapi" not in skills:
        weaknesses.append("No backend framework is clearly demonstrated")
    if "docker" not in skills:
        weaknesses.append("No containerization or DevOps tooling is mentioned")
    if "api" not in skills and "rest api" not in skills:
        weaknesses.append("API experience is not clearly demonstrated")

    return weaknesses


def improvement_suggestions(skills: list[str]) -> list[str]:
    suggestions = []

    if "flask" not in skills and "fastapi" not in skills:
        suggestions.append("Build a backend project using Flask or FastAPI")
    if "api" not in skills and "rest api" not in skills:
        suggestions.append("Add a project that exposes REST API endpoints")
    if "docker" not in skills:
        suggestions.append("Learn Docker and containerize one project")

    suggestions.append("Write stronger project descriptions focused on technologies and impact")

    return suggestions


def analyze_resume(resume_text: str) -> dict:
    skills = extract_skills(resume_text)
    strengths = find_strengths(skills)
    weaknesses = find_weaknesses(skills)
    suggestions = improvement_suggestions(skills)
    summary = generate_summary(skills)

    return {
        "professional_summary": summary,
        "key_technical_skills": skills,
        "strengths": strengths,
        "weaknesses": weaknesses,
        "suggestions_for_improvement": suggestions,
    }


def compare_resume_with_job(resume_text: str, job_description: str) -> dict:
    resume_skills = set(extract_skills(resume_text))
    job_skills = set(extract_skills(job_description))

    matching_skills = sorted(resume_skills.intersection(job_skills))
    missing_skills = sorted(job_skills.difference(resume_skills))

    if len(job_skills) == 0:
        score = 50
    else:
        score = int((len(matching_skills) / len(job_skills)) * 100)

    if score >= 80:
        evaluation = "Strong match for the role."
    elif score >= 60:
        evaluation = "Moderate match with room for improvement."
    else:
        evaluation = "Entry-level match; more targeted projects and skills are needed."

    return {
        "match_score": score,
        "matching_skills": matching_skills,
        "missing_skills": missing_skills,
        "final_evaluation": evaluation,
    }