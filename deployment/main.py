#type: ignore
import streamlit as st

st.set_page_config(page_title="Simple Streamlit App", page_icon=":smiley:")
st.title("Simple Streamlit App")
 
user_input = st.text_input("Enter some text:")

if st.button("Show Text"):
     st.write(f"You entered: {user_input}") 
     

st.write("---")
st.write("Made with :heart: by Jam")
