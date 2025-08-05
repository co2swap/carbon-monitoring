import streamlit as st

def require_login():
    if "username" not in st.session_state:
        st.session_state["username"] = ""
    st.sidebar.subheader("User Authentication")
    st.session_state["username"] = st.sidebar.text_input("Enter your username")
    if not st.session_state["username"]:
        st.warning("Please enter a username to continue.")
        st.stop()
    return st.session_state["username"]
