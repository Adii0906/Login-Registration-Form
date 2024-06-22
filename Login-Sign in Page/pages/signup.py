import streamlit as st

st.title("Signup Form 📝")
st.subheader("Create New Account")
st.markdown("Please fill out the form below to create a new account.")
st.markdown("Personal information")

username=st.text_input("👤 Enter Your Name:  ")
lastname=st.text_input("📧 Enter your Email: ")

st.markdown("Account details")
email=st.text_input("👥 Create username: ")

col1,col2=st.columns(2)
with col1:
    new_gender = st.radio('⚧ Select your gender:', ['Male', 'Female', 'Other'])
with col2:
    new_age=st.slider('🎂 Enter your age:', 5, 80, 22)

col3,col4=st.columns(2)
with col3:
    password=st.text_input("Create Password: ",type="password")
with col3:
    password_re=st.text_input("Re-type Passwprd",type="password")

# Submission button with emoji
st.markdown("## :rocket: Ready to Create Your Account?")
if st.button("Sign Up"):
    if password != password_re:
        st.error("Passwords do not match! :x:")
    else:
        st.success(f"Welcome, {username}! Your account has been created successfully. :tada:")