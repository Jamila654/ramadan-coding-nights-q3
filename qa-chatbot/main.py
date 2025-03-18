#type:ignore
import os
import chainlit as cl
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel(model_name='gemini-2.0-flash')


@cl.on_chat_start
async def start():
    await cl.Message(content="Hello! How can I help you today?").send()

@cl.on_message
async def main(message: cl.Message):
    response = model.generate_content(message.content)
    await cl.Message(content=response.text).send()


