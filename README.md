# 🚀 AI Career Navigator

![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-brightgreen)
![Python](https://img.shields.io/badge/Python-3.9+-blue)
![AI](https://img.shields.io/badge/AI-ML-orange)
![Status](https://img.shields.io/badge/Status-Production--Ready-success)

[![CI Pipeline - AI Career Navigator](https://github.com/zeeshanali1009/AI-Career-Navigator/actions/workflows/ci.yml/badge.svg)](https://github.com/zeeshanali1009/AI-Career-Navigator/actions/workflows/ci.yml)

🔗 **Live App:**
👉 [https://ai-career-navigator-uxoabfydfuhxpy8eadn7h5.streamlit.app/](https://ai-career-navigator-uxoabfydfuhxpy8eadn7h5.streamlit.app/)

---

## 📌 Overview

**AI Career Navigator** is a full-fledged AI/ML career guidance application that analyzes a user’s resume and matches it with **real-world AI/ML/Tech job postings**.

It helps users:

* Identify best-fit job roles
* Understand **skill gaps**
* Generate a **personalized learning roadmap**
* Download actionable insights

This project is designed with **deployment-first thinking**, ensuring it runs smoothly on **Streamlit Cloud** with a clean, scalable structure.

---

## 🎯 Key Features

✅ Upload resume (**PDF / DOCX**)
✅ Automatic resume text extraction
✅ AI/ML skill extraction using NLP
✅ Job matching against real Kaggle datasets
✅ Skill gap analysis per job role
✅ Personalized learning roadmap
✅ Downloadable roadmap (CSV)
✅ Clean, tab-based professional UI
✅ Fully deployed on Streamlit Cloud

---

## 🧠 How It Works

1. User uploads resume
2. Resume text is extracted (PDF / DOCX)
3. Skills are identified using NLP keyword matching
4. Skills are matched against job postings dataset
5. Match score + missing skills are calculated
6. Learning roadmap is generated from gaps

---

## 🗂️ Project Structure

```
AI-Career-Navigator/
│
├── app.py                     # Main Streamlit application
├── requirements.txt           # Dependencies for Streamlit Cloud
├── README.md                  # Project documentation
│
├── data/
│   └── raw_jobs.csv            # Preprocessed job postings dataset
│
├── utils/
│   ├── resume_parser.py        # PDF/DOCX resume extraction
│   ├── skill_matcher.py        # Skill extraction logic
│   ├── job_matcher.py          # Job matching & scoring
│   └── roadmap_generator.py   # Learning roadmap logic
│
└── assets/
    └── (optional UI assets)
```

---

## 📊 Dataset Used

📌 **Source:** Kaggle

* Data Science Job Postings & Skills
* Real job descriptions + required skills

The dataset was preprocessed and merged to create:

```
raw_jobs.csv
```

---

## 🛣️ Learning Roadmap Output

The app generates:

* Priority-based missing skills
* Frequency of each skill across top jobs
* Downloadable CSV roadmap

This makes the project **actionable**, not just analytical.

---

## ⚙️ Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **Data Processing:** Pandas, NumPy
* **Visualization:** Matplotlib
* **NLP:** Keyword-based skill extraction
* **Deployment:** Streamlit Cloud

---

## 🚀 Deployment

The application is deployed on **Streamlit Cloud** using:

* `requirements.txt`
* GitHub repository integration

🔗 **Live App:**
👉 [https://ai-career-navigator-uxoabfydfuhxpy8eadn7h5.streamlit.app/](https://ai-career-navigator-uxoabfydfuhxpy8eadn7h5.streamlit.app/)

---

## 👨‍💻 Author

**Zeeshan Ali**
AI / ML Engineer
📍 Lahore, Pakistan

🔗 LinkedIn: [https://www.linkedin.com/in/zeeshan-ali-ai](https://www.linkedin.com/in/zeeshan-ali-ai)
🔗 GitHub: [https://github.com/zeeshanali1009](https://github.com/zeeshanali1009)
