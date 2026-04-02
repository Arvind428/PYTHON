import streamlit as st
st.title("Simple Chatbot")

#Input from user
user_input=st.text_input("You: ")

#Button
if st.button("send"):
    text=user_input.lower()
    if text=="hi"or text=="hello":
        st.write("Bot: Hello😊")
    elif text=="what is your name":
        st.write("I am a simple chatbot")
    elif text=="operating sys":
        st.write("KALI LINUX")
    elif text=="scient":
        st.write("COLLEGE")
    else:
        st.write("Bot:sorry i dont understand")
