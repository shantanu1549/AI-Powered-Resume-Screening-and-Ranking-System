import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def rank_resumes(job_description, resumes, filenames):
    """Ranks resumes based on similarity to the job description using TF-IDF & Cosine Similarity."""
    if not resumes:
        return []

    documents = [job_description] + resumes
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    
    # Compute Cosine Similarity
    job_vector = tfidf_matrix[0]
    resume_vectors = tfidf_matrix[1:]
    scores = cosine_similarity(job_vector, resume_vectors).flatten()

    # Assign ranking based on scores
    sorted_results = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)
    ranked_resumes = [{"rank": i+1, "resume": filenames[idx], "score": score} for i, (idx, score) in enumerate(sorted_results)]

    return ranked_resumes

def save_results_to_csv(ranked_resumes, filename="resume_ranking.csv"):
    """Saves ranking results as a CSV file."""
    df = pd.DataFrame({
        "Rank": [res["rank"] for res in ranked_resumes],
        "Resume": [res["resume"] for res in ranked_resumes],
        "Score": [round(res["score"], 2) for res in ranked_resumes]
    })
    df.to_csv(filename, index=False)
    return filename
