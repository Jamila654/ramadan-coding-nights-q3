#type: ignore
import streamlit as st
import random
import time

st.set_page_config(page_title="Quiz App", page_icon="🧠", layout="centered")
st.title("Quiz App 🧠")

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Jupiter", "Saturn", "Mars", "Earth"],
        "answer": "Jupiter"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["Au", "Ag", "Fe", "Cu"],
        "answer": "Au"
    },
    {
        "question": "What is the tallest mammal?",
        "options": ["Giraffe", "Elephant", "Horse", "Rhino"],
        "answer": "Giraffe"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": "Pacific Ocean"
    },
]


if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)
    
question = st.session_state.current_question


st.subheader(question["question"])

selected_option = st.radio("Select an option:", question["options"], key="answer")

if st.button("Submit"):
    if selected_option == question["answer"]:
        st.success("✅ Correct!")
        st.balloons()
    else:
        st.error("❌ Incorrect! The correct answer is: " + question["answer"])

    time.sleep(2)
    st.session_state.current_question = random.choice(questions)
    st.rerun()
    
    

