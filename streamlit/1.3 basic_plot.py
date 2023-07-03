import pandas as pd 
import streamlit as st 
import plotly.express as px 


# load built-in gapminder dataset from plotly 
gapminder = px.data.gapminder() 




#fetch all unique dates 
years=gapminder['year'].unique().tolist()

years_select=st.selectbox('select year for data',years,0)

df=gapminder[gapminder['year']==years_select] 
# color by continent 
fig = px.scatter(df, x='gdpPercap', y='lifeExp', color='continent',hover_name='continent',log_x=True,size_max=55,range_x=[100,100000],range_y=[25,90])
fig.update_layout(width=900)
st.header("Customized Plot for " + str(years_select) )
st.write(fig)


