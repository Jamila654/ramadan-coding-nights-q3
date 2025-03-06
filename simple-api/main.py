#type: ignore
from fastapi import FastAPI
import random

app = FastAPI()

# we will buil 2 simple get endponts
#side hustles
# money_quotes

side_hustles = [
    "Start a blog",
    "Freelance",
    "Sell products online",
    "Teach online",
    "Consulting",
    "Social media management",
    "Virtual assistant",
    "Web design",
    "Graphic design",
    "Photography",
    "Videography",
    "Content writing",
    "SEO",
]


money_quotes = [
    "Money doesn't grow on trees, you know.",
    "A penny saved is a penny earned.",
    "Money can't buy happiness.",
    "Money is the root of all evil.",
    "Money talks.",
    "Money makes the world go round.",
    "Money is the root of all evil.",
    "Money can't buy love.",
    "Money doesn't grow on trees.",
    "Money can't buy you happiness.",
    "Money is the root of all evil.",
    "Money can't buy happiness.",
    "Money is the root of all evil.",
    "Money can't buy love.",
]

@app.get("/side_hustles")
def get_side_hustles(api_key: str):
    """Return a random side hustle"""
    if api_key != "secret":
        return {"error": "Invalid API Key"}
    return {"side_hustle": random.choice(side_hustles)}

@app.get("/money_quotes")
def get_money_quotes(api_key: str):
    """Return a random money quote"""
    if api_key != "secret":
        return {"error": "Invalid API Key"}
    return {"money_quote": random.choice(money_quotes)}


