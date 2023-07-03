import streamlit as st
import pandas as pd

df1 = pd.DataFrame({"Cats": [3, 2, 5],
               "Raptors": [6, 5, 1],
               "Snakes)": [4, 5, 7]})

df2 = pd.DataFrame({"Cats": [7, 9],
               "Raptors": [2, 6],
               "Snakes)": [3, 4]})

st.line_chart(df1)
st.line_chart(df2)

chart = st.line_chart(df1)
chart.add_rows(df2)
