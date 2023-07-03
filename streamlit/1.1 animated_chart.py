import pandas as pd 
import streamlit as st 
import plotly.express as px 

st.set_page_config(
    page_title="gapminder animated plot",
    page_icon="🦈",
)


# load built-in gapminder dataset from plotly 
gapminder = px.data.gapminder() 



fig1 = px.scatter(gapminder, x='gdpPercap', y='lifeExp', color='continent',hover_name='continent',log_x=True,size_max=55,range_x=[100,100000],range_y=[25,90],animation_frame="year",animation_group="country")
fig1.update_layout(width=900)
st.header("Demo of an animated plot")
st.write(fig1)
