import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat():
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )

        reply = response.choices[0].message.content
        print("Bot:", reply)

chat()