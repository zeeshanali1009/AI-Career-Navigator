import pandas as pd

# Load CSVs
postings = pd.read_csv("data/job_postings.csv")  # contains job_title, company, location
skills = pd.read_csv("data/job_skills.csv")      # contains job_link, job_skills

# Merge skills into postings using job_link as key
merged = postings.merge(
    skills,
    on="job_link",
    how="left"
)

# Fill missing skills
merged['job_skills'] = merged['job_skills'].fillna("")

# Keep only relevant columns for job matching
merged = merged[['job_link', 'job_title', 'job_description', 'job_skills']] \
    if 'job_description' in postings.columns else merged[['job_link', 'job_title', 'job_skills']]

# Save as raw_jobs.csv
merged.to_csv("data/raw_jobs.csv", index=False)

print("✅ raw_jobs.csv created successfully!")
