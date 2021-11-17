import streamlit as st
from auth import is_valid_user


def login_callback(placeholder, username, password):
    if is_valid_user(username, password):
        st.session_state['username'] = username
        st.session_state['password'] = password
        st.session_state['login'] = True
    else:
        placeholder.error("Please Enter Valid Username and Password")
