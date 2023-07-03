import streamlit as st

file = st.file_uploader("Select a file to upload", type=["png", "jpg"]) # It allows us to specify the type and size of the file users can upload. By default, it allows all types of files up to 200 MB. 

if file is not None:
    st.image(file)  
