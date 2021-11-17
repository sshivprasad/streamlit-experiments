import streamlit as st

if 'team1_score' not in st.session_state:
    st.session_state.team1_score = 0

if 'team2_score' not in st.session_state:
    st.session_state.team2_score = 0

def increment_counter(counter_name, increment_value=0):
    st.session_state[counter_name] += increment_value

def decrement_counter(counter_name, decrement_value=0):
    st.session_state[counter_name] -= decrement_value

team1_name = st.sidebar.text_input("Team 1")
team2_name = st.sidebar.text_input("Team 2")

"""
# The Trivia Games
"""

col1, col2 = st.columns(2)

with col1:
    st.header(f"{team1_name}")
    st.button("Add 10 points", key='team1_add', on_click=increment_counter,         
              args=('team1_score', 10))
    st.button("Minus 5 points", key = 'team1_minus', on_click=decrement_counter, 
              args=('team1_score', 5))
    st.write(st.session_state.team1_score)
    
with col2:
    st.header(f"{team2_name}")
    st.button("Add 10 points", key='team2_add', on_click=increment_counter, 
               args=('team2_score', 10))
    st.button("Minus 5 points", key='team2_minus', on_click=decrement_counter, 
               args=('team2_score', 5))
    st.write(st.session_state.team2_score)