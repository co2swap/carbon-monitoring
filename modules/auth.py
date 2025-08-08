
import streamlit as st

def check_login():
    with st.form("login_form"):
        st.subheader("🔐 Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")
        if submit:
            if username and password:
                return username
            else:
                st.error("Invalid credentials")
    return None
