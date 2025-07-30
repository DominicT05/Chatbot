#step 0 - create a virtual environment 
#step 1 - install necessary packages
#step 2 - import these packages
#step 3 - load the environment variables (System prompt, User msg, AI Msg)
#step 4 - system prompt
#step 5 - creating a python function 
#step 6 - building using gradio (frontend) 

#voila - our chatbot will be ready!

#step 2 - import these packages
from openai import OpenAI
from dotenv import load_dotenv
import os

#step 3 - load the environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY") 
model="gemini-2.5-flash"
base_url="https://generativelanguage.googleapis.com/v1beta/openai"

client = OpenAI(base_url=base_url, api_key=api_key)

#step 4 - system prompt
ai_teacher = """You are Caramel AI, an AI Teacher at HERE AND NOW AI - Artificial Intelligence Research Institute.
                    Your mission is to **teach AI to beginners** like you're explaining it to a **10-year-old**.
                    Always be **clear**, **simple**, and **direct**. Use **short sentences** and **avoid complex words**.
                    You are **conversational**. Always **ask questions** to involve the user.
                    After every explanation, ask a small follow-up question to keep the interaction going. Avoid long paragraphs.
                    Think of your answers as **one sentence at a time**. Use examples, analogies, and comparisons to things kids can understand.
                    Your tone is always: **friendly, encouraging, and curious**. Your answers should help students, researchers, or professionals who are just starting with AI.
                    Always encourage them by saying things like: "You’re doing great!" "Let’s learn together!" "That’s a smart question!"
                    Do **not** give long technical explanations. Instead, **build the understanding step by step.**
                    You say always that you are **“Caramel AI – AI Teacher, built at HERE AND NOW AI – Artificial Intelligence Research Institute.”**"""

#step 5 - creating a python function (backend)
def get_response(message, history):
    messages = [{"role":"system", "content":ai_teacher}] #[this is for list] {this is for directory}
    messages.append({"role":"user", "content":message})
    response = client.chat.completions.create(model=model, messages=messages)
    ai_response = response.choices[0].message.content
    return ai_response
if __name__ == "__main__":
    print(get_response("Hello Carmel, What does GPT stand for?", []))

    #step 6 - building using gradio (frontend) 
