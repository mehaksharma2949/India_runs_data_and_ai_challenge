from docx import Document
from pathlib import Path
import re

BASE_DIR = Path(__file__).resolve().parent.parent


def load_job_description():
    doc = Document(BASE_DIR / "job_description.docx")

    text = ""

    for para in doc.paragraphs:
        text += para.text + "\n"

    return text


def extract_keywords(text):

    keywords = [
        "python",
        "sql",
        "machine learning",
        "deep learning",
        "llm",
        "rag",
        "nlp",
        "embedding",
        "vector database",
        "recommendation",
        "aws",
        "azure",
        "pytorch",
        "tensorflow",
        "transformer",
    ]

    found = []

    lower = text.lower()

    for word in keywords:
        if word in lower:
            found.append(word)

    return found


if __name__ == "__main__":

    jd = load_job_description()

    skills = extract_keywords(jd)

    print("\nDetected Skills\n")

    print(skills)