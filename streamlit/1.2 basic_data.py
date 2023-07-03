import pandas as pd 
import streamlit as st 
import plotly.express as px 
st.set_page_config(
    page_title="gapminder data only",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="expanded",

)

# load built-in gapminder dataset from plotly 
gapminder = px.data.gapminder() 

st.header("input plotly data")
st.write(gapminder)

