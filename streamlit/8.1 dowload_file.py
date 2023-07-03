import streamlit as st
import pandas as pd

df = pd.DataFrame({"Mammal": ["Cat", "Bat", "Fox"],
                   "Number": [3, 1, 5]})

st.dataframe(df)

st.download_button("Download data",
                   df.to_csv(index=False),
                   file_name="data.csv") # This widget allows us to specify the data to be downloaded and the file name to save it as. It requires a label that gives the user instructions on what is expected.
