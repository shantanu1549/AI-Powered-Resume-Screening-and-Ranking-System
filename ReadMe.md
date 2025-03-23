# **AI Resume Screening & Ranking System**  

## **Overview**  
The **AI Resume Screening & Ranking System** is a **Streamlit-based web application** that helps automate **resume screening and ranking** based on a provided **job description**. It uses **Natural Language Processing (NLP) techniques** such as **TF-IDF Vectorization and Cosine Similarity** to rank resumes by relevance.  

## **Features**  
- Upload multiple **PDF resumes**.  
- Enter a **job description** for AI matching.  
- Extract text from resumes using **PyPDF2**.  
- Rank resumes based on **semantic similarity** to the job description.  
- Display **ranked results** in an easy-to-read format.  
- **Error handling** for corrupted files, missing inputs, and unsupported formats.  

## **Technologies Used**  
- **Python** - Core programming language  
- **Streamlit** - Web UI framework  
- **Scikit-learn** - TF-IDF vectorization & Cosine Similarity  
- **Pandas & NumPy** - Data handling & numerical operations  
- **PyPDF2** - Extracting text from PDFs  

## **Installation**  

### **Prerequisites**  
Ensure you have **Python 3.7+** installed.  

### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/yourusername/AI-Resume-Screening.git
cd AI-Resume-Screening
```

### **2️⃣ Install Dependencies**  
```sh
pip install -r requirements.txt
```

### **3️⃣ Run the Application**  
```sh
streamlit run app.py
```
- Open the displayed **local URL** in your web browser.  

## **File Structure**  
```
.
├── app.py                  # Main Streamlit application
├── utils/
│   ├── text_extraction.py  # Extracts text from PDFs
│   ├── resume_ranker.py    # Ranks resumes using TF-IDF & Cosine Similarity
├── requirements.txt        # Required dependencies
├── README.md               # Project documentation
```

## **How It Works?**  

### ** Step 1: Upload Resumes**  
- Select and upload **multiple PDF resumes**.  
- Enter a **job description** to compare resumes against.  

### ** Step 2: AI-Powered Resume Ranking**  
- Extracts resume text using **PyPDF2**.  
- Applies **TF-IDF & Cosine Similarity** for resume-job description matching.  
- Ranks resumes based on relevance.  

### ** Step 3: View & Download Results**  
- Displays **ranked resumes in a structured table**.  
- Option to **download ranked resumes as a CSV file**.  

## **Contributing**  
Want to contribute? Fork the repository, create a branch, and submit a pull request.  
