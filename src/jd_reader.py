from docx import Document
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

doc = Document(BASE_DIR / "job_description.docx")

text = ""

for para in doc.paragraphs:
    text += para.text + "\n"

print(text)