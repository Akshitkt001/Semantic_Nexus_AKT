from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from googlesearch import search as google_search
import requests
from bs4 import BeautifulSoup
import logging
import google.generativeai as genai
import os

app = FastAPI()

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Manually set your Gemini API key directly in the code
api_key = "AIzaSyC-pZuHFvKldq17d9nGcrGFlWjnNC4t4e8"
genai.configure(api_key=api_key)

# Initialize the Gemini model
model_name = "models/gemini-1.0-pro-latest"  # Ensure this model name is correct
model = genai.GenerativeModel(model_name)

# Set up logging
logging.basicConfig(level=logging.INFO)

def get_ai_response(prompt: str):
    try:
        # Use the Gemini API to generate a response
        response = model.generate_content(prompt)
        generated_text = response.text if response else 'Sorry, I could not generate a response.'
        return generated_text
    except Exception as e:
        logging.error(f"AI response generation error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"AI response generation error: {str(e)}")

@app.get("/search")
async def search(q: str):
    if not q:
        raise HTTPException(status_code=400, detail="Query parameter is required")

    try:
        # Generate AI response based on the query using Gemini API
        ai_response = get_ai_response(q)
        logging.info(f"AI Response: {ai_response}")

        # Search the web for references
        search_results = []
        for url in google_search(q, num_results=5):  # Adjust this line as needed
            try:
                page = requests.get(url, timeout=5)
                soup = BeautifulSoup(page.content, "html.parser")
                title = soup.title.string if soup.title else url
                snippet = " ".join([p.get_text() for p in soup.find_all('p')][:2])
                search_results.append({"title": title, "url": url, "snippet": snippet})
            except requests.exceptions.RequestException as e:
                logging.error(f"Failed to fetch {url}: {e}")
                search_results.append({"title": "Failed to fetch", "url": url, "snippet": str(e)})

        # Return AI response along with search results
        return {"results": search_results, "ai_response": ai_response}
    except Exception as e:
        logging.error(f"AI service error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"AI service error: {str(e)}")
