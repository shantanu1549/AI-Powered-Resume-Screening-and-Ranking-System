AI Resume Screening & Ranking System

Overview

The AI Resume Screening & Ranking System is a Streamlit-based web application that automates the process of resume screening and ranking. Users can upload multiple resumes, provide a job description, and get ranked results based on relevance using TF-IDF Vectorization and Cosine Similarity.

Features

Upload multiple PDF resumes
Input a job description for AI matching
Extract text from PDFs using PyPDF2
Rank resumes based on similarity to the job description
Display ranked results in a structured format
Handle missing inputs, corrupted PDFs, and processing errors
Installation

Prerequisites

Ensure you have Python 3.7 or later installed
Clone the Repository
git clone https://github.com/yourusername/AI-Resume-Screening.git
cd AI-Resume-Screening
Install Dependencies
pip install -r requirements.txt
Start the Application
streamlit run app.py
Open the displayed local URL in your web browser

File Structure

.
├── app.py                  # Main Streamlit application
├── utils
│   ├── text_extraction.py  # Extracts text from PDFs
│   ├── resume_ranker.py    # Ranks resumes using TF-IDF & Cosine Similarity
├── requirements.txt        # Required dependencies
├── README.md               # Project documentation

Technologies Used

Python for core programming
Streamlit for the web UI
Scikit-learn for TF-IDF vectorization and Cosine Similarity
Pandas and NumPy for data handling and numerical operations
PyPDF2 for extracting text from PDFs
Error Handling & Edge Cases


Future Enhancements

Integrate deep learning models like BERT/GPT for improved context matching
Add bias detection to ensure fair AI hiring
Expand resume format support to include DOCX, TXT, and image-based OCR processing
Deploy as a cloud-based SaaS with ATS integration
Contributing

To contribute, fork the repository, create a branch, and submit a pull request
