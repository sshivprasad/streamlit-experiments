import sqlite3
from config import URI_SQLITE_DB, ADMIN_USERNAME, ADMIN_PWD, USERS_TABLE
import streamlit as st


@st.cache(allow_output_mutation=True)
def get_connection(path: str):
    conn = sqlite3.connect(path, check_same_thread=False)
    st.session_state.sqlite_conn = conn
    return conn


def init_db():
    conn = get_connection(URI_SQLITE_DB)
    conn.execute(
        f"""CREATE TABLE IF NOT EXISTS {USERS_TABLE}
        (
            USERNAME TEXT,
            PASSWORD TEXT,
            IS_ADMIN INTEGER
        );"""
    )
    cur = conn.execute("SELECT * FROM USERS WHERE USERNAME = ? AND PASSWORD = ?",
                       (ADMIN_USERNAME, ADMIN_PWD))
    if cur.fetchone() == None:
        conn.execute(
            f"INSERT INTO {USERS_TABLE} VALUES (?, ?, ?)", (ADMIN_USERNAME, ADMIN_PWD, 1))
    conn.commit()


def is_valid_user(username, password):
    conn = st.session_state.sqlite_conn
    cur = conn.execute(f"SELECT * FROM {USERS_TABLE} WHERE USERNAME = ? AND PASSWORD = ?",
                       (username, password))
    if cur.fetchone() == None:
        return False
    else:
        return True
