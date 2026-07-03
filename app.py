import streamlit as st

#taking a user input\
name= st.text_input("enter you name")

st.title("take the input")

if st.button("submit"):
  st.write(f"print the name:{name}")
