import streamlit as st
st.title("Create an Account")
with st.form("signup_form"):
        username = st.text_input("Choose a Username")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        confirm = st.text_input("Confirm Password", type="password")
        submit = st.form_submit_button("Sign Up")

        if submit:
            if password != confirm:
                st.error("Passwords do not match.")
            elif len(username) < 3:
                st.error("Username too short.")
            else:
                st.success(f"Account created for {username}!")
                st.session_state.user = {"username": username, "email": email}