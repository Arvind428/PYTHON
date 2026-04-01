import streamlit as st
st.title("my first app")
st.write("Hello Everyone!")
username=st.text_input("Username")
password=st.text_input("password")
if st.button("Login"):
    if username=="admin" and password=="1234":
        st.success("Login Successful")
    else:
        st.error("Invalid")
