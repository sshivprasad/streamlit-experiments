import streamlit as st
from callback import login_callback


def login_page():
    login = st.container()
    with login:
        st.subheader("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        st.button("Login", on_click=login_callback,
                  args=(login, username, password,))


def search_page():
    return
