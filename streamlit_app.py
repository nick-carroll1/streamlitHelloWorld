import streamlit as st

st.title("Hello World")

myInput = st.input("Enter Text Here", "Hello")

st.write(myInput)