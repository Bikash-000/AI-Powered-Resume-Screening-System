
import streamlit as st
import pandas as pd


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide"
)


# -----------------------------
# Title
# -----------------------------

st.title("📄 AI-Powered Resume Screening System")

st.write(
    "NLP-based resume screening, skill gap analysis, "
    "ATS scoring and candidate ranking dashboard."
)


# -----------------------------
# Load Excel Report
# -----------------------------

try:

    df = pd.read_excel(
        "Resume_Screening_Report.xlsx"
    )

except FileNotFoundError:

    st.error(
        "Resume_Screening_Report.xlsx not found. "
        "Please run the screening cells first."
    )

    st.stop()


# -----------------------------
# Top Candidate
# -----------------------------

top_candidate = df.iloc[0]


st.subheader("🏆 Top Candidate")


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "Candidate",
        top_candidate["Resume"]
    )


with col2:

    st.metric(
        "Final Score",
        f'{top_candidate["Final Score"]:.2f}'
    )


with col3:

    st.metric(
        "ATS Score",
        f'{top_candidate["ATS Score"]:.2f}'
    )


with col4:

    st.metric(
        "Recommendation",
        top_candidate["Recommendation"]
    )


# -----------------------------
# Candidate Ranking
# -----------------------------

st.subheader("📊 Candidate Ranking")

st.dataframe(
    df,
    use_container_width=True
)


# -----------------------------
# Candidate Filter
# -----------------------------

st.subheader("🔎 Filter Candidates")

minimum_score = st.slider(
    "Minimum Final Score",
    min_value=0.0,
    max_value=100.0,
    value=0.0,
    step=1.0
)


filtered_df = df[
    df["Final Score"] >= minimum_score
]


st.dataframe(
    filtered_df,
    use_container_width=True
)


# -----------------------------
# Final Score Chart
# -----------------------------

st.subheader("🏆 Final Score")

st.bar_chart(
    df.set_index("Resume")["Final Score"]
)


# -----------------------------
# ATS Score Chart
# -----------------------------

st.subheader("🎯 ATS Score")

st.bar_chart(
    df.set_index("Resume")["ATS Score"]
)


# -----------------------------
# Skill Score Chart
# -----------------------------

st.subheader("🛠️ Skill Match Score")

st.bar_chart(
    df.set_index("Resume")["Skill Score"]
)


# -----------------------------
# Skill Gap Analysis
# -----------------------------

st.subheader("🔍 Skill Gap Analysis")


selected_resume = st.selectbox(
    "Select Candidate",
    df["Resume"]
)


candidate = df[
    df["Resume"] == selected_resume
].iloc[0]


col1, col2 = st.columns(2)


with col1:

    st.write("### ✅ Matched Skills")

    matched = candidate["Matched Skills"]

    if matched:

        for skill in matched.split(", "):

            st.success(skill)

    else:

        st.info("No matching skills found.")


with col2:

    st.write("### ❌ Missing Skills")

    missing = candidate["Missing Skills"]

    if missing:

        for skill in missing.split(", "):

            st.error(skill)

    else:

        st.success(
            "No major missing skills!"
        )


# -----------------------------
# Download Report
# -----------------------------

st.subheader("📥 Download Report")


with open(
    "Resume_Screening_Report.xlsx",
    "rb"
) as file:

    st.download_button(
        label="Download Excel Report",
        data=file,
        file_name="Resume_Screening_Report.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )


# -----------------------------
# Footer
# -----------------------------

st.markdown("---")

st.write(
    "Built using Python, NLP, spaCy, Scikit-Learn, "
    "TF-IDF, Cosine Similarity, Pandas and Streamlit."
)
