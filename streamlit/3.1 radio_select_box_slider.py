import streamlit as st

st.radio("Which of these is not a mammal?",
["Dog", "Cat", "Eagle", "Pig"]) # one item out of several options, Streamlit offers the following three widgets

st.selectbox("Which of these is a mammal?",
["Pigeon", "Dove", "Fox", "Vulture"]) # We need to provide both a label that lets the user know what the widget requires them to do and a list of the user’s items.

st.select_slider("Which of these is not a bird?",
["Ostrich", "Flamingo", "Turkey", "Bat", "Pigeon"])
