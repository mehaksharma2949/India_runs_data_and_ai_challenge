from sentence_transformers import SentenceTransformer
from config import MODEL_NAME

print("Loading embedding model...")

model = SentenceTransformer(MODEL_NAME)

print("Model Loaded Successfully!")

sample = "Python SQL Machine Learning"

embedding = model.encode(sample)

print("Embedding Length:", len(embedding))