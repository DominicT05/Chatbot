import gradio as gr
from text_rag import get_response
import json 
import os

with open(os.path.abspath(os.path.join(os.path.dirname(__file__), "branding.json"))) as f:
    brand_info = json.load(f)["brand"]

with gr.Blocks(theme = "default", title=brand_info["organizationName"]) as rag_bot:
    gr.HTML(f"""<div style="display: flex; justify-content: center; margin-bottom: 20px;">
            <img src="{brand_info["logo"]["title"]}" alt="{brand_info["organizationName"]} Logo" style="height=100px;">
            </div>""")
    gr.ChatInterface(
        fn=get_response,
        chatbot=gr.Chatbot(height=500, 
                           avatar_images=(None, brand_info["chatbot"]["avatar"]),
                           type="messages"),
        title=brand_info["organizationName"],
        description=brand_info["slogan"],
        type="messages",
        examples=[
            ["What is HERE AND NOW AI?"],
            ["What is the mission of HERE AND NOW AI?"],
            ["Who is Madame Deepti?"],
            ["What courses does HERE AND NOW AI offer?"],
            ["Who is the CTO of HERE AND NOW AI?"],
            ["What is the 'Business Analytics with AI' course?"],
            ["What is the 'Full-Stack AI Developer Program'?"],
            ["What is the contact information for HERE AND NOW AI?"],
        ]
    )

if __name__ == "__main__":
    rag_bot.launch()
