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


## 📊 Sample Output

The application displays candidate information such as:

| Resume | Similarity | Matched Skills | ATS Score | Final Score |
|---|---:|---:|---:|---:|
| resume2.pdf | 37.78% | 10 | 62.5 | 55.68 |
| resume3.pdf | 24.89% | 3 | 18.75 | 20.89 |
| resume1.pdf | 3.13% | 2 | 12.5 | 9.68 |

Candidates are automatically ranked based on their final scores.

## 📁 Project Structure

```text
AI-Powered-Resume-Screening-System/
│
├── app.py
├── project.ipynb
├── requirements.txt
├── README.md
├── job_description.txt
│
├── resumes/
│   ├── resume1.pdf
│   ├── resume2.pdf
│   └── resume3.pdf
│
└── outputs/
    └── Resume_Screening_Report.xlsx

## ⚙️ Installation

### 1. Clone the repository

bash
git clone https://github.com/Bikash-000/AI-Powered-Resume-Screening-System.git


### 2. Go to the project folder

bash
cd AI-Powered-Resume-Screening-System


### 3. Install dependencies

bash
pip install -r requirements.txt


### 4. Download the spaCy English model

bash
python -m spacy download en_core_web_sm


## ▶️ How to Run

Run the Streamlit application:

bash
streamlit run app.py


The application will open in your browser.

## 📌 How It Works

1. Upload the job description.
2. Upload multiple candidate resumes.
3. The system extracts text from the resumes.
4. NLP preprocessing is performed using spaCy.
5. Required skills are extracted.
6. TF-IDF converts text into numerical vectors.
7. Cosine Similarity calculates resume-job similarity.
8. ATS scores are calculated.
9. Candidates are ranked according to their final scores.
10. Skill gaps are identified.
11. Results are exported to Excel.
12. Results are displayed through the Streamlit dashboard.

## 🎯 Project Objective

The main objective of this project is to automate the initial resume screening process and help recruiters quickly identify candidates whose skills and experience best match a given job description.

## 🔮 Future Enhancements

- BERT/Transformer-based semantic matching
- Advanced skill extraction
- DOCX resume support
- Resume quality scoring
- Candidate recommendation system
- Database integration
- Permanent deployment using Streamlit Cloud
- Recruiter authentication

## 👨‍💻 Author

*Bikash Ranjan Dhir*

🎓 B.Tech — CSE (Data Science)

📍 Bhubaneswar, India

🔗 GitHub: https://github.com/Bikash-000

## ⭐ If You Like This Project

If you find this project useful, consider giving the repository a ⭐ star!
