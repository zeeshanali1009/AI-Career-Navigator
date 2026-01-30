import streamlit as st
from utils.resume_parser import extract_resume_text
from utils.skill_matcher import extract_skills
from utils.job_matcher import load_jobs, match_jobs
from utils.roadmap_generator import generate_roadmap
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# Streamlit Page Config
# ---------------------------
st.set_page_config(
    page_title="AI Career Navigator",
    page_icon="📄",
    layout="wide"
)

# ---------------------------
# Title & Instructions
# ---------------------------
st.title("AI Career Navigator")
st.subheader("Upload your resume (PDF or DOCX) to get AI/ML job matches and learning roadmap")

st.markdown("""
This tool extracts your skills from your resume and matches them against real AI/ML/Tech job postings.
You will also see **missing skills** for each role and a **personalized learning roadmap**.
""")

# ---------------------------
# File Uploader
# ---------------------------
uploaded_file = st.file_uploader(
    "Choose your resume file",
    type=["pdf", "docx"]
)

if uploaded_file is not None:
    # ---------------------------
    # Extract Text from Resume
    # ---------------------------
    with st.spinner("Processing resume..."):
        resume_text = extract_resume_text(uploaded_file)
        skills = extract_skills(resume_text)

    st.success("✅ Resume processed successfully!")

    # ---------------------------
    # Display Resume Text & Skills
    # ---------------------------
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📄 Extracted Resume Text")
        st.text_area("", resume_text, height=300)

    with col2:
        st.markdown("### 🧠 Extracted Skills")
        if skills:
            for skill in skills:
                st.markdown(f"- {skill}")
        else:
            st.warning("No skills detected.")

    # ---------------------------
    # Load Real Jobs Data
    # ---------------------------
    jobs_df = load_jobs("data/raw_jobs.csv")

    # ---------------------------
    # Match Jobs & Compute Skill Gap
    # ---------------------------
    job_matches = match_jobs(skills, jobs_df)

    # ---------------------------
    # Display Top Job Matches
    # ---------------------------
    st.markdown("## 🎯 Top 10 Job Role Matches with Skill Gap")
    for job in job_matches[:10]:
        st.markdown(f"### {job['job_role']}")
        st.progress(job["match_score"] / 100)
        st.write(f"Match Score: **{job['match_score']}%**")
        st.write(f"Matched Skills: {job['matched_skills']}")
        st.write(f"Missing Skills: {job['missing_skills']}")
        st.write(f"Skill Gap: **{job['gap_percentage']}%**")
        # Optional: show company/location if available
        if 'company' in jobs_df.columns and 'job_location' in jobs_df.columns:
            st.write(f"Company: {jobs_df.loc[jobs_df['job_title']==job['job_role'], 'company'].values[0]}")
            st.write(f"Location: {jobs_df.loc[jobs_df['job_title']==job['job_role'], 'job_location'].values[0]}")
        st.markdown("---")

    # ---------------------------
    # Generate Learning Roadmap
    # ---------------------------
    st.markdown("## 🛣️ Personalized Learning Roadmap")
    roadmap = generate_roadmap(job_matches, top_n=10)

    if roadmap:
        st.markdown("Priority learning order based on top 10 job gaps:")
        for skill, freq in roadmap:
            st.markdown(f"- **{skill}** (missing in {freq} top jobs)")

        # ---------------------------
        # Download Roadmap Button
        # ---------------------------
        roadmap_df = pd.DataFrame(roadmap, columns=["Skill", "Missing in Top Jobs"])
        st.download_button(
            label="Download Learning Roadmap",
            data=roadmap_df.to_csv(index=False),
            file_name="learning_roadmap.csv",
            mime="text/csv"
        )

        # ---------------------------
        # Plot Top 10 Missing Skills
        # ---------------------------
        top_skills = [s for s,f in roadmap[:10]]
        counts = [f for s,f in roadmap[:10]]

        plt.figure(figsize=(10,5))
        plt.bar(top_skills, counts, color='skyblue')
        plt.xticks(rotation=45, ha='right')
        plt.xlabel("Skills")
        plt.ylabel("Missing in Top Jobs")
        plt.title("Top 10 Missing Skills in Top Job Matches")
        plt.tight_layout()

        st.pyplot(plt)

    else:
        st.success("No missing skills! You are already well-prepared for top roles.")
