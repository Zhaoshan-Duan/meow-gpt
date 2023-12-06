import streamlit as st
from chatbot import MeowGPT
import openai

def set_up_ui():
    with st.sidebar:
        st.title("Meow GPT 😺")
        st.header("Pursonalized Assitant designed to answer cat-related questions.")
        st.subheader("Powered by ChatGPT")
        st.success("Connected!")

def read_api_key():
    return st.secrets['OPENAI_API_KEY']
    # st.success('API key provided', icon = '✅')

def app():
    set_up_ui()

    # Create an instance of the Chat bot

    chatbot = MeowGPT(read_api_key())

    if "messages" not in st.session_state:
        st.session_state.messages = chatbot.messages

    # set up chat bot system parameters
    chatbot.set_up_chat()

    # Display chat messages from history
    for message in st.session_state.messages:
        with st.chat_message(message["role"], 
                             avatar = "🗣️" if message["role"] == "user" else "🐱"):
            if not message["role"] == "system":
                st.markdown(message["content"])
            else:
                st.write("Hello👋")

    # React to user input
    if prompt := st.chat_input("Ask a cat-related question..."):
        with st.chat_message("user", avatar = '🗣️'):
            st.markdown(prompt)

        # Add user message to the chatbot
        chatbot.add_user_message(prompt)
        st.session_state.messages = chatbot.messages

        # Generate assistant response
        with st.chat_message("assistant", avatar="🐱"):
            message_placeholder = st.empty()
            full_response = chatbot.generate_assistant_response()
            message_placeholder.markdown(full_response + "▌")

        # Add assistant response to the chatbot
        chatbot.add_assistant_message(full_response)
        st.session_state.messages = chatbot.messages
        
    
if __name__ == "__main__":
    app()