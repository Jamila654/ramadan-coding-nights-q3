#type: ignore
import streamlit as st
import random
import string

st.set_page_config(page_title="Password Generator", page_icon=":lock:", layout="centered")

def generate_password(length, use_digits, use_special_chars):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

st.title("Password Generator")

length = st.slider("Select Password Length", min_value=8, max_value=32, value=12)
use_digits = st.checkbox("Include Digits")
use_special_chars = st.checkbox("Include Special Characters")

if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special_chars)
    st.write(f"Generated Password: `{password}`")
 
st.write("---")   
st.write("Made with :heart: by Jam")

st.write("This app is open source and available on [GitHub](https://github.com/Jamila654/ramadan-coding-nights-q3)")


    
    


