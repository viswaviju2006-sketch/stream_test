import streamlit as st
st.title("take the input")
#taking a user input\
name= st.text_input("enter you name")


if st.button("submit"):
  st.write(f"print the name:{name}")
