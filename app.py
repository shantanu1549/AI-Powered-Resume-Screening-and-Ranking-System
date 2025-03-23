import streamlit as st
import pandas as pd
import PyPDF2
from utils.text_extraction import extract_text_from_pdf
from utils.resume_ranker import rank_resumes

# Set page configuration
st.set_page_config(
    page_title="AI Resume Screening & Ranking",
    page_icon="📄",
    layout="wide"
)

# Custom CSS for Styling
st.markdown(
    """
    <style>
        .stApp { background-color: #0B3D91; color: white; }
        h1 { text-align: center; font-size: 34px; font-weight: bold; }
        .stButton>button { background-color: #FFD700 !important; color: black !important; }
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.markdown("<h1>📄 AI Resume Screening & Ranking System</h1>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# Using Columns for Layout
col1, col2 = st.columns([1, 1])  # Equal width columns

with col1:
    st.header("📝 Job Description")
    job_description = st.text_area("Enter the job description", height=200, placeholder="Type or paste job description here...")

with col2:
    st.header("📤 Upload Resumes")
    uploaded_files = st.file_uploader("Upload multiple resumes (PDF only)", type=['pdf'], accept_multiple_files=True)

# Initialize validation flags
error_flag = False

# Rank Resumes Button with Error Handling
if st.button("📊 Rank Resumes"):

    # Error Handling: Check if Job Description is Missing
    if not job_description.strip():
        st.error("❌ Error: Please enter a job description before ranking resumes.")
        error_flag = True

    # Error Handling: Check if No Files Are Uploaded
    if not uploaded_files:
        st.error("❌ Error: No resumes uploaded. Please upload at least one PDF file.")
        error_flag = True

    resumes_text = []
    filenames = []

    if not error_flag:  # Proceed only if there are no input errors
        # Error Handling for Empty or Corrupt Files
        for file in uploaded_files:
            try:
                text = extract_text_from_pdf(file)
                if not text.strip():
                    st.error(f"❌ Error: {file.name} appears to be empty or unreadable.")
                    continue
                resumes_text.append(text)
                filenames.append(file.name)
            except PyPDF2.errors.PdfReadError:
                st.error(f"❌ Error: {file.name} is a corrupted or unsupported PDF file.")
                continue
            except Exception as e:
                st.error(f"❌ Unexpected error while processing {file.name}: {str(e)}")
                continue

        # Check if any valid resumes were processed
        if not resumes_text:
            st.warning("⚠️ No valid resumes were processed. Please check the uploaded files.")
        else:
            try:
                # Rank Resumes
                ranked_resumes = rank_resumes(job_description, resumes_text, filenames)

                # Display Results
                if ranked_resumes:
                    st.markdown("<h2>🏆 Ranked Resumes</h2>", unsafe_allow_html=True)
                    results_df = pd.DataFrame(ranked_resumes)[["rank", "resume", "score"]].rename(columns={"rank": "Rank", "resume": "Resume", "score": "Score"})
                    st.dataframe(results_df, use_container_width=True)
                else:
                    st.warning("⚠️ No resumes could be ranked. Please ensure the job description is relevant.")

            except Exception as e:
                st.error(f"❌ Unexpected error occurred during ranking: {str(e)}")

