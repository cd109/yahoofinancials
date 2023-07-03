import streamlit as st

number = st.sidebar.slider("Choose a number",
                           min_value=0,
                           max_value=10,)
st.metric("Selected number", number) #widgets help us declutter the application 
