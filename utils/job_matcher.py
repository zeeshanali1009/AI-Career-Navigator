import pandas as pd
import re

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-z0-9+.# ]", " ", text)
    return text

def load_jobs(csv_path="data/raw_jobs.csv"):
    df = pd.read_csv(csv_path)
    # Clean skills
    if 'job_skills' in df.columns:
        df['skills_clean'] = df['job_skills'].apply(clean_text)
    else:
        df['skills_clean'] = ""
    return df

def match_jobs(user_skills, jobs_df):
    user_skills_set = set([s.lower() for s in user_skills])
    results = []

    for _, row in jobs_df.iterrows():
        job = row['job_title']
        required_skills = set(row['skills_clean'].split())
        matched = user_skills_set.intersection(required_skills)
        missing = required_skills - user_skills_set
        score = round((len(matched) / len(required_skills))*100, 2) if required_skills else 0
        gap_percentage = round((len(missing) / len(required_skills))*100, 2) if required_skills else 0

        results.append({
            "job_role": job,
            "match_score": score,
            "matched_skills": ", ".join(sorted(matched)),
            "missing_skills": ", ".join(sorted(missing)),
            "gap_percentage": gap_percentage
        })

    # Sort by descending match score
    results = sorted(results, key=lambda x: x['match_score'], reverse=True)
    return results
