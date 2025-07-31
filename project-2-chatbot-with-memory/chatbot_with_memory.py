from openai import OpenAI
from dotenv import load_dotenv 
import os 
from prompts import ai_travel_guide

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
model="gemini-2.5-flash-lite"
base_url="https://generativelanguage.googleapis.com/v1beta/openai"

client = OpenAI(base_url=base_url, api_key=api_key)

ai_travel_guide=ai_travel_guide

def get_response(message, history):
    messages = [{"role":"system", "content": ai_travel_guide}]
    messages.extend(history)
    messages.append({"role":"user", "content":message})
    response = client.chat.completions.create(model=model, messages=messages)
    ai_response = response.choices[0].message.content
    return ai_response
