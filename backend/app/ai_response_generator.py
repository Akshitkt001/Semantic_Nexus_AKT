from transformers import pipeline

# Load AI model
ai_model = pipeline("text-generation", model="gpt-3.5-turbo")

def generate_ai_response(query: str):
    response = ai_model(query, max_length=50, num_return_sequences=1)
    return response[0]['generated_text']
