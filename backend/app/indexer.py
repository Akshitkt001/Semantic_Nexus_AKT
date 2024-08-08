from elasticsearch import Elasticsearch
from transformers import pipeline
import numpy as np

# Connect to Elasticsearch
es = Elasticsearch(["http://localhost:9200"])

# Load NLP model for semantic analysis
nlp_model = pipeline("feature-extraction", model="bert-base-uncased")

# Sample documents to be indexed
documents = [
    {"title": "Machine Learning Basics", "content": "Introduction to ML...", "url": "http://example.com/ml-basics"},
    {"title": "Deep Learning Advances", "content": "Deep learning techniques...", "url": "http://example.com/dl-advances"},
    {"title": "Natural Language Processing", "content": "NLP with BERT...", "url": "http://example.com/nlp-bert"},
]

# Index documents
for doc in documents:
    vector = np.mean(nlp_model(doc["content"]), axis=1).tolist()  # Convert numpy array to list
    es.index(index="documents", document={
        "title": doc["title"],
        "content": doc["content"],
        "url": doc["url"],
        "vector": vector
    })

print("Documents indexed successfully.")
