# backend/app/models.py

from pydantic import BaseModel

# Define a data model for documents to be indexed
class Document(BaseModel):
    title: str
    content: str
    url: str
    vector: list
