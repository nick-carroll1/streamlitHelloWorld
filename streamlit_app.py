import streamlit as st

st.title("Hello World")

myInput = st.text_input("Enter Text Here", "Hello")

st.write(myInput)