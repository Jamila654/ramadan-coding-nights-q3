#type:ignore
import streamlit as st
import random
import time
import requests

st.set_page_config(page_title="Money Making Machine", page_icon=":moneybag:", layout="centered")

st.title("Money Making Machine")

def generate_money():
    return random.randint(1, 1000)

st.subheader("Instant money making machine")
if st.button("Generate Money"):
    st.write("Generating money...")
    time.sleep(2)
    money = generate_money()
    st.success(f"You generated ${money}!")
    st.balloons()


def fetch_side_hustle():
    try:
        response = requests.get('http://127.0.0.1:8000/side_hustles?api_key=secret')
        if response.status_code == 200:
            hustles = response.json()
            return hustles
        else:
            return {"error": "Failed to fetch side hustle"}
    except:
        return {"error": "An error occurred"}
    
st.subheader("Side Hustle Generator")
if st.button("Generate Side Hustle"):
    st.write("Generating side hustle...")
    time.sleep(2)
    hustle = fetch_side_hustle()
    if "error" in hustle:
        st.error(hustle["error"])
    else:
        st.success(f"Your side hustle: {hustle['side_hustle']}")

def fetch_money_quote():
    try:
        response = requests.get('http://127.0.0.1:8000/money_quotes?api_key=secret')
        if response.status_code == 200:
            quote = response.json()
            return quote
        else:
            return {"error": "Failed to fetch money quote"}
    except:
        return {"error": "An error occurred"}


st.subheader("Money Quote Generator")
if st.button("Generate Money Quote"):
    st.write("Generating money quote...")
    time.sleep(2)
    quote = fetch_money_quote()
    if "error" in quote:
        st.error(quote["error"])
    else:
        st.success(f"Your money quote: {quote['money_quote']}")
    