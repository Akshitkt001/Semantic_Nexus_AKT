# backend/app/config.py

import os

# Configuration settings for Elasticsearch and MongoDB
ELASTICSEARCH_HOST = os.getenv("ELASTICSEARCH_HOST", "http://localhost:9200")
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017/")
