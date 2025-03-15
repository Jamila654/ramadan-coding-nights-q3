#type:ignore
import streamlit as st
import requests


st.set_page_config(
    page_title="Random Joke Generator",
    page_icon="🤡",
 )

def get_random_joke():
    """Fetch a random joke from the joke API."""
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        if response.status_code == 200:
            joke_data = response.json()
            return f"setup: {joke_data['setup']} \n\n punchline: {joke_data['punchline']}"
        else:
            return "Error fetching joke. Please try again later."
        
    except requests.RequestException as e:
        st.error(f"Error: {e}")
        return

def main():
    """Main function to run the Streamlit app."""
    st.title("Random Joke Generator")
    st.write("Click the button to get a random joke!")
    if st.button("Get Random Joke"):
        joke = get_random_joke()
        if joke:
            st.success(joke)
        else:
            st.error("Error fetching joke. Please try again later.")
    st.divider()
    st.markdown(
    """
    <div style="text-align: center;">
    <p>Joke from Official Joke API</p>
    <p>Build with ❤️ by <a href="https://github.com/Jamila654/ramadan-coding-nights-q3">Jam</a> using streamlit</p>
    </div>
    <style>
        .stButton>button {
            width: 100%;
            background-color: #00C4B4;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        .stButton>button:hover {
            background-color: #4DD0E1;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
     



if __name__ == "__main__":
    main()


