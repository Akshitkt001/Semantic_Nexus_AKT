from elasticsearch import Elasticsearch, exceptions as es_exceptions
from transformers import pipeline

# Connect to Elasticsearch
es = Elasticsearch(["http://localhost:9301"])

# Load NLP model for semantic analysis
nlp_model = pipeline("feature-extraction", model="bert-base-uncased")

def search_documents(query: str, user_data: dict):
    try:
        # Perform semantic analysis on the query
        query_vector = nlp_model(query)[0][0]  # Adjusted indexing for correct vector extraction

        # Ensure the vector is a list or array and has the correct shape
        if not isinstance(query_vector, list) or len(query_vector) == 0:
            raise ValueError("Query vector is empty or not in the expected format")

        # Elasticsearch semantic search using vectors
        search_body = {
            "size": 10,
            "query": {
                "script_score": {
                    "query": {"match_all": {}},
                    "script": {
                        "source": "cosineSimilarity(params.query_vector, 'vector') + 1.0",
                        "params": {"query_vector": query_vector},
                    },
                }
            },
        }

        # Execute search query
        response = es.search(index="documents", body=search_body)

        # Extract search results
        results = [
            {"title": hit["_source"].get("title", "No Title"), "url": hit["_source"].get("url", "No URL")}
            for hit in response["hits"]["hits"]
        ]

        return results

    except es_exceptions.ConnectionError:
        print("Error connecting to Elasticsearch")
        return []
    except es_exceptions.RequestError as e:
        print(f"Elasticsearch request error: {e}")
        return []
    except ValueError as ve:
        print(f"Value error: {ve}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []
