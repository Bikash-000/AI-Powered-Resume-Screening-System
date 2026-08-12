# 📄 AI-Powered Resume Screening System

An AI-powered resume screening and candidate ranking system built using **Python, NLP, Scikit-learn, spaCy, Pandas, and Streamlit**.

The system automatically analyzes resumes against a given job description, extracts relevant skills, calculates ATS scores, ranks candidates, and generates an Excel report.

---

## 🌐 Live Demo

🔗 **Open AI-Powered Resume Screening System**

> https://reset-prowling-coyness.ngrok-free.dev/

---

## 🚀 Features

### 📄 Resume Processing
- Upload multiple resumes in PDF format
- Extract text automatically from resumes
- Support for resume analysis and comparison

### 📝 Job Description Analysis
- Upload or provide a job description
- Extract required skills from the job description
- Compare candidate skills with job requirements

### 🤖 AI-Based Resume Matching
- NLP-based text preprocessing using spaCy
- TF-IDF Vectorization
- Cosine Similarity for resume-job matching

### 📊 ATS Score
- Calculates an ATS score for each candidate
- Measures matching skills
- Identifies relevant candidate profiles

### 🏆 Candidate Ranking
- Automatically ranks candidates based on their final score
- Displays similarity score and ATS score
- Helps recruiters identify suitable candidates quickly

### 🔍 Skill Gap Analysis
- Identifies matched skills
- Identifies missing or required skills
- Helps candidates understand their skill gaps

### 📑 Excel Report
- Generates an Excel report containing:
  - Candidate name
  - Extracted skills
  - Matched skills
  - ATS score
  - Similarity score
  - Final score
  - Candidate ranking

### 📈 Interactive Dashboard
- Built using Streamlit
- Displays candidate ranking in a table
- Visualizes final candidate scores using charts

---

## 🛠️ Technologies Used

- **Python**
- **Natural Language Processing (NLP)**
- **spaCy**
- **Scikit-learn**
- **TF-IDF**
- **Cosine Similarity**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Streamlit**
- **PDFPlumber**
- **OpenPyXL**
- **Google Colab**

---

## 🧠 System Workflow

```text
Job Description
       ↓
Text Preprocessing
       ↓
Skill Extraction
       ↓
Resume Upload
       ↓
PDF Text Extraction
       ↓
NLP Preprocessing
       ↓
TF-IDF Vectorization
       ↓
Cosine Similarity
       ↓
ATS Score
       ↓
Candidate Ranking
       ↓
Skill Gap Analysis
       ↓
Excel Report
       ↓
Streamlit Dashboard
