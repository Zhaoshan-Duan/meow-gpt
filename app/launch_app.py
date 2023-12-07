# Name: Zhaoshan Duan
# Date: 12/6/2023
# Class: CS 5001
# Description: This file acts as the entry point of the program, 
#   send log in form information to authentication class, 
#   handles UI logic.

import streamlit as st
from chatbot import MeowGPT
import pickle
from pathlib import Path
import streamlit_authenticator as stauth

def user_authentication():
    '''
        User Authentication
    '''
    # existing users
    names = ["Zhaoshan Duan", "Erech"]
    usernames = ["jojo", "erech"]

    # load hashed passwords 
    file_path = Path(__file__).parent / "hash_pw.pkl"

    # open file in write binary mode
    with file_path.open('rb') as file:
        # load in the hashed passwords
        hashed_passwords = pickle.load(file)

    # authentication object
    authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
                                        "meow-gpt", "abcdef", cookie_expiry_days=30)
    
    # get log in from user
    name, authentication_status, username =  authenticator.login("Login", "main")
    
    # check if log in information exists
    if check_authentication_status(authentication_status):
        app(username, authenticator)

def check_authentication_status(authentication_status):
    '''
        Check authentication status
        Parameter:
            authetication_status: boolean
        Return: True if authentication is successful. False otherwise.
    '''
    if authentication_status == False:
        st.error("Username/password is incorrect")
        return False
    
    if authentication_status == None:
        st.warning("Please enter your username and password")
        return False

    if authentication_status:
        return True

def set_up_ui(username, authenticator):
    '''
        Set up Side Bar UI elements
    '''
    with st.sidebar:
        st.title("Meow GPT 😺")
        st.header("Pursonalized Assitant designed to answer cat-related questions.")
        st.subheader("Powered by ChatGPT")
        st.success(f"{username} Connected!")
        authenticator.logout("Logout", "sidebar")

def read_api_key():
    '''
        Read in API key from streamlit secrets
    '''
    return st.secrets['OPENAI_API_KEY']

def app(username, authenticator):
    '''
        Program flow and user interaction controller
    '''

    # set up UI elements
    set_up_ui(username, authenticator)

    # Create an instance of the Chat bot
    chatbot = MeowGPT(read_api_key())

    # check if session_state is empty
    if "messages" not in st.session_state:
        # assign instance attribute messages to the chat history
        st.session_state.messages = chatbot.messages

    # set up chat bot system parameters
    chatbot.set_up_chat()

    # Display chat messages from history
    for message in st.session_state.messages:
        # display role icons with corresponding avatars
        with st.chat_message(message["role"], 
                             avatar = "🗣️" if message["role"] == "user" else "🐱"):
            # for nonsystem roles, display the content
            if not message["role"] == "system":
                st.markdown(message["content"])
            else:
            # for system role, display a greeting
                st.write("Hello👋 5001 Class")

    # React to user input
    if prompt := st.chat_input("Ask a cat-related question..."):
        # display user message icon
        with st.chat_message("user", avatar = '🗣️'):
            # display user message
            st.markdown(prompt)

        # Add user message to the chatbot
        chatbot.add_user_message(prompt)

        # update session_state messages
        st.session_state.messages = chatbot.messages

        # Generate assistant response
        with st.chat_message("assistant", avatar="🐱"):
            # initalize message place holder
            message_placeholder = st.empty()

            # get the generated response from the model
            full_response = chatbot.generate_assistant_response()

            # add the response to the message place holder
            message_placeholder.markdown(full_response + "▌")

        # Add assistant response to the chatbot
        chatbot.add_assistant_message(full_response)
        # update session_state messages
        st.session_state.messages = chatbot.messages
        
    
if __name__ == "__main__":
    # call authentication
    user_authentication()