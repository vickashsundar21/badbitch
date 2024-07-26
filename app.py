

import streamlit as st
st.title("WELCOME")
name = st.text_input("Enter your name")
if name:
  st.write(f"Hello,  {name}! Welcome t the app")
