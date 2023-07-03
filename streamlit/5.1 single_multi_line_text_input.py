import streamlit as st

st.markdown("## Single-Line Input")
text_input = st.text_input("Give an example of a mammal") # To make users input just a single line of text terminate entry by pressing the “Enter” key on the keyboard.
st.write(text_input)

st.markdown("## Multi-Line Input")
text_area = st.text_area("Give a list of 3 birds") # To have users input several lines of text
st.write(text_area)
