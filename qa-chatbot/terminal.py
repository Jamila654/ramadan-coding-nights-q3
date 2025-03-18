#type:ignore
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

model = genai.GenerativeModel(model_name='gemini-2.0-flash')

user_input = input("Enter your question or message (or 'exit' to quit): ")


while user_input.lower() != "exit":
    try:
        response = model.generate_content(user_input)
        print("\nAI Response:", response.text)
    except Exception as e:
        print(f"\nAn error occurred: {e}")
    
    user_input = input("\nEnter your question or message (or 'exit' to quit): ")

print("\nGoodbye! 👋")


