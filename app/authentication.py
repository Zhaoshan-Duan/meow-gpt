# Name: Zhaoshan Duan
# Date: 12/6/2023
# Class: CS 5001
# Description: This file authenticates users using streamlit's authentication object
import pickle
from pathlib import Path
import streamlit_authenticator as stauth
import streamlit as st

# --- User Authentication
def user_authentication():
    names = ["Zhaoshan Duan", "Erech"]
    usernames = ["jojo", "erech"]

    # load hashed passwords 
    file_path = Path(__file__).parent / "hash_pw.pkl"

    # open file in write binary mode
    with file_path.open('rb') as file:
        hashed_passwords = pickle.load(file)

    # authentication object
    authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
                                        "meow-gpt", "abcdef", cookie_expiry_days=30)
    
    authentication_status =  authenticator.login("Login", "main")
    return check_authentication_status(authentication_status, authenticator)

def check_authentication_status(authentication_status, authenticator):
    if authentication_status == False:
        st.error("Username/password is incorrect")
    
    if authentication_status == None:
        st.warning("Please enter your username and password")

    if authentication_status:
        return authenticator
    
    return None