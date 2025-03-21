#type:ignore
import os
import chainlit as cl
from dotenv import load_dotenv
from typing import Optional, Dict, Any
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel,function_tool
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
github_client_id = os.getenv("OAUTH_GITHUB_CLIENT_ID")
github_client_secret = os.getenv("OAUTH_GITHUB_CLIENT_SECRET")


provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
    )

model = OpenAIChatCompletionsModel(
    openai_client=provider,
    model="gemini-2.0-flash",
)

@function_tool("get_weather")
async def get_weather(location: str, unit: str = "C") -> str:
    """
    Fetches the weather for a given location and returns a response.

    """
    return f"The weather in {location} is 30 degrees {unit} and sunny today!"




agent = Agent(
    name="Greeting Agent",
    instructions="You are a cheerful greeting agent named Jam, here to brighten the user's day with warm responses! Your role is to respond to greetings in a friendly and polite manner. For example: if the user says 'Hello' or 'Hi', respond with 'Hello there! How can I make your day better?'; if the user says 'Good morning', respond with 'Good morning, sunshine! Hope your day’s off to a great start!'; if the user says 'Good afternoon', respond with 'Good afternoon! How’s your day going?'; if the user says 'Good evening', respond with 'Good evening! Ready to unwind?'; if the user says 'How are you?', respond with 'I’m doing awesome, thanks for asking! How about you?'; if the user says 'bye' or 'goodbye', respond with 'See you later! Have a fantastic day!'; for any other greeting like 'Hey' or 'Hola', respond with 'Hey there! So nice to hear from you!'. Always keep your tone warm, welcoming, and positive! if the user asks for the weather, provide the weather in their location.",
    model=model,
    tools=[get_weather],
)

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
    result = await cl.make_async(Runner.run_sync)(agent, input=history)
    response_text = result.final_output
    await cl.Message(content=response_text).send()
    history.append({"role": "assistant", "content": response_text})
    cl.user_session.set("history", history)