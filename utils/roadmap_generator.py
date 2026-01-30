from collections import Counter

def generate_roadmap(job_matches, top_n=10):
    """
    Generate learning roadmap based on missing skills in top N jobs
    """
    # Collect all missing skills in top N jobs
    missing_skills = []
    for job in job_matches[:top_n]:
        if job['missing_skills']:
            missing_skills.extend([s.strip() for s in job['missing_skills'].split(",")])

    # Count frequency
    skill_counter = Counter(missing_skills)

    # Sort skills by frequency (most important first)
    roadmap = skill_counter.most_common()

    return roadmap
