import streamlit as st
from page import login_page, search_page
from auth import init_db


def app_title():
    st.title("Multipage App")
    st.write("An Experimental Multipage App")


def main():
    init_db()

    app_title()

    menu = ['Login', 'Search']
    menu_selection = st.sidebar.radio("Menu", menu, key='menu_selection')

    if menu_selection == 'Login':
        if 'login' not in st.session_state or not st.session_state['login']:
            login_page()
        elif 'login' in st.session_state and st.session_state['login']:
            st.success(
                f"\n You are successfully logged in as user '{st.session_state.username}'")
    elif menu_selection == 'Search':
        if 'login' in st.session_state and st.session_state['login']:
            search_page()
        else:
            st.warning("\n Please Login before you proceed \n")


if __name__ == "__main__":
    main()
