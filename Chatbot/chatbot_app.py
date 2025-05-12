import streamlit as st
from chatbot_setup import ask_question

st.set_page_config(page_title="Mental Health Chatbot", page_icon="🧠")

st.title("🧠 Mental Health Risk Analysis Chatbot")
st.write("Ask any question about mental health.")

user_input = st.text_input("Your Question:")

if user_input:
    response = ask_question(user_input)
    st.markdown("### Answer:")
    st.write(response)
