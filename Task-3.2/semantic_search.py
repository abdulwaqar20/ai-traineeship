"""
Task 3.2 - Part 3
Semantic Search using Sentence Transformers

Description:
This program demonstrates semantic search using a pretrained
Sentence Transformer model.

Steps:
1. Load a pretrained embedding model.
2. Create sample documents.
3. Convert documents into embeddings.
4. Accept a user query.
5. Convert query into an embedding.
6. Compute cosine similarity.
7. Return the Top-K most similar documents.
"""

from sentence_transformers import SentenceTransformer
from sentence_transformers import util
import torch

# Load Pretrained Sentence Transformer
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Model Loaded Successfully!\n")

# Sample Documents (20 Documents)
documents = [
    "How to reset your password",
    "How to create a Gmail account",
    "Installing Python on Windows",
    "Learn Machine Learning from scratch",
    "Introduction to Deep Learning",
    "How to delete your Facebook account",
    "Create a virtual environment in Python",
    "Difference between AI and Machine Learning",
    "Learn PyTorch for Deep Learning",
    "What is Transfer Learning",
    "Best programming languages for beginners",
    "Recover your email account",
    "Change your account password",
    "How to use Git and GitHub",
    "Python lists and tuples explained",
    "Train a CNN on CIFAR-10",
    "Fine-tuning a ResNet model",
    "Natural Language Processing basics",
    "Semantic Search using Embeddings",
    "Vector Databases explained"
]

# Convert Documents into Embeddings
print("Creating document embeddings...")
document_embeddings = model.encode(documents, convert_to_tensor=True)
print("Embeddings Created!\n")

# User Query
query = input("Enter your search query: ")

# Convert query into embedding
query_embedding = model.encode(query,convert_to_tensor=True)

# Compute Cosine Similarity
cosine_scores = util.cos_sim(query_embedding,document_embeddings)

# Top-K Results
K = 3
top_results = torch.topk(cosine_scores,k=K)

print("\n")
print("Semantic Search Results")
for rank, (score, index) in enumerate(
    zip(top_results.values[0], top_results.indices[0]),
    start=1
):
    print(f"\nResult {rank}")
    print(f"Document : {documents[index]}")
    print(f"Similarity Score : {score:.4f}")