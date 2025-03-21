#type:ignore
import os
import chainlit as cl
import google.generativeai as genai
from dotenv import load_dotenv
from typing import Optional, Dict, Any

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
github_client_id = os.getenv("OAUTH_GITHUB_CLIENT_ID")
github_client_secret = os.getenv("OAUTH_GITHUB_CLIENT_SECRET")

genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel(model_name='gemini-2.0-flash')

@cl.oauth_callback
def oauth_callback(
    provider_id: str,
    token: str,
    raw_user_data: Dict[str, str],
    default_user: cl.User,
) -> Optional[cl.User]:
    """_summary_
    handle oauth callback and return user object
    """
    print(f"provider_id: {provider_id}")
    print(f"token: {token}")
    print(f"raw_user_data: {raw_user_data}")
    print(f"default_user: {default_user}")
    return default_user

@cl.on_chat_start
async def start():
    
    cl.user_session.set("history",[])
    await cl.Message(content="Hello! How can I help you today?").send()
@cl.on_message
async def main(message: cl.Message):
    history = cl.user_session.get("history")
    history.append({"role": "user", "content": message.content})
    response = model.generate_content(message.content)
    formatted_history = []
    for msg in history:
        role = "user" if msg["role"] == "user" else "assistant"
        formatted_history.append({"role": role, "parts": [{"text": msg["content"]}]})
    response = model.generate_content(formatted_history)
    history.append({"role": "assistant", "content": response.text})
    cl.user_session.set("history", history)
    await cl.Message(content=response.text).send()