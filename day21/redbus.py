import streamlit as st
st.title("RED BUS")
name=st.text_input("Enter your name")
destination=st.selectbox(
    "select",["hyderabad","banga"]
)
date=st.date_input("travel Date")
tickets=st.number_input(tickets,min_value=1,step=1)
prices=("hyderabad":500,
        "chennai")
total=tickets*prices[destination]