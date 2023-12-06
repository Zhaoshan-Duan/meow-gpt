# Create pick file 
import pickle
from pathlib import Path
import streamlit_authenticator as stauth

names = ["Zhaoshan Duan", "Sofia Erech"]
usernames = ["jojo", "baby"]
passwords = ["5001", "hehe"]

# stauth.Hasher use bcrypt
hashed_password = stauth.Hasher(passwords).generate()

# pickel file file path
file_path = Path(__file__).parent / "hash_pw.pkl"

# open file in write binary mode
with file_path.open('wb') as file:
    pickle.dump(hashed_password, file)

