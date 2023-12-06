import streamlit as st


from chatbot import MeowGPT

class UIHandler:
    @staticmethod
    def set_up_sidebar():
        st.title("🐈‍⬛💬 Meow GPT")

    @staticmethod
    def display_chat(messages):
        for msg in messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

    @staticmethod
    def get_user_input():
        return st.chat_input("Get user input")

def config():
    with st.sidebar:
        

    # save the messages
    if "messages" not in st.session_state:
        st.session_state.message = []

    # intialize the bot class
    
    
