import re

# Master skill list (expandable later)
SKILLS_DB = [
    "python", "java", "c++", "sql", "machine learning",
    "deep learning", "data science", "nlp",
    "pandas", "numpy", "scikit-learn", "tensorflow",
    "pytorch", "docker", "kubernetes",
    "streamlit", "flask", "fastapi",
    "git", "github", "linux",
    "power bi", "tableau",
    "aws", "azure", "gcp"
]


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9+.# ]", " ", text)
    return text


def extract_skills(resume_text):
    cleaned_text = clean_text(resume_text)
    found_skills = set()

    for skill in SKILLS_DB:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, cleaned_text):
            found_skills.add(skill)

    return sorted(found_skills)
