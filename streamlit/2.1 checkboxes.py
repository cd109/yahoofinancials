import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.checkbox("Click to add a check mark") # On its own, the checkbox widget isn’t useful. 

sample_data = {"Mammals": ["Cat", "Dog", "Bat", "Fox", "Pig"],
               "Number": [5, 3, 7, 1, 6]}
df = pd.DataFrame(sample_data)

st.dataframe(df)

if st.checkbox("Click to show a graph of the data"): # However, when used with other code, a checkbox can be used as a toggle.
    fig, ax = plt.subplots()
    ax = sns.barplot(x="Mammals", y="Number", data=df)
    st.pyplot(fig)
