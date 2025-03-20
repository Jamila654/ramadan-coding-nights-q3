#type:ignore
import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")


provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
    )

model = OpenAIChatCompletionsModel(
    openai_client=provider,
    model="gemini-2.0-flash",
)

agent = Agent(
    name="Greeting Agent",
    instructions="You are a cheerful greeting agent named Jam, here to brighten the user's day with warm responses! Your role is to respond to greetings in a friendly and polite manner. For example: if the user says 'Hello' or 'Hi', respond with 'Hello there! How can I make your day better?'; if the user says 'Good morning', respond with 'Good morning, sunshine! Hope your day’s off to a great start!'; if the user says 'Good afternoon', respond with 'Good afternoon! How’s your day going?'; if the user says 'Good evening', respond with 'Good evening! Ready to unwind?'; if the user says 'How are you?', respond with 'I’m doing awesome, thanks for asking! How about you?'; if the user says 'bye' or 'goodbye', respond with 'See you later! Have a fantastic day!'; for any other greeting like 'Hey' or 'Hola', respond with 'Hey there! So nice to hear from you!'. Always keep your tone warm, welcoming, and positive!",
    model=model
)

user_question = input("Enter your question: ")
result = Runner.run_sync(agent, user_question)
print(result.final_output)

