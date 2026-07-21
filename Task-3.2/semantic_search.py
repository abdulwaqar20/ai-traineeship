from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode("This is a test sentence for semantic search.")

print("Embedding shape:", embeddings.shape)
print("Embedding vector:", embeddings)