import streamlit as st

st.multiselect("Which of these are birds?",
["Fox", "Eagle",
"Bat", "Dove"])


slider_int = st.slider("Select an integer",
                       min_value=0,
                       max_value=100,
                       value=25)
st.write(slider_int, type(slider_int))

slider_float = st.slider("Select a float",
                         min_value=0.0,
                         max_value=100.0,
                         value=25.0)
st.write(slider_float, type(slider_float))
