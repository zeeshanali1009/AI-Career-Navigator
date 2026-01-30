import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from utils.resume_parser import extract_resume_text
from utils.skill_matcher import extract_skills
from utils.job_matcher import load_jobs, match_jobs
from utils.roadmap_generator import generate_roadmap

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="AI Career Navigator",
    page_icon="🚀",
    layout="wide"
)

# ---------------------------
# Header
# ---------------------------
st.title("🚀 AI Career Navigator")
st.caption(
    "Upload your resume to get AI/ML job matches, skill gaps, and a personalized learning roadmap."
)

st.markdown("---")

# ---------------------------
# Resume Upload Section
# ---------------------------
st.markdown("## 📤 Upload Resume")

uploaded_file = st.file_uploader(
    "Supported formats: PDF, DOCX",
    type=["pdf", "docx"]
)

# ===========================
# MAIN LOGIC
# ===========================
if uploaded_file:

    with st.spinner("🔍 Analyzing your resume..."):
        resume_text = extract_resume_text(uploaded_file)
        skills = extract_skills(resume_text)

    st.success("✅ Resume processed successfully")

    # ---------------------------
    # Tabs Layout
    # ---------------------------
    tab1, tab2, tab3 = st.tabs(
        ["📄 Resume & Skills", "🎯 Job Matches", "🛣️ Learning Roadmap"]
    )

    # ===========================
    # TAB 1: Resume & Skills
    # ===========================
    with tab1:
        col1, col2 = st.columns(2)

        with col1:
            with st.expander("📄 Extracted Resume Text", expanded=True):
                st.text_area(
                    "Resume Content",
                    resume_text,
                    height=350
                )

        with col2:
            with st.expander("🧠 Extracted Skills", expanded=True):
                if skills:
                    st.write(", ".join(skills))
                else:
                    st.warning("No skills detected.")

    # ===========================
    # Load Jobs Data
    # ===========================
    jobs_df = load_jobs("data/raw_jobs.csv")

    job_matches = match_jobs(skills, jobs_df)

    # ===========================
    # TAB 2: Job Matches
    # ===========================
    with tab2:
        st.markdown("## 🎯 Top Job Matches")

        for job in job_matches[:10]:
            with st.expander(f"💼 {job['job_role']}"):
                st.progress(job["match_score"] / 100)

                col1, col2 = st.columns(2)

                with col1:
                    st.write(f"**Match Score:** {job['match_score']}%")
                    st.write(f"**Skill Gap:** {job['gap_percentage']}%")

                with col2:
                    st.write("**Matched Skills**")
                    st.write(job["matched_skills"])

                st.markdown("**Missing Skills**")
                st.write(job["missing_skills"])

    # ===========================
    # TAB 3: Learning Roadmap
    # ===========================
    with tab3:
        st.markdown("## 🛣️ Personalized Learning Roadmap")

        roadmap = generate_roadmap(job_matches, top_n=10)

        if roadmap:
            roadmap_df = pd.DataFrame(
                roadmap,
                columns=["Skill", "Missing in Top Jobs"]
            )

            col1, col2 = st.columns([2, 1])

            # ---- Roadmap Table
            with col1:
                st.dataframe(
                    roadmap_df,
                    use_container_width=True
                )

                st.download_button(
                    label="📥 Download Learning Roadmap (CSV)",
                    data=roadmap_df.to_csv(index=False),
                    file_name="learning_roadmap.csv",
                    mime="text/csv"
                )

            # ---- Roadmap Chart
            with col2:
                top_skills = roadmap_df["Skill"][:10]
                counts = roadmap_df["Missing in Top Jobs"][:10]

                plt.figure(figsize=(6, 4))
                plt.bar(top_skills, counts)
                plt.xticks(rotation=45, ha="right")
                plt.title("Top Skill Gaps")
                plt.tight_layout()

                st.pyplot(plt)

        else:
            st.success("🎉 No major skill gaps found. You're in great shape!")
