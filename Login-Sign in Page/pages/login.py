import streamlit as st
st.title("Login Page :lock:")
st.subheader("Enter your credentials to login")

username1=st.text_input("Enter Email or Username: ")
password=st.text_input("Enter the password",type="password")

if st.button("Login"):
    if password != password:
        st.error("Passwords do not match! :x:")
    else:
        st.success(f"Welcome, {username1}! Your account has been created successfully. :tada:")

