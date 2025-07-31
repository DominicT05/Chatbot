from openai import OpenAI
from dotenv import load_dotenv
import os
import requests
import PyPDF2

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
model = "gemini-2.5-flash-lite"
client = OpenAI(base_url=base_url, api_key=api_key)

url = "https://raw.githubusercontent.com/hereandnowai/sathyabama-be-cse-ai-pt1-07-2025-hands-on-professional-training-on-genai-and-ai-agents/main/general-profile-of-hereandnowai.pdf"
response = requests.get(url)
PDF_FILE_NAME = "profile-of-hereandnowai.pdf"
PDF_DIR = os.path.dirname(__file__)
PDF_PATH = os.path.join(PDF_DIR, PDF_FILE_NAME)

with open(PDF_PATH, "wb") as f:
    f.write(response.content)
try:
    with open(PDF_PATH, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        pdf_text_chunks = []
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                pdf_text_chunks.append(page_text.strip())
        pdf_context = "\n".join(pdf_text_chunks) if pdf_text_chunks else "No text found"
except Exception as e:
    print(f"Error reading PDF {e}")
    pdf_context = "Error extracting text from PDF"

def get_response(message, history):
    system_prompt = f"""Context from {PDF_PATH}:\n{pdf_context}
                \n\nQuestion:{message}
                \n\nAnswer based only on the context: """
    messages = [{"role":"system", "content":system_prompt}]
    messages.extend(history)
    messages.append({"role":"user", "content":message})
    response = client.chat.completions.create(model=model, messages=messages)
    ai_response = response.choices[0].message.content
    return ai_response