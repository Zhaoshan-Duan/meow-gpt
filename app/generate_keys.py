# Name: Zhaoshan Duan
# Date: 12/6/2023
# Class: CS 5001
# Description: This file creates users with usernames and passwords
import pickle
from pathlib import Path
import streamlit_authenticator as stauth


names = ["Zhaoshan Duan", "Sofia Erech"]
usernames = ["jojo", "erech"]
passwords = ["5001", "my_love"]

# stauth.Hasher use bcrypt
hashed_password = stauth.Hasher(passwords).generate()

# pickel file file path
file_path = Path(__file__).parent / "hash_pw.pkl"

# open file in write binary mode
with file_path.open('wb') as file:
    pickle.dump(hashed_password, file)

